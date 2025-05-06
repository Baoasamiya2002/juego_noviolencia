########## DEVIL SPIδεR'S POINT'n'CLICK PLUGIN ##########
# This plugin implements a modular point'n'click feature to make gameplay more interactive
# Currently supported features:
#   - Conditional interaction - make interactions available only when a certain condition is met
#   - Perspective switching - make segments take place in multiple rooms or angles
#   - Multiple ways to start or end one point'n'click segment - it's all a matter of jumping in and out of the segment

## Parameters ##
# There are numerous occasions where I list out a format for parameters. If the argument is in quotation marks in the format (like "this")
# the argument should also be in quotation marks

## Images ##
# There should an arbitrary amount of image pairs in game/point_and_click/image:
# the pair should consist of images in the filename format of X_idle.png and X_hover.png, where X is a word or a phrase
# this will be needed later in the plugin.

# This is the code that renders the point'n'click elements to the player

# To see steps necessary outside the PnC segments that initialize them, see the demo game's script.rpy file
# If you don't have the demo script, the rundown is that you have to set the current_room variable correctly and start the segment like this:
#   $ current_room = "example" # this value can be changed
#   jump pnc_loop

init -3:
    #Los valores de cada flor serán dentro de un array en enteros representando la violencia de cada cita
    #Ejemplo: En la primera cita el jugador no recibe violencia, pero sí en la segunda cita -> relacionFlags["flor_tuya"] = [0, 1]
    default relacionFlags = {"flor_tuya": [], "flor_pareja": []} 
screen show_buttons:
    for i in buttons:
        if (i[3] is None) or (eval(i[3])):
            imagebutton idle "point_and_click/image/" + str(i[0]) + ".webp" pos i[1] action Return(i[2])

style pnc_image_button:
    anchor (0.5, 0.5)

define diss = {"screens" : Dissolve(0.15)} # this allows the textbox to be hidden and shown without any pause

### INTERACTION LISTS ###
# The plugin supports creation of an unlimited amount of so-called interaction lists, which are Python lists of tuples of a given format:
# (("image_name"),(x_coordinate, y_coordinate),"label_name", condition),
# - image_name represents a string that will determine the button's appearance. To demonstrate with an example, if this parameter was "dog",
# then the plug-in expects dog_idle.png and dog_hover.png to exist in game/point_and_click/image.
# - x_coordinate and y_coordinate correspond to the position of the button in the screen, relative to the button's center.
# - label_name represents the label that triggers when that button is pressed.
# - conditions corresponds to either:
# -- a string containing Python expression that determines the button's visibility - it shows when the condition is True
# -- the None value - making the button visible at all times
# The lists should end in _buttons
define buttons = [
    (("chapultepec"),(0.312, 0.27),"citaChapultepec", None),
    (("zocalo"),(0.49, 0.21),"opcionNoDisponible", None),
    (("casa"),(0.53, 0.47),"opcionNoDisponible", None)
]

# This label handles showing the screen to the player.
label citasMapa:
    $ quick_menu = False
    window hide diss
    call screen show_buttons 
    window show diss
    $ quick_menu = True
    jump expression _return





### POINT'n'CLICK LABELS ###
# Labels within a point'n'click segment almost always end in a jump statement.

label citaChapultepec:
    scene chapultepec_fondo 
    show chapultepec_primer_plano
    narrador "Es domingo por la tarde. Ximena y Carlos caminan entre los árboles, disfrutando de un helado." 
    $ palabraGenero = "pensativo" if nombrePareja == "Carlos" else "pensativa"
    narrador "El ambiente es tranquilo, pero [nombrePareja] ha estado [palabraGenero]"
    $ palabraGenero = "callada" if nombreJugador == "Carlos" else "callado"
    $ renpy.show("ximena_triste" if nombrePareja  == "Ximena" else "carlos_triste")
    jugador "(Observando a [nombrePareja])  Estás muy [palabraGenero]…"
    pareja "(Suspira) Tengo la sensación de que nuestra comunicación está empeorando."
    
    menu:
        "¿Tú respuesta?"
        "Abrirse más y preguntar qué puede hacer mejor" if not parejaViolenta:
            $ renpy.show("ximena_neutral" if nombreJugador == "Ximena" else "carlos_neutral")
            jugador "¿Hay algo que puedas decirme ahora que me ayude a entenderte más? Quiero ser una pareja que te escuche de verdad."
            pareja "(Se relaja un poco)  Con que no me minimices cuando hablo. A veces solo quiero que me acompañes en lo que siento, sin que intentes corregirme."
            jugador "Lo voy a intentar. Me importa cómo te sientes."
            jump logro_aspersor
        "Exigir que se deje de hablar del tema" if not parejaViolenta:
            $ renpy.show("ximena_enojada" if nombreJugador == "Ximena" else "carlos_enojado")
            jugador "Ya basta, [nombrePareja]. No quiero hablar de tus cosas ahorita. ¿Puedes dejarlo por un día? Estoy harto de que todo sea “hablar y hablar”."
            $ palabraGenero = "incómoda" if nombrePareja == "Ximena" else "incómodo"
            pareja "(Traga saliva, [palabraGenero])  Está bien…"
            jump penalizacion_aspersor
        "Reconocer el error del día anterior y proponer una charla honesta" if not parejaViolenta:
            $ renpy.show("ximena_neutral" if nombreJugador == "Ximena" else "carlos_neutral")
            jugador "Sé que lo que dije ayer no fue justo. Me cerré sin pensar cómo te haría sentir. ¿Te parece si hablamos de eso con calma ahora?"
            pareja "Gracias por decirlo. Sí, me parece bien. Me gusta que podamos tener este tipo de conversaciones."
            jump logro_aspersor        
        "Insistir en que [nombrePareja] es el que causa los problemas" if parejaViolenta:
            $ renpy.show("ximena_enojada" if nombreJugador == "Ximena" else "carlos_enojado")
            jugador "La neta es que tú provocas todo esto. Siempre hay drama cuando estás tú. Si cambiaras un poco, todo sería más fácil."
            pareja "(Baja la mirada, en silencio)  …"
            jump penalizacion_aspersor
        "Abrirse más y preguntar qué puede hacer mejor " if parejaViolenta:
            $ renpy.show("ximena_neutral" if nombreJugador == "Ximena" else "carlos_neutral")
            jugador "¿Hay algo que puedas decirme ahora que me ayude a entenderte más? Quiero ser una pareja que te escuche de verdad."
            pareja "(Se relaja un poco)  Con que no me minimices cuando hablo. A veces solo quiero que me acompañes en lo que siento, sin que intentes corregirme."
            jugador "Lo voy a intentar. Me importa cómo te sientes."
            jump logro_aspersor   
        "Exigir que deje de hablar del tema" if parejaViolenta:
            $ renpy.show("ximena_enojada" if nombreJugador == "Ximena" else "carlos_enojado")
            $ palabraGenero = "harta" if nombreJugador == "Ximena" else "harto"
            jugador "Ya basta, [nombrePareja]. No quiero hablar de tus cosas ahorita. ¿Puedes dejarlo por un día? Estoy [palabraGenero] de que todo sea “hablar y hablar”."
            $ palabraGenero = "incómoda" if nombrePareja == "Ximena" else "incómodo"
            pareja "(Traga saliva, [palabraGenero])  Está bien…"
            jump penalizacion_aspersor

label opcionNoDisponible:
    narrador "Disculpa, esta cita todavía no está disponible.\nDa click o toca cualquier otra parte de la pantalla para poder volver a elegir"
    jump eleccionCita

label logro_aspersor:
    show logro_aspersor:
        xalign .05
    narrador "Con tu respuesta reflejaste empatía. Obtuviste un aspersor de agua limpia para tu planta.\nDa click en el elemento para recogerlo y guardar."
    jump planta_florece

label penalizacion_aspersor:
    show penalizacion_aspersor:
        xalign .05
    narrador "¡Oh no! La mejor opción hubiera sido hablarlo. Obtuviste un aspersor de agua sucia para tu planta. Da click en el elemento para recogerlo y guardar."
    jump planta_marchita

label planta_florece:
    scene chapultepec_fondo
    show planta_florece:
        yalign .3
        xalign .5
    narrador "Tu flor ha comenzado a florecer."
    jump finalJuego

label planta_marchita:
    scene chapultepec_fondo
    show planta_marchita:
        yalign .3
        xalign .5
    narrador "Tu flor se siente un poco enferma."
    jump finalJuego