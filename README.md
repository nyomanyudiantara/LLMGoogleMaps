# LLMGoogleMaps
Local LLM that can output Google Maps's especially on where to find places to go/eat/etc.

🌍 Google Maps Discovery Tool: Setup Guide
This guide provides step-by-step instructions for a technical recruiter to deploy and verify the Google Maps Discovery Tool within an Open WebUI environment.

1. Prerequisites
Before starting, ensure you have the following:

Open WebUI Instance: Access to an Open WebUI environment (Local or Docker).

Google Cloud API Key: A key with the following APIs enabled:

Places API

Maps Embed API

Python 3.11+: The tool is designed for modern Python environments.

2. Google Cloud Configuration (Security)
To ensure the code runs successfully while maintaining security best practices, the following configurations were applied to the API key:

API Restrictions: The key is restricted to only call the Places API and Maps Embed API.

Usage Quotas: A daily cap of 100 requests has been set to ensure the project remains within the free tier.

Application Restrictions: During local development, application/referrer restrictions are set to None to allow for seamless server-side calls across varying local ports (e.g., 8080 or 3000).

3. Installation Steps
Step A: Import the Tool
Log in to your Open WebUI dashboard.

Navigate to Workspace > Tools.

Click Create Tool (or the + icon).

Copy the code from search_places.py and paste it into the editor.

Click Save.

Step B: Configure the Valve (API Key)
Once saved, click the Gear Icon (Settings) on the newly created tool.

In the Valves section, paste your Google Cloud API Key into the Maps_API_KEY field.

Click Save Settings.

Step C: Enable for Model
Go to Workspace > Models.

Select the model you wish to use (e.g., Llama-3 or GPT-4o).

Click Edit and ensure the toggle for the Google Maps Discovery Tool is set to ON.

4. Verification & Testing
To verify that the integration is successful, prompt the model with a location-based query:

Example Prompt: "Find the best pizza spots in Rome and show me a map of the top result."

Expected Output:
Data Synthesis: The LLM should identify the location and execute the tool.

Visual Map: An interactive Google Map iframe should render directly in the chat window.

Navigation Link: A clickable "Directions" link using the official Google Maps Search URL.

5. Troubleshooting
"Dynamic Link Not Found": Ensure you are using the official API endpoints provided in Version 1.9 of the code. This error occurs if Google misidentifies a URL as a Firebase Short Link.

Empty Map Frame: Verify that the Maps Embed API is specifically "Enabled" in the Google Cloud Console library.

Tool Not Triggering: Check the model's "System Prompt" or "Tools" toggle to ensure the model has permission to call the function.
