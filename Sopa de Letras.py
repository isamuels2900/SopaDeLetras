from tkinter import *
from tkinter import messagebox
import ast
import random
import copy
import time

color = 'dark sea green'
color2 = 'black'

fuente = ('Arial', 15)
fuente_mapa = ('Arial', 7)

anchobd = '5'
ancho = "25"
borde = "ridge"

idioma = 'español'


class Interfaz:
    # O = Se crea el frame de la primer ventana y consulta al usuario que idioma desea seleccionar para el juego y se crean variables para utilizar después
    # E = La ventana de Tkinter para coloca el primer frame
    # S = La ventana con el frame y los botones para seleccionar idioma
    # R = ---
    def __init__(self, master):
        fr_idioma = self.crearframe()

        titulo = Label(fr_idioma, text="Selecciona un idioma", font=fuente, bg=color, fg=color2).grid(row=0, column=0)
        espacio = Label(fr_idioma, text=" ", font=fuente, bg=color, fg=color2).grid(row=1, column=0)

        boton_español = Button(fr_idioma, text="Español", width=ancho, font=fuente, bg=color, fg=color2,
                               cursor="hand2", bd=anchobd, relief=borde,
                               command=lambda: [self.idioma_seleccionado('español'),
                                                fr_idioma.destroy()]).grid(row=2, column=0)

        boton_ingles = Button(fr_idioma, text="Inglés", width=ancho, font=fuente, bg=color, fg=color2,
                              cursor="hand2", bd=anchobd, relief=borde,
                              command=lambda: [self.idioma_seleccionado('ingles'),
                                               fr_idioma.destroy()]).grid(row=3, column=0)

        # variables menu principal
        self.titulo_menu = ''
        self.texto_boton_jugar = ''
        self.texto_boton_estadisticas = ''
        self.texto_boton_base = ''
        self.texto_boton_salir = ''
        self.texto_boton_ayuda = ''

        # variables menu juego
        self.titulo_menu_juego = ''
        self.texto_boton_tradicional = ''
        self.texto_boton_contiempo = ''
        self.texto_boton_contrareloj = ''
        self.texto_boton_versus = ''
        self.texto_boton_volver = ''

        # Menú escribir palabras
        self.titulo_escribir_palabras = ''
        self.titulo_palabra_escrita = ''
        self.mensaje_palabra_escrita = ''
        self.titulo_error_pe = ''
        self.mensaje_error_pe = ''

        self.titulo_selec_palabras = ''
        self.texto_boton_normal = ''
        self.texto_boton_escribir = ''

        # variables menu dificultad
        self.titulo_menu_dificultad = ''
        self.texto_boton_prin = ''
        self.texto_boton_inter = ''
        self.texto_boton_avan = ''

        # variables base de datos
        self.titulo_menu_bases = ''
        self.texto_boton_ver = ''
        self.texto_boton_agregar = ''
        self.texto_boton_modificar = ''
        self.texto_boton_eliminar = ''

        # Menu agregar palabra
        self.titulo_menu_agregar = ''
        self.texto_boton_aceptar = ''
        self.mensaje_error = ''
        self.mensaje_completado = ''

        # Menu eliminar palabra
        self.titulo_menu_eliminar = ''

        # Menu modificar palabra
        self.titulo_menu_modificar = ''
        self.titulo_menu_modificar_aux = ''

        # Idioma del diccionario
        self.diccionario = ''

        # Variables del juego
        self.juego_iniciado = 'no'
        self.texto_nombre = ''
        self.texto_tiempo = ''

        # Mensajes del juego
        self.titulo_seleccionar_inicio = ''
        self.mensaje_seleccionar_inicio = ''

        self.titulo_seleccionar_final = ''
        self.mensaje_seleccionar_final = ''

        self.titulo_error_mp = ''
        self.mensaje_error_mp = ''

        self.mensaje_error1_vd = ''
        self.titulo_error1_vd = ''
        self.mensaje_error2_vd = ''
        self.titulo_error2_vd = ''

        self.titulo_ganaste = ''
        self.mensaje_ganaste = ''

        self.boton_mostrar_solucion = ''

        self.titulo_error_nombre = ''
        self.mensaje_error_nombre = ''

        # Menu ayuda
        self.boton_ayu_modos = ''
        self.boton_ayu_sopas = ''
        self.boton_ayu_estadisticas = ''

        self.faltan = ''
        self.turno = ''

    # O = Luego de seleccionar el idioma la función recibe una cadena de texto indicando el idioma de acuerdo a el idioma elegido se crean los textos para los menús y la sopa de letras
    # E = Una cadena de texto indicando cual idioma se ha seleccionado
    # S = Creación de de las variables para los textos de los menús y llamada a la función de menu_principal
    # R = ---
    def idioma_seleccionado(self, idioma):
        if idioma == 'ingles':
            # variables menu principal
            self.titulo_menu = 'Word puzzle'
            self.texto_boton_jugar = 'Play'
            self.texto_boton_estadisticas = 'Stats'
            self.texto_boton_base = 'Word database'
            self.texto_boton_ayuda = 'Help'
            self.texto_boton_salir = 'Exit'
            # variables menu juego
            self.titulo_menu_juego = 'Choose a game mode'
            self.texto_boton_tradicional = 'Classic'
            self.texto_boton_contiempo = 'With timer'
            self.texto_boton_contrareloj = 'Time trial'
            self.texto_boton_versus = 'Versus'
            self.texto_boton_volver = 'Return'
            # variables menu dificultad
            self.titulo_menu_dificultad = 'Choose a difficulty level'
            self.texto_boton_prin = 'Beginner'
            self.texto_boton_inter = 'Intermediate'
            self.texto_boton_avan = 'Advanced'
            # variables base de datos
            self.titulo_menu_bases = 'Choose an option'
            self.texto_boton_ver = 'Show words'
            self.texto_boton_agregar = 'Add word'
            self.texto_boton_modificar = 'Modify word'
            self.texto_boton_eliminar = 'Delete word'
            # Menu agregar palabra
            self.titulo_menu_agregar = 'Type in new word'
            self.texto_boton_aceptar = 'Accept'
            self.mensaje_error = 'There was an error'
            self.mensaje_completado = 'Succesfully completed'
            # Menu eliminar
            self.titulo_menu_eliminar = 'Type in word to delete'
            # Menu modificar palabra
            self.titulo_menu_modificar = 'Type in word to modify'
            self.titulo_menu_modificar_aux = 'Type in new word'
            # Mensajes del juego
            self.titulo_seleccionar_inicio = 'Beginning'
            self.mensaje_seleccionar_inicio = 'Select as the beginning of the word?'
            self.titulo_seleccionar_final = 'End'
            self.mensaje_seleccionar_final = 'Select as the end of the word?'
            self.titulo_error_mp = 'No match'
            self.mensaje_error_mp = 'Selected word does not match'
            self.mensaje_error1_vd = 'Selected space is invalid'
            self.titulo_error1_vd = 'Invalid selected space'
            self.mensaje_error2_vd = 'Selected spaces are invalid'
            self.titulo_error2_vd = 'Invalid selected spaces'
            self.faltan = 'words left: '
            self.titulo_ganaste = 'Winner!'
            self.mensaje_ganaste = 'You won!'
            self.boton_mostrar_solucion = 'Show solution'
            self.texto_nombre = 'Type in your name'
            self.texto_tiempo = 'Time'
            self.titulo_error_nombre = 'Invalid name'
            self.mensaje_error_nombre = 'Invalid name'
            # Menú escribir palabras
            self.titulo_escribir_palabras = 'Type in the words to search'
            self.titulo_palabra_escrita = 'Word registered'
            self.mensaje_palabra_escrita = 'Words left: '
            self.titulo_error_pe = 'Error'
            self.mensaje_error_pe = 'Invalid word'
            # Menu seleccionar sopa
            self.titulo_selec_palabras = 'Choose a type of soup'
            self.texto_boton_normal = 'Normal'
            self.texto_boton_escribir = 'Custom'
            # Menu ayuda
            self.boton_ayu_modos = 'Game modes'
            self.boton_ayu_sopas = 'Types of soup'
            # Ayuda Modos de Juego
            self.ayu_trad1 = 'The player must find the words listed to rhe right of the board'
            self.ayu_trad2 = 'The player selects the first letter of the word and then the last letter'
            self.ayu_trad3 = 'With the show solution button the words the player must find are highlighted'
            self.ayu_trad4 = 'The game is won when all words are found'
            self.ayu_trad5 = 'If the game mode is time trial the player loses when the time runs out'
            # Ayuda Tipos de Sopas
            self.ayu_sopa1 = 'Beginner Level:\n-A word puzzle of 12 letters of height and 12 letters of width\n-The are 6 words to find\n-In case that you chose "Time Trail" game mode, you will have 1 minute to find the words'
            self.ayu_sopa2 = 'Intermediate Level:\n-A word puzzle of 20 letters of height and 20 letters of width\n-The are 10 words to find\n-In case that you chose "Time Trail" game mode, you will have 2 minutes to find the words'
            self.ayu_sopa3 = 'Advanced Level:\n-A word puzzle of 28 letters of height and 28 letters of width\n-The are 14 words to find\n-In case that you chose "Time Trail" game mode, you will have 3 minutes to find the words'
            # Ayuda Estadísticas
            self.ayu_esta1 = 'Stats:\nIt shows the best 3 times on each difficulty level (Beginner, Intermediate & Advanced)'
            self.ayu_esta2 = 'Time Trial:\nIt shows the best 3 players with less time used on each difficulty level (Beginner, Intermediate & Advanced)'
            # Ayuda Base de Datos
            self.ayu_datos1 = 'Show words:\nIt shows a list of the words from the database'
            self.ayu_datos2 = 'Add word:\nBrings the option to add a new word to the database'
            self.ayu_datos3 = 'Modify word:\nBrings the option of modify a word from the database'
            self.ayu_datos4 = 'Delete word:\nBrings the option of delete a word from the database'
            # Idioma del diccionario
            self.diccionario = 'diccionario_ingles.txt'
            return self.menu_principal()
        else:
            # variables menu principal
            self.titulo_menu = 'Sopa de letras'
            self.texto_boton_jugar = 'Jugar'
            self.texto_boton_estadisticas = 'Estadisticas'
            self.texto_boton_base = 'Base de datos'
            self.texto_boton_ayuda = 'Ayuda'
            self.texto_boton_salir = 'Salir'
            # variables menu juego
            self.titulo_menu_juego = 'Seleccione un modo de juego'
            self.texto_boton_tradicional = 'Tradicional'
            self.texto_boton_contiempo = 'Con tiempo'
            self.texto_boton_contrareloj = 'Contra reloj'
            self.texto_boton_versus = 'Versus'
            self.texto_boton_volver = 'Volver'
            # variables menu dificultad
            self.titulo_menu_dificultad = 'Selecciona una dificultad'
            self.texto_boton_prin = 'Principiante'
            self.texto_boton_inter = 'Intermedio'
            self.texto_boton_avan = 'Avanzado'
            # variables base de datos
            self.titulo_menu_bases = 'Seleccione una opción'
            self.texto_boton_ver = 'Ver palabras'
            self.texto_boton_agregar = 'Agregar palabra'
            self.texto_boton_modificar = 'Modificar palabra'
            self.texto_boton_eliminar = 'Eliminar palabra'
            # Menu agregar palabra
            self.titulo_menu_agregar = 'Ingrese una nueva palabra'
            self.texto_boton_aceptar = 'Aceptar'
            self.mensaje_error = 'Ocurrió un error'
            self.mensaje_completado = 'Completado exitosamente'
            # Menu eliminar
            self.titulo_menu_eliminar = 'Ingrese la palabra a eliminar'
            # Menu modificar palabra
            self.titulo_menu_modificar = 'Ingrese una palabra'
            self.titulo_menu_modificar_aux = 'Ingrese la nueva palabra'
            # Mensajes del juego
            self.titulo_seleccionar_inicio = 'Inicio'
            self.mensaje_seleccionar_inicio = 'Marcar como inicio de la palabra?'
            self.titulo_seleccionar_final = 'Final'
            self.mensaje_seleccionar_final = 'Marcar como final de la palabra'
            self.titulo_error_mp = 'Palabra no coincide'
            self.mensaje_error_mp = 'La palabra seleccionada no coincide'
            self.mensaje_error1_vd = 'Espacio seleccionado no es válido'
            self.titulo_error1_vd = 'Espacio invalido'
            self.mensaje_error2_vd = 'Los espacios seleccionados no son válidos'
            self.titulo_error2_vd = 'Espacios inválidos'
            self.faltan = 'Palabras restantes: '
            self.titulo_ganaste = 'Ganador!'
            self.mensaje_ganaste = 'Has ganado!'
            self.boton_mostrar_solucion = 'Mostrar solución'
            self.texto_nombre = 'Ingrese su nombre'
            self.texto_tiempo = 'Tiempo'
            self.titulo_error_nombre = 'Nombre invalido'
            self.mensaje_error_nombre = 'Nombre invalido'
            # Menú escribir palabras
            self.titulo_escribir_palabras = 'Ingrese las palabras deseadas'
            self.titulo_palabra_escrita = 'Palabra registrada'
            self.mensaje_palabra_escrita = 'Palabras restantes: '
            self.titulo_error_pe = 'Error'
            self.mensaje_error_pe = 'Palabra inválida'
            # Menu seleccionar sopa
            self.titulo_selec_palabras = 'Seleccione un tipo de sopa'
            self.texto_boton_normal = 'Normal'
            self.texto_boton_escribir = 'Personalizada'
            # Menu ayuda
            self.boton_ayu_modos = 'Modos de juego'
            self.boton_ayu_sopas = 'Tipos de sopa'
            # Ayuda Modos de Juego
            self.ayu_trad1 = 'Se deben buscar las palabras mostradas a la derecha en el tablero'
            self.ayu_trad2 = 'Se marca la letra inicial de la palabra y luego la ultima letra de la palabra'
            self.ayu_trad3 = 'Con el boton mostrar solución aparecerán resaltadas todas las palabras que se tienen que buscar'
            self.ayu_trad4 = 'Se gana cuando se encuentran todas las palabras'
            self.ayu_trad5 = 'Si el modo de juego es contrareloj se puede perder si se acaba el jugador pierde'
            # Ayuda Tipos de Sopas
            self.ayu_sopa1 = 'Nivel Principiante:\n-Tiene una sopa de letras con un tamaño de 12 letras de largo por 12 letras de ancho\n-Hay 6 palabras por encontrar\n-En caso de seleccionar el modo de juego "Contrareloj" cuenta con 1 minuto para encontrar las palabras'
            self.ayu_sopa2 = 'Nivel Intermedio:\n-Tiene una sopa de letras con un tamaño de 20 letras de largo por 20 letras de ancho\n-Hay 10 palabras por encontrar\n-En caso de seleccionar el modo de juego "Contrareloj" cuenta con 2 minutos para encontrar las palabras'
            self.ayu_sopa3 = 'Nivel Intermedio:\n-Tiene una sopa de letras con un tamaño de 28 letras de largo por 28 letras de ancho\n-Hay 14 palabras por encontrar\n-En caso de seleccionar el modo de juego "Contrareloj" cuenta con 3 minutos para encontrar las palabras'
            # Ayuda Estadísticas
            self.ayu_esta1 = 'Con tiempo:\nSe muestran los 3 mejores tiempos de cada dificultad (Principiante, Intermedio y Avanzado)'
            self.ayu_esta2 = 'Contrareloj:\nSe muestran los 3 jugadores con menor tiempo utlizado de cada dificultad (Principiante, Intermedio y Avanzado)'
            # Ayuda Base de Datos
            self.ayu_datos1 = 'Ver palabras:\nMuestra una lista de las palabras en la base de datos'
            self.ayu_datos2 = 'Agregar palabra:\nDa la opción de agregar una nueva palabra a la base de datos'
            self.ayu_datos3 = 'Modificar palabra:\nDa la opción de modificar una palabra de la base de datos'
            self.ayu_datos4 = 'Eliminar palabra:\nDa la opción de elimiar una palara de la base de datos'
            # Idioma del diccionario
            self.diccionario = 'diccionario_español.txt'
            return self.menu_principal()

    # O = Se crea el frame con el menú principal y los botones que lo componen con las llamadas a las funciones correcpondientes
    # E = ---
    # S = El frame con el menú y los botones funcionales
    # R = ---
    def menu_principal(self):
        fr_menu = self.crearframe()

        titulo = Label(fr_menu, text=self.titulo_menu, font=fuente, bg=color, fg=color2).grid(row=0, column=0)
        espacio = Label(fr_menu, text=" ", font=fuente, bg=color, fg=color2).grid(row=1, column=0)
        boton_jugar = Button(fr_menu, text=self.texto_boton_jugar, width=ancho, font=fuente, bg=color, fg=color2,
                             cursor="hand2", bd=anchobd, relief=borde,
                             command=lambda: [self.menu_juegos(), fr_menu.destroy()]).grid(row=2, column=0)
        boton_estadisticas = Button(fr_menu, text=self.texto_boton_estadisticas, width=ancho, font=fuente, bg=color,
                                    fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                    command=lambda: [self.estadisticas(), fr_menu.destroy()]).grid(row=3, column=0)
        boton_base = Button(fr_menu, text=self.texto_boton_base, width=ancho, font=fuente, bg=color, fg=color2,
                            cursor="hand2", bd=anchobd, relief=borde,
                            command=lambda: [self.base_de_datos(), fr_menu.destroy()]).grid(row=4, column=0)
        boton_ayuda = Button(fr_menu, text=self.texto_boton_ayuda, width=ancho, font=fuente, bg=color, fg=color2,
                             cursor="hand2", bd=anchobd, relief=borde,
                             command=lambda: [self.ayuda(), fr_menu.destroy()]).grid(row=5, column=0)
        boton_salir = Button(fr_menu, text=self.texto_boton_salir, width=ancho, font=fuente, bg=color, fg=color2,
                             cursor="hand2", bd=anchobd, relief=borde, command=lambda: exit()).grid(row=6, column=0)

    # O = Crea el frame para mostrar las estadisticas por modos de juego y en cada uno el mejor tiempo de cada nivel de dificultad
    # E = ---
    # S = El frame con las estadísticas por modos de juego y niveles de dificultad
    # R = ---
    def estadisticas(self):
        frame = self.crearframe()
        mostrar = Text(frame, state='normal', bg=color, fg=color2, font=fuente)
        mostrar.grid(row=0, column=0, sticky='NSWE')
        boton_volver = Button(frame, text=self.texto_boton_volver, width=ancho, font=fuente, bg=color, fg=color2,
                              cursor="hand2", bd=anchobd, relief=borde,
                              command=lambda: [self.menu_principal(), frame.destroy()]).grid(row=1, column=0)

        ranks_con = self.abrir_rangos('contiempo')
        ranks_contra = self.abrir_rangos('contrareloj')

        principiante = ranks_con[0]
        principiante = principiante[::-1]  # Los "::" se utilizan para invertir la lista

        intermedio = ranks_con[1]
        intermedio = intermedio[::-1]

        avanzado = ranks_con[2]
        avanzado = avanzado[::-1]

        p_contra = ranks_contra[0]
        p_contra = p_contra[::-1]

        i_contra = ranks_contra[1]
        i_contra = i_contra[::-1]

        a_contra = ranks_contra[2]
        a_contra = a_contra[::-1]

        mostrar.insert(INSERT, self.texto_boton_prin + ' ' + self.texto_boton_contiempo + '\n')
        mostrar.insert(INSERT, '\n')
        self.ordenar(principiante, mostrar)
        mostrar.insert(INSERT, '\n')
        mostrar.insert(INSERT, self.texto_boton_inter + ' ' + self.texto_boton_contiempo + '\n')
        mostrar.insert(INSERT, '\n')
        self.ordenar(intermedio, mostrar)
        mostrar.insert(INSERT, '\n')
        mostrar.insert(INSERT, self.texto_boton_avan + ' ' + self.texto_boton_contiempo + '\n')
        mostrar.insert(INSERT, '\n')
        self.ordenar(avanzado, mostrar)
        mostrar.insert(INSERT, '\n')
        mostrar.insert(INSERT, self.texto_boton_prin + ' ' + self.texto_boton_contrareloj + '\n')
        mostrar.insert(INSERT, '\n')
        self.ordenar(p_contra, mostrar)
        mostrar.insert(INSERT, '\n')
        mostrar.insert(INSERT, self.texto_boton_inter + ' ' + self.texto_boton_contrareloj + '\n')
        mostrar.insert(INSERT, '\n')
        self.ordenar(i_contra, mostrar)
        mostrar.insert(INSERT, '\n')
        mostrar.insert(INSERT, self.texto_boton_avan + ' ' + self.texto_boton_contrareloj + '\n')
        mostrar.insert(INSERT, '\n')
        self.ordenar(a_contra, mostrar)

        # O = Ordenar los tiempos de los rankings de menor a mayor

    # E = La lista de rankings
    # S = La lista ordenada de menor a mayor
    # R = ---
    def ordenar(self, lista, widget):
        res = 0
        for tiempo in lista:
            if res == 3:
                break
            else:
                widget.insert(INSERT, tiempo[0] + ' ~ ' + tiempo[1] + '\n')

                # O = Crea el frame para el menú de ayuda y los botones para las opciones a seleccionar y obtener ayuda

    # E = ---
    # S = Un frame con el menú de ayuda y los botones con sus respectivas funcionalidades
    # R = ---
    def ayuda(self):
        frame = self.crearframe()

        titulo = Label(frame, text=self.titulo_menu, font=fuente, bg=color, fg=color2).grid(row=0, column=0)
        espacio = Label(frame, text=" ", font=fuente, bg=color, fg=color2).grid(row=1, column=0)
        Button(frame, text=self.boton_ayu_modos, width=ancho, font=fuente, bg=color, fg=color2, cursor="hand2",
               bd=anchobd, relief=borde, command=lambda: [self.ayuda_modos(), frame.destroy()]).grid(row=2, column=0)
        Button(frame, text=self.boton_ayu_sopas, width=ancho, font=fuente, bg=color, fg=color2, cursor="hand2",
               bd=anchobd, relief=borde, command=lambda: [self.ayuda_sopas(), frame.destroy()]).grid(row=3, column=0)
        Button(frame, text=self.texto_boton_estadisticas, width=ancho, font=fuente, bg=color, fg=color2, cursor="hand2",
               bd=anchobd, relief=borde, command=lambda: [self.ayuda_estadisticas(), frame.destroy()]).grid(row=4,
                                                                                                            column=0)
        Button(frame, text=self.texto_boton_base, width=ancho, font=fuente, bg=color, fg=color2, cursor="hand2",
               bd=anchobd, relief=borde, command=lambda: [self.ayuda_base(), frame.destroy()]).grid(row=5, column=0)
        boton_volver = Button(frame, text=self.texto_boton_volver, width=ancho, font=fuente, bg=color, fg=color2,
                              cursor="hand2", bd=anchobd, relief=borde,
                              command=lambda: [self.menu_principal(), frame.destroy()]).grid(row=6, column=0)

    # O = Muestra un frame con texto que ayuda al usuario a comprender los modos de juego
    # E = ---
    # S = Un frame con texto de ayuda para los modos de juego
    # R = ---
    def ayuda_modos(self):
        frame = self.crearframe()

        Label(frame, text=self.ayu_trad1, font=fuente, bg=color, fg=color2).grid(row=0, column=0)
        Label(frame, text=self.ayu_trad2, font=fuente, bg=color, fg=color2).grid(row=1, column=0)
        Label(frame, text=self.ayu_trad3, font=fuente, bg=color, fg=color2).grid(row=2, column=0)
        Label(frame, text=self.ayu_trad4, font=fuente, bg=color, fg=color2).grid(row=3, column=0)
        Label(frame, text=self.ayu_trad5, font=fuente, bg=color, fg=color2).grid(row=4, column=0)
        boton_volver = Button(frame, text=self.texto_boton_volver, width=ancho, font=fuente, bg=color, fg=color2,
                              cursor="hand2", bd=anchobd, relief=borde,
                              command=lambda: [self.ayuda(), frame.destroy()]).grid(row=5, column=0)

        # O = Muestra un frame con texto que ayuda a el usuario a comprender los niveles de dificultad que tienen las sopas de letras y porqué algunas son mas largas o tienen más palabras

    # E = ---
    # S = Un frame con texto que ayuda al usuario sobre niveles del juego
    # R = ---
    def ayuda_sopas(self):
        frame = self.crearframe()

        Label(frame, text=self.ayu_sopa1, font=fuente, bg=color, fg=color2).grid(row=0, column=0)
        Label(frame, text=self.ayu_sopa2, font=fuente, bg=color, fg=color2).grid(row=1, column=0)
        Label(frame, text=self.ayu_sopa3, font=fuente, bg=color, fg=color2).grid(row=2, column=0)
        boton_volver = Button(frame, text=self.texto_boton_volver, width=ancho, font=fuente, bg=color, fg=color2,
                              cursor="hand2", bd=anchobd, relief=borde,
                              command=lambda: [self.ayuda(), frame.destroy()]).grid(row=5, column=0)

    # O = Muestra un frame con texto que ayuda a el usuario a comprender las estadísticas
    # E = ---
    # S = Un frame con texto que ayuda al usuario sobre las estadísticas
    # R = ---
    def ayuda_estadisticas(self):
        frame = self.crearframe()

        Label(frame, text=self.ayu_esta1, font=fuente, bg=color, fg=color2).grid(row=0, column=0)
        Label(frame, text=self.ayu_esta2, font=fuente, bg=color, fg=color2).grid(row=1, column=0)
        boton_volver = Button(frame, text=self.texto_boton_volver, width=ancho, font=fuente, bg=color, fg=color2,
                              cursor="hand2", bd=anchobd, relief=borde,
                              command=lambda: [self.ayuda(), frame.destroy()]).grid(row=5, column=0)

    # O = Muestra un frame con texto que ayuda al el usuario a comprender la base de datos y sus funcionalidades como lo son ver, agregar, modificar y eliminar palabras de la base de datos
    # E = ---
    # S = Un frame con texto que ayuda al usuario sobre la base de datos y sus funciones
    # R = ---
    def ayuda_base(self):
        frame = self.crearframe()

        Label(frame, text=self.ayu_datos1, font=fuente, bg=color, fg=color2).grid(row=0, column=0)
        Label(frame, text=self.ayu_datos2, font=fuente, bg=color, fg=color2).grid(row=1, column=0)
        Label(frame, text=self.ayu_datos3, font=fuente, bg=color, fg=color2).grid(row=2, column=0)
        Label(frame, text=self.ayu_datos4, font=fuente, bg=color, fg=color2).grid(row=3, column=0)
        boton_volver = Button(frame, text=self.texto_boton_volver, width=ancho, font=fuente, bg=color, fg=color2,
                              cursor="hand2", bd=anchobd, relief=borde,
                              command=lambda: [self.ayuda(), frame.destroy()]).grid(row=5, column=0)

    # O = Crea un frame para el menú de modos de juego y los botones para seleccionar el modo de juego que desea el usuario
    # E = ---
    # S = Un frame con el menú de modos de juego y los botones con sus funciones respectivas
    # R = ---
    def menu_juegos(self):
        fr_juego = self.crearframe()

        titulo = Label(fr_juego, text=self.titulo_menu_juego, font=fuente, bg=color, fg=color2).grid(row=0, column=0)
        espacio = Label(fr_juego, text=" ", font=fuente, bg=color, fg=color2).grid(row=1, column=0)
        boton_tradicional = Button(fr_juego, text=self.texto_boton_tradicional, width=ancho, font=fuente, bg=color,
                                   fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                   command=lambda: [self.menu_dificultad('tradicional'), fr_juego.destroy()]).grid(
            row=2, column=0)
        boton_contiempo = Button(fr_juego, text=self.texto_boton_contiempo, width=ancho, font=fuente, bg=color,
                                 fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                 command=lambda: [self.menu_dificultad('contiempo'), fr_juego.destroy()]).grid(row=3,
                                                                                                               column=0)
        boton_contrareloj = Button(fr_juego, text=self.texto_boton_contrareloj, width=ancho, font=fuente, bg=color,
                                   fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                   command=lambda: [self.menu_dificultad('contrareloj'), fr_juego.destroy()]).grid(row=4,
                                                                                                                   column=0)
        boton_volver = Button(fr_juego, text=self.texto_boton_volver, width=ancho, font=fuente, bg=color, fg=color2,
                              cursor="hand2", bd=anchobd, relief=borde,
                              command=lambda: [self.menu_principal(), fr_juego.destroy()]).grid(row=5, column=0)

    # O = Crea un nuevo frame para un menú y sus botones para que el usuario escoga que Nivel de Juego desea jugar
    # E = El modo de juego elegido anteriormente por el usuario
    # S = Un frame con el menú de niveles de juego y los botones con sus funciones respectivas
    # R = ---
    def menu_dificultad(self, modo):
        fr_dificultad = self.crearframe()

        titulo = Label(fr_dificultad, text=self.titulo_menu_dificultad, font=fuente, bg=color, fg=color2).grid(row=0,
                                                                                                               column=0)
        espacio = Label(fr_dificultad, text=" ", font=fuente, bg=color, fg=color2).grid(row=1, column=0)
        if modo == 'tradicional':
            boton_principiante = Button(fr_dificultad, text=self.texto_boton_prin, width=ancho, font=fuente, bg=color,
                                        fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                        command=lambda: [self.seleccionar_sopa(modo, 'principiante.txt', 6),
                                                         fr_dificultad.destroy()]).grid(row=2, column=0)
            boton_intermedio = Button(fr_dificultad, text=self.texto_boton_inter, width=ancho, font=fuente, bg=color,
                                      fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                      command=lambda: [self.seleccionar_sopa(modo, 'intermedio.txt', 10),
                                                       fr_dificultad.destroy()]).grid(row=3, column=0)
            boton_avanzado = Button(fr_dificultad, text=self.texto_boton_avan, width=ancho, font=fuente, bg=color,
                                    fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                    command=lambda: [self.seleccionar_sopa(modo, 'avanzado.txt', 14),
                                                     fr_dificultad.destroy()]).grid(row=4, column=0)
            boton_volver = Button(fr_dificultad, text=self.texto_boton_volver, width=ancho, font=fuente, bg=color,
                                  fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                  command=lambda: [self.menu_juegos(), fr_dificultad.destroy()]).grid(row=5, column=0)
        elif modo == 'contiempo':
            boton_principiante = Button(fr_dificultad, text=self.texto_boton_prin, width=ancho, font=fuente, bg=color,
                                        fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                        command=lambda: [self.seleccionar_sopa(modo, 'principiante.txt', 6),
                                                         fr_dificultad.destroy()]).grid(row=2, column=0)
            boton_intermedio = Button(fr_dificultad, text=self.texto_boton_inter, width=ancho, font=fuente, bg=color,
                                      fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                      command=lambda: [self.seleccionar_sopa(modo, 'intermedio.txt', 10),
                                                       fr_dificultad.destroy()]).grid(row=3, column=0)
            boton_avanzado = Button(fr_dificultad, text=self.texto_boton_avan, width=ancho, font=fuente, bg=color,
                                    fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                    command=lambda: [self.seleccionar_sopa(modo, 'avanzado.txt', 14),
                                                     fr_dificultad.destroy()]).grid(row=4, column=0)
            boton_volver = Button(fr_dificultad, text=self.texto_boton_volver, width=ancho, font=fuente, bg=color,
                                  fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                  command=lambda: [self.menu_juegos(), fr_dificultad.destroy()]).grid(row=5, column=0)
        elif modo == 'contrareloj':
            boton_principiante = Button(fr_dificultad, text=self.texto_boton_prin, width=ancho, font=fuente, bg=color,
                                        fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                        command=lambda: [self.seleccionar_sopa(modo, 'principiante.txt', 6),
                                                         fr_dificultad.destroy()]).grid(row=2, column=0)
            boton_intermedio = Button(fr_dificultad, text=self.texto_boton_inter, width=ancho, font=fuente, bg=color,
                                      fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                      command=lambda: [self.seleccionar_sopa(modo, 'intermedio.txt', 10),
                                                       fr_dificultad.destroy()]).grid(row=3, column=0)
            boton_avanzado = Button(fr_dificultad, text=self.texto_boton_avan, width=ancho, font=fuente, bg=color,
                                    fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                    command=lambda: [self.seleccionar_sopa(modo, 'avanzado.txt', 14),
                                                     fr_dificultad.destroy()]).grid(row=4, column=0)
            boton_volver = Button(fr_dificultad, text=self.texto_boton_volver, width=ancho, font=fuente, bg=color,
                                  fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                  command=lambda: [self.menu_juegos(), fr_dificultad.destroy()]).grid(row=5, column=0)
        elif modo == 'versus':
            boton_principiante = Button(fr_dificultad, text=self.texto_boton_prin, width=ancho, font=fuente, bg=color,
                                        fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                        command=lambda: [self.juego_versus('principiante.txt'),
                                                         fr_dificultad.destroy()]).grid(row=2, column=0)
            boton_intermedio = Button(fr_dificultad, text=self.texto_boton_inter, width=ancho, font=fuente, bg=color,
                                      fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                      command=lambda: [self.juego_versus('intermedio.txt'),
                                                       fr_dificultad.destroy()]).grid(row=3, column=0)
            boton_avanzado = Button(fr_dificultad, text=self.texto_boton_avan, width=ancho, font=fuente, bg=color,
                                    fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                    command=lambda: [self.juego_versus('avanzado.txt'), fr_dificultad.destroy()]).grid(
                row=4, column=0)
            boton_volver = Button(fr_dificultad, text=self.texto_boton_volver, width=ancho, font=fuente, bg=color,
                                  fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                  command=lambda: [self.menu_juegos(), fr_dificultad.destroy()]).grid(row=5, column=0)

    # O = Se crea un nuevo frame con un menú pequeño para que el usuario decida si quiere usar palabras aleatorias de la base de datos o ingresar las palabras a buscar por su cuenta
    # E = El modo previamente elegido por el usuario, La dificultad elegida anteriormente y el numero de palabras que se van a buscar
    # S = El frame con el menu para seleccionar si desea palabras aleatorias o ingresarlas por su cuenta
    # R = ---
    def seleccionar_sopa(self, modo, dificultad, num):
        frame = self.crearframe()

        titulo = Label(frame, text=self.titulo_selec_palabras, font=fuente, bg=color, fg=color2).grid(row=0, column=0)
        espacio = Label(frame, text=" ", font=fuente, bg=color, fg=color2).grid(row=1, column=0)
        self.palabras_escritas = num
        self.palabras = []
        if modo == 'tradicional':
            boton_escribir = Button(frame, text=self.texto_boton_escribir, width=ancho, font=fuente, bg=color,
                                    fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                    command=lambda: [self.escribir_palabras(modo, dificultad), frame.destroy()]).grid(
                row=2, column=0)
            boton_normal = Button(frame, text=self.texto_boton_normal, width=ancho, font=fuente, bg=color, fg=color2,
                                  cursor="hand2", bd=anchobd, relief=borde,
                                  command=lambda: [self.seleccionar_palabras(modo, dificultad), frame.destroy()]).grid(
                row=3, column=0)
        elif modo == 'contiempo':
            boton_escribir = Button(frame, text=self.texto_boton_escribir, width=ancho, font=fuente, bg=color,
                                    fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                    command=lambda: [self.escribir_palabras(modo, dificultad), frame.destroy()]).grid(
                row=2, column=0)
            boton_normal = Button(frame, text=self.texto_boton_normal, width=ancho, font=fuente, bg=color, fg=color2,
                                  cursor="hand2", bd=anchobd, relief=borde,
                                  command=lambda: [self.seleccionar_palabras(modo, dificultad), frame.destroy()]).grid(
                row=3, column=0)
        elif modo == 'contrareloj':
            boton_escribir = Button(frame, text=self.texto_boton_escribir, width=ancho, font=fuente, bg=color,
                                    fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                    command=lambda: [self.escribir_palabras(modo, dificultad), frame.destroy()]).grid(
                row=2, column=0)
            boton_normal = Button(frame, text=self.texto_boton_normal, width=ancho, font=fuente, bg=color, fg=color2,
                                  cursor="hand2", bd=anchobd, relief=borde,
                                  command=lambda: [self.seleccionar_palabras(modo, dificultad), frame.destroy()]).grid(
                row=3, column=0)
        boton_volver = Button(frame, text=self.texto_boton_volver, width=ancho, font=fuente, bg=color, fg=color2,
                              cursor="hand2", bd=anchobd, relief=borde,
                              command=lambda: [self.menu_juegos(), frame.destroy()]).grid(row=4, column=0)

    # O = Se crea el frame para el menú de la base de datos, y los botones para ver, agregar, modificar y eliminar las palabras de la base de datos.
    # E = ---
    # S = Un frame con el menú para la Base de Datos y sus botones con sus respectivas funcionalidades
    # R = ---
    def base_de_datos(self):
        fr_base = self.crearframe()

        titulo = Label(fr_base, text=self.titulo_menu_bases, font=fuente, bg=color, fg=color2).grid(row=0, column=0)
        espacio = Label(fr_base, text=" ", font=fuente, bg=color, fg=color2).grid(row=1, column=0)
        boton_ver = Button(fr_base, text=self.texto_boton_ver, width=ancho, font=fuente, bg=color, fg=color2,
                           cursor="hand2", bd=anchobd, relief=borde,
                           command=lambda: [self.ver_palabras(), fr_base.destroy()]).grid(row=2, column=0)
        boton_agregar = Button(fr_base, text=self.texto_boton_agregar, width=ancho, font=fuente, bg=color, fg=color2,
                               cursor="hand2", bd=anchobd, relief=borde,
                               command=lambda: [self.menu_agregar(), fr_base.destroy()]).grid(row=3, column=0)
        boton_modificar = Button(fr_base, text=self.texto_boton_modificar, width=ancho, font=fuente, bg=color,
                                 fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                 command=lambda: [self.menu_modificar(), fr_base.destroy()]).grid(row=4, column=0)
        boton_eliminar = Button(fr_base, text=self.texto_boton_eliminar, width=ancho, font=fuente, bg=color, fg=color2,
                                cursor="hand2", bd=anchobd, relief=borde,
                                command=lambda: [self.menu_eliminar(), fr_base.destroy()]).grid(row=5, column=0)
        boton_volver = Button(fr_base, text=self.texto_boton_volver, width=ancho, font=fuente, bg=color, fg=color2,
                              cursor="hand2", bd=anchobd, relief=borde,
                              command=lambda: [self.menu_principal(), fr_base.destroy()]).grid(row=6, column=0)

    # O = Un nuevo frame en caso de que se quiera ingresar las palabras a buscar con un cuadro de texto para escribir las palabras que se desean buscar
    # E = El modo seleccionado por el usuario y el nivel de juego seleccionado previamente
    # S = Un frame con un cuadro de entrada de texto para ingresar las palabras a buscar y un botón para aceptar la palabra y otro para volver al menú de modos de juego
    # R = ---
    def escribir_palabras(self, modo, dificultad):
        frame = self.crearframe()

        titulo = Label(frame, text=self.titulo_escribir_palabras, font=fuente, bg=color, fg=color2).grid(row=0,
                                                                                                         column=0)
        espacio = Label(frame, text=" ", font=fuente, bg=color, fg=color2).grid(row=1, column=0)
        escribir = Entry(frame, font=fuente, bg=color, fg=color2)
        escribir.grid(row=2, column=0)
        boton_aceptar = Button(frame, text=self.texto_boton_aceptar, width=ancho, font=fuente, bg=color, fg=color2,
                               cursor="hand2", bd=anchobd, relief=borde,
                               command=lambda: [self.restar_escritas(modo, dificultad, escribir.get()),
                                                frame.destroy()]).grid(row=3, column=0)
        boton_volver = Button(frame, text=self.texto_boton_volver, width=ancho, font=fuente, bg=color, fg=color2,
                              cursor="hand2", bd=anchobd, relief=borde,
                              command=lambda: [self.menu_juegos(), frame.destroy()]).grid(row=4, column=0)
        if self.palabras_escritas == 0:
            return self.enviar_datos(modo, dificultad, self.palabras)
        else:
            pass

    # O = Agrega las palabras personalizadas a la lista de palabras y resta 1 cada vez que ingresa una nueva palabra a la lista
    # para contar la cantidad de palabras ingresadas y validar el nivel de juego
    # E = El modo de juego elegido por el usuario, la dificultad seleccionada y la palabra ingresada por el usuario
    # S = La palabra ingresada a la lista de las palabras por incluir en la sopa de letras
    # R = No se pueden ingresar palabras iguales
    def restar_escritas(self, modo, dificultad, palabra):
        palabra = palabra.upper()
        if self.esta(palabra, self.palabras):
            error = messagebox.showerror(self.titulo_error_pe, self.mensaje_error_pe)
            return self.escribir_palabras(modo, dificultad)
        elif palabra.isalpha():
            self.palabras_escritas -= 1
            self.palabras += [palabra]
            registrada = messagebox.showinfo(self.titulo_palabra_escrita,
                                             self.mensaje_palabra_escrita + str(self.palabras_escritas))
            return self.escribir_palabras(modo, dificultad)
        else:
            error = messagebox.showerror(self.titulo_error_pe, self.mensaje_error_pe)
            return self.escribir_palabras(modo, dificultad)

    # O = Abre el archivo de texto del diccionario de palabras del idioma que se está utilizando y crea un frame para mostrar todas las palabras que están actualemente en la base de datos
    # E = ---
    # S = Un frame con la lista de palabras que hay en la base de datos
    # R = ---
    def ver_palabras(self):
        diccionario = self.abrir_diccionario(self.diccionario)

        fr_ver = self.crearframe()

        mostrar = Text(fr_ver, state='normal', bg=color, fg=color2, font=fuente)
        mostrar.grid(row=0, column=0, sticky='NSWE')
        boton_volver = Button(fr_ver, text=self.texto_boton_volver, width=ancho, font=fuente, bg=color, fg=color2,
                              cursor="hand2", bd=anchobd, relief=borde,
                              command=lambda: [self.base_de_datos(), fr_ver.destroy()]).grid(row=1, column=0)
        for elemento in diccionario:
            mostrar.insert(INSERT, elemento + '\n')
        mostrar.config(state='disabled')

    # O = Evalúa la cantidad de elementos que tiene una lista
    # E = Una lista
    # S = El largo de la lista ingresada
    # R = El elemento ingresao debe se una lista
    def largo(self, lista):
        res = 0
        for elemento in lista:
            res += 1
        return res

    # O = Abre el archivo de texto del diccionario de palabras del idioma que se está utilizando y crea un frame para agregar una palabra de la base de datos con textos y
    # una entrada para ingresar la palabra que se desea agregar de la base de datos
    # E = ---
    # S = Un frame con un cuadro de texto para ingresar la palabra a agregar y botones para continuar o volver
    # R = ---
    def menu_agregar(self):
        diccionario = self.abrir_diccionario(self.diccionario)

        fr_agregar = self.crearframe()

        titulo = Label(fr_agregar, text=self.titulo_menu_agregar, font=fuente, bg=color, fg=color2).grid(row=0,
                                                                                                         column=0)
        espacio = Label(fr_agregar, text=" ", font=fuente, bg=color, fg=color2).grid(row=1, column=0)
        escribir = Entry(fr_agregar, font=fuente, bg=color, fg=color2)
        escribir.grid(row=2, column=0)
        boton_aceptar = Button(fr_agregar, text=self.texto_boton_aceptar, width=ancho, font=fuente, bg=color, fg=color2,
                               cursor="hand2", bd=anchobd, relief=borde,
                               command=lambda: [self.agregar(escribir.get(), diccionario), fr_agregar.destroy()]).grid(
            row=3, column=0)
        boton_volver = Button(fr_agregar, text=self.texto_boton_volver, width=ancho, font=fuente, bg=color, fg=color2,
                              cursor="hand2", bd=anchobd, relief=borde,
                              command=lambda: [self.base_de_datos(), fr_agregar.destroy()]).grid(row=4, column=0)

    # O = #O = Abre el archivo de texto del diccionario de palabras del idioma que se está utilizando y crea un frame para eliminar una palabra de la base de datos con textos y
    # una entrada para ingresar la palabra que se desea eliminar de la base de datos
    # E = ---
    # S = Un frame con un cuadro de texto para ingresar la palabra a eliminar y botones para continuar o volver
    # R = ---
    def menu_eliminar(self):
        diccionario = self.abrir_diccionario(self.diccionario)

        fr_eliminar = self.crearframe()

        titulo = Label(fr_eliminar, text=self.titulo_menu_eliminar, font=fuente, bg=color, fg=color2).grid(row=0,
                                                                                                           column=0)
        espacio = Label(fr_eliminar, text=" ", font=fuente, bg=color, fg=color2).grid(row=1, column=0)
        escribir = Entry(fr_eliminar, font=fuente, bg=color, fg=color2)
        escribir.grid(row=2, column=0)
        boton_aceptar = Button(fr_eliminar, text=self.texto_boton_aceptar, width=ancho, font=fuente, bg=color,
                               fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                               command=lambda: [self.eliminar(escribir.get(), diccionario),
                                                fr_eliminar.destroy()]).grid(row=3, column=0)
        boton_volver = Button(fr_eliminar, text=self.texto_boton_volver, width=ancho, font=fuente, bg=color, fg=color2,
                              cursor="hand2", bd=anchobd, relief=borde,
                              command=lambda: [self.base_de_datos(), fr_eliminar.destroy()]).grid(row=4, column=0)

    # O = Abre el archivo de texto del diccionario de palabras del idioma que se está utilizando y crea un frame para modificar una palabra de la base de datos con textos y
    # una entrada para ingresar la palabra que se desea modificar de la base de datos
    # E = ---
    # S = Un frame con un cuadro de texto para ingresar la palabra a modificar y botones para continuar o volver
    # R = ---
    def menu_modificar(self):
        diccionario = self.abrir_diccionario(self.diccionario)

        fr_modificar = self.crearframe()

        titulo = Label(fr_modificar, text=self.titulo_menu_modificar, font=fuente, bg=color, fg=color2).grid(row=0,
                                                                                                             column=0)
        espacio = Label(fr_modificar, text=" ", font=fuente, bg=color, fg=color2).grid(row=1, column=0)
        escribir = Entry(fr_modificar, font=fuente, bg=color, fg=color2)
        escribir.grid(row=2, column=0)
        boton_aceptar = Button(fr_modificar, text=self.texto_boton_aceptar, width=ancho, font=fuente, bg=color,
                               fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                               command=lambda: [self.modificar(escribir.get(), diccionario),
                                                fr_modificar.destroy()]).grid(row=3, column=0)
        boton_volver = Button(fr_modificar, text=self.texto_boton_volver, width=ancho, font=fuente, bg=color, fg=color2,
                              cursor="hand2", bd=anchobd, relief=borde,
                              command=lambda: [self.base_de_datos(), fr_modificar.destroy()]).grid(row=4, column=0)

    # O = Continua la función de modificar una palabra en la base de datos y solicita que escriba la palabra con la modificación realizada
    # E = La palabra a modificar y el diccionario que se está utilizando actualmente
    # S = Un frame con un cuadro de texto para ingresar la palabra modificada y botones para continuar o volver
    # R = ---
    def menu_modificar_aux(self, palabra, diccionario):
        fr_modificar = self.crearframe()

        titulo = Label(fr_modificar, text=self.titulo_menu_modificar_aux, font=fuente, bg=color, fg=color2).grid(row=0,
                                                                                                                 column=0)
        espacio = Label(fr_modificar, text=" ", font=fuente, bg=color, fg=color2).grid(row=1, column=0)
        escribir = Entry(fr_modificar, font=fuente, bg=color, fg=color2)
        escribir.grid(row=2, column=0)
        boton_aceptar = Button(fr_modificar, text=self.texto_boton_aceptar, width=ancho, font=fuente, bg=color,
                               fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                               command=lambda: [self.modificar_aux(escribir.get(), palabra, diccionario),
                                                fr_modificar.destroy()]).grid(row=3, column=0)
        boton_volver = Button(fr_modificar, text=self.texto_boton_volver, width=ancho, font=fuente, bg=color, fg=color2,
                              cursor="hand2", bd=anchobd, relief=borde,
                              command=lambda: [self.base_de_datos(), fr_modificar.destroy()]).grid(row=4, column=0)

    # O = Cambia todos los caracteres de la palabra a modificar en caracteres en mayúscula y verifica si la palabra se encuenta en la base de datos
    # E = La palabra a modificar y el diccionario que se está utilizando actualmente
    # S = Una llamada a otra función
    # R = La palabra debe existir en la base de datos
    def modificar(self, palabra, diccionario):
        palabra = palabra.upper()
        if self.esta(palabra, diccionario):
            return self.menu_modificar_aux(palabra, diccionario)
        return self.pantalla_error()

    # O = Se encarga de modificar la palabra en el diccionario y realizar el cambio respectivo y actualizacion de la base de datos
    # E = La palabra modificada, la palabra a modificar y el diccionario que se está utilizando actualmente
    # S = Una llamada a otra función y la base de datos actualizada
    # R = La palabra ingresada no puede ser un número
    def modificar_aux(self, cambio, palabra, diccionario):
        if palabra.isalpha():
            palabra = palabra.upper()
            cambio = cambio.upper()
            if self.largo(cambio) > 28:
                return self.pantalla_error()
            else:
                if self.esta(cambio, diccionario):
                    return self.pantalla_error()
                else:
                    nueva = []
                    for elemento in diccionario:
                        if palabra == elemento:
                            nueva += [cambio]
                        else:
                            nueva += [elemento]
                    with open(self.diccionario, 'w') as archivo:
                        archivo.write(str(nueva))
                        archivo.close()
                        return self.completado()
        else:
            return self.pantalla_error()

            # O = Crea un frame con un mensaje de error en caso de existir un error en el programa o una función

    # E = ---
    # S = Un frame con un mensaje de error y un botón de aceptar
    # R = ---
    def pantalla_error(self):
        fr_error = self.crearframe()

        titulo = Label(fr_error, text=self.mensaje_error, font=fuente, bg=color, fg=color2).grid(row=0, column=0)
        espacio = Label(fr_error, text=" ", font=fuente, bg=color, fg=color2).grid(row=1, column=0)
        boton_aceptar = Button(fr_error, text=self.texto_boton_aceptar, width=ancho, font=fuente, bg=color, fg=color2,
                               cursor="hand2", bd=anchobd, relief=borde,
                               command=lambda: [self.base_de_datos(), fr_error.destroy()]).grid(row=2, column=0)

    # O = Crea un frame con un mensaje para informar al usuario que se completó alguna función
    # E = ---
    # S = Un frame con un mensaje de completado y un botón de aceptar
    # R = ---
    def completado(self):
        fr_completo = self.crearframe()

        titulo = Label(fr_completo, text=self.mensaje_completado, font=fuente, bg=color, fg=color2).grid(row=0,
                                                                                                         column=0)
        boton_aceptar = Button(fr_completo, text=self.texto_boton_aceptar, width=ancho, font=fuente, bg=color,
                               fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                               command=lambda: [self.base_de_datos(), fr_completo.destroy()]).grid(row=1, column=0)

    # O = Ejecuta la inclusión de la nueva palabra a la base de datos
    # E = La palabra a agregar y el diccionario que se está utilizando actualmente
    # S = La nueva palabra agregada a la base de datos y llamada a una función
    # R = La palabra ingresada no puede ser un número
    def agregar(self, palabra, diccionario):
        if palabra.isalpha():
            palabra = palabra.upper()
            if self.largo(palabra) > 28:
                return self.pantalla_error()
            else:
                if self.esta(palabra, diccionario):
                    return self.pantalla_error()
                else:
                    palabra = palabra.upper()
                    diccionario += [palabra]
                    with open(self.diccionario, 'w') as archivo:
                        archivo.write(str(diccionario))
                        archivo.close()
                        return self.completado()
        else:
            return self.pantalla_error()

    # O = Ejecuta la eliminación de una palabra existente en la base de datos
    # E = La palabra a eliminar y el diccionario que se está utilizando actualmente
    # S = La palabra eliminada de la base de datos y una llamada a otra función
    # R = La palabra ingresada no puede ser un número
    def eliminar(self, palabra, diccionario):
        if palabra.isalpha():
            palabra = palabra.upper()
            if self.esta(palabra, diccionario):
                nueva = []
                for elemento in diccionario:
                    if palabra != elemento:
                        nueva += [elemento]
                with open(self.diccionario, 'w') as archivo:
                    archivo.write(str(nueva))
                    archivo.close()
                    return self.completado()
            else:
                return self.pantalla_error()
        else:
            return self.pantalla_error()

    # O = Evalúa si la palabra ingresada existe en la base de datos ingresada
    # E = La palabra a evaluar y el diccionario a utilizar
    # S = Un valor booleano True o False si la palabra se encuentra en el diccionario ingresado
    # R = ---
    def esta(self, palabra, diccionario):
        for elemento in diccionario:
            if palabra == elemento:
                return True
        return False

    # O = Se abre el archivo csv, se lee y se convierte en una lista
    # E = El nombre del archivo de texto según el idioma selecionado
    # S = Una lista conformada por los datos del archivo csv
    # R = Debe existir el archivo
    def abrir_diccionario(self, idioma):
        with open(idioma, 'r') as archivo:
            contenido = archivo.read()
            lista = ast.literal_eval(contenido)
            return lista

    # O = Selecciona las palabras de manera aleatoria para la creación de la sopa de letras
    # E = El modo seleccionado y la dificultad seleccionada previamente por el usuario
    # S = Una llamada a otra funcion con un lista de palabras para incluir en la sopa de letras
    # R = ---
    def seleccionar_palabras(self, modo, dificultad):
        self.dificultad = dificultad
        cantidad = self.tamaño_matriz()
        cantidad = cantidad - (
                    cantidad // 2)  # La cantidad de palabras a buscar es el tamaño de la matriz dividido entre 2
        self.cantidad_restante = cantidad
        matriz = self.abrir(dificultad)  # Se abre la matriz de la dificultad respectiva
        self.matriz_juego = matriz
        palabras = self.abrir_diccionario(self.diccionario)
        palabras = random.sample(palabras, cantidad)
        self.palabras_sopa = palabras
        print(palabras)
        direcciones = ['H', 'V', 'D']
        res = []
        for elemento in palabras:
            palabra = elemento
            direccion = random.choice(direcciones)
            res += [[palabra, direccion]]
        palabras = res
        if modo == 'tradicional':
            return self.juego_tradicional_inicio(dificultad, palabras, matriz)
        elif modo == 'contiempo':
            return self.juego_contiempo_inicio(dificultad, palabras, matriz)
        elif modo == 'contrareloj':
            return self.juego_contrareloj_inicio(dificultad, palabras, matriz)

    # O = Crear el campo de juego con todo lo necesario para jugar la sopa de letras tradicional
    # E = La dificultad del juego
    # S = El campo de juego tradicional
    # R = Se debe ingresar una de las 3 dificultades posibles
    def enviar_datos(self, modo, dificultad, palabras):
        self.dificultad = dificultad
        cantidad = self.tamaño_matriz()
        cantidad = cantidad - (
                    cantidad // 2)  # La cantidad de palabras a buscar es el tamaño de la matriz dividido entre 2
        self.cantidad_restante = cantidad
        matriz = self.abrir(dificultad)  # Se abre la matriz de la dificultad respectiva
        self.matriz_juego = matriz
        self.palabras_sopa = palabras
        print(palabras)
        direcciones = ['H', 'V', 'D']
        res = []
        for elemento in palabras:
            palabra = elemento
            direccion = random.choice(direcciones)
            res += [[palabra, direccion]]
        palabras = res
        if modo == 'tradicional':
            return self.juego_tradicional_inicio(dificultad, palabras, matriz)
        elif modo == 'contiempo':
            return self.juego_contiempo_inicio(dificultad, palabras, matriz)
        elif modo == 'contrareloj':
            return self.juego_contrareloj_inicio(dificultad, palabras, matriz)

    # O = Crear el campo de juego con todo lo necesario para jugar la sopa de letras tradicional
    # E = La dificultad del juego
    # S = El campo de juego tradicional
    # R = Se debe ingresar una de las 3 dificultades posibles
    def mostrar_palabras(self, frame, palabras, num):
        x = num
        for elemento in palabras:
            Label(frame, text=elemento, font=fuente, bg=color, fg=color2).grid(row=x, column=0)
            x += 1

    # O = Guardar el nombre del usuario que acaba de ganar una partida
    # E = El modo de juego ganado
    # S = El nombre ingresado guardado en la lista de rankings
    # R = No puede ser un nombre ya existente
    def guardar_nombre(self, modo):
        frame = self.crearframe()

        Label(frame, text=self.texto_nombre, font=fuente, bg=color, fg=color2).grid(row=0, column=0)
        nombre = Entry(frame, font=fuente, bg=color, fg=color2)
        nombre.grid(row=1, column=0)
        Label(frame, text=self.texto_tiempo, font=fuente, bg=color, fg=color2).grid(row=2, column=0)
        tiempo = Label(frame, text=var_tiempo.get(), font=fuente, bg=color, fg=color2)
        tiempo.grid(row=3, column=0)
        boton_aceptar = Button(frame, text=self.texto_boton_aceptar, width=ancho, font=fuente, bg=color, fg=color2,
                               cursor="hand2", bd=anchobd, relief=borde,
                               command=lambda: self.verificar_nombre(var_tiempo.get(), nombre.get(), frame, modo)).grid(
            row=4, column=0)

    # O = Guardar el nombre del usuario que acaba de ganar una partida
    # E = El modo de juego ganado
    # S = El nombre ingresado guardado en la lista de rankings
    # R = No puede ser un nombre ya existente
    def verificar_nombre(self, tiempo, nombre, frame, modo):
        lista = self.abrir_rangos(modo)
        nombre = nombre.upper()
        if nombre.isalpha():
            if self.dificultad == 'principiante.txt':
                num = 0
            elif self.dificultad == 'intermedio.txt':
                num = 1
            elif self.dificultad == 'avanzado.txt':
                num = 2
            for elemento in lista[num]:
                if elemento[0] == nombre:
                    messagebox.showerror(self.titulo_error_nombre, self.mensaje_error_nombre)
                    return self.guardar_nombre(modo)
            if modo == 'contiempo':
                with open('ranks_contiempo.txt', 'w') as archivo:
                    lista[num] += [[nombre, tiempo]]
                    archivo.write(str(lista))
                    return self.menu_principal()
            elif modo == 'contrareloj':
                with open('ranks_contrareloj.txt', 'w') as archivo:
                    lista[num] += [[nombre, tiempo]]
                    archivo.write(str(lista))
                    return self.menu_principal()
        else:
            messagebox.showerror(self.titulo_error_nombre, self.mensaje_error_nombre)
            return self.guardar_nombre(modo)

    # O = Guardar el nombre del usuario que acaba de ganar una partida
    # E = El modo de juego ganado
    # S = El nombre ingresado guardado en la lista de rankings
    # R = No puede ser un nombre ya existente
    def abrir_rangos(self, modo):
        if modo == 'contiempo':
            with open('ranks_contiempo.txt', 'r') as archivo:
                contenido = archivo.read()
                res = ast.literal_eval(contenido)
                return res
        elif modo == 'contrareloj':
            with open('ranks_contrareloj.txt', 'r') as archivo:
                contenido = archivo.read()
                res = ast.literal_eval(contenido)
                return res

    # O = Crear el campo de juego con todo lo necesario para jugar la sopa de letras tradicional
    # E = La dificultad del juego
    # S = El campo de juego tradicional
    # R = Se debe ingresar una de las 3 dificultades posibles
    def juego_tradicional_inicio(self, dificultad, palabras, matriz):
        juego = self.crearframe()
        juego_jr = self.crearframe()
        juego_jr.grid(row=0, column=1)

        if self.juego_iniciado == 'no':  # Solo la primera vez que se corre la función entra a este bloque
            self.dificultad = dificultad
            self.color_palabras = 'dark sea green'
            self.juego_actual = 'tradicional'

            sopa = self.crear_sopa(matriz, juego, palabras)
            self.crear_tablero(sopa, juego, 'inicio')

            faltan = Label(juego_jr, text=self.faltan + str(self.cantidad_restante), font=fuente, bg=color,
                           fg=color2).grid(row=0, column=0)
            boton_aceptar = Button(juego_jr, text=self.boton_mostrar_solucion, width=ancho, font=fuente, bg=color,
                                   fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                   command=lambda: self.mostrar_solucion(self.matriz_juego, juego, 'inicio')).grid(
                row=1, column=0)
            boton_salir = Button(juego_jr, text=self.texto_boton_salir, width=ancho, font=fuente, bg=color, fg=color2,
                                 cursor="hand2", bd=anchobd, relief=borde,
                                 command=lambda: [self.menu_principal(), juego.destroy(), juego_jr.destroy()]).grid(
                row=2, column=0)
            self.mostrar_palabras(juego_jr, self.palabras_sopa, 3)

        else:
            if self.cantidad_restante == 0:  # Si la cantidad de palabras a buscar es cero significa que ya el usuario ganó
                gane = messagebox.showinfo(self.titulo_ganaste, self.mensaje_ganaste)
                juego.destroy()
                juego_jr.forget()
                juego_jr.destroy()
                return self.menu_principal()
            else:
                faltan = Label(juego_jr, text=self.faltan + str(self.cantidad_restante), font=fuente, bg=color,
                               fg=color2).grid(row=0, column=0)
                boton_solucion = Button(juego_jr, text=self.boton_mostrar_solucion, width=ancho, font=fuente, bg=color,
                                        fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                        command=lambda: self.mostrar_solucion(self.matriz_juego, juego, 'inicio')).grid(
                    row=1, column=0)
                boton_salir = Button(juego_jr, text=self.texto_boton_salir, width=ancho, font=fuente, bg=color,
                                     fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                     command=lambda: self.menu_principal()).grid(row=2, column=0)
                self.mostrar_palabras(juego_jr, self.palabras_sopa, 3)
                self.crear_tablero(self.matriz_juego, juego, 'inicio')

    # O = Crear el campo de juego con todo lo necesario para jugar la sopa de letras tradicional
    # E = La dificultad del juego
    # S = El campo de juego tradicional
    # R = Se debe ingresar una de las 3 dificultades posibles
    def juego_contiempo_inicio(self, dificultad, palabras, matriz):
        juego = self.crearframe()
        juego_jr = self.crearframe()
        juego_jr.grid(row=0, column=1)

        if self.juego_iniciado == 'no':  # Solo la primera vez que se corre la función entra a este bloque
            self.dificultad = dificultad
            self.color_palabras = 'dark sea green'
            self.juego_actual = 'contiempo'

            sopa = self.crear_sopa(matriz, juego, palabras)
            self.crear_tablero(sopa, juego, 'inicio')

            faltan = Label(juego_jr, text=self.faltan + str(self.cantidad_restante), font=fuente, bg=color,
                           fg=color2).grid(row=0, column=0)
            boton_aceptar = Button(juego_jr, text=self.boton_mostrar_solucion, width=ancho, font=fuente, bg=color,
                                   fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                   command=lambda: self.mostrar_solucion(self.matriz_juego, juego, 'inicio')).grid(
                row=1, column=0)
            boton_salir = Button(juego_jr, text=self.texto_boton_salir, width=ancho, font=fuente, bg=color, fg=color2,
                                 cursor="hand2", bd=anchobd, relief=borde,
                                 command=lambda: [self.menu_principal(), juego.destroy(), juego_jr.destroy()]).grid(
                row=2, column=0)
            self.mostrar_palabras(juego_jr, self.palabras_sopa, 4)
            temporizador = Label(juego_jr, textvariable=var_tiempo, font=fuente, bg=color, fg=color2, bd=anchobd,
                                 relief=borde).grid(row=3, column=0)
            self.tiempo(juego_jr)
        else:
            if self.cantidad_restante == 0:  # Si la cantidad de palabras a buscar es cero significa que ya el usuario ganó
                gane = messagebox.showinfo(self.titulo_ganaste, self.mensaje_ganaste)
                juego.destroy()
                juego_jr.forget()
                return self.guardar_nombre('contiempo')
            else:
                faltan = Label(juego_jr, text=self.faltan + str(self.cantidad_restante), font=fuente, bg=color,
                               fg=color2).grid(row=0, column=0)
                boton_solucion = Button(juego_jr, text=self.boton_mostrar_solucion, width=ancho, font=fuente, bg=color,
                                        fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                        command=lambda: self.mostrar_solucion(self.matriz_juego, juego, 'inicio')).grid(
                    row=1, column=0)
                boton_salir = Button(juego_jr, text=self.texto_boton_salir, width=ancho, font=fuente, bg=color,
                                     fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                     command=lambda: [self.menu_principal(), juego.destroy(), juego_jr.destroy()]).grid(
                    row=2, column=0)
                self.mostrar_palabras(juego_jr, self.palabras_sopa, 4)
                self.crear_tablero(self.matriz_juego, juego, 'inicio')
                temporizador = Label(juego_jr, textvariable=var_tiempo, font=fuente, bg=color, fg=color2, bd=anchobd,
                                     relief=borde).grid(row=3, column=0)

    # O = Crear el campo de juego con todo lo necesario para jugar la sopa de letras tradicional
    # E = La dificultad del juego
    # S = El campo de juego tradicional
    # R = Se debe ingresar una de las 3 dificultades posibles
    def juego_contrareloj_inicio(self, dificultad, palabras, matriz):
        juego = self.crearframe()
        juego_jr = self.crearframe()
        juego_jr.grid(row=0, column=1)

        if self.juego_iniciado == 'no':  # Solo la primera vez que se corre la función entra a este bloque
            self.dificultad = dificultad
            self.color_palabras = 'dark sea green'
            self.juego_actual = 'contrareloj'

            sopa = self.crear_sopa(matriz, juego, palabras)
            self.crear_tablero(sopa, juego, 'inicio')

            faltan = Label(juego_jr, text=self.faltan + str(self.cantidad_restante), font=fuente, bg=color,
                           fg=color2).grid(row=0, column=0)
            boton_aceptar = Button(juego_jr, text=self.boton_mostrar_solucion, width=ancho, font=fuente, bg=color,
                                   fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                   command=lambda: self.mostrar_solucion(self.matriz_juego, juego, 'inicio')).grid(
                row=1, column=0)
            boton_salir = Button(juego_jr, text=self.texto_boton_salir, width=ancho, font=fuente, bg=color, fg=color2,
                                 cursor="hand2", bd=anchobd, relief=borde,
                                 command=lambda: [self.menu_principal(), juego.destroy(), juego_jr.destroy()]).grid(
                row=2, column=0)
            self.mostrar_palabras(juego_jr, self.palabras_sopa, 4)
            temporizador = Label(juego_jr, textvariable=var_tiempo, font=fuente, bg=color, fg=color2, bd=anchobd,
                                 relief=borde).grid(row=3, column=0)
            self.contrareloj(juego, juego_jr)
        else:
            if self.cantidad_restante == 0:  # Si la cantidad de palabras a buscar es cero significa que ya el usuario ganó
                gane = messagebox.showinfo(self.titulo_ganaste, self.mensaje_ganaste)
                juego.destroy()
                juego_jr.forget()
                return self.guardar_nombre('contrareloj')
            else:
                faltan = Label(juego_jr, text=self.faltan + str(self.cantidad_restante), font=fuente, bg=color,
                               fg=color2).grid(row=0, column=0)
                boton_solucion = Button(juego_jr, text=self.boton_mostrar_solucion, width=ancho, font=fuente, bg=color,
                                        fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                        command=lambda: self.mostrar_solucion(self.matriz_juego, juego, 'inicio')).grid(
                    row=1, column=0)
                boton_salir = Button(juego_jr, text=self.texto_boton_salir, width=ancho, font=fuente, bg=color,
                                     fg=color2, cursor="hand2", bd=anchobd, relief=borde,
                                     command=lambda: [self.menu_principal(), juego.destroy(), juego_jr.destroy()]).grid(
                    row=2, column=0)
                self.mostrar_palabras(juego_jr, self.palabras_sopa, 4)
                self.crear_tablero(self.matriz_juego, juego, 'inicio')
                temporizador = Label(juego_jr, textvariable=var_tiempo, font=fuente, bg=color, fg=color2, bd=anchobd,
                                     relief=borde).grid(row=3, column=0)

    # O = Seleccionar la direccion de las palabras para el modo versus
    # E = La lista de palabras
    # S = La lista de palabras con la direccion en la que va cada una
    # R = ---
    def seleccionar_direcciones_versus(self, palabras):
        print(palabras)
        direcciones = ['H', 'V', 'D']
        res = []
        for elemento in palabras:
            palabra = elemento
            direccion = random.choice(direcciones)
            res += [[palabra, direccion]]
        return res

    # O = Cambiar el valor de la variable que controla el color de las palabras a buscar en el tablero y volver a crear el tablero
    # E = la matriz, el frame del juego y la función inicio
    # S = Las palabras a buscar resaltadas en el tablero
    # R = ---
    def mostrar_solucion(self, matriz, juego, funcion):
        self.color_palabras = 'red'
        self.crear_tablero(matriz, juego, funcion)

    # O = Se vuelve a cargar el tablero para seleccionar la posicion final de la palabra
    # E = punto inicial y la matriz
    # S = El tablero con la funcion de seleccionar el punto final
    # R = ---
    def juego_tradicional_final(self, coord_inicio, matriz):
        juego = self.crearframe()

        self.coord_inicio = coord_inicio
        self.crear_tablero(matriz, juego, 'final')

    # O = Se crea la sopa de letras en la matriz
    # E = La matriz, un frame y la lista de palabras
    # S = La sopa de letras en la matriz
    # R = ---
    def crear_sopa(self, matriz, frame, palabras):
        largo_matriz = self.largo(matriz)  # Longitud de la matriz
        while palabras != []:
            print('cargando')
            fila_inicial = random.randint(0,
                                          largo_matriz - 1)  # Se busca una fila al azar ingresando un numero en el rango de el largo de la matriz
            columna_inicial = random.randint(0,
                                             largo_matriz - 1)  # Se busca una columna al azar ingresando un numero en el rango de el largo de la matriz
            for fila in range(largo_matriz):
                for columna in range(largo_matriz):
                    if fila == fila_inicial and columna == columna_inicial:
                        if palabras[0][1] == 'H':  # La palabra se coloca de forma horizontal
                            if self.hay_espacio(matriz, fila, columna, self.largo(palabras[0][0]), largo_matriz,
                                                palabras[0][1]):  # Si la palabra cabe en el espacio indicado se coloca
                                palabra = palabras[0][0]
                                x = fila
                                y = columna
                                while palabra != '':
                                    if matriz[x][y] == '0':  # Si el espacio está vacio se coloca la letra de la palabra
                                        matriz[x][y] = palabra[0]
                                        y += 1
                                        palabra = palabra[1:]
                                    else:
                                        fila_inicial = random.randint(0, largo_matriz - 1)
                                        columna_inicial = random.randint(0, largo_matriz - 1)
                                palabras = palabras[1:]
                            else:
                                fila_inicial = random.randint(0, largo_matriz - 1)
                                columna_inicial = random.randint(0, largo_matriz - 1)
                        elif palabras[0][1] == 'V':  # La palabra se coloca de forma vertical
                            if self.hay_espacio(matriz, fila, columna, self.largo(palabras[0][0]), largo_matriz,
                                                palabras[0][1]):
                                palabra = palabras[0][0]
                                x = fila
                                y = columna
                                while palabra != '':
                                    if matriz[x][y] == '0':
                                        matriz[x][y] = palabra[0]
                                        x += 1
                                        palabra = palabra[1:]
                                    else:
                                        fila_inicial = random.randint(0, largo_matriz - 1)
                                        columna_inicial = random.randint(0, largo_matriz - 1)
                                palabras = palabras[1:]
                            else:
                                fila_inicial = random.randint(0, largo_matriz - 1)
                                columna_inicial = random.randint(0, largo_matriz - 1)
                        elif palabras[0][1] == 'D':  # La palabra se coloca de forma diagonal
                            if self.hay_espacio(matriz, fila, columna, self.largo(palabras[0][0]), largo_matriz,
                                                palabras[0][1]):
                                palabra = palabras[0][0]
                                x = fila
                                y = columna
                                while palabra != '':
                                    if matriz[x][y] == '0':
                                        matriz[x][y] = palabra[0]
                                        x += 1
                                        y += 1
                                        palabra = palabra[1:]
                                    else:
                                        fila_inicial = random.randint(0, largo_matriz - 1)
                                        columna_inicial = random.randint(0, largo_matriz - 1)
                                palabras = palabras[1:]
                            else:
                                fila_inicial = random.randint(0, largo_matriz - 1)
                                columna_inicial = random.randint(0, largo_matriz - 1)
        return matriz

    # O = Se verifica si es posible meter una palabra en el espacio indicado
    # E = La matriz, la fila y la columna donde inicia la palabra, el largo de la palabra y el de la matriz, la direccion de la palabra
    # S = True si la palabra cabe en el espacio ingresado
    # R = ---
    def hay_espacio(self, matriz, fila, columna, largo_palabra, largo_matriz, direccion):
        tamaño = self.tamaño_matriz()
        if direccion == 'H':  # Si la direccion es horizontal
            cant_elementos = self.largo(matriz[fila][
                                        columna:])  # La cantidad de elementos que hay en el espacio donde se quiere meter la palabra
            if largo_palabra <= cant_elementos:  # Si la palabra es más grande que los espacios retorna False
                while matriz[fila][
                      columna:] != []:  # Mientras la lista con los espacios no sea vacia se podrá seguir metiendo la palabra letra por letra
                    if matriz[fila][columna] == '0':
                        columna += 1
                    else:
                        return False
                return True
            else:
                return False
        elif direccion == 'V':
            cant_elementos = 0
            while matriz[fila:] != []:
                if matriz[fila][columna] == '0':
                    cant_elementos += 1
                    fila += 1
                else:
                    return False
            if largo_palabra <= cant_elementos:
                return True
            else:
                return False
        else:
            cant_elementos = 0
            while matriz[fila:] != []:
                if fila < tamaño and columna < tamaño:
                    if matriz[fila][columna] == '0':
                        cant_elementos += 1
                        fila += 1
                        columna += 1
                    else:
                        return False
                else:
                    return False
            if largo_palabra <= cant_elementos:
                return True
            else:
                return False

    # O = Se abre el archivo csv, se lee y se convierte en matriz
    # E = ---
    # S = Una matriz con cada fila del archivo csv como una sublista
    # R = Debe existir el archivo
    def tamaño_matriz(self):
        if self.dificultad == 'principiante.txt':
            return 12
        elif self.dificultad == 'intermedio.txt':
            return 20
        else:
            return 28

    # O = Se abre un archivo que contiene el tablero para un nivel
    # E = El nivel de dificultad a abrir
    # S = Una matriz con los contenidos del archivo
    # R = Debe existir el archivo
    def abrir(self, nivel):
        with open(nivel, 'r') as archivo:
            contenido = archivo.read()
            matriz = ast.literal_eval(contenido)
            return matriz

    # E = ---
    # S = Un nuevo frame en la ventana maestra
    # R = ---
    # O = Crear un nuevo frame en la ventana maestra
    def crearframe(self):
        frame = Frame(master)
        frame.config(bg=color)
        frame.grid(row=0, column=0, sticky="NSWE")
        return frame

    # O = Crear un tablero con botones que tengan la funcion de marcar punto inicial o final y cambien de color para
    # indicar palabras encontradas o palabras a buscar
    # E = Una matriz y un frame y una funcion
    # S = El frame con un mapa formado por lo que esté en la matriz
    # R = Debe ingresar una matriz y un frame existente
    def crear_tablero(self, matriz, frame, funcion):
        letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # Lista de letras para reemplazar los ceros
        mapa_column = 0
        mapa_row = 0
        if funcion == 'inicio':  # Se indica funcion para crear los botones con la funcion de seleccionar el inicio o
                                # el final de una palabra
            for sublista in matriz:
                for elemento in sublista:
                    if elemento == '1':  # Si hay un 1 en la matriz significa que es una palabra encontrada
                        color_bloque = "lime green"
                        texto = 'X'
                    elif elemento == '0':  # Los ceros son espacios donde no hay nada
                        color_bloque = "dark sea green"
                        texto = random.choice(letras)  # Se selecciona una palabra al azar para reemplazar el cero
                    else:
                        color_bloque = self.color_palabras
                        texto = elemento
                    bloque = Button(frame, text=texto, bg=color_bloque, width='1', height='1', font=fuente_mapa,
                                    command=lambda x=mapa_row, y=mapa_column: self.seleccionar_inicio([x, y], matriz))
                    bloque.grid(row=mapa_row, column=mapa_column, sticky="NSEW")
                    mapa_column += 1
                mapa_column = 0
                mapa_row += 1
        else:
            for sublista in matriz:
                for elemento in sublista:
                    if elemento == '1':
                        color_bloque = "lime green"
                        texto = 'X'
                    elif elemento == '0':
                        color_bloque = "dark sea green"
                        texto = random.choice(letras)
                    else:
                        color_bloque = self.color_palabras
                        texto = elemento
                    bloque = Button(frame, text=texto, bg=color_bloque, width='1', height='1', font=fuente_mapa,
                                    command=lambda x=mapa_row, y=mapa_column: self.seleccionar_final([x, y],
                                                                                                     self.coord_inicio,
                                                                                                     matriz))
                    bloque.grid(row=mapa_row, column=mapa_column, sticky="NSEW")
                    mapa_column += 1
                mapa_column = 0
                mapa_row += 1

    # O = Marcar el inicio de una palabra en el tablero
    # E = La coordenada de inicio y la matriz
    # S = Las coordenadas enviadas a la funcion para marcar el punto final
    # R = ---
    def seleccionar_inicio(self, coord, matriz):
        opcion = messagebox.askquestion(self.titulo_seleccionar_inicio, self.mensaje_seleccionar_inicio)
        if opcion == 'yes':
            return self.juego_tradicional_final(coord, matriz)
        elif opcion == 'no':
            pass

    # O = Marcar la palabra que se forma con los puntos ingresados
    # E = Un punto de inicio y un punto final y la matriz
    # S = La palabra encontrada marcada en el tablero
    # R = Si no se ingresan puntos validos se mostrará un mensaje
    def seleccionar_final(self, coord_final, coord_inicio, matriz):
        opcion = messagebox.askquestion(self.titulo_seleccionar_final, self.mensaje_seleccionar_final)
        if opcion == 'yes':
            direccion = self.verificar_direcciones(coord_final,
                                                   coord_inicio)  # Se encuentra en que dirección va la palabra
            palabra = self.marcar_palabra(coord_final, coord_inicio, matriz,
                                          direccion)  # Se marca la palabra que se encuentra en esta linea si existe
        elif opcion == 'no':
            pass

    # O = Verificar que los dos puntos ingresados formen una linea horizontal, vertical o diagonal
    # E = Un punto de inicio y un punto final
    # S = La letra respectiva dependiendo de la direccion de la palara
    # R = Debe ingresar dos puntos que puedan formar una línea recta
    def verificar_direcciones(self, final, inicio):
        if inicio == final:
            mensaje = messagebox.showerror(self.titulo_error1_vd, self.mensaje_error1_vd)
        elif inicio[0] == final[0] and inicio[1] < final[
            1]:  # Si las posiciones están en la misma fila y la columna inicial es menor a la final pues la palabra es horizontal
            return 'H'
        elif inicio[1] == final[1] and inicio[0] < final[
            0]:  # Si las posiciones están en la misma columna y la fila inicial es menor a la final pues la palabra es vertical
            return 'V'
        elif self.verificar_diagonal(inicio, final):  # Se llama a la  funcion para verificar si la palabra es diagonal
            return 'D'
        else:
            mensaje = messagebox.showerror(self.titulo_error2_vd, self.mensaje_error2_vd)

            # O = Ir de celda en celda de forma diagonal empezando desde el punto que marcó el ususario hasta llegar al punto final indicado para ver si es posible ir en diagonal

    # E = Un punto de inicio y un punto final
    # S = True si los puntos van en una linea diagonal
    # R = Deben ser puntos presentes en la matriz
    def verificar_diagonal(self, inicio, final):
        lugar = inicio[:]
        while lugar[0] != final[0] + 1 and lugar[1] != final[
            1] + 1:  # Si la posicion es diferente a la posicion final + un espacio se continua con el ciclo
            if lugar[0] == final[0] and lugar[1] == final[
                1]:  # Si la posicion llega a ser True significa que la palabra va en diagonal
                return True
            else:
                lugar[0] += 1
                lugar[1] += 1
        return False

    # O = Se envia la dirección en la que va la palabra y se verifica si desde la posicion inicial y la posicion final se forma una de las palabras que se tienen que buscar
    # E = La posición final, inicial, la mtriz y una de las tres direcciones posibles
    # S = Si con las posiciones se forma una palabra entonces se cambia esa palabra por unos, si no se muestra un mensaje de error
    # R = Se deben ingresar posiciones validas, una matriz valida y una direccion = 'H' o 'V' o 'D'
    def marcar_palabra(self, final, inicio, matriz, direccion):
        nueva_matriz = copy.deepcopy(
            matriz)  # Se crea una copia de la matriz para no guadar cambios si la palabra no es correcta
        palabra = ''
        lugar = inicio
        if direccion == 'H':  # Horizontal
            while lugar[1] != final[1] + 1:
                if nueva_matriz[lugar[0]][
                    lugar[1]] == '0':  # Si en la seleccion hay un 0 significa que la palabra no es correcta
                    palabra = '0'
                    mensaje = messagebox.showerror(self.titulo_error_mp, self.mensaje_error_mp)
                    break
                else:
                    palabra += nueva_matriz[lugar[0]][lugar[1]]
                    nueva_matriz[lugar[0]][lugar[1]] = '1'  # Se cambia por un 1 si es una letra en la matriz
                    lugar[1] += 1
            for elemento in self.palabras_sopa:  # Se busca en la lista de las palabras seleccionadas para la sopa
                if elemento == palabra:  # Si la palabra formada está en la lista entra
                    self.juego_iniciado = 'si'  # Se marca el juego como ya iniciado
                    self.matriz_juego = nueva_matriz  # La matriz del juego cambia por la matriz con la palabra tachada
                    self.cantidad_restante -= 1  # Se le resta 1 al total de palabras restantes
                    if self.juego_actual == 'tradicional':  # Dependiendo de el tipo de juego actual se llama a la funcion de cada modo de juego
                        return self.juego_tradicional_inicio('', [], [])
                    elif self.juego_actual == 'contiempo':
                        return self.juego_contiempo_inicio('', [], [])
                    elif self.juego_actual == 'contrareloj':
                        return self.juego_contrareloj_inicio('', [], [])
            self.matriz_juego = matriz  # Si no coincide la palabra no pasa nada
            self.juego_iniciado = 'si'
            if self.juego_actual == 'tradicional':
                return self.juego_tradicional_inicio('', [], [])
            elif self.juego_actual == 'contiempo':
                return self.juego_contiempo_inicio('', [], [])
            elif self.juego_actual == 'contrareloj':
                return self.juego_contrareloj_inicio('', [], [])
        elif direccion == 'V':
            while lugar[0] != final[0] + 1:
                if nueva_matriz[lugar[0]][lugar[1]] == '0':
                    palabra = '0'
                    mensaje = messagebox.showerror(self.titulo_error_mp, self.mensaje_error_mp)
                    break
                else:
                    palabra += nueva_matriz[lugar[0]][lugar[1]]
                    nueva_matriz[lugar[0]][lugar[1]] = '1'
                    lugar[0] += 1
            for elemento in self.palabras_sopa:
                if elemento == palabra:
                    self.juego_iniciado = 'si'
                    self.matriz_juego = nueva_matriz
                    self.cantidad_restante -= 1
                    if self.juego_actual == 'tradicional':
                        return self.juego_tradicional_inicio('', [], [])
                    elif self.juego_actual == 'contiempo':
                        return self.juego_contiempo_inicio('', [], [])
                    elif self.juego_actual == 'contrareloj':
                        return self.juego_contrareloj_inicio('', [], [])
            self.matriz_juego = matriz
            self.juego_iniciado = 'si'
            if self.juego_actual == 'tradicional':
                return self.juego_tradicional_inicio('', [], [])
            elif self.juego_actual == 'contiempo':
                return self.juego_contiempo_inicio('', [], [])
            elif self.juego_actual == 'contrareloj':
                return self.juego_contrareloj_inicio('', [], [])

        elif direccion == 'D':
            while lugar[0] != final[0] + 1 and lugar[1] != final[1] + 1:
                if nueva_matriz[lugar[0]][lugar[1]] == '0':
                    palabra = '0'
                    mensaje = messagebox.showerror(self.titulo_error_mp, self.mensaje_error_mp)
                    break
                else:
                    palabra += nueva_matriz[lugar[0]][lugar[1]]
                    nueva_matriz[lugar[0]][lugar[1]] = '1'
                    lugar[0] += 1
                    lugar[1] += 1
            for elemento in self.palabras_sopa:
                if elemento == palabra:
                    self.juego_iniciado = 'si'
                    self.matriz_juego = nueva_matriz
                    self.cantidad_restante -= 1
                    if self.juego_actual == 'tradicional':
                        return self.juego_tradicional_inicio('', [], [])
                    elif self.juego_actual == 'contiempo':
                        return self.juego_contiempo_inicio('', [], [])
                    elif self.juego_actual == 'contrareloj':
                        return self.juego_contrareloj_inicio('', [], [])
            self.matriz_juego = matriz
            self.juego_iniciado = 'si'
            if self.juego_actual == 'tradicional':
                return self.juego_tradicional_inicio('', [], [])
            elif self.juego_actual == 'contiempo':
                return self.juego_contiempo_inicio('', [], [])
            elif self.juego_actual == 'contrareloj':
                return self.juego_contrareloj_inicio('', [], [])
        else:
            self.juego_iniciado = 'si'
            if self.juego_actual == 'tradicional':
                return self.juego_tradicional_inicio('', [], [])
            elif self.juego_actual == 'contiempo':
                return self.juego_contiempo_inicio('', [], [])
            elif self.juego_actual == 'contrareloj':
                return self.juego_contrareloj_inicio('', [], [])

    # E = Un frame
    # S = Un contador de tiempo
    # R = Debe ser un frame existente
    # O = Crear un contador de tiempo que se actualice automaticamente
    def tiempo(self, frame):
        m = 00
        s = 00
        for m in range(100):
            for s in range(60):
                var_tiempo.set(str(m) + ":" + str(s))
                time.sleep(1)
                frame.update()

    # E = Dos frames
    # S = Un contador regresivo
    # R = Deben ser dos frames existentes
    # O = Crear un reloj regresivo que se actualice automaticamente
    def contrareloj(self, frame, framejr):
        if self.dificultad == 'principiante.txt':
            m = 0
            s = 59
        elif self.dificultad == 'intermedio.txt':
            m = 1
            s = 0
        elif self.dificultad == 'avanzado.txt':
            m = 2
            s = 0
        while m > -1:
            s = 59
            while s > -1:
                time.sleep(1)
                var_tiempo.set(str(m) + ":" + str(s))
                frame.update()
                s -= 1
            m -= 1
        messagebox.showinfo("GAME OVER", "GAME OVER")
        frame.destroy()
        framejr.destroy()
        return self.menu_principal()


master = Tk()
master.resizable(0, 0)
master.title('Sopa de letras')

var_tiempo = StringVar()

programa = Interfaz(master)

master.mainloop()
