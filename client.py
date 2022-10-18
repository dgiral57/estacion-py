
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Aplication(Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.iconbitmap('icon.ico')
        self.state('zoomed')
        self.bgImage = Image.open('bg.jpg')
        self.bgImage2 = ImageTk.PhotoImage(self.bgImage)
        self.label = Label(self,image=self.bgImage2)
        self.style = ttk.Style()


        self.temperatureButton = ttk.Button(self,text='Temperatura',command=self.getTemperature,padding=(20,20))
        self.humidityButton = ttk.Button(self,text='Humedad',command=self.getHummidity,padding=(20,20))
        self.pressureButton = ttk.Button(self,text='Presión',command=self.getPressure,padding=(20,20))
        self.returnButton = ttk.Button(self,text='Regresar',command=self.goBack,padding=(20,20))
        self.refreshButton = ttk.Button(self,text='Refrescar',command=self.refresh,padding=(20,20))

        self.label.place(relx=0.5,rely=0.4,anchor=CENTER)
        self.temperatureButton.place(relx=0.25,rely=0.5,anchor=CENTER)
        self.humidityButton.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.pressureButton.place(relx=0.75,rely=0.5,anchor=CENTER)
        self.mainloop()
    
    def getTemperature(self):
        self.temperatureButton.place_forget()
        self.humidityButton.place_forget()
        self.pressureButton.place_forget()
        self.returnButton.place(relx=0.25,rely=0.75,anchor=CENTER)
        self.refreshButton.place(relx=0.75,rely=0.75,anchor=CENTER)
        return 0

    def getHummidity(self):
        self.temperatureButton.place_forget()
        self.humidityButton.place_forget()
        self.pressureButton.place_forget()
        self.returnButton.place(relx=0.25,rely=0.75,anchor=CENTER)
        self.refreshButton.place(relx=0.75,rely=0.75,anchor=CENTER)
        return 0
    
    def getPressure(self):
        self.temperatureButton.place_forget()
        self.humidityButton.place_forget()
        self.pressureButton.place_forget()
        self.returnButton.place(relx=0.25,rely=0.75,anchor=CENTER)
        self.refreshButton.place(relx=0.75,rely=0.75,anchor=CENTER)
        return 0

    def goBack(self):
        self.returnButton.place_forget()
        self.refreshButton.place_forget()
        self.temperatureButton.place(relx=0.25,rely=0.5,anchor=CENTER)
        self.humidityButton.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.pressureButton.place(relx=0.75,rely=0.5,anchor=CENTER)
        return 0
    
    def refresh(self):
        return 0

def main():
    app = Aplication('Estación Meteorologica')
    return 0

if __name__ == '__main__':
    main()
