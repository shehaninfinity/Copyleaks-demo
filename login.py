from copyleaks.copyleaks import Copyleaks
from copyleaks.exceptions.command_error import CommandError
from copyleaks.models.submit.document import FileDocument
from copyleaks.models.submit.properties.scan_properties import ScanProperties
from copyleaks.models.export import Export, ExportCrawledVersion, ExportResult
import base64
import random

EMAIL_ADDRESS = "shehanv@infyinnos.com"
API_KEY = "7b908237-0f5b-42bc-b1a6-b1c9eb26018b"

# Login to Copyleaks
try:
    auth_token = Copyleaks.login(EMAIL_ADDRESS, API_KEY)
except CommandError as ce:
    response = ce.get_response()
    print(f"An error occurred (HTTP status code {response.status_code}):")
    print(response.content)
    exit(1)

print("Logged successfully!\nToken:")
print(auth_token)