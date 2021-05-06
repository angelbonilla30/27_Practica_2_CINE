from tkinter import *
from tkinter import ttk
import cine_database

window = Tk()
frame_app = Frame(window, width=400, height=600, bg="red")
frame_app.pack()

pelicula = StringVar()
hora = StringVar()
fecha = StringVar()
idioma = StringVar()



def crear_sala():
    pelicula = entry_pelicula.get()
    hora = entry_hora.get()
    fecha = entry_fecha.get()
    idioma = entry_idioma.get()
    
    cine_db = cine_database.MyDatabase()
    data = (pelicula, hora, fecha, idioma)
    print(data)
    cine_db.insert_db(pelicula, hora, fecha, idioma)

frame_navbar = Frame(frame_app, width=400, height=100)
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=400, height=150)
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=400, height=500)
frame_options.grid(row=2, column=0)

frame_food = Frame(frame_options, width=350, height=500, bg="#d48df0")
frame_food.place(x=25, y=30)
label_pelicula = Label(frame_food, 
              text="Pelicula:",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#d48df0")
label_pelicula.place(x=20, y=60)
entry_pelicula = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_pelicula.place(x=20, y=100)
label_hora = Label(frame_food, 
              text="Hora:",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#d48df0")
label_hora.place(x=20, y=130)
entry_hora = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_hora.place(x=20, y=170)
label_fecha = Label(frame_food, 
              text="Fecha:",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#d48df0")
label_fecha.place(x=20, y=200)
entry_fecha = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_fecha.place(x=20, y=240)

label_idioma = Label(frame_food, 
              text="Idioma:",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#d48df0")
label_idioma.place(x=20, y=270)
entry_idioma = Entry(frame_food, justify=LEFT, width=30, font=("Calibri", "14", "bold"))
entry_idioma.place(x=20, y=310)


button_agregar = Button(frame_food, text="Crear Cartelera", command=crear_sala, font=("Calibri", "14", "bold"))
button_agregar.place(x=20, y=350)

title = Label(frame_navbar, text="CINE LOVE",
              font=("Century Gothic", "14"))
title.place(x=280, y=40)


title1 = Label(frame_title, 
             text="CARTELERAS DE CINE", 
              font=("Century Gothic", "22", "bold"),
              justify=LEFT)
title1.place(x=25, y=10)
title2 = Label(frame_title, 
              text="Todos los campos son obligartorios.", 
              font=("Century Gothic", "14"),justify=LEFT)
title2.place(x=25, y=50)

window.mainloop()