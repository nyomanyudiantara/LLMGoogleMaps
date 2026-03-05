# LLMGoogleMaps
Local LLM that can output Google Maps's especially on where to find places to go/eat/etc.

# 🌍 Google Maps Discovery Tool for Open WebUI

This repository contains a Python-based tool designed for **Open WebUI**. It enables local LLMs to perform real-time location discovery, rendering interactive Google Maps and navigation links directly within the chat interface.

---

## 🚀 Features
* **Real-time Search:** Uses Google Places API to find accurate locations.
* **Interactive Maps:** Embeds a live Google Map directly in the LLM chat bubble.
* **Deep Linking:** Generates direct navigation links for mobile and desktop.
* **Security Focused:** Uses Open WebUI "Valves" for credential isolation.

---

## 1. Prerequisites
Before deployment, ensure the following requirements are met:
* [ ] **Open WebUI Instance:** Access to a running instance (Local or Docker).
* [ ] **Python 3.11+:** Required for backend tool execution.
* [ ] **Google Cloud API Key:** An active key with the following APIs enabled:
    * `Places API`
    * `Maps Embed API`

---

## 2. Security & Quota Best Practices
To ensure project integrity and stay within the Google Cloud free tier:

> [!IMPORTANT]
> **API Restrictions:** Restrict your key specifically to the *Places API* and *Maps Embed API* in the Google Cloud Console.

* **Usage Quotas:** Set a daily cap (e.g., 100 requests) to prevent unexpected billing.
* **Application Restrictions:** For local testing, set Referrer restrictions to `None` to ensure compatibility with local port variations (8080/3000).

---

## 3. Installation & Setup

### Step A: Import the Tool
1. Log in to your **Open WebUI** dashboard.
2. Navigate to **Workspace > Tools**.
3. Click the **+ (Create Tool)** icon.
4. Copy the code from `main.py` and paste it into the code editor.
5. Click **Save**.

### Step B: Configure the API Key (Valves)
The tool uses "Valves" to securely manage credentials without hard-coding them.
1. In the **Tools** menu, locate your new Google Maps tool.
2. Click the **Gear Icon (Settings)**.
3. Find the **Valves** section.
4. Enter your API Key into the `Maps_API_KEY` field.
5. Click **Save** at the bottom of the settings window.

### Step C: Enable the Tool for your Model
1. Go to **Workspace > Models**.
2. Select your preferred model (e.g., Llama-3, Mistral).
3. Click **Edit** and scroll to the **Tools** section.
4. Toggle the **Google Maps Discovery Tool** to **ON**.

---

## 4. Verification & Testing
Test the integration by prompting the model with a location-based intent:

> **Example:** *"I'm looking for a highly-rated sushi restaurant in Tokyo. Please show me where it is."**

### Expected Results:
* **Function Calling:** The model identifies the intent and triggers the `search_places` function.
* **Interactive UI:** A 350px interactive map renders within the chat bubble.
* **Deep Linking:** A direct "View Directions" link is provided.

---

## 5. Troubleshooting
* **Map Not Rendering:** Ensure the **Maps Embed API** is "Enabled" in your Google Cloud Library.
* **404 Error:** Ensure you are using the direct `maps.googleapis.com` endpoints defined in the script.
* **Request Denied:** Check your Google Cloud Billing status; Google requires a linked billing account even for free tier usage.
