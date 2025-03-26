import base64
from copyleaks.models.submit.document import FileDocument
from copyleaks.copyleaks import Copyleaks
from copyleaks.models.submit.properties.scan_properties import ScanProperties

# Your credentials                                          
EMAIL_ADDRESS = "shehanv@infyinnos.com"
API_KEY = "7b908237-0f5b-42bc-b1a6-b1c9eb26018b"

# Define the PDF file name
pdf_file_name = "Myfile.pdf"

# Read the PDF file in binary mode and convert it to BASE64
with open(pdf_file_name, "rb") as pdf_file:
    pdf_content = pdf_file.read()
base64_file_content = base64.b64encode(pdf_content).decode('utf8')

print("Submitting a new PDF file...")
file_submission = FileDocument(base64_file_content, pdf_file_name)

# Set scan properties
scan_properties = ScanProperties('https://eolhwict5lm8i4x.m.pipedream.net?event={{STATUS}}')
scan_properties.set_sandbox(False)  # Turn on sandbox mode; turn off in production.
file_submission.set_properties(scan_properties)

# Login to retrieve the proper auth_token object
auth_token = Copyleaks.login(EMAIL_ADDRESS, API_KEY)

print(auth_token)

scan_id = "00014"  # Replace with your actual scan id

# Submit the PDF file for scanning
Copyleaks.submit_file(auth_token, scan_id, file_submission)
print("Sent to scanning")
print("You will be notified, using your webhook, once the scan is completed.")
