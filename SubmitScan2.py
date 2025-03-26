import http.client
import json
from copyleaks.copyleaks import Copyleaks

# Your credentials                                          
EMAIL_ADDRESS = "shehanv@infyinnos.com"
API_KEY = "7b908237-0f5b-42bc-b1a6-b1c9eb26018b"

# Log in to retrieve the auth token.
auth_token = Copyleaks.login(EMAIL_ADDRESS, API_KEY)
access_token = auth_token["access_token"]
print("Access token:", access_token)

# Define your scan and export IDs.
scan_id = "00014"           # Replace with your actual scan id.
export_id = "export-unique2" # Ensure this is unique (>= 3 characters).

# Build the export payload without the PDF report.
payload_dict = {
    "results": [
        {
            "id": "06e6f60c35",  # Replace with your actual result id from the completed scan webhook.
            "verb": "POST",
            "headers": [
                ["header-key", "header-value"]
            ],
            "endpoint": f"https://eolhwict5lm8i4x.m.pipedream.net/export/{export_id}/results/06e6f60c35"
        }
    ],
    "crawledVersion": {
        "verb": "POST",
        "headers": [
            ["header-key", "header-value"]
        ],
        "endpoint": f"https://eolhwict5lm8i4x.m.pipedream.net/export/{export_id}/crawled-version"
    },
    "completionWebhook": f"https://eolhwict5lm8i4x.m.pipedream.net/export/{export_id}/completed",
    "maxRetries": 3
}

payload = json.dumps(payload_dict)

headers = {
    "Authorization": "Bearer " + access_token,
    "Content-Type": "application/json"
}

url_path = f"/v3/downloads/{scan_id}/export/{export_id}"

conn = http.client.HTTPSConnection("api.copyleaks.com")
conn.request("POST", url_path, payload, headers)

res = conn.getresponse()
data = res.read()

print("Export API response:")
print(data.decode("utf-8"))
