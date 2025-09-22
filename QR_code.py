import qrcode
#taking upi id as input 
upi_id=input("Enter the UPI ID=")
#defining the payment url based on the upi id and the payment app
#u can modify the url with the payment app 
phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create qr for each payment 
phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
google_qr=qrcode.make(google_url)
#save the QR code to image file (optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_qr.save('google_qr.png')
#display the qr code 
phonepe_qr.show()
paytm_qr.show()
google_qr.shoow()