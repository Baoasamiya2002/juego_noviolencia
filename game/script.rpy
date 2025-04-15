init python:
    import random

#personajes
define jugador = Character("[nombreJugador]")
define pareja = Character("[nombrePareja]")

#imagenes
image fondo_inicio = Movie(play="images/fondo_inicio.webm", loop = True)
image aparicion_mapa = Movie(play="images/aparicion_mapa.webm", loop = False)
image aparicion_mapa_2 = Movie(play="images/aparicion_mapa_2.webm", loop = False)
image mapa = "images/mapa.png"
image chapultepec = "images/chapultepec.png"
image flor_s_s = "images/flor_s_s.png" #flor tuya sana y pareja sana
image flor_s_m = "images/flor_s_m.png" #flor tuya sana y pareja marchita
image flor_m_s = "images/flor_m_s.png" #flor tuya marchita y pareja sana
image flor_m_m = "images/flor_m_m.png" #flor tuya marchita y pareja marchita

#variables
default nombreJugador = ""
default nombrePareja = ""
default generoJugador = ""
default generoPareja = ""
default parejaViolenta = bool(random.getrandbits(1))

#escena inicial
label start:
    scene fondo_inicio
    "¡Bienvenido a 'Nuestra flor amorilla', un juego persuasivo donde tus decisiones marcarán el rumbo de una relación llena de ilusión y retos! 🌸💌"
    "Acabas de comenzar un nuevo noviazgo con alguien de la universidad con quien compartes sueños. Pero, ¿todo es tan perfecto como parece? Tienes claro que quieres construir algo distinto: una relación sana y duradera."
    "A lo largo del juego, enfrentarás situaciones cotidianas y desafiantes que pondrán a prueba no solo la relación, sino también tu autoestima, tus valores y tu capacidad para identificar señales de alerta."
    "Cada decisión que tomes afectará las flores que representan el amor y la salud emocional de ambos."
    "¿Podrás mantener vivas las flores de tu relación o permitirás que las actitudes negativas las marchiten? Descifra las pistas, elige con sabiduría y descubre si este noviazgo es el camino hacia tus sueños… o una lección que necesitas aprender."
    "Tú decides: florecer juntos o marchitarse en el intento. 🌷✨"
    "¿Listo para enfrentarte a los retos del noviazgo? ¡Tu historia comienza ahora! ❤️"

label definirNombreJugador:    
    $ nombreJugador = renpy.input("¿Cuál es tu nombre?", exclude = "0123456789+=,.?!{}[]()<>", length = 36).strip()

    if nombreJugador == "":
        "Por favor escribe un nombre"
        jump definirNombreJugador

label definirNombrePareja:
    $ nombrePareja = renpy.input("¿Cuál es el nombre de tu pareja? Puede ser ficticio", exclude = "0123456789+=,.?!{}[]()<>", length = 36).strip()
    if nombrePareja == "":
        "Por favor escribe un nombre"
        jump definirNombrePareja

menu definirGeneroJugador:
    "¿Con qué género te identificas?"
    "Femenino":
        $ generoJugador = "F"
    "Masculino":
        $ generoJugador = "M"
    "No binario":
        $ generoJugador = "NB"
    "Otro":
        $ generoJugador = renpy.input("Por favor escríbelo", exclude = "0123456789+=,.?!{}[]()<>", length = 36).strip()
        if generoJugador == "":
            "Por favor escribe el género o selecciona uno"
            jump definirGeneroJugador

menu definirGeneroPareja:
    with fade
    "¿Con qué género identificas a tu pareja?"
    "Femenino":
        $ generoPareja = "F"
    "Masculino":
        $ generoPareja = "M"
    "No binario":
        $ generoPareja = "NB"
    "Otro":
        $ generoPareja = renpy.input("Por favor escríbelo", exclude = "0123456789+=,.?!{}[]()<>", length = 36).strip()
        if generoPareja == "":
            "Por favor escribe el género o selecciona uno"
            jump definirGeneroPareja

label eleccionCita:
    scene fondo_inicio
    pause 0.5
    $ renpy.movie_cutscene("images/aparicion_mapa.webm")
    $ renpy.movie_cutscene("images/aparicion_mapa_2.webm")
    show mapa

    "Ahora elige, ¿Dónde tendrás una cita?\nDa click en cualquier parte de la pantalla para minimizar este mensaje"
    jump citasMapa

label finalJuego:
    "Muuchas gracias por jugar esta primera versión del juego"
    return
