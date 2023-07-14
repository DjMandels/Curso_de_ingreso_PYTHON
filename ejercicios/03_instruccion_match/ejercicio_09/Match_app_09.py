import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata       tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):

        dest = self.combobox_destino.get()
        estaciones = self.combobox_estaciones.get()
        viaje = 15000
        
        match estaciones:
            case 'Invierno':
                
                match dest:
                    case 'Bariloche':
                        mensaje = "aumento del 20%"
                        calculo = 1
                        valor= 20
                    case 'Mar del plata':
                        mensaje = "descuento del 20%"
                        calculo = 0
                        valor= 20
                    case other:
                        mensaje = "descuento del 10%"
                        calculo = 0
                        valor= 10
         
            case 'Verano':
                
                match dest:
                    case 'Bariloche':
                        mensaje = "descuento del 20%"
                        calculo = 0
                        valor= 20
                    case 'Mar del plata':
                        mensaje = "aumento del 20%"
                        calculo = 1
                        valor= 20
                    case other:
                        mensaje = "aumento del 10%"
                        calculo = 1
                        valor= 10

            case other:
                
                match dest:
                    case 'Cordoba':
                        mensaje = "precio sin descuento"
                        calculo = 3
                        valor = 1
                    case _:
                        mensaje = "aumento del 10%"
                        calculo = 1
                        valor= 10
             
        tarifa = viaje * valor / 100      
        
        match calculo:
            case 1:
                #aumento
                total = viaje + tarifa
                print("11")
            case 0:
                #descuento
                total = viaje - tarifa
                print("22")
            case _:
                #igual
                print("33")
                total = viaje

        
        alert("Alerta!!","Tiene un " + mensaje + ", total=" + str(total))
        
        pass
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()