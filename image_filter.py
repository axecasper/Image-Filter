import cv2
import numpy as np
from PIL import Image
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import filedialog
import imutils
import tkinter.messagebox
import argparse

def raise_frame(frame):
    frame.tkraise()
    
pencere=tk.Tk()
f2 = tk.Frame(pencere)
f1 = tk.Frame(pencere)
v=tk.IntVar()
for frame in (f1, f2) :
    frame.grid(row=0, column=0, sticky='news')
    
tk.Button(f1, text="2.sayfaya geç", command=lambda:raise_frame(f2)).grid(row=0,column=0)
tk.Label(f1, text="1.sayfa").grid(row=0,column=1)
tk.Label(f2, text='2.sayfa').grid(row=0,column=1)
tk.Button(f2, text='1.sayfaya geç', command=lambda:raise_frame(f1)).grid(row=0,column=0)

def yeni():
   file_path = filedialog.askopenfilename()
   return file_path
file_path=yeni()


tk.menubar=tk.Menu(pencere)
tk.filemenu=tk.Menu(tk.menubar,tearoff=0)
tk.filemenu.add_command(label="New Picture",command=yeni)
tk.filemenu.add_command(label="exit",command=pencere.destroy)
tk.menubar.add_cascade(label="İşlemler",menu=tk.filemenu)
pencere.config(menu=tk.menubar)


image=cv2.imread(file_path)
height=len(image)
width=len(image[0])


def Resmigöster():
    cv2.imshow("Resmin Orjinali",image)


def gray():
    a=cv2.imread(file_path,cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Siyah Beyaz",a)
    def jpg1():
       j=".jpg"
       b=cv2.imwrite("grey"+j,a)
    def png1():
       j=".png"
       b=cv2.imwrite("grey"+j,a)
    tk.Radiobutton(f1,indicatoron=0,text="jpg kaydet",command=jpg1,value=200).grid(row=2,column=1)
    tk.Radiobutton(f1,indicatoron=0,text="png kaydet",command=png1,value=300).grid(row=3,column=1)

def negatif():
    a=cv2.imread(file_path,cv2.IMREAD_GRAYSCALE)
    img=np.zeros((height,width,1),np.uint8)
    for i in  range(height):
       
        for j in range(width):
            img[i,j]=255-a[i,j]
    cv2.imshow("negatif",img)
    def jpg2():
        j=".jpg"
        b=cv2.imwrite("negatif"+j,img)
    def png2():
        j=".png"
        b=cv2.imwrite("negatif"+j,img)
    tk.Radiobutton(f1,indicatoron=0,text="jpg kaydet",command=jpg2,value=201).grid(row=2,column=2)
    tk.Radiobutton(f1,indicatoron=0,text="png kaydet",command=png2,value=301).grid(row=3,column=2)

def resize():
    tk.genişlik=tk.Label(f1,text="width")
    tk.genişlik.grid(row=2,column=3)
    tk.uzunluk=tk.Label(f1,text="height")
    tk.uzunluk.grid(row=4,column=3)
    tk.wid=tk.Entry(f1)
    tk.wid.grid(row=3,column=3)
    tk.hei=tk.Entry(f1)
    tk.hei.grid(row=5,column=3)
    def sized():
        a=int(tk.wid.get())
        b=int(tk.hei.get())
        img=cv2.resize(image,(a,b))
        cv2.imshow("yeni boyut",img)
        def jpg3():
            j=".jpg"
            cv2.imwrite("boyutlandırılmış"+j,img)
        def png3():
            j=".png"
            cv2.imwrite("boyutlandırılmış"+j,img)
        tk.Radiobutton(f1,indicatoron=0,text="jpg kaydet",command=jpg3,value=103).grid(row=7,column=3)
        tk.Radiobutton(f1,indicatoron=0,text="png kaydet",command=png3,value=203).grid(row=8,column=3)
    tk.Radiobutton(f1,indicatoron=0,text="resme bak",command=sized,value=102).grid(row=6,column=3)

def çevir():
   tk.açi=tk.Label(f1,text="döndürme açınızı giriniz(saat yönünün tersine döndürür)")
   tk.açi.grid(row=2,column=4)
   tk.aç=tk.Entry(f1)
   tk.aç.grid(row=3,column=4)
   def çevirme():
      açı=int(tk.aç.get())
      for angle in np.arange(0, 360,açı):
         rotated = imutils.rotate_bound(image,angle)
         cv2.imshow("Rotated (Correct)", rotated)
         def jpg4():
            j=".jpg"
            cv2.imwrite("döndürülmüş"+j,rotated)
         def png4():
            j=".png"
            cv2.imwrite("döndürülmüş"+j,rotated)
         tk.Radiobutton(f1,indicatoron=0,text="jpg kaydet",command=jpg4,value=105).grid(row=5,column=4)
         tk.Radiobutton(f1,indicatoron=0,text="png kaydet",command=png4,value=205).grid(row=6,column=4)
   tk.Radiobutton(f1,indicatoron=0,text="resme bak",command=çevirme,value=104).grid(row=4,column=4)
   
def corp():
   r=cv2.selectROI(image)
   imCrop = image[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
   cv2.imshow("Image", imCrop)
   def jpg5():
      a=cv2.imwrite("kesilmiş.jpg",imCrop)
   def png5():
      a=cv2.imwrite("kesilmiş.png",imCrop)
   tk.Radiobutton(f1,indicatoron=0,text="jpg kaydet",command=jpg5,value=106).grid(row=2,column=5)
   tk.Radiobutton(f1,indicatoron=0,text="png kaydet",command=png5,value=206).grid(row=3,column=5)

def blur():
   tk.blur=tk.Label(f2,text="blur oranını girin")
   tk.blur.grid(row=2,column=6)
   tk.oran1=tk.Entry(f2)
   tk.oran1.grid(row=3,column=6)
   def blurbak():
      oran=int(tk.oran1.get())
      kernel_3x3 = np.ones((oran, oran), np.float32) /(oran*oran)
      blurred = cv2.filter2D(image, -1, kernel_3x3)
      
      cv2.imshow('bluring', blurred)
      def png6():
         a=cv2.imwrite("blurlanmış.png",blurred)
      def jpg6():
         a=cv2.imwrite("blurlanmış.jpg",blurred)
      tk.Radiobutton(f2,indicatoron=0,text="jpg kaydet",command=jpg6,value=108).grid(row=5,column=6)
      tk.Radiobutton(f2,indicatoron=0,text="png kaydet",command=png6,value=208).grid(row=6,column=6)
   tk.Radiobutton(f2,indicatoron=0,text="blur bak",command=blurbak,value=107).grid(row=4,column=6)

def sharp():
   kernel_sharpening = np.array([[-1,-1,-1], [-1, 9,-1],[-1,-1,-1]])
   sharpened = cv2.filter2D(image, -1, kernel_sharpening)
   cv2.imshow('Image Sharpening', sharpened)
   def png7():
      a=cv2.imwrite("netleşmiş.png",sharpened)
   def jpg7():
      a=cv2.imwrite("netleşmiş.jpg",sharpened)
   tk.Radiobutton(f2,indicatoron=0,text="png kaydet",command=png7,value=109).grid(row=2,column=7)
   tk.Radiobutton(f2,indicatoron=0,text="jpg kaydet",command=jpg7,value=209).grid(row=3,column=7)

def median():
   median = cv2.medianBlur(image,5)
   cv2.imshow("median",median)
   def png8():
      cv2.imwrite("pürüzsüz.png",median)
   def jpg8():
      cv2.imwrite("pürüzsüz.jpg",median)
   tk.Radiobutton(f2,indicatoron=0,text="png kaydet",command=png8,value=110).grid(row=2,column=8)
   tk.Radiobutton(f2,indicatoron=0,text="jpg kaydet",command=jpg8,value=210).grid(row=3,column=8)
def yol():
   img=np.zeros((height,width,1),np.uint8)
   
   a=cv2.imread(file_path,cv2.IMREAD_GRAYSCALE)
   for i in  range(height):
      for j in range(width):
         if ((a[i,j]>190) and (a[i,j]<220)):
            img[i,j]=255
  
   cv2.imshow("ada",img)
   def png9():
      cv2.imwrite("sadece yol.png",img)
   def jpg9():
      cv2.imwrite("sadece yol.jpg",img)
   tk.Radiobutton(f2,indicatoron=0,text="png kaydet",command=png9,value=112).grid(row=2,column=9)
   tk.Radiobutton(f2,indicatoron=0,text="jpg kaydet",command=jpg9,value=212).grid(row=3,column=9)
def bright():  
   tk.katı=tk.Label(f2,text="kaç kat oranında parlaklık değiştirilsin")
   tk.katı.grid(row=2,column=10)
   tk.kat=tk.Entry(f2)
   tk.kat.grid(row=3,column=10)
   tk.ekleme=tk.Label(f2,text="scale kaç birim değiştirilsin")
   tk.ekleme.grid(row=4,column=10)
   tk.ekle=tk.Entry(f2)
   tk.ekle.grid(row=5,column=10)
   
   def hesap():
      alpha=float(tk.kat.get())
      beta=float(tk.ekle.get())
      new = np.zeros(image.shape, image.dtype)
      for y in range(image.shape[0]):
         for x in range(image.shape[1]):
            for c in range(image.shape[2]):
               new[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)
      cv2.imshow('New Image', new)
      def png10():
         cv2.imwrite("parlaklık.png",new)
      def jpg10():
         cv2.imwrite("parlaklık.jpg",new)
      tk.Radiobutton(f2,indicatoron=0,text="png kaydet",command=png10,value=111).grid(row=7,column=10)
      tk.Radiobutton(f2,indicatoron=0,text="jpg kaydet",command=jpg10,value=211).grid(row=8,column=10)
   tk.Radiobutton(f2,indicatoron=0,text="Parlaklığa bak",command=hesap,value=111).grid(row=6,column=10)
 
def su():
   img=np.zeros((height,width,1),np.uint8)
   
   a=cv2.imread(file_path,cv2.IMREAD_GRAYSCALE)
   for i in  range(height):
      for j in range(width):
         if ((a[i,j]>26) and (a[i,j]<56)):
            img[i,j]=255
  
   cv2.imshow("ada",img)
   def png9():
      cv2.imwrite("sadece su.png",img)
   def jpg9():
      cv2.imwrite("sadece su.jpg",img)
   tk.Radiobutton(f2,indicatoron=0,text="png kaydet",command=png9,value=112).grid(row=2,column=11)
   tk.Radiobutton(f2,indicatoron=0,text="jpg kaydet",command=jpg9,value=212).grid(row=3,column=11)
   


tk.Radiobutton(f1,indicatoron=0,text="resmin orjinalini göster",command=Resmigöster,value=1).grid(row=1,column=0)
tk.Radiobutton(f1,indicatoron=0,text="siyah beyaz bak",command=gray,value=2).grid(row=1,column=1)
tk.Radiobutton(f1,indicatoron=0,text="Negatif bak",command=negatif,value=3).grid(row=1,column=2)        
tk.Radiobutton(f1,indicatoron=0,text="resize oranı seç",command=resize,value=4).grid(row=1,column=3)
tk.Radiobutton(f1,indicatoron=0,text="resmi çevir",command=çevir,value=5).grid(row=1,column=4)
tk.Radiobutton(f1,indicatoron=0,text="resmi kes",command=corp,value=6).grid(row=1,column=5)
tk.Radiobutton(f2,indicatoron=0,text="blur oranı seç",command=blur,value=7).grid(row=1,column=6)
tk.Radiobutton(f2,indicatoron=0,text="netleştirilmiş bak",command=sharp,value=8).grid(row=1,column=7)
tk.Radiobutton(f2,indicatoron=0,text="pürüz gider",command=median,value=9).grid(row=1,column=8)
tk.Radiobutton(f2,indicatoron=0,text="sadece yollar",command=yol,value=10).grid(row=1,column=9)
tk.Radiobutton(f2,indicatoron=0,text="brightness",command=bright,value=11).grid(row=1,column=10)
tk.Radiobutton(f2,indicatoron=0,text="sadece su",command=su,value=12).grid(row=1,column=11)

pencere.mainloop()
plt.show()
raise_frame(f1)




