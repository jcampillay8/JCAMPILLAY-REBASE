from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox
from PyDictionary import PyDictionary
from google_trans_new import google_translator
import speech_recognition as sr
import random
import pyttsx3
import pyaudio
import time
import webbrowser


root = Tk()

root.title("READ ENGLISH BOOK AND STUDY ENGLISH (REBASE)")
root.resizable(width=True,height=True)
root.iconbitmap("North2.ico")

archivotexto_nombre_resolucion_pantalla=open("memory/resolucion_pantalla.txt",encoding="utf8")
resolucion_pantalla=archivotexto_nombre_resolucion_pantalla.read()
archivotexto_nombre_resolucion_pantalla.close()


#size=float(resolucion_pantalla)
size=int(resolucion_pantalla)
screen_size=None

if size == 1:
        screen_size="1366x768"
elif size==0:
        screen_size="1920x1080"

size_options=["1366x768","1920x1080"]

save_words_setence_options=["SENTENCE","WORD"]

lista_textos=os.listdir(r"texto_lectura")
lista_fondo_pantalla=os.listdir(r"images")
group_w=os.listdir(r"memory\f_words")
grupo_w2=os.listdir(r"memory\f_words")
group_s=os.listdir(r"memory\f_sentences")


if size == 1:
        miCanvas=Canvas(root, width=1366, height=768)
        miCanvas.pack()
else:
        miCanvas=Canvas(root, width=1920, height=1080)
        miCanvas.pack()

my_img=None
#texto_ENG=None

camino_carpeta_images="images/"

archivotexto_nombre_fondo_panatalla=open("memory/nombre_fondo_pantalla.txt",encoding="utf8")
fondo_pantalla = camino_carpeta_images+archivotexto_nombre_fondo_panatalla.read()
archivotexto_nombre_fondo_panatalla.close()

background_image = PhotoImage(file=str(fondo_pantalla))
background_label = Label(root, image=background_image).place(relwidth=1, relheight=1)

def home():

        if size == 1:
#1.0------------------------------- Titulo Pagina Inicio -------------------------------------------
                titulo1=Label(background_label, text="WELCOME TO REBASE", font=("Bookman Old Style",round(20)),bg="#e8dabd")
                titulo1.place(x=450, y=10)
                titulo2=Label(background_label, text=" READ ENGLISH BOOK AND STUDY ENGLISH", font=("Bookman Old Style",round(20)),bg="#e8dabd")
                titulo2.place(x=320, y=50)
                titulo3=Label(background_label, text=" PLEASE, CHOOSE AN OPTION", font=("Bookman Old Style",round(20)),bg="#e8dabd")
                titulo3.place(x=410, y=90)
#1.1.1 ------------------------------- Ventana Modo Lectura -------------------------------------------
                def window_read():
                        global my_img
                        global save_words_setence_options
                        global screen_size

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

#1.1.2 ------------------------------- Funciones Modo Lectura -------------------------------------------

                        def texto_inicio():
                                num_lista=contador.get()
                                camino_texto_lectura="texto_lectura/"+almacena_titulo
                                abrir_texto_inicio=open(camino_texto_lectura, encoding="utf8")
                                for line in abrir_texto_inicio:
                                        line=line.split(".")
                                        line=line[int(num_lista)]
                                        line=line.strip()
                                        texto_ENG.insert(END, line)
                                abrir_texto_inicio.close

                        def ingresar_texto():
                                texto_nuevo=str(clicked_texto.get())
                                camino_texto_lectura="texto_lectura/"+texto_nuevo
                                abrir_texto=open(camino_texto_lectura, encoding="utf8")
                                lectura_libro_texto=abrir_texto.read()
                                abrir_texto.close

                                texto_contiene_titulo2=open("memory/titulo_texto.txt","w")
                                texto_contiene_titulo2.write(clicked_texto.get())
                                texto_contiene_titulo2.close()

                                messagebox.showinfo("REBASE"," El texto ha sido cambiado por \n\n"+clicked_texto.get()+"\n\n")
                                ventana_lectura.destroy()
                                window_read()

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
                                        texto = len(line)
                                        if (texto-siguiente) >= 1:
                                                line=line[siguiente]
                                                line=line.strip()
                                                texto_ENG.insert(END, line)
                                                texto-=1
                                        else:
                                                texto_ENG.insert(END,"END OF TEXT, CONGRATULATION")
                                                texto_ENG.config(bg="#109FEC")
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
                                        line=line.strip()
                                        texto_ENG.insert(END, line)
                                abrir_texto_inicio.close

                        def english_dictionary():

                                dictionary_word=PyDictionary()
                                meaning_word = dictionary_text.get()
                                result=dictionary_word.meaning(meaning_word)
                                messagebox.showinfo("REBASE"," DICTIONARY  \n\n"+str(result))

                        def page_marker():

                                marcador_pagina=open("memory/page_marker.txt","w")
                                marcador_pagina.write(contador.get())
                                messagebox.showinfo("English Assitant"," El marcador de página \n\n"+contador.get()+"\n\n ha sido guardado ")
                                marcador_pagina.close()

                        def save_word_sentence():
                                save_words_setence_options=["SENTENCE","WORD"]
                                if clicked_read.get() == "SENTENCE":

                                        sentencia_para_estudiar=open("memory/f_sentences/new_sentences.txt","w")
                                        sentencia_para_estudiar.write("\n")
                                        sentencia_para_estudiar.write(cuadro_save_words_setence.get())
                                        messagebox.showinfo("English Assitant"," La Sentencia \n\n"+cuadro_save_words_setence.get()+"\n\n fue incluida a new_sentences.txt")
                                        sentencia_para_estudiar.close()

                                elif clicked_read.get() == "WORD":
                                        palabra_para_estudiar=open("memory/f_words/new_words.txt","w")
                                        palabra_para_estudiar.write("\n")
                                        palabra_para_estudiar.write(cuadro_save_words_setence.get())
                                        messagebox.showinfo("English Assitant"," La Palabra \n\n"+cuadro_save_words_setence.get()+"\n\n fue incluida a new_words.txt ")
                                        palabra_para_estudiar.close()

                #1.1.3 ------------------------------- Botones Modo Lectura -------------------------------------------

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

                #1.1.4 ------------------------------- Cuadro texto Modo Lectura -------------------------------------------

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

                #1.1.5 ------------------------------- Titulo Modo Lectura -------------------------------------------
                        titulo=Label(ventana_lectura, text="READING MODE REBASE", font=("Bookman Old Style",round(20)), bg="#e8dabd")
                        titulo.place(x=round(450), y=round(10))
                        titulo_texto=Label(ventana_lectura, text="TITLE OF THE TEXT",font=("Bookman Old Style",round(10),"bold"),bg="#FACC2E")
                        titulo_texto.place(x=round(525), y=round(55))

                #1.1.6------------------------------- Etiquetas Modo Lectura -------------------------------------------

                        text_save_as=Label(ventana_lectura,text="SAVE AS",font=("Bookman Old Style",round(10),"bold"))
                        text_save_as.place(x=round(200),y=round(520))
                        text_save_as.config(bg="#FACC2E", width=15)

#------------------------------------- funciones/Botones Consulta Ventana Palabras -------------------------------------

                        def consulta_elegir_grupo():
                                messagebox.showinfo("REBASE", "Elige un texto de la lista desplegable\nluego le das click en aplicar y la eleccion se habrá cargado")
                        def consulta_page_marker():
                                messagebox.showinfo("REBASE", "Guarda el numero de sentencia,\nasí puedes cerrar el programa y retormarlo más tarde")
                        def consulta_dictionary():
                                messagebox.showinfo("REBASE", "Diccionario soporta solo palabras simples")
                        def consulta_save():
                                messagebox.showinfo("REBASE", "Elige de la lista desplegable\n si guardarlo como una horación o como plabrta\n\nRecuerda que las plabras debe ser singular")

                        button_consulta1 = Button(ventana_lectura, text="?",font=("Bookman Old Style",round(12),"bold"), command=consulta_elegir_grupo, borderwidth=0)
                        button_consulta1.place(x=round(820), y=round(85))
                        button_consulta1.config(bg="#0A43B4", fg="white")

                        button_consulta_page_marker = Button(ventana_lectura, text="?",font=("Bookman Old Style",round(12),"bold"), command=consulta_page_marker, borderwidth=0)
                        button_consulta_page_marker.place(x=round(345), y=round(320))
                        button_consulta_page_marker.config(bg="#0A43B4", fg="white")

                        button_consulta_dictionary = Button(ventana_lectura, text="?",font=("Bookman Old Style",round(12),"bold"), command=consulta_dictionary, borderwidth=0)
                        button_consulta_dictionary.place(x=round(1160), y=round(320))
                        button_consulta_dictionary.config(bg="#0A43B4", fg="white")

                        button_consulta_save = Button(ventana_lectura, text="?",font=("Bookman Old Style",round(12),"bold"), command=consulta_save, borderwidth=0)
                        button_consulta_save.place(x=round(345), y=round(520))
                        button_consulta_save.config(bg="#0A43B4", fg="white")
                #1.2 ------------------------------- Ventana Modo Estudio -------------------------------------------
                def window_study():
                        return
                #1.3 ------------------------------- Ventana Configuración -------------------------------------------
                #1.3.1 ------------------------------- Funciones Configuracióm -------------------------------------------
                def configuracion():
                        global my_img
                        global screen_size

                        root.withdraw()
                        ventana_configuracion=Toplevel()

                        archivotexto_nombre_resolucion_pantalla=open("memory/resolucion_pantalla.txt", encoding="utf8")
                        resolucion_pantalla=archivotexto_nombre_resolucion_pantalla.read()
                        archivotexto_nombre_resolucion_pantalla.close()

                        if resolucion_pantalla == 1:
                                screen_size="1366x768"
                        elif resolucion_pantalla == 0:
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
                                messagebox.showinfo("REBASE"," El fondo de pantalla ha sido cambiado por \n\n"+clicked_fondo_pantalla.get()+"\n\n Cierre el programa y vuela a abrirlo para ver cambios ")
                                ventana_configuracion.destroy()
                                configuracion()

                        def size_selection():
                                global size
                                #election_size = Label(ventana_configuracion, text=clicked.get())
                                if clicked.get() == "1366x768":
                                        archivotexto_nombre_resolucion_pantalla=open("memory/resolucion_pantalla.txt","w")
                                        archivotexto_nombre_resolucion_pantalla.write(str(1))
                                        archivotexto_nombre_resolucion_pantalla.close()
                                elif clicked.get() == "1920x1080":
                                        archivotexto_nombre_resolucion_pantalla=open("memory/resolucion_pantalla.txt","w")
                                        archivotexto_nombre_resolucion_pantalla.write(str(0))
                                        archivotexto_nombre_resolucion_pantalla.close()

                                messagebox.showinfo("REBASE"," La resolucion de pantalla ha sido cambiado a \n\n"+clicked.get()+"\n\n Cierre el programa y vuela a abrirlo para ver cambios ")
                                ventana_configuracion.destroy()
                                configuracion()


                #1.3.2 ------------------------------- Titulo Modo Lectura -------------------------------------------
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

                #1.3.3 ------------------------------- Botones Configuración -------------------------------------------

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



                #1.3.4 ------------------------------- Cuadro de texto Configuración -------------------------------------------



                #1.3.5------------------------------- Etiquetas Ventana Configuración -------------------------------------------

                        texto_set_image_label=Label(ventana_configuracion,text="Set Image's Name Here: ")
                        texto_set_image_label.place(x=round(100),y=round(200))
                        texto_set_image_label.config(bg="#FACC2E", width=round(20), font=("Bookman Old Style",round(12),"bold"))

                        texto_set_image_label=Label(ventana_configuracion,text="Set Resolution Here: ")
                        texto_set_image_label.place(x=round(100),y=round(400))
                        texto_set_image_label.config(bg="#FACC2E", width=round(20), font=("Bookman Old Style",round(12),"bold"))

# 1.5.1---------------------------------------Ventena presentacion ---------------------------------------------------------------------------------------------------------
                def presentacion():
                        global my_img

                        root.withdraw()
                        ventana_presentacion=Toplevel()                      
                        
                        archivotexto_nombre_resolucion_pantalla=open("memory/resolucion_pantalla.txt",encoding="utf8")
                        resolucion_pantalla=archivotexto_nombre_resolucion_pantalla.read()
                        archivotexto_nombre_resolucion_pantalla.close()

                        if resolucion_pantalla == 1:
                                screen_size="1366x768"
                        elif resolucion_pantalla == 0:
                                screen_size="1920x1080"

                        ventana_presentacion.geometry("1920x1080")
                        archivotexto_nombre_fondo_panatalla=open("memory/nombre_fondo_pantalla.txt",encoding="utf8")
                        fondo_pantalla = camino_carpeta_images+archivotexto_nombre_fondo_panatalla.read()
                        archivotexto_nombre_fondo_panatalla.close()                        

                        my_img = ImageTk.PhotoImage(Image.open(fondo_pantalla))
                        my_label = Label(ventana_presentacion, image=my_img).place(relwidth=1, relheight=1)

                        mi_foto =ImageTk.PhotoImage(Image.open("img\Foto_Perfil.png"))
                        foto_label= Label(ventana_presentacion, image=mi_foto)
                        foto_label.photo= mi_foto
                        foto_label.place(x=220, y=220)

                        my_linked_In = ImageTk.PhotoImage(Image.open("img_in.png"))
                        linked_label= Label(ventana_presentacion, image=my_linked_In)
                        linked_label.photo= my_linked_In
                        #linked_label.place(x=220, y=560)

                        def my_cv():
                                webbrowser.open("https://jaimecampillayresume.herokuapp.com/")
                        
                        def my_linkedIn():
                                webbrowser.open("https://www.linkedin.com/in/jgcampillayr/")
                        
                        def ir_leer():
                                ventana_presentacion.destroy()
                                window_read()
                        
                        def ir_estudiar():
                                ventana_presentacion.destroy()
                                window_study()

                        button_likendIn = Button(ventana_presentacion,image=my_linked_In, width=180, height=38, borderwidth=0 , command=my_linkedIn)
                        button_likendIn.place(x=235, y=510)

                        my_cv=Button(ventana_presentacion,text="IR A MI SITIO",font=("Bookman Old Style",round(12),"bold"), width=round(20), borderwidth=5 , command=my_cv)
                        my_cv.place(x=220, y=460)
                        my_cv.config(bg="#FACC2E") 

                        button_quit = Button(ventana_presentacion, text="SALIR PROGRAMA",font=("Bookman Old Style",round(10),"bold") , command=root.quit)
                        button_quit.place(x=1100, y=950) 

                        button_quit = Button(ventana_presentacion, text="LEER",font=("Bookman Old Style",round(10),"bold"), width=20 , command=ir_leer)
                        button_quit.place(x=650, y=950)

                        button_quit = Button(ventana_presentacion, text="ESTUDIAR",font=("Bookman Old Style",round(10),"bold"), width=20 , command=ir_estudiar)
                        button_quit.place(x=875, y=950)

                        titulo=Label(ventana_presentacion, text="PRESENTACIÓN", font=("Bookman Old Style",round(30)),bg="#e8dabd")
                        titulo.place(x=round(650), y=(30))

                        titulo=Label(ventana_presentacion, text='¡Hola!\n\nMi nombre es Jaime Gabriel Campillay Rojas\nDe profesión Ingeniero Civil Industrial con Magister en Ingenieria Industrial \ny de Sistemas\n\nEl programa actual es el resultado de un proceso de reflexión, aprendizaje y \nmuchas horas de estudio de Python que comenzó en el mes de octubre\ndel año 2020 cuando quedé desempleado por necesidades de la empresa. \n\nHasta antes de la fecha mencionada no me había dado cuenta lo fascinante\ndel mundo de la programación, y ahora no tengo dudas que quiero algún \ndía ganarme la vida como Programador. \n\nPor tanto te presento este proyecto que estás viendo llamado REBASE que \nbusca ayudarte a leer y estudiar ingles con el fin de aprender este idioma,\na la vez que en lo personal me permitió aventurarme en el desafío que implicó\naprender este lenguaje de programación, del cual no sabia nada en ese\nmomento.\n\nCorreo: jcampillayworks@gmail.com\n\nFecha Término REBASE: 24/01/2021', font=("Bookman Old Style",round(16)),bg="#e8dabd", width=80, height=30, justify="left")
                        titulo.place(x=round(470), y=200)

                        titulo=Label(ventana_presentacion, text="El programa es gratuito y por tanto\nlibre para su distribución", font=("Bookman Old Style",round(16)),bg="#e8dabd",fg="red", width=45, height=2, justify="left")
                        titulo.place(x=round(900), y=(850))

#2.0 ----------------------------------VENTANA RESOLUCION 1920 X 1080 ------------------------------------------------------------------
        else:
                titulo1=Label(background_label, text="WELCOME TO REBASE", font=("Bookman Old Style",30),bg="#e8dabd")
                titulo1.place(x=670, y=10)
                titulo2=Label(background_label, text=" READ ENGLISH BOOK AND STUDY ENGLISH", font=("Bookman Old Style",30),bg="#e8dabd")
                titulo2.place(x=500, y=70)
                titulo3=Label(background_label, text=" PLEASE, CHOOSE AN OPTION", font=("Bookman Old Style",30),bg="#e8dabd")
                titulo3.place(x=600, y=130)
#2.1.1 ------------------------------- Ventana Modo Lectura -------------------------------------------
                
                def window_read():

                        global my_img
                        global save_words_setence_options
                        global screen_size


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
                        drop_read_save.place(x=round(250),y=round(750))
                        drop_read_save.config(width=round(10), font=("Book Old Style", round(12),"bold"))

                        clicked_texto=StringVar()
                        clicked_texto.set(lista_textos[0])

                        drop_text=OptionMenu(ventana_lectura,clicked_texto, *lista_textos)
                        drop_text.place(x=round(800), y=round(200))
                        drop_text.config(width=round(20), font=("Book Old Style", round(10),"bold"))

#2.1.2 ------------------------------- Funciones Modo Lectura -------------------------------------------
                        def texto_inicio():
                                num_lista=contador.get()
                                camino_texto_lectura="texto_lectura/"+almacena_titulo
                                abrir_texto_inicio=open(camino_texto_lectura, encoding="utf8")
                                for line in abrir_texto_inicio:
                                        line=line.split(".")
                                        line=line[int(num_lista)]
                                        line=line.strip()
                                        texto_ENG.insert(END, line)
                                abrir_texto_inicio.close
                        def ingresar_texto():
                                texto_nuevo=str(clicked_texto.get())
                                camino_texto_lectura="texto_lectura/"+texto_nuevo
                                abrir_texto=open(camino_texto_lectura, encoding="utf8")
                                lectura_libro_texto=abrir_texto.read()
                                abrir_texto.close

                                texto_contiene_titulo2=open("memory/titulo_texto.txt","w")
                                texto_contiene_titulo2.write(clicked_texto.get())
                                texto_contiene_titulo2.close()

                                messagebox.showinfo("REBASE"," El texto ha sido cambiado por \n\n"+clicked_texto.get()+"\n\n")
                                ventana_lectura.destroy()
                                window_read()

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
                                        texto = len(line)
                                        if (texto-siguiente) >= 1:
                                                line=line[siguiente]
                                                line=line.strip()
                                                texto_ENG.insert(END, line)
                                                texto-=1
                                                print(texto)
                                        else:
                                                texto_ENG.insert(END,"END OF TEXT, CONGRATULATION")
                                                texto_ENG.config(bg="#109FEC")

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
                                        line=line.strip()
                                        texto_ENG.insert(END, line)
                                abrir_texto_inicio.close

                        def english_dictionary():

                                dictionary_word=PyDictionary()
                                meaning_word = dictionary_text.get()
                                result=dictionary_word.meaning(meaning_word)
                                messagebox.showinfo("REBASE"," DICTIONARY  \n\n"+str(result))

                        def page_marker():

                                marcador_pagina=open("memory/page_marker.txt","w")
                                marcador_pagina.write(contador.get())
                                messagebox.showinfo("English Assitant"," El marcador de página \n\n"+contador.get()+"\n\n ha sido guardado ")
                                marcador_pagina.close()

                        def save_word_sentence():
                                save_words_setence_options=["SENTENCE","WORD"]
                                if clicked_read.get() == "SENTENCE":

                                        sentencia_para_estudiar=open("memory/f_sentences/new_sentences.txt","a")
                                        sentencia_para_estudiar.write("\n")
                                        sentencia_para_estudiar.write(cuadro_save_words_setence.get())
                                        messagebox.showinfo("English Assitant"," La Sentencia \n\n"+cuadro_save_words_setence.get()+"\n\n fue incluida a new_sentences.txt")
                                        sentencia_para_estudiar.close()

                                elif clicked_read.get() == "WORD":
                                        palabra_para_estudiar=open("memory/f_words/new_words.txt","a")
                                        palabra_para_estudiar.write("\n")
                                        palabra_para_estudiar.write(cuadro_save_words_setence.get())
                                        messagebox.showinfo("English Assitant"," La Palabra \n\n"+cuadro_save_words_setence.get()+"\n\n fue incluida a new_words.txt")
                                        palabra_para_estudiar.close()

#2.1.3 ------------------------------- Botones Modo Lectura -------------------------------------------

                        button_save_word_setence=Button(ventana_lectura,text="SAVE WORD/SENTENCE ",font=("Bookman Old Style",round(12),"bold"), command=save_word_sentence)
                        button_save_word_setence.place(x=round(670),y=round(700))
                        button_save_word_setence.config(width=25)

                        button_spanish_translate_text=Button(ventana_lectura,text="VER TRADUCCIÓN ",font=("Bookman Old Style",round(12),"bold"), command=spanish_translate_text)
                        button_spanish_translate_text.place(x=round(50),y=round(525))
                        button_spanish_translate_text.config(bg="#FACC2E", width=15)

                        button_texto_inicio=Button(ventana_lectura,text="DAR INICO ",font=("Bookman Old Style",round(12),"bold"),command=texto_inicio)
                        button_texto_inicio.place(x=round(50),y=round(280))
                        button_texto_inicio.config(bg="#FACC2E", width=15)

                        button_page_marker=Button(ventana_lectura, text="PAGE MARKER",font=("Bookman Old Style",round(10),"bold"),width=12 , command=page_marker)
                        button_page_marker.place(x=round(255), y=round(420))
                        button_page_marker.config(bg="#FACC2E")

                        button_english_dictionary=Button(ventana_lectura, text="ENGLISH DICTIONARY",font=("Bookman Old Style",round(10),"bold"),width=20 , command=english_dictionary)
                        button_english_dictionary.place(x=round(900), y=round(420))

                        button_ingresar_texto=Button(ventana_lectura,text="APPLY NEW TEXT",font=("Bookman Old Style",round(10),"bold") , command=ingresar_texto)
                        button_ingresar_texto.place(x=round(610), y=round(200))

                        button_next_line=Button(ventana_lectura, text="NEXT",font=("Bookman Old Style",round(10),"bold"),width=round(10) , command=next_line)
                        button_next_line.place(x=round(705), y=round(420))

                        button_previous_line=Button(ventana_lectura, text="PREVIOUS",font=("Bookman Old Style",round(10),"bold"),width=round(10) , command=previous_line)
                        button_previous_line.place(x=round(525), y=round(420))

                        button_quit = Button(ventana_lectura, text="Exit Program",font=("Bookman Old Style",round(12),"bold") , command=root.quit)
                        button_quit.place(x=round(700), y=round(810))

#2.1.4 ------------------------------- Cuadro texto Modo Lectura -------------------------------------------

                        cuadro_save_words_setence=Entry(ventana_lectura, width=round(80), borderwidth=round(5), justify="left")
                        cuadro_save_words_setence.place(x=round(400), y=round(750))
                        cuadro_save_words_setence.config(font=("Bookman Old Style",round(12),"bold"))

                        nombre_texto=Entry(ventana_lectura, width=round(40), borderwidth=round(5), justify="center")
                        nombre_texto.place(x=round(520), y=round(150))
                        nombre_texto.config(font=("Bookman Old Style",round(14),"bold"))
                        nombre_texto.insert(0,almacena_titulo)
                        #recoger_nombre_texto=nombre_texto.get()

                        dictionary_text=Entry(ventana_lectura, width=round(30), borderwidth=round(5), justify="center")
                        dictionary_text.place(x=round(1100), y=round(420))
                        dictionary_text.config(font=("Bookman Old Style",round(12),"bold"))

                        texto_ENG=Text(ventana_lectura, width=round(125), height=round(4), font=("Helvetica",round(14),"bold"),borderwidth=round(5))
                        texto_ENG.place(x=round(240),y=round(280))
                        #texto_ENG.insert(END, lista_texto[])

                        texto_ESP=Text(ventana_lectura, width=round(125), height=round(4), font=("Helvetica",round(14),"bold"),borderwidth=round(5))
                        texto_ESP.place(x=round(240),y=round(525))

                        contador = Entry(ventana_lectura, width=5, borderwidth=5, justify="center")
                        contador.place(x=round(635) , y=round(420))
                        contador.config(font=("Bookman Old Style",round(10),"bold"))
                        contador.insert(0,almacena_page_marker)

#2.1.5 ------------------------------- Titulo Modo Lectura -------------------------------------------
                        titulo=Label(ventana_lectura, text="READING MODE REBASE", font=("Bookman Old Style",round(30)), bg="#e8dabd")
                        titulo.place(x=round(520), y=round(30))
                        titulo_texto=Label(ventana_lectura, text="TITLE OF THE TEXT",font=("Bookman Old Style",round(14),"bold"),bg="#FACC2E")
                        titulo_texto.place(x=round(680), y=round(100))

#2.1.6------------------------------- Etiquetas Modo Lectura -------------------------------------------

                        text_save_as=Label(ventana_lectura,text="SAVE AS",font=("Bookman Old Style",round(12),"bold"))
                        text_save_as.place(x=round(240),y=round(700))
                        text_save_as.config(bg="#FACC2E", width=15)
#------------------------------------- funciones/Botones Consulta Ventana Palabras -------------------------------------

                        def consulta_elegir_grupo():
                                messagebox.showinfo("REBASE", "Elige un texto de la lista desplegable\nluego le das click en aplicar y la eleccion se habrá cargado")
                        def consulta_page_marker():
                                messagebox.showinfo("REBASE", "Guarda el numero de sentencia,\nasí puedes cerrar el programa y retormarlo más tarde")
                        def consulta_dictionary():
                                messagebox.showinfo("REBASE", "Diccionario soporta solo palabras simples")
                        def consulta_save():
                                messagebox.showinfo("REBASE", "Elige de la lista desplegable\n si guardarlo como una horación o como plabrta\n\nRecuerda que las plabras debe ser singular")

                        button_consulta1 = Button(ventana_lectura, text="?",font=("Bookman Old Style",round(12),"bold"), command=consulta_elegir_grupo, borderwidth=0)
                        button_consulta1.place(x=round(1010), y=round(200))
                        button_consulta1.config(bg="#0A43B4", fg="white")

                        button_consulta_page_marker = Button(ventana_lectura, text="?",font=("Bookman Old Style",round(12),"bold"), command=consulta_page_marker, borderwidth=0)
                        button_consulta_page_marker.place(x=round(380), y=round(420))
                        button_consulta_page_marker.config(bg="#0A43B4", fg="white")

                        button_consulta_dictionary = Button(ventana_lectura, text="?",font=("Bookman Old Style",round(12),"bold"), command=consulta_dictionary, borderwidth=0)
                        button_consulta_dictionary.place(x=round(1450), y=round(420))
                        button_consulta_dictionary.config(bg="#0A43B4", fg="white")

                        button_consulta_save = Button(ventana_lectura, text="?",font=("Bookman Old Style",round(12),"bold"), command=consulta_save, borderwidth=0)
                        button_consulta_save.place(x=round(420), y=round(700))
                        button_consulta_save.config(bg="#0A43B4", fg="white")

#2.2 ------------------------------- Ventana Modo Estudio -------------------------------------------
                def window_study():
                        global my_img
                        global save_words_setence_options
                        global screen_size

                        #ventana_configuracion.destroy()
                        root.withdraw()
                        ventana_studio=Toplevel()
                        if  size == 1:
                                screen_size="1366x768"
                        elif size == 0:
                                screen_size="1680x1050"

                        ventana_studio.geometry(screen_size)
                        my_img = ImageTk.PhotoImage(Image.open(fondo_pantalla))
                        my_label = Label(ventana_studio, image=my_img).place(relwidth=1, relheight=1)
#2.2.1------------------------------Ventana Modo Estudio ---------------------------------------------------
#2.2.1.1----------------------------Ventana Modo Palabras -------------------------------------------------
                        def window_words():

                                global my_img
                                global save_words_setence_options
                                global screen_size
                                global group_w

                                ventana_studio.destroy()
                                root.withdraw()
                                ventana_studiow=Toplevel()
                                if  size == 1:
                                        screen_size="1366x768"
                                elif size == 0:
                                        screen_size="1680x1050"

                                ventana_studiow.geometry(screen_size)
                                my_img = ImageTk.PhotoImage(Image.open(fondo_pantalla))
                                my_label = Label(ventana_studiow, image=my_img).place(relwidth=1, relheight=1)

                                grupo_actual=open("memory/memoria_ultimo_grupow","r")
                                grw=grupo_actual.read()
                                grupo_actual.close()

                                archivo_contador_w=open("memory/contador_w.txt","r")
                                cont_w=archivo_contador_w.read()
                                archivo_contador_w.close()

                                camino_palabra= str("memory/f_words/"+grw)
                                archivo_palabras=open(camino_palabra,"r")

                                lista_palabras_temporal=[]

                                lista_palabras=archivo_palabras.readlines()
                                lista_formateada=[]
                                for elemento in lista_palabras:
                                        linea =elemento.strip("\n")
                                        lista_formateada.append(linea)

                                lista_respaldo=lista_formateada[:]

#2.2.1.2----------------------------Ventana Modo Sentencias Textos -------------------------------------------------
                                def dar_aleatorio():
                                        meaning_ENG.delete(1.0,END)
                                        respuesta_propia.delete(0,END)
                                        respuesta_corta.delete(0,END)
                                        respuesta_correcta.delete(0,END)
                                        respuesta_espanol.delete(0,END)
                                        contador.delete(0,END)
                                        respuesta_corta.config(bg="white")

                                        num_aleatorio=len(lista_respaldo)
                                        if len(lista_formateada)>=1:

                                                while respuesta_correcta.get() == "":
                                                        try:
                                                                aleatorio_lista = random.randint(0,int(num_aleatorio))
                                                                sacar=lista_respaldo[aleatorio_lista]
                                                                filtro=(sacar in lista_formateada)
                                                                
                                                                if filtro == False:
                                                                        respuesta_correcta.insert(0,"")

                                                                else:
                                                                        contador.insert(0,int(aleatorio_lista))

                                                                respuesta_correcta.insert(0,lista_respaldo[int(contador.get())])
                                                                respuesta_correcta.configure(fg="white")

                                                                dictionary_word=PyDictionary()
                                                                recoger_respuesta_correcta=respuesta_correcta.get()
                                                                result=dictionary_word.meaning(recoger_respuesta_correcta)
                                                                meaning_ENG.insert(END,str(result))
                                                        except:
                                                                respuesta_correcta.insert(0,"")
                                        else:
                                              respuesta_corta.insert(0,"NO HAY PALABRA")
                                              respuesta_corta.configure(bg="#109FEC",fg="black")  

                                        
                                def recoger_enviar_otrogrupo():
                                        w_num=contador.get()
                                        grupo_nuevo=str(clicked_enviar_otro_grupo.get())
                                        camino_grupo_estudio="memory/f_words/"+grupo_nuevo
                                        text_file=open(camino_grupo_estudio,"a")
                                        text_file.write("\n")
                                        text_file.write(lista_respaldo[int(w_num)])
                                        text_file.close
                                        #lista_palabras_temporal.append(lista_formateada[int(w_num)])
                                        for i in lista_formateada:
                                                if i == lista_respaldo[int(w_num)]:
                                                        lista_formateada.remove(i)
                                        messagebox.showinfo("REBASE"," La palabra\n\n"+lista_respaldo[int(w_num)]+"\n\n ha sido enviada a "+clicked_enviar_otro_grupo.get())

                                def ver_respuesta():
                                        recoger_respuesta_propia=respuesta_propia.get()
                                        recoger_respuesta_correcta=respuesta_correcta.get()
                                        if recoger_respuesta_correcta == recoger_respuesta_propia:
                                                respuesta_corta.insert(0,"CORRECT")
                                                respuesta_corta.configure(bg="#33FF51")
                                                respuesta_correcta.configure(fg="black")
                                        else:
                                                respuesta_corta.insert(0,"WRONG")
                                                respuesta_corta.configure(bg="#FF3333")
                                                respuesta_correcta.configure(fg="black")

                                def ver_traduccion():
                                        control=0
                                        while control == 0:
                                                palabra_ingles=respuesta_correcta.get()
                                                try:
                                                        line2= palabra_ingles
                                                        linea_Esp=line2
                                                        translator=google_translator()
                                                        translation=translator.translate(linea_Esp,lang_src="en", lang_tgt="es")
                                                        respuesta_espanol.insert(0,translation)
                                                except:
                                                        translation = None
                                                recoger_pregunta=respuesta_espanol.get()
                                                num_lista2=contador.get()
                                                if recoger_pregunta!="" or num_lista2==str(len(lista_formateada)):
                                                        control+=1

                                def cambiar_grupo():
                                        grupo_nuevo=str(clicked_groupw.get())
                                        camino_grupo_estudio="memory/f_words/"+grupo_nuevo
                                        abrir_grupo=open(camino_grupo_estudio, encoding="utf8")
                                        estudio_grupo=abrir_grupo.read()
                                        abrir_grupo.close

                                        grupo_contiene=open("memory/memoria_ultimo_grupow","w")
                                        grupo_contiene.write(clicked_groupw.get())
                                        grupo_contiene.close()

                                        messagebox.showinfo("REBASE"," El texto ha sido cambiado por \n\n"+clicked_groupw.get()+"\n\n")
                                        ventana_studiow.destroy()
                                        window_words()

                                def hablarNormal():
                                        engine = pyttsx3.init()
                                        voices = engine.getProperty("voices")
                                        engine.setProperty("voice", voices[1].id)
                                        engine.setProperty("rate", 140)
                                        engine.say(respuesta_correcta.get())
                                        engine.runAndWait()

                                def hablarlento():
                                        engine = pyttsx3.init()
                                        voices = engine.getProperty("voices")
                                        engine.setProperty("voice", voices[1].id)
                                        engine.setProperty("rate", 80)
                                        engine.say(respuesta_correcta.get())
                                        engine.runAndWait()

                                def guardar_cambios():

                                        grupo_viejo=str(cuadro_grupo.get())
                                        camino_grupo_estudio="memory/f_words/"+grupo_viejo
                                        text_file2=open(camino_grupo_estudio,"w")
                                        for j in lista_formateada:
                                                text_file2.write("\n")
                                                text_file2.write(j)
                                        text_file2.close
                                        messagebox.showinfo("REBASE"," Los cambios han sido guardado\n\n")

#--------------------------------- ------------CLICKED VENTANA PALABRAS ---------------------------------------------

                                clicked_groupw=StringVar()
                                clicked_groupw.set(group_w[0])

                                drop_read_save=OptionMenu(ventana_studiow,clicked_groupw, *group_w)
                                drop_read_save.place(x=round(740),y=round(145))
                                drop_read_save.config(width=round(25), font=("Book Old Style", round(12),"bold"))

                                clicked_enviar_otro_grupo=StringVar()
                                clicked_enviar_otro_grupo.set(group_w[0])

                                drop_enviar_palabra=OptionMenu(ventana_studiow,clicked_enviar_otro_grupo, *group_w)
                                drop_enviar_palabra.place(x=round(710),y=round(740))
                                drop_enviar_palabra.config(width=round(25), font=("Book Old Style", round(12),"bold"))
# --------------------------------------------- BOTONES VENTANA PALABRAS-------------------------------------------------

                                button_guardar_cambios=Button(ventana_studiow, text="SAVE CHANGES",font=("Bookman Old Style",round(10),"bold"), width=round(20) , command=guardar_cambios)
                                button_guardar_cambios.place(x=1000, y=740)
                                button_guardar_cambios.config(bg="#FACC2E")

                                button_cambiar_grupo=Button(ventana_studiow, text="SEND TO",font=("Bookman Old Style",round(10),"bold"), width=round(20) , command=recoger_enviar_otrogrupo)
                                button_cambiar_grupo.place(x=500, y=740)
                                button_cambiar_grupo.config(bg="#FACC2E")

                                button_hablar_normal=Button(ventana_studiow, text="Speak Normal",font=("Bookman Old Style",round(10),"bold"), width=15 , command=hablarNormal)
                                button_hablar_normal.place(x=round(1270), y=round(460))

                                button_hablar_lento=Button(ventana_studiow, text="Speak Slow",font=("Bookman Old Style",round(10),"bold"), width=15 , command=hablarlento)
                                button_hablar_lento.place(x=round(1270), y=round(540))

                                button_dar_aleatorio=Button(ventana_studiow, text="GIVE RANDOM",font=("Bookman Old Style",round(12),"bold") , command=dar_aleatorio)
                                button_dar_aleatorio.place(x=round(735), y=round(425))

                                button_elegir_grupo=Button(ventana_studiow, text="Choose Group",font=("Bookman Old Style",round(10),"bold") , command=cambiar_grupo)
                                button_elegir_grupo.place(x=round(620), y=round(145))

                                button_ver_respuesta=Button(ventana_studiow, text="SEE ANSWER",font=("Bookman Old Style",round(12),"bold") , command=ver_respuesta)
                                button_ver_respuesta.place(x=round(735), y=round(550))

                                boton_ver_respuesta_espanol=Button(ventana_studiow, text="VER TRADDUCIÓN",font=("Bookman Old Style",round(10),"bold"), width=round(20) , command=ver_traduccion)
                                boton_ver_respuesta_espanol.place(x=500, y=620)
                                boton_ver_respuesta_espanol.config(bg="#FACC2E")

                                button_quit = Button(ventana_studiow, text="Exit Program",font=("Bookman Old Style",round(10),"bold") , command=root.quit)
                                button_quit.place(x=round(740), y=round(850))
#------------------------------------------- ETIQUETAS VENTANA PALABRAS ------------------------------------------
                                titulo=Label(ventana_studiow, text="WORKING VOCABULARY", font=("Bookman Old Style",round(30)),bg="#e8dabd")
                                titulo.place(x=round(570), y=(70))

                                etiqueta_respuesta_propia=Label(ventana_studiow, text="INPUT YOUR ANSWER HERE", font=("Bookman Old Style",round(12),"bold"),bg="#FACC2E")
                                etiqueta_respuesta_propia.place(x=round(370), y=(470))

                                etiqueta_respuesta_correcta=Label(ventana_studiow, text="CURRENT WORD", font=("Bookman Old Style",round(12),"bold"),bg="#FACC2E")
                                etiqueta_respuesta_correcta.place(x=round(1000), y=(470))
#--------------------------------------------CUADRO DE TEXTO VENTANA PALABRAS---------------------------------------------------
                                meaning_ENG=Text(ventana_studiow, width=round(125), height=round(5), font=("Helvetica",round(13),"bold"),borderwidth=round(5))
                                meaning_ENG.place(x=round(240),y=round(280))

                                cuadro_grupo=Entry(ventana_studiow, width=round(35), borderwidth=round(5), justify="center")
                                cuadro_grupo.place(x=round(600), y=round(200))
                                cuadro_grupo.config(font=("Bookman Old Style",round(12),"bold"))
                                cuadro_grupo.insert(0,grw)

                                respuesta_propia=Entry(ventana_studiow, width=round(25), borderwidth=round(5), justify="center")
                                respuesta_propia.place(x=round(350), y=round(500))
                                respuesta_propia.config(font=("Bookman Old Style",round(12),"bold"))

                                respuesta_corta=Entry(ventana_studiow, width=round(15), borderwidth=round(5), justify="center")
                                respuesta_corta.place(x=round(720), y=round(500))
                                respuesta_corta.config(font=("Bookman Old Style",round(12),"bold"))

                                respuesta_correcta=Entry(ventana_studiow, width=round(25), borderwidth=round(5), justify="center")
                                respuesta_correcta.place(x=round(950), y=round(500))
                                respuesta_correcta.config(font=("Bookman Old Style",round(12),"bold"))

                                respuesta_espanol=Entry(ventana_studiow, width=round(35), borderwidth=round(5), justify="center")
                                respuesta_espanol.place(x=round(700), y=round(620))
                                respuesta_espanol.config(font=("Bookman Old Style",round(12),"bold"))

                                contador = Entry(ventana_studiow, width=5, borderwidth=5, justify="center")
                                contador.place(x=round(775) , y=round(465))
                                contador.config(font=("Bookman Old Style",round(10),"bold"))
                                contador.insert(0,cont_w)
#------------------------------------- funciones/Botones Consulta Ventana Palabras -------------------------------------

                                def consulta_elegir_grupo():
                                        messagebox.showinfo("REBASE", "El titulo del cuandro texto indica con que archivo estás trabajando")
                                
                                def consulta_sobre_concepto_grupo():
                                        messagebox.showinfo("REBASE", "Existe 4 archivos que te ayudaran a ordenar tu progreso y funciona de la siguiente manera:\n\nnew_words.txt: Aqui se almacenan las palabras que guardaste desde la ventana lectura, su objetivo agrupar palabras nuevas \npara el estudiante.\n\ngroup_1w.txt: Las palabras que ya dejan de ser novedosas para el estudiante pueden pasar al grupo 1 que son palabras \nque no se dominan pero se tiene un leve manejo.\n\ngroup_2w.txt: Aqui se asignan las plabras que pasan del grupo 1 al grupo 2, cuando estas ya se asimilan y hay un\nnotorio progreso en su manejo\n\ngroup_3w.txt: Este es el grupo de palabras que ya dominas y por tanto se pueden guardar en este grupo que es como\nun baúl")
                                
                                def consulta_enviar_grupo():
                                        messagebox.showinfo("REBASE", "Recoge la palabra en ingles y la envia al grupo que selecciones")

                                def consulta_guardar_cambios():
                                        messagebox.showinfo("REBASE", "Para conservar los cambios hechos y no exista dupliacion de datos\nse recomienda dar a guardar los cambios")

                                button_consulta1 = Button(ventana_studiow, text="?",font=("Bookman Old Style",round(12),"bold"), command=consulta_elegir_grupo, borderwidth=0)
                                button_consulta1.place(x=round(1010), y=round(200))
                                button_consulta1.config(bg="#0A43B4", fg="white")

                                button_consulta_significado_grupo = Button(ventana_studiow, text="?",font=("Bookman Old Style",round(12),"bold"), command=consulta_sobre_concepto_grupo, borderwidth=0)
                                button_consulta_significado_grupo.place(x=round(1025), y=round(145))
                                button_consulta_significado_grupo.config(bg="#0A43B4", fg="white")

                                button_consulta_enviar_grupo = Button(ventana_studiow, text="?",font=("Bookman Old Style",round(12),"bold"), command=consulta_enviar_grupo, borderwidth=0)
                                button_consulta_enviar_grupo.place(x=round(465), y=round(740))
                                button_consulta_enviar_grupo.config(bg="#0A43B4", fg="white")

                                button_consulta_guardar_cambios = Button(ventana_studiow, text="?",font=("Bookman Old Style",round(12),"bold"), command=consulta_guardar_cambios, borderwidth=0)
                                button_consulta_guardar_cambios.place(x=round(1200), y=round(740))
                                button_consulta_guardar_cambios.config(bg="#0A43B4", fg="white")


#2.2.1.2----------------------------Ventana Modo Sentencias -------------------------------------------------
                        def window_sentences():
                                global my_img
                                global save_words_setence_options
                                global screen_size
                                global group_s

                                ventana_studio.destroy()
                                root.withdraw()
                                ventana_studios=Toplevel()
                                if  size == 1:
                                        screen_size="1366x768"
                                elif size == 0:
                                        screen_size="1680x1050"

                                ventana_studios.geometry(screen_size)
                                my_img = ImageTk.PhotoImage(Image.open(fondo_pantalla))
                                my_label = Label(ventana_studios, image=my_img).place(relwidth=1, relheight=1)

                                grupo_actual=open("memory/memoria_ultimo_grupos.txt","r")
                                grs=grupo_actual.read()
                                grupo_actual.close()

                                archivo_contador_s=open("memory/contador_s.txt","r")
                                cont_w=archivo_contador_s.read()
                                archivo_contador_s.close()

                                camino_palabra= str("memory/f_sentences/"+grs)
                                archivo_palabras=open(camino_palabra,"r")

                                lista_palabras=archivo_palabras.readlines()
                                lista_formateada=[]
                                for elemento in lista_palabras:
                                        linea =elemento.strip("\n")
                                        lista_formateada.append(linea)

                                lista_respaldo=lista_formateada[:]

#2.2.1.2----------------------------Ventana Modo Sentencias Textos -------------------------------------------------
                                def dar_aleatorio():
                                        respuesta_propia.delete(0,END)
                                        respuesta_corta.delete(0,END)
                                        respuesta_correcta.delete(0,END)
                                        respuesta_espanol.delete(0,END)
                                        contador.delete(0,END)
                                        respuesta_corta.config(bg="white")

                                        num_aleatorio=len(lista_respaldo)

                                        if len(lista_formateada)>=1:
                                                while respuesta_espanol.get() == "":
                                                        try:
                                                                aleatorio_lista = random.randint(0,int(num_aleatorio))
                                                                sacar=lista_respaldo[aleatorio_lista]
                                                                filtro=(sacar in lista_formateada)
                                                                
                                                                if filtro == False:
                                                                        respuesta_espanol.insert(0,"")

                                                                else:
                                                                        contador.insert(0,int(aleatorio_lista))
                                                                        control=0
                                                                        while control == 0:
                                                                                num_lista=contador.get()
                                                                                try:
                                                                                        line2= lista_respaldo[int(num_lista)]
                                                                                        linea_Esp=line2
                                                                                        translator=google_translator()
                                                                                        translation=translator.translate(linea_Esp,lang_src="en", lang_tgt="es")
                                                                                        respuesta_espanol.insert(0,translation)
                                                                                except:
                                                                                        translation = None
                                                                                recoger_pregunta=respuesta_espanol.get()
                                                                                num_lista2=contador.get()
                                                                                if recoger_pregunta!="" or num_lista2==str(len(lista_respaldo)):
                                                                                        control+=1

                                                                respuesta_correcta.insert(0,lista_respaldo[int(contador.get())])
                                                                respuesta_correcta.config(fg="white")
                                                        except:
                                                                respuesta_espanol.insert(0,"")
                                        else:
                                              respuesta_corta.insert(0,"NO HAY PALABRA")
                                              respuesta_corta.configure(bg="#109FEC",fg="black")

                                def recoger_enviar_otrogrupo():
                                        w_num=contador.get()
                                        grupo_nuevo=str(clicked_enviar_otro_grupo.get())
                                        camino_grupo_estudio="memory/f_sentences/"+grupo_nuevo
                                        text_file=open(camino_grupo_estudio,"a")
                                        text_file.write("\n")
                                        text_file.write(lista_respaldo[int(w_num)])
                                        text_file.close
                                        #lista_palabras_temporal.append(lista_formateada[int(w_num)])
                                        for i in lista_formateada:
                                                if i == lista_respaldo[int(w_num)]:
                                                        lista_formateada.remove(i)
                                        
                                def ver_respuesta():
                                        recoger_respuesta_propia=respuesta_propia.get()
                                        recoger_respuesta_correcta=respuesta_correcta.get()
                                        if recoger_respuesta_correcta == recoger_respuesta_propia:
                                                respuesta_corta.insert(0,"CORRECT")
                                                respuesta_corta.configure(bg="#33FF51")
                                                respuesta_correcta.configure(fg="black")
                                                respuesta_correcta.config(fg="black")
                                        else:
                                                respuesta_corta.insert(0,"WRONG")
                                                respuesta_corta.configure(bg="#FF3333")
                                                respuesta_correcta.configure(fg="black")
                                                respuesta_correcta.config(fg="black")

                                def ver_traduccion():
                                        control=0
                                        while control == 0:
                                                num_lista=contador.get()
                                                try:
                                                        line2= lista_formateada[int(num_lista)]
                                                        linea_Esp=line2
                                                        translator=google_translator()
                                                        translation=translator.translate(linea_Esp,lang_src="en", lang_tgt="es")
                                                        respuesta_espanol.insert(0,translation)
                                                except:
                                                        translation = None
                                                recoger_pregunta=respuesta_espanol.get()
                                                num_lista2=contador.get()
                                                if recoger_pregunta!="" or num_lista2==str(len(lista_formateada)):
                                                        control+=1

                                def cambiar_grupo():
                                        grupo_nuevo=str(clicked_groups.get())
                                        camino_grupo_estudio="memory/f_sentences/"+grupo_nuevo
                                        abrir_grupo=open(camino_grupo_estudio, encoding="utf8")
                                        estudio_grupo=abrir_grupo.read()
                                        abrir_grupo.close

                                        grupo_contiene=open("memory/memoria_ultimo_grupos.txt","w")
                                        grupo_contiene.write(clicked_groups.get())
                                        grupo_contiene.close()

                                        messagebox.showinfo("REBASE"," El texto ha sido cambiado por \n\n"+clicked_groups.get()+"\n\n")
                                        ventana_studios.destroy()
                                        window_sentences()

                                def hablarNormal():
                                        engine = pyttsx3.init()
                                        voices = engine.getProperty("voices")
                                        engine.setProperty("voice", voices[1].id)
                                        engine.setProperty("rate", 120)
                                        engine.say(respuesta_correcta.get())
                                        engine.runAndWait()

                                def hablarlento():
                                        engine = pyttsx3.init()
                                        voices = engine.getProperty("voices")
                                        engine.setProperty("voice", voices[1].id)
                                        engine.setProperty("rate", 90)
                                        engine.say(respuesta_correcta.get())
                                        engine.runAndWait()

                                def guardar_cambios():

                                        grupo_viejo=str(cuadro_grupo.get())
                                        camino_grupo_estudio="memory/f_sentences/"+grupo_viejo
                                        text_file2=open(camino_grupo_estudio,"w")
                                        for j in lista_formateada:
                                                text_file2.write("\n")
                                                text_file2.write(j)
                                        text_file2.close
                                        messagebox.showinfo("REBASE"," Los cambios han sido guardados \n\n")
                                
                                def hablar_respuesta():
                                        #cuadro_speak.insert(0,"SPEAK!")
                                        #cuadro_speak.configure(bg="#33FF51")                                  
                                        #if cuadro_speak.get=="SPEAK!":
                                        r = sr.Recognizer()
                                        with sr.Microphone() as source:
                                                r.adjust_for_ambient_noise(source)
                                                print("Say something!")
                                                audio = r.listen(source)
                                        try:
                                                text = r.recognize_google(audio)
                                                respuesta_propia.insert(0,text)
                                        except :
                                                respuesta_propia.insert(0,"Sorry could not recognize your voice")

#--------------------------------- ------------CLICKED VENTANA PALABRAS ---------------------------------------------

                                clicked_groups=StringVar()
                                clicked_groups.set(group_s[0])

                                drop_read_save=OptionMenu(ventana_studios,clicked_groups, *group_s)
                                drop_read_save.place(x=round(740),y=round(145))
                                drop_read_save.config(width=round(25), font=("Book Old Style", round(12),"bold"))

                                clicked_enviar_otro_grupo=StringVar()
                                clicked_enviar_otro_grupo.set(group_s[0])

                                drop_enviar_palabra=OptionMenu(ventana_studios,clicked_enviar_otro_grupo, *group_s)
                                drop_enviar_palabra.place(x=round(710),y=round(750))
                                drop_enviar_palabra.config(width=round(25), font=("Book Old Style", round(12),"bold"))
# --------------------------------------------- BOTONES VENTANA SENTENCES-------------------------------------------------

                                button_guardar_cambios=Button(ventana_studios, text="SAVE CHANGES",font=("Bookman Old Style",round(10),"bold"), width=round(20) , command=guardar_cambios)
                                button_guardar_cambios.place(x=1000, y=750)
                                button_guardar_cambios.config(bg="#FACC2E")

                                button_cambiar_grupo=Button(ventana_studios, text="SEND TO",font=("Bookman Old Style",round(10),"bold"), width=round(20) , command=recoger_enviar_otrogrupo)
                                button_cambiar_grupo.place(x=500, y=750)
                                button_cambiar_grupo.config(bg="#FACC2E")

                                button_hablar_normal=Button(ventana_studios, text="Speak Normal",font=("Bookman Old Style",round(10),"bold"), width=20 , command=hablarNormal)
                                button_hablar_normal.place(x=round(850), y=round(400))

                                button_hablar_lento=Button(ventana_studios, text="Speak Slow",font=("Bookman Old Style",round(10),"bold"), width=20 , command=hablarlento)
                                button_hablar_lento.place(x=round(1100), y=round(400))

                                button_dar_aleatorio=Button(ventana_studios, text="GIVE RANDOM",font=("Bookman Old Style",round(12),"bold") , command=dar_aleatorio)
                                button_dar_aleatorio.place(x=round(460), y=round(580))

                                button_elegir_grupo=Button(ventana_studios, text="Choose Group",font=("Bookman Old Style",round(10),"bold") , command=cambiar_grupo)
                                button_elegir_grupo.place(x=round(620), y=round(145))

                                button_ver_respuesta=Button(ventana_studios, text="SEE ANSWER",font=("Bookman Old Style",round(12),"bold") , command=ver_respuesta)
                                button_ver_respuesta.place(x=round(750), y=round(580))

                                boton_ver_respuesta_espanol=Button(ventana_studios, text="TRY SPEECH TO TEXT",font=("Bookman Old Style",round(10),"bold"), width=round(20) , command=hablar_respuesta)
                                boton_ver_respuesta_espanol.place(x=500, y=400)
                                boton_ver_respuesta_espanol.config(bg="#FACC2E")

                                button_quit = Button(ventana_studios, text="Exit Program",font=("Bookman Old Style",round(10),"bold") , command=root.quit)
                                button_quit.place(x=round(790), y=round(850))
#------------------------------------------- ETIQUETAS VENTANA SENTENCIA ------------------------------------------
                                titulo=Label(ventana_studios, text="WORKING SENTENCES", font=("Bookman Old Style",round(30)),bg="#e8dabd")
                                titulo.place(x=round(590), y=(70))

                                etiqueta_respuesta_propia=Label(ventana_studios, text="INPUT YOUR ANSWER HERE", font=("Bookman Old Style",round(12),"bold"), width=25, bg="#FACC2E")
                                etiqueta_respuesta_propia.place(x=round(120), y=(480))

                                etiqueta_respuesta_correcta=Label(ventana_studios, text="SPANISH SETENCE", font=("Bookman Old Style",round(12),"bold"), width=25, bg="#FACC2E")
                                etiqueta_respuesta_correcta.place(x=round(120), y=(280))

                                etiqueta_respuesta_correcta=Label(ventana_studios, text="ENGLISH SETENCE", font=("Bookman Old Style",round(12),"bold"), width=25, bg="#FACC2E")
                                etiqueta_respuesta_correcta.place(x=round(120), y=(660))
#--------------------------------------------CUADRO DE TEXTO VENTANA SENTENCIA---------------------------------------------------

                                cuadro_grupo=Entry(ventana_studios, width=round(35), borderwidth=round(5), justify="center")
                                cuadro_grupo.place(x=round(600), y=round(200))
                                cuadro_grupo.config(font=("Bookman Old Style",round(12),"bold"))
                                cuadro_grupo.insert(0,grs)

                                respuesta_propia=Entry(ventana_studios, width=round(80), borderwidth=round(5), justify="center")
                                respuesta_propia.place(x=round(420), y=round(480))
                                respuesta_propia.config(font=("Bookman Old Style",round(16),"bold"))

                                respuesta_corta=Entry(ventana_studios, width=round(15), borderwidth=round(5), justify="center")
                                respuesta_corta.place(x=round(900), y=round(580))
                                respuesta_corta.config(font=("Bookman Old Style",round(12),"bold"))

                                respuesta_correcta=Entry(ventana_studios, width=round(80), borderwidth=round(5), justify="center")
                                respuesta_correcta.place(x=round(420), y=round(660))
                                respuesta_correcta.config(font=("Bookman Old Style",round(16),"bold"))

                                respuesta_espanol=Entry(ventana_studios, width=round(80), borderwidth=round(5), justify="center")
                                respuesta_espanol.place(x=round(420), y=round(280))
                                respuesta_espanol.config(font=("Bookman Old Style",round(16),"bold"))

                                contador = Entry(ventana_studios, width=5, borderwidth=5, justify="center")
                                contador.place(x=round(620) , y=round(580))
                                contador.config(font=("Bookman Old Style",round(10),"bold"))
                                contador.insert(0,cont_w)

#------------------------------------- funciones/Botones Consulta Ventana Sentencias -------------------------------------

                                def consulta_significado_grupo():
                                        messagebox.showinfo("REBASE", "Existe 4 archivos que te ayudaran a ordenar tu progreso y funciona de la siguiente manera:\n\nnew_sentences.txt: Aqui se almacenan las horaciones que guardaste desde la ventana lectura, su objetivo agrupar horaciones nuevas \npara el estudiante.\n\ngroup_1s.txt: Las horaciones que ya dejan de ser novedosas para el estudiante pueden pasar al grupo 1 que son horaciones \nque no se dominan pero se tiene un leve manejo.\n\ngroup_2s.txt: Aqui se asignan las horaciones que pasan del grupo 1 al grupo 2, cuando estas ya se asimilan y hay un\nnotorio progreso en su manejo\n\ngroup_3s.txt: Este es el grupo de horaciones que ya dominas y por tanto se pueden guardar en este grupo que es como\nun baúl")

                                def consulta_enviar_grupow():
                                        messagebox.showinfo("REBASE", "Recoge la horación en ingles y la envia al grupo que selecciones")

                                def consulta_guardar_cambiosw():
                                        messagebox.showinfo("REBASE", "Para conservar los cambios hechos y no exista dupliacion de datos se recomienda dar a guardar los cambios")
                                
                                def consulta_elegir_grupos():
                                        messagebox.showinfo("REBASE", "El titulo del cuandro texto indica con que archivo estás trabajando")

                                def consulta_speech_text():
                                        messagebox.showinfo("REBASE", "Este boton permite que trabajes la pronunciación.\n\nCuando le des click el boton cambia de color para escucharte hablar ingles")
                                                                
                                button_consulta1 = Button(ventana_studios, text="?",font=("Bookman Old Style",round(12),"bold"), command=consulta_speech_text, borderwidth=0)
                                button_consulta1.place(x=round(465), y=round(400))
                                button_consulta1.config(bg="#0A43B4", fg="white")
                                                                
                                button_consulta1 = Button(ventana_studios, text="?",font=("Bookman Old Style",round(12),"bold"), command=consulta_significado_grupo, borderwidth=0)
                                button_consulta1.place(x=round(1025), y=round(145))
                                button_consulta1.config(bg="#0A43B4", fg="white")

                                button_consulta1 = Button(ventana_studios, text="?",font=("Bookman Old Style",round(12),"bold"), command=consulta_elegir_grupos, borderwidth=0)
                                button_consulta1.place(x=round(1010), y=round(200))
                                button_consulta1.config(bg="#0A43B4", fg="white")

                                button_consulta_enviar_grupo = Button(ventana_studios, text="?",font=("Bookman Old Style",round(12),"bold"), command=consulta_enviar_grupow, borderwidth=0)
                                button_consulta_enviar_grupo.place(x=round(465), y=round(750))
                                button_consulta_enviar_grupo.config(bg="#0A43B4", fg="white")

                                button_consulta_guardar_cambios = Button(ventana_studios, text="?",font=("Bookman Old Style",round(12),"bold"), command=consulta_guardar_cambiosw, borderwidth=0)
                                button_consulta_guardar_cambios.place(x=round(1200), y=round(750))
                                button_consulta_guardar_cambios.config(bg="#0A43B4", fg="white")


#2.2.1--------------------------------------- Ventana Seleccion Modo Estudio ------------------------------------------------------------------
                        titulo=Label(ventana_studio, text="PLEASE, CHOOSE STUDY MODE", font=("Bookman Old Style",round(30)),bg="#e8dabd")
                        titulo.place(x=round(430), y=(70))
                        boton_WORDS=Button(ventana_studio, text=("WORDS"),font=("Bookman Old Style",round(14),"bold"),width=round(40),height=round(2), command=window_words)
                        boton_WORDS.place(x=500, y=370)
                        boton_SETENCE=Button(ventana_studio, text=("SETENCES"),font=("Bookman Old Style",round(14),"bold"), width=round(40),height=round(2),command=window_sentences)
                        boton_SETENCE.place(x=500, y=520)
#2.3 ------------------------------- Ventana Configuración -------------------------------------------
#2.3.1 ------------------------------- Funciones Configuracióm -------------------------------------------
                def configuracion():
                        global my_img
                        global screen_size
                        root.withdraw()
                        ventana_configuracion=Toplevel()

                        archivotexto_nombre_resolucion_pantalla=open("memory/resolucion_pantalla.txt",encoding="utf8")
                        resolucion_pantalla=archivotexto_nombre_resolucion_pantalla.read()
                        archivotexto_nombre_resolucion_pantalla.close()

                        if resolucion_pantalla == 1:
                                screen_size="1366x768"
                        elif resolucion_pantalla == 0:
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
                                messagebox.showinfo("REBASE"," El fondo de pantalla ha sido cambiado por \n\n"+clicked_fondo_pantalla.get()+"\n\n Cierre el programa y vuela a abrirlo para ver cambios ")
                                ventana_configuracion.destroy()
                                configuracion()

                        def size_selection():
                                global size
                                #election_size = Label(ventana_configuracion, text=clicked.get())
                                if clicked.get() == "1366x768":
                                        archivotexto_nombre_resolucion_pantalla=open("memory/resolucion_pantalla.txt","w")
                                        archivotexto_nombre_resolucion_pantalla.write(str(1))
                                        archivotexto_nombre_resolucion_pantalla.close()
                                elif clicked.get() == "1920x1080":
                                        archivotexto_nombre_resolucion_pantalla=open("memory/resolucion_pantalla.txt","w")
                                        archivotexto_nombre_resolucion_pantalla.write(str(0))
                                        archivotexto_nombre_resolucion_pantalla.close()

                                messagebox.showinfo("REBASE"," La resolucion de pantalla ha sido cambiado a \n\n"+clicked.get()+"\n\n Cierre el programa y vuela a abrirlo para ver cambios ")
                                ventana_configuracion.destroy()
                                configuracion()
                        
                        def ventana_configuracion_leer():
                                ventana_configuracion.destroy()
                                window_read()
                        
                        def ventana_configuracion_estudio():
                                ventana_configuracion.destroy()
                                window_study()

#2.3.2 ------------------------------- Titulo Modo Lectura -------------------------------------------
                        titulo=Label(ventana_configuracion, text="SET CONFIGURATION REBASE", font=("Bookman Old Style",round(30)),bg="#e8dabd")
                        titulo.place(x=round(530), y=(30))

                        clicked = StringVar()
                        clicked.set(size_options[0])

                        drop= OptionMenu(ventana_configuracion, clicked, *size_options)
                        drop.place(x=round(400), y=round(500))
                        drop.config(width=round(60), font=("Bookman Old Style",round(14),"bold"))

                        clicked_fondo_pantalla=StringVar()
                        clicked_fondo_pantalla.set(lista_fondo_pantalla[0])

                        drop_fondo_pantalla=OptionMenu(ventana_configuracion,clicked_fondo_pantalla, *lista_fondo_pantalla)
                        drop_fondo_pantalla.place(x=round(400), y=round(300))
                        drop_fondo_pantalla.config(width=round(70), font=("Book Old Style", round(14),"bold"))

#2.3.3 ------------------------------- Botones Configuración -------------------------------------------

                        boton_aplicar_fondo_pantalla=Button(ventana_configuracion, text=("APPLY WALLPAPER"),font=("Bookman Old Style",round(14),"bold"),width=round(20),height=round(1), command=cambiar_fondo)
                        boton_aplicar_fondo_pantalla.place(x=round(1300), y=round(300))

                        boton_read=Button(ventana_configuracion, text=("READ BOOK/TEXT"),font=("Bookman Old Style",round(14),"bold"),width=round(20),height=round(1), command=ventana_configuracion_leer)
                        boton_read.place(x=round(520), y=round(750))
                        boton_study=Button(ventana_configuracion, text=("STUDY ENGLISH"),font=("Bookman Old Style",round(14),"bold"), width=round(20),height=round(1),command=ventana_configuracion_estudio)
                        boton_study.place(x=round(920), y=round(750))

                        button_quit = Button(ventana_configuracion, text="Exit Program",font=("Bookman Old Style",round(12),"bold") , command=root.quit)
                        button_quit.place(x=round(795), y=round(850))

                        boton_size_selection=Button(ventana_configuracion, text=("APPLY SIZE RESOLUTION"),font=("Bookman Old Style",round(14),"bold"),width=round(20), command=size_selection)
                        boton_size_selection.place(x=round(1300), y=round(500))

#2.3.4 ------------------------------- Cuadro de texto Configuración -------------------------------------------



#2.3.5------------------------------- Etiquetas Ventana Configuración -------------------------------------------

                        texto_set_image_label=Label(ventana_configuracion,text="Set Image's Name Here: ")
                        texto_set_image_label.place(x=round(100),y=round(300))
                        texto_set_image_label.config(bg="#FACC2E", width=round(20), font=("Bookman Old Style",round(14),"bold"))

                        texto_set_image_label=Label(ventana_configuracion,text="Set Resolution Here: ")
                        texto_set_image_label.place(x=round(100),y=round(500))
                        texto_set_image_label.config(bg="#FACC2E", width=round(20), font=("Bookman Old Style",round(14),"bold"))
#
# 2.5.1---------------------------------------Ventena presentacion ---------------------------------------------------------------------------------------------------------
                def presentacion():
                        global my_img

                        root.withdraw()
                        ventana_presentacion=Toplevel()                      
                        
                        archivotexto_nombre_resolucion_pantalla=open("memory/resolucion_pantalla.txt",encoding="utf8")
                        resolucion_pantalla=archivotexto_nombre_resolucion_pantalla.read()
                        archivotexto_nombre_resolucion_pantalla.close()

                        if resolucion_pantalla == 1:
                                screen_size="1366x768"
                        elif resolucion_pantalla == 0:
                                screen_size="1920x1080"

                        ventana_presentacion.geometry("1920x1080")
                        archivotexto_nombre_fondo_panatalla=open("memory/nombre_fondo_pantalla.txt",encoding="utf8")
                        fondo_pantalla = camino_carpeta_images+archivotexto_nombre_fondo_panatalla.read()
                        archivotexto_nombre_fondo_panatalla.close()                        

                        my_img = ImageTk.PhotoImage(Image.open(fondo_pantalla))
                        my_label = Label(ventana_presentacion, image=my_img).place(relwidth=1, relheight=1)

                        mi_foto =ImageTk.PhotoImage(Image.open("img\Foto_Perfil.png"))
                        foto_label= Label(ventana_presentacion, image=mi_foto)
                        foto_label.photo= mi_foto
                        foto_label.place(x=220, y=220)

                        my_linked_In = ImageTk.PhotoImage(Image.open("img_in.png"))
                        linked_label= Label(ventana_presentacion, image=my_linked_In)
                        linked_label.photo= my_linked_In
                        #linked_label.place(x=220, y=560)

                        def my_cv():
                                webbrowser.open("https://jaimecampillayresume.herokuapp.com/")
                        
                        def my_linkedIn():
                                webbrowser.open("https://www.linkedin.com/in/jgcampillayr/")
                        
                        def ir_leer():
                                ventana_presentacion.destroy()
                                window_read()
                        
                        def ir_estudiar():
                                ventana_presentacion.destroy()
                                window_study()

                        button_likendIn = Button(ventana_presentacion,image=my_linked_In, width=180, height=38, borderwidth=0 , command=my_linkedIn)
                        button_likendIn.place(x=235, y=510)

                        my_cv=Button(ventana_presentacion,text="IR A MI SITIO",font=("Bookman Old Style",round(12),"bold"), width=round(20), borderwidth=5 , command=my_cv)
                        my_cv.place(x=220, y=460)
                        my_cv.config(bg="#FACC2E") 

                        button_quit = Button(ventana_presentacion, text="SALIR PROGRAMA",font=("Bookman Old Style",round(10),"bold") , command=root.quit)
                        button_quit.place(x=1100, y=950) 

                        button_quit = Button(ventana_presentacion, text="LEER",font=("Bookman Old Style",round(10),"bold"), width=20 , command=ir_leer)
                        button_quit.place(x=650, y=950)

                        button_quit = Button(ventana_presentacion, text="ESTUDIAR",font=("Bookman Old Style",round(10),"bold"), width=20 , command=ir_estudiar)
                        button_quit.place(x=875, y=950)

                        titulo=Label(ventana_presentacion, text="PRESENTACIÓN", font=("Bookman Old Style",round(30)),bg="#e8dabd")
                        titulo.place(x=round(650), y=(30))

                        titulo=Label(ventana_presentacion, text='¡Hola!\n\nMi nombre es Jaime Gabriel Campillay Rojas\nDe profesión Ingeniero Civil Industrial con Magister en Ingenieria Industrial \ny de Sistemas\n\nEl programa actual es el resultado de un proceso de reflexión, aprendizaje y \nmuchas horas de estudio de Python que comenzó en el mes de octubre\ndel año 2020 cuando quedé desempleado por necesidades de la empresa. \n\nHasta antes de la fecha mencionada no me había dado cuenta lo fascinante\ndel mundo de la programación, y ahora no tengo dudas que quiero algún \ndía ganarme la vida como Programador. \n\nPor tanto te presento este proyecto que estás viendo llamado REBASE que \nbusca ayudarte a leer y estudiar ingles con el fin de aprender este idioma,\na la vez que en lo personal me permitió aventurarme en el desafío que implicó\naprender este lenguaje de programación, del cual no sabia nada en ese\nmomento.\n\nCorreo: jcampillayworks@gmail.com\n\nFecha Término REBASE: 24/01/2021', font=("Bookman Old Style",round(16)),bg="#e8dabd", width=80, height=30, justify="left")
                        titulo.place(x=round(470), y=200)

                        titulo=Label(ventana_presentacion, text="El programa es gratuito y por tanto\nlibre para su distribución", font=("Bookman Old Style",round(16)),bg="#e8dabd",fg="red", width=45, height=2, justify="left")
                        titulo.place(x=round(900), y=(850))
                        
# 2.6.1---------------------------------------Ventena presentacion ---------------------------------------------------------------------------------------------------------
                def manual():
                        global my_img

                        root.withdraw()
                        ventana_manual=Toplevel()                      
                        
                        archivotexto_nombre_resolucion_pantalla=open("memory/resolucion_pantalla.txt",encoding="utf8")
                        resolucion_pantalla=archivotexto_nombre_resolucion_pantalla.read()
                        archivotexto_nombre_resolucion_pantalla.close()

                        if resolucion_pantalla == 1:
                                screen_size="1366x768"
                        elif resolucion_pantalla == 0:
                                screen_size="1920x1080"

                        ventana_manual.geometry("1920x1080")
                        archivotexto_nombre_fondo_panatalla=open("memory/nombre_fondo_pantalla.txt",encoding="utf8")
                        fondo_pantalla = camino_carpeta_images+archivotexto_nombre_fondo_panatalla.read()
                        archivotexto_nombre_fondo_panatalla.close()                        

                        my_img = ImageTk.PhotoImage(Image.open(fondo_pantalla))
                        my_label = Label(ventana_manual, image=my_img).place(relwidth=1, relheight=1)

                        def video_inicio():
                                webbrowser.open("https://www.youtube.com/watch?v=ISk7xVzRvSA")
                        
                        def video_2():
                                webbrowser.open("https://www.youtube.com/watch?v=NuJ8hM1LeSE")
                        
                        def video_3():
                                webbrowser.open("https://www.youtube.com/watch?v=uCxVddKsA4s")
                        
                        def go_read():
                                ventana_manual.destroy()
                                window_read()
                        
                        def go_study():
                                ventana_manual.destroy()
                                window_study()

                        video_inicio=Button(ventana_manual,text="VIDEO 01: INICIO",font=("Bookman Old Style",round(12),"bold"), width=round(30), height=2, borderwidth=3 , command=video_inicio)
                        video_inicio.place(x=700, y=300)
                        video_inicio.config(bg="#FACC2E")

                        video_2=Button(ventana_manual,text="VIDEO 02: INICIO",font=("Bookman Old Style",round(12),"bold"), width=round(30), height=2, borderwidth=3 , command=video_2)
                        video_2.place(x=700, y=375)
                        video_2.config(bg="#FACC2E") 

                        video_3=Button(ventana_manual,text="VIDEO 03: INICIO",font=("Bookman Old Style",round(12),"bold"), width=round(30), height=2, borderwidth=3 , command=video_3)
                        video_3.place(x=700, y=450)
                        video_3.config(bg="#FACC2E")  

                        button_quit = Button(ventana_manual, text="SALIR PROGRAMA",font=("Bookman Old Style",round(10),"bold") , command=root.quit)
                        button_quit.place(x=810, y=910) 

                        button_quit = Button(ventana_manual, text="READ ENGLISH",font=("Bookman Old Style",round(12),"bold"), width=25 , command=go_read)
                        button_quit.place(x=500, y=830)

                        button_quit = Button(ventana_manual, text="STUDY ENGLISH",font=("Bookman Old Style",round(12),"bold"), width=25 , command=go_study)
                        button_quit.place(x=1000, y=830)

                        titulo=Label(ventana_manual, text="TUTORIAL REBASE", font=("Bookman Old Style",round(30)),bg="#e8dabd")
                        titulo.place(x=round(650), y=(60))
                        
        
#------------------------------- Botones Funciones Ventana inicio -------------------------------------------
        if size == 1:
                boton_written=Button(background_label, text=("READ BOOK/TEXT"),font=("Bookman Old Style",round(12),"bold"),width=round(22),height=round(2), command=window_read)
                boton_written.place(x=230, y=300)
                boton_listen=Button(background_label, text=("STUDY ENGLISH"),font=("Bookman Old Style",round(12),"bold"), width=round(22),height=round(2),command=window_study)
                boton_listen.place(x=720, y=300)
                button_quit = Button(background_label, text="Exit Program",font=("Bookman Old Style",round(10),"bold") , command=root.quit)
                button_quit.place(x=570, y=630)

                boton_configuracio=Button(background_label, text="SET CONFIGURATION",font=("Bookman Old Style",round(10),"bold"), width=round(20) , command=configuracion)
                boton_configuracio.place(x=530, y=580)
                boton_configuracio.config(bg="#FACC2E")

                boton_configuracio=Button(background_label, text="PRESENTATION",font=("Bookman Old Style",round(12),"bold"), width=round(20) , command=presentacion)
                boton_configuracio.place(x=770, y=775)
                boton_configuracio.config(bg="#FACC2E")  
        else:
                boton_written=Button(background_label, text=("READ BOOK/TEXT"),font=("Bookman Old Style",round(14),"bold"),width=round(22),height=round(2), command=window_read)
                boton_written.place(x=350, y=450)
                boton_listen=Button(background_label, text=("STUDY ENGLISH"),font=("Bookman Old Style",round(14),"bold"), width=round(22),height=round(2),command=window_study)
                boton_listen.place(x=1200, y=450)
                button_quit = Button(background_label, text="Exit Program",font=("Bookman Old Style",round(12),"bold") , command=root.quit)
                button_quit.place(x=850, y=925)

                boton_configuracio=Button(background_label, text="SET CONFIGURATION",font=("Bookman Old Style",round(12),"bold"), width=round(20) , command=configuracion)
                boton_configuracio.place(x=800, y=850)
                boton_configuracio.config(bg="#FACC2E")

                boton_configuracio=Button(background_label, text="PRESENTATION",font=("Bookman Old Style",round(12),"bold"), width=round(20) , command=presentacion)
                boton_configuracio.place(x=800, y=800)
                boton_configuracio.config(bg="#FACC2E")

                boton_configuracio=Button(background_label, text="GUIDE",font=("Bookman Old Style",round(12),"bold"), width=round(20) , command=manual)
                boton_configuracio.place(x=800, y=750)
                boton_configuracio.config(bg="#FACC2E")  

home()

root.mainloop()
