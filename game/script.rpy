#personajes
define narrador = Character(
    "", what_color="#ffffff", 
    window_background=Frame("gui/narrador_textbox.png"))
define novia = Character("Ximena", 
    window_background=Frame("gui/pareja_textbox_trans.png"))
define novio = Character("Carlos", 
    window_background=Frame("gui/pareja_textbox_trans.png"))
define oncahui = Character("Oncahui", 
    window_background=Frame("gui/oncahui_textbox.png"))

#constantes
define apodoNovia = "Xime"
define apodoNovio = "Charly"

#variables
default coleccionables = []
default decisionesJugador = []
default listaMito = []
#[0] = violencias ejercidas por la pareja
#[1] = violencias ejercidas por el jugador
default listaViolencia = [[],[]]
default listaPresion = []
default jugador = Persona(nombre="???")
default pareja = Persona(nombre="???")
default retroalimentacion = False

#videos
image fondo_inicio = Movie(
    size=(2560,1600), play="images/fondo_inicio.webm", loop = True)
image seleccion_personaje = Movie(
    size=(2560,1600), play="images/seleccion_personaje.webm", loop = False, 
    image="images/seleccion_personaje.png")
image emocion_seriedad_Carlos = Movie(
    size=(2560,1600), play="images/emocion/Carlos/seriedad.webm", loop = True)
image emocion_enojo_Carlos = Movie(
    size=(2560,1600), play="images/emocion/Carlos/enojo.webm", loop = True)
image emocion_felicidad_Carlos = Movie(
    size=(2560,1600), play="images/emocion/Carlos/felicidad.webm", loop = True)
image emocion_tristeza_Carlos = Movie(
    size=(2560,1600), play="images/emocion/Carlos/tristeza.webm", loop = True)
image emocion_seriedad_Ximena = Movie(
    size=(2560,1600), play="images/emocion/Ximena/seriedad.webm", loop = True)
image emocion_enojo_Ximena = Movie(
    size=(2560,1600), play="images/emocion/Ximena/enojo.webm", loop = True)
image emocion_felicidad_Ximena = Movie(
    size=(2560,1600), play="images/emocion/Ximena/felicidad.webm", loop = True)
image emocion_tristeza_Ximena = Movie(
    size=(2560,1600), play="images/emocion/Ximena/tristeza.webm", loop = True)

image oncahui_zoomout = Movie(
    size=(2560,1600), play="images/Caminata uamito.webm", loop = False, 
    image="uamito.png")
image oncahui_zoomin = Movie(
    size=(2560,1600), play="images/Salida.webm", loop = False)
image creditos = Movie(
    size=(2560,1600), play="images/creditos.webm", loop = False)

image cine_fondo = Movie(
    size=(2560,1600), play="images/cine fondo.webm", loop = True)
image caminata_chapultepec = Movie(
    size=(2560,1600), play="images/caminata_chapultepec.webm", loop = False, 
    image="images/caminata_chapultepec.png")

#imagenes estaticas
image chapultepec_fondo = "images/chapus fondo.png"
image planta_conjunto = "images/planta/capullo_conjunto.png"
image flor_capullo = "images/planta/capullo.png"
image planta_florece = "images/planta/florece.png"
image planta_marchita = "images/planta/marchita.png"
image boton_seleccion_ximena = "images/boton_seleccion_ximena.png"
image boton_seleccion_carlos = "images/boton_seleccion_carlos.png"
image chapultepec_primer_plano = "images/chapus fondo primer plano.png"
image logro_aspersor = "images/coleccionables/logro_aspersor.png"
image penalizacion_aspersor = "images/coleccionables/penalizacion_aspersor.png"
image tarjeta_spotify_intacta = "images/coleccionables/tarjeta_spotify_intacta.png"
image tarjeta_spotify_rota = "images/coleccionables/tarjeta_spotify_rota.png"
image oncahui = "uamito.png"


#texto de introducción
init python:

    with renpy.file('intro.txt', encoding='utf8') as f:
        texto_intro = f.read()


screen boton_eleccion_personaje():

    zorder 1
    imagebutton:
        xalign .19
        yalign .15
        idle "boton_seleccion_ximena"
        action Jump("seleccionNovia")
    imagebutton:
        xalign .75
        yalign .15
        idle "boton_seleccion_carlos"
        action Jump("seleccionNovio")


#introducción
label splashscreen:

    play music musica_fondo loop 
    scene fondo_inicio
    show screen intro
    pause
    hide screen intro
    return

screen intro():
    frame:
        xalign 0.6
        yalign 0.5
        xsize 2300
        ysize 1300
        padding (100, 30)
        background Frame("gui/narrador_textbox.png")
        truncate_text (texto_intro):
            shrink_to_fit 10 adjust_line_spacing_to_fit -10
            shrink_before_spacing False
            yalign 0.5

label start:

    scene fondo_inicio
    narrador "¡Bienvenide! Te explicaré cómo funciona el juego."
    narrador "Vas a tomar el papel de uno de los personajes que se te 
        mencionaron anteriormente, [novia.name] o [novio.name]."
    show planta_conjunto:
        yalign .3
        xalign .5
    narrador "Además, cada quien tiene una planta que representa el estado de 
        su relación."
    narrador "Sus decisiones las ayudarán a crecer o marchitarlas."
    hide planta_conjunto
    narrador "También hay botones en la parte inferior de la pantalla que te llevan a los principales menús (aunque desde ahí también hay otros para guardar/cargar partida, ir al menú principal y más información del juego)"
    narrador "El de progreso es para que veas es el estado actual de las plantas, los coleccionables que has ganado y para revisitar los dialogos."
    narrador "El de opciones te permite cambiar la letra, la velocidad del texto mostrado, volumen de la música y más. No dudes en personalizar tu experiencia de juego en cualquier momento."
    if renpy.variant("pc"):
        narrador "El de salir, como su nombre, cierra el juego. ¡No olvides guardar antes!"
    narrador "Y finalmente, el de ¡quitar! te da una salida de \"emergencia\" si en tu entorno alguien se te acerca y no quieres dar explicaciones. Te llevará a unas conferencias ofrecidas por la UPAV y silenciará la música del juego."
    narrador "Queremos que juegues con total comidad y honestidad, ninguna de tus respuestas serán grabadas."


label eleccionPersonaje:
    
    narrador "Y ¡oh mira! [novia.name] y [novio.name] están en el cine, vamos a 
        conocerlos." 
    show cine_fondo
    narrador "En el cine dentro de una sala, están Ximena y Carlos esperando a 
        que empiece la película."
    novia "Ay amor, ¡gracias por los boletos! Seguro te costó un buen 
        conseguirlos, escuché que había pocos."
    novio "Es que estuve pegado a la compu desde la preventa, sabía que tenías 
        muchas ganas de verla. Lo único malo es que vino mucha gente y solo 
        alcanzamos unas palomitas chicas..."
    novia "No te preocupes, me encanta compartir las palomitas y más si es 
        contigo."
    novio "Gracias amor, me haces muy feliz Xime."
    hide cine_fondo
    show seleccion_personaje
    show screen boton_eleccion_personaje
    narrador "Ahora que los conoces un poco, elige el personaje con el que 
        quieres jugar."


label seleccionNovia:

    hide screen boton_eleccion_personaje
    $ jugador = Persona(novia.name, apodoNovia, Character(
        novia.name, 
        window_background=Frame("gui/jugador_textbox_trans.png")))
    $ pareja = Persona(novio.name, apodoNovio, Character(
        novio.name, 
        window_background=Frame("gui/pareja_textbox_trans.png")))
    narrador "Has seleccionado a [jugador.nombre]"
    hide seleccion_personaje
    jump telefonoConversacion


label seleccionNovio:

    hide screen boton_eleccion_personaje
    $ jugador = Persona(novio.name, apodoNovio, Character(
        novio.name, 
        window_background=Frame("gui/jugador_textbox_trans.png")))
    $ pareja = Persona(novia.name, apodoNovia, Character(
        novia.name, 
        window_background=Frame("gui/pareja_textbox_trans.png")))
    narrador "Has seleccionado a [jugador.nombre]"
    hide seleccion_personaje
    jump citaChapultepec


label eleccionCita:

    show mapa
    narrador "Elige el lugar de la cita.\nDa click o toca en la 
        pantalla para minimizar este mensaje."
    #jump citasMapa

label finalJuego:

    scene fondo_inicio
    narrador "¡Muchas gracias por jugar esta primera versión del juego!"
    narrador "Si tienes comentarios, por favor compartelos con nosotros y 
        ayudanos a mejorar"
    jump evaluacion


label evaluacion:
    window hide diss
    scene black
    show oncahui_zoomout with fade
    oncahui "¡Ya terminé el juego!"

    menu:
        oncahui "Y analizándolo, creo que el {b}videojuego{/b}…"
        "Me gustó":
            oncahui "Si, ¡se me hizo bueno!"
        "Me fue indiferente":
            oncahui "Si, estuvo ok."
        "No me gustó":
            oncahui "Si, ¡no estuvo bueno!"
    
    menu:
        oncahui "Y en el caso de la {b}diversión{/b}, fue un juego… "
        "Entretenido":
            oncahui "La pasé bien jugándolo."
        "Regular":
            oncahui "Pudo ser más divertido."
        "Aburrido":
            oncahui "No pasó nada divertido..."
    
    menu:
        oncahui "Además, la {b}dificultad{/b} del juego fue..."
        "Fácil":
            oncahui "Fue un juego fácil."
        "Moderado":
            oncahui "Fue un juego moderado."
        "Difícil":
            oncahui "Fue un juego difícil."

    menu:
        oncahui "Donde su {b}interfaz{/b} como menús, ventanas y botones me 
            parecieron..."
        "Entendibles":
            oncahui "Le doy a su interfaz un 5 de 5 en claridad."
        "Aceptables":
            oncahui "Le doy a su interfaz un 3 de 5 en claridad."
        "Confusos":
            oncahui "Le doy a su interfaz un 0 de 5 en claridad."

    menu:
        oncahui "¡Ah! Otra cosa que recuerdo es el {b}lenguaje{/b} usado. El 
            tono, palabras usadas y diálogos se me hicieron..."
        "Adecuados":
            oncahui "Noté que el guión fue apropiado."
        "Irregulares":
            oncahui "Noté que el guión tuvo cosas por mejorar."
        "Inadecuados":
            oncahui "Noté que el guión no era adecuado para mí."

    menu:
        oncahui "Además, honestamente, los {b}elementos visuales{/b} como 
            ilustraciones y botones me parecieron..."
        "Atractivos":
            oncahui "¡Me gustó el estilo visual!"
        "Mixtos":
            oncahui "Varios elementos pudieron ser mejores."
        "Inadecuados":
            oncahui "No me gustaron..."

    oncahui "Bueno, voy a terminar de ver los créditos del juego y apreciar el 
        esfuerzo de todos los involucrados"
    #hide oncahui    
    hide oncahui_zoomout
    show oncahui_zoomin
    pause 9.0
    hide oncahui_zoomin
    show creditos with fade
    pause 6.0
    return