import qrcode
from PIL import Image


website_url = " "                                                 #eklemek istediğiniz Url'yi " " içine yazın
qrkod = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qrkod.add_data(website_url)
qrkod.make(fit=True)

qr_img = qrkod.make_image(fill_color="black", back_color="white")


overlay_img = Image.open("")                               #eklemek istediğiniz resmi dosyaya koyun sonrasında  "" içine .png formatında ekleyin                         
overlay_img = overlay_img.resize((100, 100))  


qr_img.paste(overlay_img, (150, 150))  


qr_img.save("sonhali.png")
