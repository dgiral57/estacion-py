
from tkinter import *
from tkinter import ttk, font
import requests

class Aplication(Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.state('zoomed')
        self.fuente = font.Font(weight='bold',size=25)
        self.default = StringVar(self)
        self.default.set(0)


        self.qty = ttk.Label(self,text='Catidad de datos',font=self.fuente)
        self.box = ttk.Spinbox(self,from_=0,to=20,width=2,textvariable=self.default,font=self.fuente)
        self.temperatureButton = ttk.Button(self,text='Temperatura',command=self.getTemperature,padding=(20,20))
        self.humidityButton = ttk.Button(self,text='Humedad',command=self.getHummidity,padding=(20,20))
        self.pressureButton = ttk.Button(self,text='Presión',command=self.getPressure,padding=(20,20))
        self.returnButton = ttk.Button(self,text='Regresar',command=self.goBack,padding=(20,20))

        self.qty.place(relx=0.5,rely=0.35,anchor=CENTER)
        self.box.place(relx=0.5,rely=0.42,anchor=CENTER)
        self.temperatureButton.place(relx=0.25,rely=0.55,anchor=CENTER)
        self.humidityButton.place(relx=0.5,rely=0.55,anchor=CENTER)
        self.pressureButton.place(relx=0.75,rely=0.55,anchor=CENTER)
        self.mainloop()
    
    def getTemperature(self):
        self.boxValue = int(self.box.get())
        self.temperatureButton.place_forget()
        self.humidityButton.place_forget()
        self.pressureButton.place_forget()
        self.qty.place_forget()
        self.box.place_forget()
        self.frame = ttk.Frame(self,borderwidth=5,relief="raised",padding=(10,10))
        self.frame.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.returnButton.place(relx=0.5,rely=0.8,anchor=CENTER)
        column1Title = ttk.Label(self.frame,text='Temperature')
        column2Title = ttk.Label(self.frame,text='Date')
        column1Title.grid(column=0,row=0,padx=10,pady=10)
        column2Title.grid(column=1,row=0,padx=10,pady=10)
        queryString : str = "http://localhost:8080/values/?type=temperature&size=" + str(self.boxValue)
        data = requests.get(url = queryString)
        response : str = data.text
        Temperature = []
        date = []
        print(response)
        for x in range(self.boxValue):
            Temperature.append(response[response.find(":") + 1 : response.find(",")])
            date.append(response[response.find("\"time\":") + len("\"time\":\"") : response.find("\"}")])
            response = response[response.find("}")+2:]
        for x in range(self.boxValue):
            column0 = ttk.Label(self.frame,text=Temperature[x])
            column1 = ttk.Label(self.frame,text=date[x])
            column0.grid(column=0,row=x+1,padx=10,pady=10)
            column1.grid(column=1,row=x+1,padx=10,pady=10)


    def getHummidity(self):
        self.boxValue = int(self.box.get())
        self.temperatureButton.place_forget()
        self.humidityButton.place_forget()
        self.pressureButton.place_forget()
        self.qty.place_forget()
        self.box.place_forget()
        self.frame = ttk.Frame(self,borderwidth=5,relief="raised",padding=(10,10))
        self.frame.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.returnButton.place(relx=0.5,rely=0.8,anchor=CENTER)
        column1Title = ttk.Label(self.frame,text='Humidity')
        column2Title = ttk.Label(self.frame,text='Date')
        column1Title.grid(column=0,row=0,padx=10,pady=10)
        column2Title.grid(column=1,row=0,padx=10,pady=10)
        queryString : str = "http://localhost:8080/values/?type=humidity&size=" + str(self.boxValue)
        data = requests.get(url = queryString)
        response : str = data.text
        Humidity = []
        date = []
        for x in range(self.boxValue):
            Humidity.append(response[response.find(":") + 1 : response.find(",")])
            date.append(response[response.find("\"time\":") + len("\"time\":\"") : response.find("\"}")])
            response = response[response.find("}")+2:]
        for x in range(self.boxValue):
            column0 = ttk.Label(self.frame,text=Humidity[x])
            column1 = ttk.Label(self.frame,text=date[x])
            column0.grid(column=0,row=x+1,padx=10,pady=10)
            column1.grid(column=1,row=x+1,padx=10,pady=10)  


    def getPressure(self):
        self.boxValue = int(self.box.get())
        self.temperatureButton.place_forget()
        self.humidityButton.place_forget()
        self.pressureButton.place_forget()
        self.qty.place_forget()
        self.box.place_forget()
        self.frame = ttk.Frame(self,borderwidth=5,relief="raised",padding=(10,10))
        self.frame.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.returnButton.place(relx=0.5,rely=0.8,anchor=CENTER)
        column1Title = ttk.Label(self.frame,text='Pressure')
        column2Title = ttk.Label(self.frame,text='Date')
        column1Title.grid(column=0,row=0,padx=10,pady=10)
        column2Title.grid(column=1,row=0,padx=10,pady=10)
        queryString : str = "http://localhost:8080/values/?type=pressure&size=" + str(self.boxValue)
        data = requests.get(url = queryString)
        response : str = data.text
        Pressure = []
        date = []
        print(response)
        for x in range(self.boxValue):
            Pressure.append(response[response.find(":") + 1 : response.find(",")])
            date.append(response[response.find("\"time\":") + len("\"time\":\"") : response.find("\"}")])
            response = response[response.find("}")+2:]
        for x in range(self.boxValue):
            column0 = ttk.Label(self.frame,text=Pressure[x])
            column1 = ttk.Label(self.frame,text=date[x])
            column0.grid(column=0,row=x+1,padx=10,pady=10)
            column1.grid(column=1,row=x+1,padx=10,pady=10)

    def goBack(self):
        self.returnButton.place_forget()
        self.frame.destroy()
        self.temperatureButton.place(relx=0.25,rely=0.5,anchor=CENTER)
        self.humidityButton.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.pressureButton.place(relx=0.75,rely=0.5,anchor=CENTER)
        self.qty.place(relx=0.5,rely=0.35,anchor=CENTER)
        self.box.place(relx=0.5,rely=0.42,anchor=CENTER)


def main():
    app = Aplication('Estación Meteorologica')
    return 0

if __name__ == '__main__':
    main()
