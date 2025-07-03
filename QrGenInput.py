import qrcode

# Prompt user for contact details
print("📇 Apple Contact QR Code Generator\nPlease enter the following contact details:")

first_name = input("First Name: ").strip()
last_name = input("Last Name: ").strip()
organization = input("Organization/Company: ").strip()
title = input("Job Title: ").strip()
mphone = input("Mobile Phone (include country code, e.g., +11234567890): ").strip()
wphone = input("Work Phone (include country code, e.g., +11234567890): ").strip()
email = input("Email Address: ").strip()
website = input("Website URL (optional): ").strip()
street = input("Street Address: ").strip()
city = input("City: ").strip()
state = input("State/Province: ").strip()
zip_code = input("ZIP/Postal Code: ").strip()
country = input("Country: ").strip()
note = input("Notes about the contact: ").strip()

showas = "COMPANY"

# Build vCard string
vcard = f"""BEGIN:VCARD
VERSION:3.0
N:{last_name};{first_name};;;
FN:{first_name} {last_name}
ORG:{organization}
TITLE:{title}
TEL;TYPE=CELL:{mphone}
TEL;TYPE=WORK:{wphone}
EMAIL:{email}
NOTE:{note}
X-ABSHOWAS:{showas}"""
if website:
    vcard += f"\nURL:{website}"

vcard += f"""
ADR;TYPE=WORK:;;{street};{city};{state};{zip_code};{country}
END:VCARD
"""

# Generate QR code
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=10,
    border=4,
)
qr.add_data(vcard)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Save QR code image
file_name = f"{first_name.lower()}_{last_name.lower()}_contact_qr.png"
img.save(file_name)

print(f"\n✅ QR code saved as '{file_name}'.")
