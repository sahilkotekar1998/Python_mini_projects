import qrcode

upi_id = input("Enter UPI ID: ")  # Accept UPI ID as string

# UPI URL structure for payments
# pa is UPI ID, pn = recipient's Name, mc = merchant code,# # am= ammount
# cu=currency
phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
gpay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

# Create QR codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
gpay_qr = qrcode.make(gpay_url)

# Save the QR codes to image files
phonepe_qr.save("phonepe_qr.png")
gpay_qr.save("googlepay_qr.png")

# Displaying QR codes is system-specific and show() might not work on all systems
# It's better to open or view the saved images using an image viewer or browser



