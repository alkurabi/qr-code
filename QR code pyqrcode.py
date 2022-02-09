import pyqrcode
import png
from pyqrcode import QRCode
  
# String which represent the QR code 
website = "https://secure.actblue.com/donate/horford4house"

# Generate QR code 
url = pyqrcode.create(website)
  
# Create and save the svg file, change size, color, background color, and white space border width
url.svg("jondonateQRcode_black_and_white.svg", scale = 10, module_color="#000000", background='white', quiet_zone=5)

# Create and save the png file
url.png('jondonateQRcode_BC2129_bg.png', scale = 20, module_color="#FFFFFF", background='#BC2129', quiet_zone=5)