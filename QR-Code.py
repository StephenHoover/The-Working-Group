# from PIL import ImageTk
import qrcode
import qrcode.image.svg

# Add your URL
data = "www.stephenhoover.org"

# Define shape, border and error correction
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Encode Data (URL) into QR
qr.add_data(data)
qr.make(fit=True)

# Change Colors
img = qr.make_image(fill_color=(0, 51, 102), back_color="white")

# Format as vector image 
qrcode.image.svg.SvgFillImage

# Save as PNG
img.save("YourURL.png")
# Save as SVG
img.save("YourURL.svg") 
