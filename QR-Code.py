# from PIL import ImageTk
import qrcode
import qrcode.image.svg

data = "www.stephenhoover.org"

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color=(0, 51, 102), back_color="white")
qrcode.image.svg.SvgFillImage

# Save as PNG
img.save("YourURL.png")
# Save as SVG
img.save("YourURL.svg") 