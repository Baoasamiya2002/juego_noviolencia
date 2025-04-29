init python:
    import random

    def continuar_frame(t, st, at):
        global frame_numero_formato
        global frame_numero
        global frame_numero_total

        if frame_numero < frame_numero_total:
            frame_numero += 1
        
        if frame_numero < 10:
            frame_numero_formato = "00" + str(frame_numero)
        elif frame_numero < 100:
            frame_numero_formato = "0" + str(frame_numero)

#personajes
define jugador = Character("[nombreJugador]")
define pareja = Character("[nombrePareja]")

#imagenes
image fondo_inicio = Movie(size=(2560,1600), play="images/fondo_inicio.webm", loop = True)
image mapa = "images/mapa.webp"
image chapultepec_fondo = "images/chapus fondo.png"
image flor_s_s = "images/flor_s_s.png" #flor tuya sana y pareja sana
image flor_s_m = "images/flor_s_m.png" #flor tuya sana y pareja marchita
image flor_m_s = "images/flor_m_s.png" #flor tuya marchita y pareja sana
image flor_m_m = "images/flor_m_m.png" #flor tuya marchita y pareja marchita
image aparicion_mapa:
        "images/aparicion_mapa/Mapa[frame_numero_formato].png"
        0.05
        function continuar_frame
        repeat
image caja_texto_grande = "images/caja_texto_grande.png"

#variables
default nombreJugador = ""
default nombrePareja = ""
default generoJugador = ""
default generoPareja = ""
default parejaViolenta = bool(random.getrandbits(1))
default frame_numero = 1
default frame_numero_formato = "001"
default frame_numero_total = 0
  
#intro
label splashscreen:
    scene fondo_inicio
    $ frame_numero_total = 74
    show aparicion_mapa
    pause 5.0
    show caja_texto_grande:
        xalign .6
    show text """{color=#ffffff}{size=+9}UAM Cuajimalpa. Donde los pasillos universitarios guardan secretos que nadie ve...
    \nXimena y Carlos se conocieron en clase. Todo comenzó con una mirada, un dibujo, una canción compartida. Lo que parecía un noviazgo común se transforma cuando ciertas decisiones empiezan a romper la superficie.
    \nUna ciudad. Tres escenarios. Un vínculo que puede florecer... o desmoronarse. Cada elección que tomes los acercará al amor o los empujará hacia el abismo.
    \n{i}¿Estás listo para atravesar las capas de Latencia?{/i}{/size}
    \n\n{size=+20}¡Da click o toca tu pantalla!{/size}{/color}""" with Dissolve(1.5)
    pause 20.0
    return


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
    show mapa
    "Ahora elige, ¿Dónde tendrás una cita?\nDa click en cualquier parte de la pantalla para minimizar este mensaje"
    jump citasMapa

label finalJuego:
    "Muuchas gracias por jugar esta primera versión del juego"
    return
