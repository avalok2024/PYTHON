import qrcode as qr 
image = qr.make("https://youtu.be/th4OBktqK1I?si=gkFnTVySJZGbfKSg")
image.save("youtube.png")