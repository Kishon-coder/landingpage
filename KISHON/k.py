from tkinder import Tk,Label,PhotoImage
from PIL import Image,ImageTk
root=Tk()
image=Image.open("C://Users//Amin/Music//lion.jpg")
new_size=(600,600)
resized_image=image,resized(new_size)
resized_image=resized_image.convert('RGB')
photo=imageTk.photoImage(resized_image)
label=Label(root,image=photo)
label.pack()
