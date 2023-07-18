import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):

        vuelta = True
        negativo = 0
        positivo = 0
        cant_negativo = 0
        cant_positivo = 0
        cant_zero = 0

        while vuelta:
            char = prompt("Ingresar","Valor:")
            if char==None:
                break
            if char == "": ## or not char.isnumeric()
                alert("Alerta!!", "Debe Ingresar un numero")
                continue
            
            val = int(char)

            match val:
                case _ as value if value < 0 :
                    negativo += val
                    #negativo -= val
                    cant_negativo += 1
                case _ as value if value > 0 :
                    positivo += val
                    cant_positivo += 1
                case 0:
                    cant_zero += 1

        dif = positivo - negativo

        alert("Resultados","negativos=" + str(negativo) + " (cant:" + str(cant_negativo) + ") / positivos=" + str(positivo) + " (cant:" + str(cant_positivo) + ") / diferencia entre ambos=" + str(dif) + " / cant ceros=" + str(cant_zero))
                
        alert("Alerta!!", "FIN")

        pass

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
