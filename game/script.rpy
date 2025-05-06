init python:
    import random
    
    def continuar_frame(t, st, at):
        global frame_numero_formato
        global frame_numero
        global frame_numero_total
        global loop

        if frame_numero < frame_numero_total:
            frame_numero += 1
        else:
            if loop:
                frame_numero = 1
        
        if frame_numero < 10:
            frame_numero_formato = "00" + str(frame_numero)
        elif frame_numero < 100:
            frame_numero_formato = "0" + str(frame_numero)
        else:
            frame_numero_formato = str(frame_numero)

#personajes
define jugador = Character("[nombreJugador]")
define pareja = Character("[nombrePareja]")
define narrador = Character("", window_background=Frame("images/caja_texto_instruccion.png", 1, 1), what_color="#ffffff")

#videos
image fondo_inicio = Movie(size=(2560,1600), play="images/fondo_inicio.webm", loop = True)
image seleccion_personaje = Movie(size=(2560,1600), play="images/seleccion_personaje.webm", loop = False, image="images/seleccion_personaje.png")
image ximena_neutral = Movie(size=(2560,1600), play="images/ximena neutral.webm", loop = False, image="images/ximena neutral.png")
image carlos_neutral = Movie(size=(2560,1600), play="images/carlos neutral.webm", loop = False, image="images/carlos neutral.png")
image ximena_triste = Movie(size=(2560,1600), play="images/ximena triste.webm", loop = False, image="images/ximena triste.png")
image carlos_triste = Movie(size=(2560,1600), play="images/carlos triste.webm", loop = False, image="images/carlos triste.png")
image ximena_enojada = Movie(size=(2560,1600), play="images/ximena enojada.webm", loop = False, image="images/ximena enojada.png")
image carlos_enojado = Movie(size=(2560,1600), play="images/carlos enojado.webm", loop = False, image="images/carlos enojado.png")

#imagenes estaticas
image mapa = "images/mapa.webp"
image chapultepec_fondo = "images/chapus fondo.png"
image flor_capullo = "images/capullo.png"
image planta_florece = "images/planta_florece.png"
image planta_marchita = "images/planta_marchita.png"
image caja_texto_grande = "images/caja_texto_grande.png"
image boton_seleccion_ximena = "images/boton_seleccion_ximena.png"
image boton_seleccion_carlos = "images/boton_seleccion_carlos.png"
image chapultepec_primer_plano = "images/chapus fondo primer plano.png"
image logro_aspersor = "images/logro_aspersor.png"
image penalizacion_aspersor = "images/penalizacion_aspersor.png"

#animaciones
image aparicion_mapa:
    "images/aparicion_mapa/Mapa[frame_numero_formato].png"
    .05
    function continuar_frame
    repeat

#variables
default nombreJugador = ""
default nombrePareja = ""
default parejaViolenta = bool(random.getrandbits(1))
default frame_numero = 1
default frame_numero_formato = "001"
default frame_numero_total = 0
default loop = False
default accionJugador = ""

screen boton_eleccion_personaje():
    zorder 1
    imagebutton:
        xalign .33
        yalign .15
        idle "boton_seleccion_ximena"
        action Jump("seleccionXimena")
    imagebutton:
        xalign .61
        yalign .15
        idle "boton_seleccion_carlos"
        action Jump("seleccionCarlos")

#intro
label splashscreen:
    scene fondo_inicio
    $ frame_numero_total = 74
    show aparicion_mapa
    pause 5.0
    show caja_texto_grande:
        xalign .6
    show text """{color=#ffffff}{size=+8}UAM Cuajimalpa. Donde los pasillos universitarios guardan secretos que nadie ve...
    \nXimena y Carlos se conocieron en clase. Todo comenzó con una mirada, un dibujo, una canción compartida. Lo que parecía un noviazgo común se transforma cuando ciertas decisiones empiezan a romper la superficie.
    \nUna ciudad. Tres escenarios. Un vínculo que puede florecer... o desmoronarse. Cada elección que tomes los acercará al amor o los empujará hacia el abismo.
    \n{i}¿Estás listo para atravesar las capas de Latencia?{/i}{/size}
    \n\n{size=+20}¡Da click o toca tu pantalla!{/size}{/color}""" with Dissolve(1.5)
    pause
    return


#escena inicial
label start:
    scene fondo_inicio
    show mapa
    narrador "¡Bienvenide! Te explicaré cómo funciona el juego."
    narrador "Vas a tomar el papel de uno de los personajes que se te presentaron anteriormente, Ximena o Carlos."
    narrador "En el mapa que puedes ver, eligirás un lugar y tener una cita"
    hide mapa
    show flor_capullo:
        yalign .3
        xalign .5
    narrador "Además, tienes una planta que representa el estado de su relación."
    narrador """Necesitas mantener viva a tu planta, de acuerdo a las desiciones que tomes, 
    podrás recolectar ítems que la ayuden a crecer o la marchiten."""

label eleccionPersonaje:
    hide flor_capullo    
    show seleccion_personaje
    show screen boton_eleccion_personaje
    narrador "Elige el personaje con el que quieres jugar."

label seleccionXimena:
    hide screen boton_eleccion_personaje
    $ nombreJugador = "Ximena"
    $ nombrePareja = "Carlos"
    narrador "Haz seleccionado a Ximena"
    hide seleccion_personaje
    jump eleccionCita

label seleccionCarlos:
    hide screen boton_eleccion_personaje
    $ nombreJugador = "Carlos"
    $ nombrePareja = "Ximena"
    narrador "Haz seleccionado a Carlos"
    hide seleccion_personaje
    jump eleccionCita

label eleccionCita:
    show mapa
    narrador "Elige el lugar de la cita.\nDa click o toca cualquier parte de la pantalla para minimizar este mensaje."
    jump citasMapa

label finalJuego:
    scene fondo_inicio
    narrador "¡Muchas gracias por jugar esta primera versión del juego!"
    narrador "Si tienes comentarios, por favor compartelos con nosotros y ayudanos a mejorar"
    return
