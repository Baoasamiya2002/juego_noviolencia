init python:
    import random

#personajes
define jugador = Character("[nombreJugador]")
define pareja = Character("[nombrePareja]")
define narrador = Character("", window_background=Frame("images/caja_texto_instruccion.png", 1, 1), what_color="#ffffff")
define oncahui = Character("Oncahui")

#videos
image fondo_inicio = Movie(size=(2560,1600), play="images/fondo_inicio.webm", loop = True)
image aparicion_mapa = Movie(size=(2560,1600), play="images/mapa_aparicion.webm", loop = False, image="images/aparicion_mapa/Mapa074.png")
image seleccion_personaje = Movie(size=(2560,1600), play="images/seleccion_personaje.webm", loop = False, image="images/seleccion_personaje.png")
image ximena_neutral = Movie(size=(2560,1600), play="images/ximena neutral.webm", loop = False, image="images/ximena neutral.png")
image carlos_neutral = Movie(size=(2560,1600), play="images/carlos neutral.webm", loop = False, image="images/carlos neutral.png")
image ximena_triste = Movie(size=(2560,1600), play="images/ximena triste.webm", loop = False, image="images/ximena triste.png")
image carlos_triste = Movie(size=(2560,1600), play="images/carlos triste.webm", loop = False, image="images/carlos triste.png")
image ximena_enojada = Movie(size=(2560,1600), play="images/ximena enojada.webm", loop = False, image="images/ximena enojada.png")
image carlos_enojado = Movie(size=(2560,1600), play="images/carlos enojado.webm", loop = False, image="images/carlos enojado.png")
#image oncahui_zoomout = Movie(size=(2560,1600), play="images/84ShYPezdrF1.webm", loop = False)
#image oncahui_zoomin = Movie(size=(2560,1600), play="images/iAr2wFDRsQgo.webm", loop = False)
image oncahui_zoomout = Movie(size=(2560,1600), play="images/Caminata uamito.webm", loop = False, image="uamito.png")
image oncahui_zoomin = Movie(size=(2560,1600), play="images/Salida.webm", loop = False)
image creditos = Movie(size=(2560,1600), play="images/creditos.webm", loop = False)

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
#image oncahui = "6.png"
image oncahui = "uamito.png"

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
    show aparicion_mapa
    pause 5.0
    hide aparicion_mapa
    show mapa
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
    jump evaluacion

label evaluacion:
    window hide diss
    scene black
    show oncahui_zoomout with fade
    #pause 3.0
    #show oncahui
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
        oncahui "Donde su {b}interfaz{/b} como menús, ventanas y botones me parecieron..."
        "Entendibles":
            oncahui "Le doy a su interfaz un 5 de 5 en claridad."
        "Aceptables":
            oncahui "Le doy a su interfaz un 3 de 5 en claridad."
        "Confusos":
            oncahui "Le doy a su interfaz un 0 de 5 en claridad."

    menu:
        oncahui "¡Ah! Otra cosa que recuerdo es el {b}lenguaje{/b} usado. El tono, palabras usadas y diálogos se me hicieron..."
        "Adecuados":
            oncahui "Noté que el guión fue apropiado."
        "Irregulares":
            oncahui "Noté que el guión tuvo cosas por mejorar."
        "Inadecuados":
            oncahui "Noté que el guión no era adecuado para mí."

    menu:
        oncahui "Además, honestamente, los {b}elementos visuales{/b} como ilustraciones y botones me parecieron..."
        "Atractivos":
            oncahui "¡Me gustó el estilo visual!"
        "Mixtos":
            oncahui "Varios elementos pudieron ser mejores."
        "Inadecuados":
            oncahui "No me gustaron..."

    oncahui "Bueno, voy a terminar de ver los créditos del juego y apreciar el esfuerzo de todos los involucrados"
    #hide oncahui    
    hide oncahui_zoomout
    show oncahui_zoomin
    pause 9.0
    hide oncahui_zoomin
    show creditos with fade
    pause 6.0
    return