from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox
from PyDictionary import PyDictionary
from google_trans_new import google_translator


root = Tk()
root.title("READ ENGLISH BOOK AND STUDY ENGLISH (REBASE)")
root.resizable(width=True,height=True)
root.iconbitmap("North2.ico")

archivotexto_nombre_resolucion_pantalla=open("memory/resolucion_pantalla.txt",encoding="utf8")
resolucion_pantalla=archivotexto_nombre_resolucion_pantalla.read()
archivotexto_nombre_resolucion_pantalla.close()


#size=float(resolucion_pantalla)
size=int(resolucion_pantalla)

size_options=["1366X768","1920x1080"]

save_words_setence_options=["SENTENCE","WORD"]

lista_textos=os.listdir(r"texto_lectura")
lista_fondo_pantalla=os.listdir(r"images")

if size == 1:
        miCanvas=Canvas(root, width=1366, height=768)
        miCanvas.pack()
else:
        miCanvas=Canvas(root, width=1920, height=1080)
        miCanvas.pack()        

my_img=None
#texto_ENG=None

lista_texto=[]
#lista_fondo_pantalla=[]

camino_carpeta_images="images/"

archivotexto_nombre_fondo_panatalla=open("memory/nombre_fondo_pantalla.txt",encoding="utf8")
fondo_pantalla = camino_carpeta_images+archivotexto_nombre_fondo_panatalla.read()
archivotexto_nombre_fondo_panatalla.close()

background_image = PhotoImage(file=str(fondo_pantalla))
background_label = Label(root, image=background_image).place(relwidth=1, relheight=1)

def home():
        
        if size == 1:
#1.0------------------------------- Titulo Pagina Inicio -------------------------------------------
                titulo=Label(background_label, text="WELCOME TO REBASE", font=("Bookman Old Style",round(20)),bg="#e8dabd")
                titulo.place(x=450, y=10)
                titulo=Label(background_label, text=" READ ENGLISH BOOK AND STUDY ENGLISH", font=("Bookman Old Style",round(20)),bg="#e8dabd")
                titulo.place(x=320, y=50)
                titulo=Label(background_label, text=" PLEASE, CHOOSE AN OPTION", font=("Bookman Old Style",round(20)),bg="#e8dabd")
                titulo.place(x=410, y=90)                
#1.1 ------------------------------- Ventana Modo Lectura -------------------------------------------
                def window_read():
                        global my_img
                        global save_words_setence_options
                        

                        root.withdraw()
                        ventana_lectura=Toplevel()
                        if  size == 1:
                                screen_size="1366x768"
                        elif size == 0:
                                screen_size="1680x1050"
                        

                        ventana_lectura.geometry(screen_size)
                        my_img = ImageTk.PhotoImage(Image.open(fondo_pantalla))
                        my_label = Label(ventana_lectura, image=my_img).place(relwidth=1, relheight=1)

                        texto_contiene_titulo=open("memory/titulo_texto.txt",encoding="utf8")
                        almacena_titulo=texto_contiene_titulo.read()
                        texto_contiene_titulo.close()

                        texto_contiene_page_marker=open("memory/page_marker.txt",encoding="utf8")
                        almacena_page_marker=texto_contiene_page_marker.read()
                        texto_contiene_page_marker.close()

                        clicked_read=StringVar()
                        clicked_read.set(save_words_setence_options[0])

                        drop_read_save=OptionMenu(ventana_lectura,clicked_read, *save_words_setence_options)
                        drop_read_save.place(x=round(200),y=round(560))
                        drop_read_save.config(width=round(10), font=("Book Old Style", round(10),"bold"))

                        clicked_texto=StringVar()
                        clicked_texto.set(lista_textos[0])

                        drop_text=OptionMenu(ventana_lectura,clicked_texto, *lista_textos)
                        drop_text.place(x=round(600), y=round(125))
                        drop_text.config(width=round(20), font=("Book Old Style", round(10),"bold"))

#1.1 ------------------------------- Funciones Modo Lectura -------------------------------------------
                        def texto_inicio():
                                num_lista=contador.get()
                                camino_texto_lectura="texto_lectura/"+almacena_titulo
                                abrir_texto_inicio=open(camino_texto_lectura, encoding="utf8")
                                for line in abrir_texto_inicio:                
                                        line=line.split(".")
                                        line=line[int(num_lista)]
                                        line=line[1:]
                                        texto_ENG.insert(END, line)
                                abrir_texto_inicio.close
                        def ingresar_texto():
                                
                                texto_nuevo=nombre_texto.get()
                                camino_texto_lectura="texto_lectura/"+texto_nuevo
                                abrir_texto=open(camino_texto_lectura, encoding="utf8")
                                lectura_libro_texto=abrir_texto.read()
                                abrir_texto.close

                                texto_contiene_titulo2=open("memory/titulo_texto.txt","w")
                                texto_contiene_titulo2.write(nombre_texto.get())
                                texto_contiene_titulo2.close()
                                
                                messagebox.showinfo("REABSE"," El texto ha sido cambiado por \n\n"+nombre_texto.get()+"\n\n")

                        def spanish_translate_text():
                                cntrl=0
                                while cntrl==0:
                                        num_lista=contador.get()
                                        camino_texto_lectura="texto_lectura/"+almacena_titulo
                                        abrir_texto=open(camino_texto_lectura, encoding="utf8")
                                        
                                        try:
                                                for line in abrir_texto:
                                                        line=line.rstrip("\n")                
                                                        line=line.split(".")
                                                        linea_Esp=line[int(num_lista)]
                                                        translator=google_translator()
                                                        translation=translator.translate(linea_Esp,lang_src="en", lang_tgt="es")
                                                        texto_ESP.insert(END, translation)
                                        except:
                                                texto_ESP.insert(END,0)
                                        abrir_texto.close()
                                        recoger_respuesta=int(texto_ESP.get(1.0,END))
                                        if recoger_respuesta == 0:
                                                cntrl+=0
                                                texto_ESP.delete(1.0,END)
                                        else:
                                                cntrl+=1
                                                

                        def next_line():
                                texto_ESP.delete(1.0,END)
                                texto_ENG.delete(1.0,END)
                                cuadro_save_words_setence.delete(0,END)
                                dictionary_text.delete(0,END)
                                num_lista=contador.get()
                                siguiente=int(num_lista)+1
                                contador.delete(0,END)
                                contador.insert(0,siguiente)

                                camino_texto_lectura="texto_lectura/"+almacena_titulo
                                abrir_texto_inicio=open(camino_texto_lectura, encoding="utf8")

                                for line in abrir_texto_inicio:                
                                        line=line.split(".")
                                        line=line[siguiente]
                                        line=line[1:]
                                        texto_ENG.insert(END, line)
                                abrir_texto_inicio.close

                        
                        def previous_line():
                                texto_ESP.delete(1.0,END)
                                texto_ENG.delete(1.0,END)
                                cuadro_save_words_setence.delete(0,END)
                                dictionary_text.delete(0,END)
                                num_lista=contador.get()
                                anterior=int(num_lista)-1
                                contador.delete(0,END)
                                contador.insert(0,anterior)

                                camino_texto_lectura="texto_lectura/"+almacena_titulo
                                abrir_texto_inicio=open(camino_texto_lectura, encoding="utf8")

                                for line in abrir_texto_inicio:                
                                        line=line.split(".")
                                        line=line[anterior]
                                        line=line[1:]
                                        texto_ENG.insert(END, line)
                                abrir_texto_inicio.close
                        
                        def english_dictionary():

                                dictionary_word=PyDictionary()
                                meaning_word = dictionary_text.get()
                                result=dictionary_word.meaning(meaning_word)                                                
                                messagebox.showinfo("REABSE"," DICTIONARY  \n\n"+str(result))
                        
                        def page_marker():
                                
                                marcador_pagina=open("memory/page_marker.txt","w")
                                marcador_pagina.write(contador.get())
                                messagebox.showinfo("English Assitant"," El marcador de página \n\n"+contador.get()+"\n\n ha sido guardado ")
                                marcador_pagina.close()

                        def save_word_sentence():
                                save_words_setence_options=["SENTENCE","WORD"]
                                if clicked_read.get() == "SENTENCE":
                                        
                                        sentencia_para_estudiar=open("memory/sentencias_para_estudiar.txt","w")
                                        sentencia_para_estudiar.write("\n")
                                        sentencia_para_estudiar.write(cuadro_save_words_setence.get())
                                        messagebox.showinfo("English Assitant"," La Sentencia \n\n"+cuadro_save_words_setence.get()+"\n\n fue incluida ")
                                        sentencia_para_estudiar.close()

                                elif clicked_read.get() == "WORD":
                                        palabra_para_estudiar=open("memory/palabras_para_estudiar.txt","w")
                                        palabra_para_estudiar.write("\n")
                                        palabra_para_estudiar.write(cuadro_save_words_setence.get())
                                        messagebox.showinfo("English Assitant"," La Palabra \n\n"+cuadro_save_words_setence.get()+"\n\n fue incluida ")
                                        palabra_para_estudiar.close()

                #1 ------------------------------- Botones Modo Lectura -------------------------------------------
                        
                        button_save_word_setence=Button(ventana_lectura,text="SAVE WORD/SENTENCE ",font=("Bookman Old Style",round(10),"bold"), command=save_word_sentence)
                        button_save_word_setence.place(x=round(550),y=round(520))
                        button_save_word_setence.config(width=20)

                        button_spanish_translate_text=Button(ventana_lectura,text="VER TRADUCCIÓN ",font=("Bookman Old Style",round(10),"bold"), command=spanish_translate_text)
                        button_spanish_translate_text.place(x=round(50),y=round(390))
                        button_spanish_translate_text.config(bg="#FACC2E", width=15)

                        button_texto_inicio=Button(ventana_lectura,text="DAR INICO ",font=("Bookman Old Style",round(10),"bold"),command=texto_inicio)
                        button_texto_inicio.place(x=round(50),y=round(200))
                        button_texto_inicio.config(bg="#FACC2E", width=15)
                        
                        button_page_marker=Button(ventana_lectura, text="PAGE MARKER",font=("Bookman Old Style",round(10),"bold"),width=12 , command=page_marker)
                        button_page_marker.place(x=round(220), y=round(320))
                        button_page_marker.config(bg="#FACC2E")
                        
                        button_english_dictionary=Button(ventana_lectura, text="ENGLISH DICTIONARY",font=("Bookman Old Style",round(10),"bold"),width=20 , command=english_dictionary)
                        button_english_dictionary.place(x=round(670), y=round(320))
                        
                        button_ingresar_texto=Button(ventana_lectura,text="APPLY NEW TEXT",font=("Bookman Old Style",round(10),"bold") , command=ingresar_texto)
                        button_ingresar_texto.place(x=round(400), y=round(125))

                        button_next_line=Button(ventana_lectura, text="NEXT",font=("Bookman Old Style",round(10),"bold"),width=round(10) , command=next_line)
                        button_next_line.place(x=round(555), y=round(320))

                        button_previous_line=Button(ventana_lectura, text="PREVIOUS",font=("Bookman Old Style",round(10),"bold"),width=round(10) , command=previous_line)
                        button_previous_line.place(x=round(375), y=round(320))

                        button_quit = Button(ventana_lectura, text="Exit Program",font=("Bookman Old Style",round(10),"bold") , command=root.quit)
                        button_quit.place(x=round(550), y=round(610))

                #1 ------------------------------- Cuadro texto Modo Lectura -------------------------------------------

                        cuadro_save_words_setence=Entry(ventana_lectura, width=round(75), borderwidth=round(5), justify="left")
                        cuadro_save_words_setence.place(x=round(320), y=round(560))
                        cuadro_save_words_setence.config(font=("Bookman Old Style",round(12),"bold"))

                        nombre_texto=Entry(ventana_lectura, width=round(35), borderwidth=round(5), justify="center")
                        nombre_texto.place(x=round(400), y=round(85))
                        nombre_texto.config(font=("Bookman Old Style",round(12),"bold"))
                        nombre_texto.insert(0,almacena_titulo)
                        #recoger_nombre_texto=nombre_texto.get()

                        dictionary_text=Entry(ventana_lectura, width=round(25), borderwidth=round(5), justify="center")
                        dictionary_text.place(x=round(870), y=round(320))
                        dictionary_text.config(font=("Bookman Old Style",round(12),"bold"))

                        texto_ENG=Text(ventana_lectura, width=round(105), height=round(4), font=("Helvetica",round(12),"bold"),borderwidth=round(5))
                        texto_ENG.place(x=round(200),y=round(200))
                        #texto_ENG.insert(END, lista_texto[])

                        texto_ESP=Text(ventana_lectura, width=round(105), height=round(4), font=("Helvetica",round(12),"bold"),borderwidth=round(5))
                        texto_ESP.place(x=round(200),y=round(390))

                        contador = Entry(ventana_lectura, width=5, borderwidth=5, justify="center")
                        contador.place(x=round(485) , y=round(320))
                        contador.config(font=("Bookman Old Style",round(10),"bold"))
                        contador.insert(0,almacena_page_marker)
                                
                #1 ------------------------------- Titulo Modo Lectura -------------------------------------------
                        titulo=Label(ventana_lectura, text="READING MODE REBASE", font=("Bookman Old Style",round(20)), bg="#e8dabd")
                        titulo.place(x=round(450), y=round(10))
                        titulo_texto=Label(ventana_lectura, text="TITLE OF THE TEXT",font=("Bookman Old Style",round(10),"bold"),bg="#FACC2E")
                        titulo_texto.place(x=round(525), y=round(55))

                #1------------------------------- Etiquetas Modo Lectura -------------------------------------------

                        text_save_as=Label(ventana_lectura,text="SAVE AS",font=("Bookman Old Style",round(10),"bold"))
                        text_save_as.place(x=round(200),y=round(520))
                        text_save_as.config(bg="#FACC2E", width=15)

                #2 ------------------------------- Ventana Modo Estudio -------------------------------------------
                def window_study():
                        return
                #3 ------------------------------- Ventana Configuración -------------------------------------------
                #3 ------------------------------- Funciones Configuracióm -------------------------------------------
                def configuracion():
                        global my_img
                        
                        root.withdraw()
                        ventana_configuracion=Toplevel()
                        if size == 1:
                                screen_size="1366x768"
                        elif size == 0:
                                screen_size="1920x1080"                        
                        
                        ventana_configuracion.geometry(screen_size)
                        archivotexto_nombre_fondo_panatalla=open("memory/nombre_fondo_pantalla.txt",encoding="utf8")
                        fondo_pantalla = camino_carpeta_images+archivotexto_nombre_fondo_panatalla.read()
                        archivotexto_nombre_fondo_panatalla.close()

                        my_img = ImageTk.PhotoImage(Image.open(fondo_pantalla))
                        my_label = Label(ventana_configuracion, image=my_img).place(relwidth=1, relheight=1)

                        def cambiar_fondo():
                                

                                archivotexto_nombre_fondo_panatalla=open("memory/nombre_fondo_pantalla.txt","w")
                                fondo_pantalla=archivotexto_nombre_fondo_panatalla.write(str(clicked_fondo_pantalla.get()))
                                archivotexto_nombre_fondo_panatalla.close()

                                #archivotexto_nombre_fondo_panatalla=open("memory/nombre_fondo_pantalla.txt",encoding="utf8")
                                #fondo_pantalla = camino_carpeta_images+archivotexto_nombre_fondo_panatalla.read()
                                #archivotexto_nombre_fondo_panatalla.close()
                                messagebox.showinfo("REABSE"," El fondo de pantalla ha sido cambiado por \n\n"+clicked_fondo_pantalla.get()+"\n\n Cierre el programa y vuela a abrirlo para ver cambios ")
                                ventana_configuracion.destroy()
                                configuracion()

                        def size_selection():
                                global size
                                #election_size = Label(ventana_configuracion, text=clicked.get())
                                if clicked.get() == "1366x768": 
                                        size=1
                                elif clicked.get() == "1920x1080":
                                        size=0
                                
                                archivotexto_nombre_resolucion_pantalla=open("memory/resolucion_pantalla_x.txt","w")            
                                resolucion_pantalla_x=archivotexto_nombre_resolucion_pantalla.write(str())
                                archivotexto_nombre_resolucion_pantalla.close()

                                messagebox.showinfo("REABSE"," La resolucion de pantalla ha sido cambiado a \n\n"+clicked.get()+"\n\n Cierre el programa y vuela a abrirlo para ver cambios ")
                                ventana_configuracion.destroy()
                                configuracion()

                        
                #3 ------------------------------- Titulo Modo Lectura -------------------------------------------
                        titulo=Label(ventana_configuracion, text="SET CONFIGURATION REBASE", font=("Bookman Old Style",round(20)),bg="#e8dabd")
                        titulo.place(x=round(450), y=(10))      

                        clicked = StringVar()
                        clicked.set(size_options[0])
                        
                        drop= OptionMenu(ventana_configuracion, clicked, *size_options)
                        drop.place(x=round(350), y=round(400))
                        drop.config(width=round(50), font=("Bookman Old Style",round(10),"bold"))

                        clicked_fondo_pantalla=StringVar()
                        clicked_fondo_pantalla.set(lista_fondo_pantalla[0])

                        drop_fondo_pantalla=OptionMenu(ventana_configuracion,clicked_fondo_pantalla, *lista_fondo_pantalla)
                        drop_fondo_pantalla.place(x=round(350), y=round(200))
                        drop_fondo_pantalla.config(width=round(60), font=("Book Old Style", round(10),"bold"))
                
                #3 ------------------------------- Botones Configuración -------------------------------------------

                        boton_aplicar_fondo_pantalla=Button(ventana_configuracion, text=("APPLY WALLPAPER"),font=("Bookman Old Style",round(10),"bold"),width=round(20),height=round(1), command=cambiar_fondo)
                        boton_aplicar_fondo_pantalla.place(x=round(900), y=round(200))
                        
                        boton_read=Button(ventana_configuracion, text=("READ BOOK/TEXT"),font=("Bookman Old Style",round(10),"bold"),width=round(20),height=round(1), command=window_read)
                        boton_read.place(x=round(400), y=round(600))
                        boton_study=Button(ventana_configuracion, text=("STUDY ENGLISH"),font=("Bookman Old Style",round(10),"bold"), width=round(20),height=round(1),command=window_study)
                        boton_study.place(x=round(700), y=round(600))
                        
                        button_quit = Button(ventana_configuracion, text="Exit Program",font=("Bookman Old Style",round(10),"bold") , command=root.quit)
                        button_quit.place(x=round(600), y=round(650))

                        boton_size_selection=Button(ventana_configuracion, text=("APPLY SIZE RESOLUTION"),font=("Bookman Old Style",round(10),"bold"),width=round(20), command=size_selection)
                        boton_size_selection.place(x=round(900), y=round(400))

                #3 ------------------------------- Cuadro de texto Configuración -------------------------------------------

                        

                #3------------------------------- Etiquetas Ventana Configuración -------------------------------------------

                        texto_set_image_label=Label(ventana_configuracion,text="Set Image's Name Here: ")
                        texto_set_image_label.place(x=round(100),y=round(200))
                        texto_set_image_label.config(bg="#FACC2E", width=round(20), font=("Bookman Old Style",round(12),"bold"))

                        texto_set_image_label=Label(ventana_configuracion,text="Set Resolution Here: ")
                        texto_set_image_label.place(x=round(100),y=round(400))
                        texto_set_image_label.config(bg="#FACC2E", width=round(20), font=("Bookman Old Style",round(12),"bold"))
                        
                #------------------------------- Botones Funciones Ventana inicio -------------------------------------------
                boton_written=Button(background_label, text=("READ BOOK/TEXT"),font=("Bookman Old Style",round(12),"bold"),width=round(18),height=round(2), command=window_read)
                boton_written.place(x=250, y=330)
                boton_listen=Button(background_label, text=("STUDY ENGLISH"),font=("Bookman Old Style",round(12),"bold"), width=round(18),height=round(2),command=window_study)
                boton_listen.place(x=800, y=330)
                button_quit = Button(background_label, text="Exit Program",font=("Bookman Old Style",round(10),"bold") , command=root.quit)
                button_quit.place(x=570, y=600)

                boton_configuracio=Button(background_label, text="SET CONFIGURATION",font=("Bookman Old Style",round(10),"bold"), width=round(20) , command=configuracion)
                boton_configuracio.place(x=535, y=550)
                boton_configuracio.config(bg="#FACC2E")
        else:
                print("hola mundo")

home()

root.mainloop()