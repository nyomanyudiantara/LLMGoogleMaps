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
            default="GOOGLE_MAPS_API_KEY_HERE",
            description="Google Cloud API Key",
        )

    def search_places(self, query: str) -> str:
        """
        Search for places and return a map and directions.
        :param query: The search term (e.g., 'best pizza in Rome')
        """
        if not self.valves.GOOGLE_MAPS_API_KEY:
            return "❌ API Key is missing."

        search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        params = {"query": query, "key": self.valves.GOOGLE_MAPS_API_KEY}

        try:
            response = requests.get(search_url, params=params, timeout=10)
            data = response.json()

            if data.get("status") != "OK":
                return f"❌ Google Maps Error: {data.get('status')}"

            results = data.get("results", [])[
                :1
            ]  # Limit to 1 for the cleanest test output
            output = ""

            for place in results:
                name = place.get("name")
                address = place.get("formatted_address")
                place_id = place.get("place_id")

                # ✅ Standard Navigation URL
                nav_url = f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote(name)}&query_place_id={place_id}"

                # ✅ Standard Embed URL (No Shorteners)
                embed_url = f"https://www.google.com/maps/embed/v1/place?key={self.valves.GOOGLE_MAPS_API_KEY}&q=place_id:{place_id}"

                # Formatting for Open WebUI to render correctly
                output += f"### {name}\n"
                output += f"**Address:** {address}\n\n"
                output += f'<iframe width="100%" height="300" src="{embed_url}" frameborder="0" style="border:0" allowfullscreen></iframe>\n\n'
                output += f"👉 [Click here for Directions]({nav_url})\n"

            return output

        except Exception as e:
            return f"❌ Error: {str(e)}"
