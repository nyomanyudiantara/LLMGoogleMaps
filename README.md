# LLMGoogleMaps
Local LLM that can output Google Maps's especially on where to find places to go/eat/etc.

🌍 Google Maps Discovery Tool for Open WebUI
This repository contains a Python-based tool designed for Open WebUI. It enables local LLMs to perform real-time location discovery, rendering interactive Google Maps and navigation links directly within the chat interface.

1. Prerequisites
Before deployment, ensure the following requirements are met:

Open WebUI Instance: Access to a running instance (Local or Docker).

Python 3.11+: Required for backend tool execution.

Google Cloud API Key: An active key with the following APIs enabled:

Places API

Maps Embed API

2. Security & Quota Best Practices
To ensure project integrity and stay within the Google Cloud free tier, the following configurations are recommended:

API Restrictions: Restrict the key specifically to the Places API and Maps Embed API.

Usage Quotas: Set a daily cap (e.g., 100 requests) in the Google Cloud Console to prevent unexpected billing.

Application Restrictions: For local testing, set Referrer restrictions to None to ensure the server-side Python requests are not blocked by local port variations (8080/3000).

3. Installation & Setup
Step A: Import the Tool
Log in to your Open WebUI dashboard.

Navigate to Workspace > Tools.

Click the + (Create Tool) icon.

Copy the code from main.py and paste it into the code editor.

Click Save.

Step B: Configure the API Key (Valves)
The tool uses "Valves" to securely manage credentials without hard-coding them.

In the Tools menu, locate your new Google Maps tool.

Click the Gear Icon (Settings).

Find the Valves section.

Enter your API Key into the Maps_API_KEY field.

Click Save at the bottom of the settings window.

Step C: Enable the Tool for your Model
Go to Workspace > Models.

Select your preferred model (e.g., Llama-3, Mistral).

Click Edit and scroll to the Tools section.

Toggle the Google Maps Discovery Tool to ON.

4. Verification & Testing
Test the integration by prompting the model with a location-based intent:

Example: "I'm looking for a highly-rated sushi restaurant in Tokyo. Please show me where it is."

Expected Results:
Function Calling: The model identifies the intent and triggers the search_places function.

Interactive UI: A 350px interactive map renders within the chat bubble.

Deep Linking: A direct "View Directions" link is provided for mobile/desktop navigation.

5. Troubleshooting
Map Not Rendering: Ensure the Maps Embed API is specifically enabled in your Google Cloud Library.

404 / Dynamic Link Error: This usually indicates an incorrect URL format. Ensure you are using the direct maps.googleapis.com endpoints defined in the provided script.

Request Denied: Check your Google Cloud Billing status; Google requires a linked billing account even for free tier usage.
