"""
title: Google Maps Discovery Tool
author: a mutant
description: Search for places and return official embedded maps.
version: 1.9
"""

import requests
import urllib.parse
from pydantic import BaseModel, Field

class Tools:
    def __init__(self):
        self.valves = self.Valves()

    class Valves(BaseModel):
        GOOGLE_MAPS_API_KEY: str = Field(
            default="", 
            description="Enter your Google Cloud API Key here."
        )

    def search_places(self, query: str) -> str:
        """
        Search for places and return an interactive map and direction links.
        :param query: The search term (e.g., 'best pizza in Rome')
        """
        if not self.valves.GOOGLE_MAPS_API_KEY:
            return "❌ API Key is missing. Please configure it in the Tool Settings."

        # 1. Fetch data from Google Places API
        search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        params = {"query": query, "key": self.valves.GOOGLE_MAPS_API_KEY}

        try:
            response = requests.get(search_url, params=params, timeout=10)
            data = response.json()

            if data.get("status") != "OK":
                return f"❌ Google Maps API Error: {data.get('status')}"

            results = data.get("results", [])[:1] 
            output = ""

            for place in results:
                name = place.get("name")
                address = place.get("formatted_address")
                place_id = place.get("place_id")

                # Best Practice: Official Navigation URL
                nav_url = f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote(name)}&query_place_id={place_id}"

                # Best Practice: Official Embed URL (v1/place)
                embed_url = f"https://www.google.com/maps/embed/v1/place?key={self.valves.GOOGLE_MAPS_API_KEY}&q=place_id:{place_id}"

                output += f"### {name}\n"
                output += f"**Address:** {address}\n\n"
                
                # HTML Iframe for the embedded map requirement
                output += f'<iframe width="100%" height="350" src="{embed_url}" frameborder="0" style="border:0" allowfullscreen></iframe>\n\n'
                
                # Link for the "view directions" requirement
                output += f"👉 [View Directions on Google Maps]({nav_url})\n"

            return output

        except Exception as e:
            return f"❌ Unexpected Error: {str(e)}"
