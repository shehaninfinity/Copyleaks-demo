import base64

def pdf_to_base64_file(input_pdf_path, output_base64_path):
    # Read the PDF file in binary mode
    with open(input_pdf_path, 'rb') as pdf_file:
        pdf_data = pdf_file.read()

    # Encode the binary PDF data to Base64
    base64_data = base64.b64encode(pdf_data).decode('utf-8')

    # Write the Base64 string to a text file
    with open(output_base64_path, 'w') as base64_file:
        base64_file.write(base64_data)

    print(f"Base64 encoded data saved to: {output_base64_path}")

# Example usage
input_pdf = 'Myfile.pdf'             # Replace with your PDF file path
output_base64 = 'encoded_output.txt'  # Replace with desired output file name
pdf_to_base64_file(input_pdf, output_base64)