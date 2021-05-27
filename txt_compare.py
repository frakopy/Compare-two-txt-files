import  tkinter as tk
from tkinter import font
from PIL import Image,ImageTk
from tkinter import filedialog, messagebox
import os, re


class Ventana_Principal():
    
    def __init__(self):
        '''This class configures and populates the rootlevel window.
        root is the rootlevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family {Segoe UI} -size 11 -weight bold"
        font9 = "-family {Segoe UI} -size 14 -weight bold"

        self.DIR_ESCRITORIO = 'C:/Users/FRANK BOJORQUEZ/Desktop'
        self.dir_resultado = 'D:/A_PYTHON/ProgramasPython/Control_NodosCA/Alarm_Comparer/Alarmas/Resultado.txt'

        self.archivo1 = ''
        self.archivo2 = ''

        #Se crea el archivo donde se guardaran los resultados de las diferencias
        self.resultado = open(self.dir_resultado,'w')
        self.resultado.close()

        self.root = tk.Tk()
        self.root.geometry("600x466")
        self.root.resizable(0, 0)
        self.root.iconbitmap('comparacion.ico')
        self.root.wm_attributes('-alpha', 0.8) #Para darle transparanecia a la ventana
        self.root.title("ALARM COMPARER CREADO POR FRANCISCO BOJORQUE")
        self.root.configure(background="black")

        self.Etiqueta_titulo = tk.Label(self.root)
        self.Etiqueta_titulo.place(relx=0.233, rely=0.020, height=52, width=314)
        self.Etiqueta_titulo.configure(background="black")
        self.Etiqueta_titulo.configure(disabledforeground="#a3a3a3")
        self.Etiqueta_titulo.configure(font=font9)
        self.Etiqueta_titulo.configure(foreground="white")
        self.Etiqueta_titulo.configure(text='Selecciona los Archivos a Comparar')

        self.B_file1 = tk.Button(self.root, command=self.cargar_file1)
        self.B_file1.place(relx=0.08, rely=0.150, height=44, width=500)
        self.B_file1.configure(activebackground="#ececec")
        self.B_file1.configure(activeforeground="#000000")
        self.B_file1.configure(background="#00ca00")
        self.B_file1.configure(disabledforeground="#a3a3a3")
        self.B_file1.configure(font=font11)
        self.B_file1.configure(foreground="#000000")
        self.B_file1.configure(highlightbackground="#d9d9d9")
        self.B_file1.configure(highlightcolor="black")
        self.B_file1.configure(pady="0")
        self.B_file1.configure(text='''Archivo Antiguo''')

        self.B_file2 = tk.Button(self.root, command=self.cargar_file2)
        self.B_file2.place(relx=0.08, rely=0.290, height=44, width=500)
        self.B_file2.configure(activebackground="#ececec")
        self.B_file2.configure(activeforeground="#000000")
        self.B_file2.configure(background="#00ca00")
        self.B_file2.configure(disabledforeground="#a3a3a3")
        self.B_file2.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.B_file2.configure(foreground="#000000")
        self.B_file2.configure(highlightbackground="#d9d9d9")
        self.B_file2.configure(highlightcolor="black")
        self.B_file2.configure(pady="0")
        self.B_file2.configure(text='''Archivo Actual''')

        #Se carga una imagen en la variable img para agregarla mas adelante al boton comparar
        self.img = Image.open('start.png')
        self.img = self.img.resize((125, 115), Image.ANTIALIAS) # Redimension (Ancho, Alto)
        self.img = ImageTk.PhotoImage(self.img)

        self.B_comparar = tk.Button(self.root,image=self.img, command=self.compara,borderwidth=0)
        self.B_comparar.place(relx=0.370, rely=0.430, height=120, width=135)
        self.B_comparar.configure(activebackground="#ececec")
        self.B_comparar.configure(activeforeground="#000000")
        self.B_comparar.configure(background="black")
        self.B_comparar.configure(disabledforeground="#a3a3a3")
        self.B_comparar.configure(foreground="#000000")
        self.B_comparar.configure(highlightbackground="#d9d9d9")
        self.B_comparar.configure(highlightcolor="black")
        self.B_comparar.configure(pady="0")

        #Se carga una imagen en la variable img para agregarla mas adelante al boton comparar
        self.imagen = Image.open('open_File2.png')
        self.imagen = self.imagen.resize((100, 95), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.imagen = ImageTk.PhotoImage(self.imagen)

        self.B_abrir = tk.Button(self.root,command=self.abrir_arrchivo,image=self.imagen,borderwidth=0)
        self.B_abrir.place(relx=0.415, rely=0.740, height=93, width=100)
        self.B_abrir.configure(activebackground="#ececec")
        self.B_abrir.configure(activeforeground="#000000")
        self.B_abrir.configure(background="black")
        self.B_abrir.configure(disabledforeground="#a3a3a3")
        self.B_abrir.configure(foreground="#000000")
        self.B_abrir.configure(highlightbackground="#d9d9d9")
        self.B_abrir.configure(highlightcolor="black")
        self.B_abrir.configure(pady="0")


        self.root.mainloop()

    def abrir_arrchivo(self):
        os.startfile(self.dir_resultado)

    def cargar_file1(self):
        
        self.archivo1 = filedialog.askopenfilename(initialdir=self.DIR_ESCRITORIO, filetypes=[('Archivos TXT', '*.txt')])
        
        if self.archivo1 == '':
            self.B_file1.configure(text='Archivo Antiguo')
            self.B_file2.configure(text='Archivo Actual')
            messagebox.showinfo('Aviso','No se selecciono ningún archivo')
        else:
            self.nombre_archivo1 = self.archivo1.split('/')[-1]
            self.B_file1.configure(text=self.nombre_archivo1)

    def cargar_file2(self):

        self.archivo2 = filedialog.askopenfilename(initialdir=self.DIR_ESCRITORIO, filetypes=[('Archivos TXT', '*.txt')])
        
        if self.archivo2 == '':
            self.B_file1.configure(text='Archivo Antiguo')
            self.B_file2.configure(text='Archivo Actual')
            messagebox.showinfo('Aviso','No se selecciono ningún archivo')
        
        else:
            self.nombre_archivo2 = self.archivo2.split('/')[-1]
            self.B_file2.configure(text=self.nombre_archivo2)

    def compara(self):

        if self.archivo1 and self.archivo2:

            #Modificamos el texto del label para informar que se estan comparando los archivos
            self.Etiqueta_titulo.configure(text='Comparando archivos!!!')
            
            #Creamos diferentes patrones para utilizarlos en la eliminacion de las fechas y horas de las Alarmas
            #con esto solo estariamos comparando el contenido de las Alarmas y asi evitarnos falsos positivos
            #en los casos cuando se actualizan las horas y fechas de las alarmas por los reinicios de los nodos.
            patron_vpni2kv3 = r'\d+/\d+/\d+\s\d+:\d+:\d+\s\w\w\s-05:00'
            patron_pps = r'\d+/\d+/\d+\s\d+:\d+:\d+'
            patron_mgw_vpni2kv5_stp = r'\d+-\d+-\d+\s+\d+:\d+:\d+'
            patron_msc = r'\d{6}\s{3}\d{4}'

            patron_fecha_hora = patron_pps+'|'+patron_vpni2kv3+'|'+patron_mgw_vpni2kv5_stp+'|'+patron_msc

            #Comparamos cada linea del archivo actual contra todas las lineas del archivo antiguo para validar si existe
            #nueva informacion en el archivo actual y si es asi la escribimos en un archivo de texto
            with open(self.archivo2, 'r') as archivo_actual:
                with open(self.archivo1, 'r') as archivo_antiguo:
                    with open (self.dir_resultado, "w") as out_file:
                        lineas_archivo_antiguo = archivo_antiguo.read()
                        lineas_archivo_antiguo = re.sub(patron_fecha_hora, '', lineas_archivo_antiguo)
                        for linea in archivo_actual:
                            linea = re.sub(patron_fecha_hora, '', linea)#Reemplazamos el texto de fecha y hora por nada
                            if linea not in lineas_archivo_antiguo:
                                out_file.write(linea)

            #Abrimos una ventana emergente para informar de la finalización de la comparación de los archivos
            self.respuesta=messagebox.askyesno('Comparación finalizada','¿Desea abrir el archivo?')

            #Cambiamos el texto de los botones al texto original en caso que se desee realizar una nueva comparación
            self.B_file1.configure(text='Archivo Antiguo')
            self.B_file2.configure(text='Archivo Actual')

            #Modificamos el texto del label con su texto original
            self.Etiqueta_titulo.configure(text='Selecciona los Archivos a Comparar')
            
            #Si la respuesta para la pregunta realizada por medio del messagebox es positiva entonces 
            #abrimos el archivo con los resultados de la comparación
            if self.respuesta:
                os.startfile(self.dir_resultado)

        else:
            self.B_file1.configure(text='Archivo Antiguo')
            self.B_file2.configure(text='Archivo Actual')
            messagebox.showerror('ERROR','Debes seleccionar 2 archivos para comparar')

if __name__ == "__main__":
    v = Ventana_Principal()

