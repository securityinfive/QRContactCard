import qrcode

# Expand this to all inputs, custom.

# Create the vCard string (3.0 works well with iOS)
vcard = """BEGIN:VCARD
VERSION:3.0
N:Smith;Joe;;;
FN:Joe Smith
ORG:Acme Inc.
TITLE:CEO
TEL;TYPE=CELL:+11234567890
EMAIL:joe@acme.com
URL:https://acme.com
ADR;TYPE=work:;;123 Main St;Somewhere;CA;90210;USA
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
img.save("qr_contact_card.png")

