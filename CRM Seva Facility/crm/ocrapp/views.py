import pytesseract
from PIL import Image
import re
from django.shortcuts import render
from django.http import JsonResponse
from .models import VisitingCard
from .forms import VisitingCardForm

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    # Extract text from image using Tesseract.
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def scan_visiting_card(request):
    if request.method == 'POST':
        form = VisitingCardForm(request.POST, request.FILES)
        if form.is_valid():
            # Save uploaded image
            card = form.save()

            # Extract text from the image
            extracted_text = extract_text_from_image(card.card_image.path)


            print('extracted text: ',extracted_text)


            # extracting name, email, and phone from text
            name = extract_name(extracted_text)
            email = extract_email(extracted_text)
            phone = extract_phone(extracted_text)
            company = 'TEIM'
            address = extract_address(extracted_text)

            # Update the VisitingCard model with extracted data
            card.name = name
            card.email = email
            card.phone = phone
            card.company = company
            card.address = address
            card.save()

            return JsonResponse({'success': True, 'data': {
                'name': name,
                'email': email,
                'phone': phone,
                'company': company,
                'address' : address,
            }})
    else:
        form = VisitingCardForm()
    return render(request, 'ocrapp/scan.html', {'form': form})


def extract_email(text):
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    email_match = re.search(email_pattern, text)
    return email_match.group(0) if email_match else None

def extract_phone(text):
    phone_pattern = r'(\+91\s?\d{5}\s?\d{5})'
    phone_match = re.search(phone_pattern, text)
    return phone_match.group(0) if phone_match else None

def extract_name(text):
    lines = text.splitlines()

    for line in lines:
        if line.isupper() and len(line.split()) >= 2:
            return line.strip()
    
    return "Name not found"

def extract_address(text):
    match = re.search(r'@([\s\S]*?)(?=©|\Z)', text)
    if match:
        # Clean up whitespace and extra characters
        address = match.group(1).strip().replace("\n", " ")
        return address
    return None



