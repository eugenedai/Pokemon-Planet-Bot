import pytesseract

# Use Tesseract to extract text from the screenshot
text = pytesseract.image_to_string(primary_scareen)

# Print the extracted text
print("Extracted Text:")
print(text)