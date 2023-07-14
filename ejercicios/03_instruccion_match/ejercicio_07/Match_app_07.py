import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Enunciado:
Obtener el destino seleccionado en el combobox_destino, luego al presionar el 
botón ‘Informar’ indicar el punto cardinal de nuestro país donde se encuentra: 
Norte, Sur, Este u Oeste
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Ushuaia']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):

        dest = self.combobox_destino.get()

        match dest:
            case 'Bariloche':
                mensaje = "Esta en el Oeste"
            case 'Mar del plata':
                mensaje = "Esta en el Este"
            case 'Cataratas':
                mensaje = "Esta en el Norte"
            case 'Ushuaia':
                mensaje = "Esta en el Sur"
       
        alert("Alerta!!",mensaje)
    
        pass
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()