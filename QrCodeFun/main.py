import qrcode

img = qrcode.make('Bip Booop')
type(img)
img.save("qr.png")
