import qrcode

# Taking UPI ID as Input

upi_id = input("Enter your UPI ID: ")

#upi.//pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

# Defining the payment URL based on the UPI ID and the payment app
# URL can be modified based upon the payments app we want to support

phonepay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipent%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipent%20Name&mc=1234'

# Create QR codes for each application
phonepe_qr = qrcode.make(phonepay_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save the QR as image file (Optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# Displaying the QR codes
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()