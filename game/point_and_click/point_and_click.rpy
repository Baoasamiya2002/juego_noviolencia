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
    (("chapultepec"),(0.312, 0.33),"citaChapultepec", None),
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
    "Tú y [nombrePareja] deciden ir al Bosque de Chapultepec"
    pareja "Oye [nombreJugador], la verdad me siento con un poco de ansiedad por lo difícil que es la escuela y todavía me siento triste por lo de mi abuelita..."
    menu:
        "¿Tú respuesta?"
        "Ay [nombrePareja], sólo te estás ahogando en un vaso de agua":
            $ relacionFlags["flor_pareja"].append(NivelViolencia.INICIAL.value)
            pareja "(llorando y gritando)\n¡Como tú tienes todo no me puedes entender!"
            $ relacionFlags["flor_tuya"].append(NivelViolencia.INICIAL.value)
            menu:
                "¿Tú respuesta?"
                "Ay ya, mejor me voy y cuando te tranquilices hablamos":
                    $ relacionFlags["flor_pareja"][-1] = NivelViolencia.AUMENTO.value
                    jump decisionViolenta
                "Pues es que no te entiendo... pero quiero hacerlo":
                    $ relacionFlags["flor_pareja"][-1] = NivelViolencia.DISMINUCION.value
                    jump decisionMixta
        "Este...\nNo entiendo lo que sientes, pero quiero que me cuentes más":
            $ relacionFlags["flor_pareja"].append(NivelViolencia.NINGUNO.value)
            if parejaViolenta:
                pareja "Tú nunca me entiendes, mejor olvídalo"
                $ relacionFlags["flor_tuya"].append(NivelViolencia.INICIAL.value)
                jump decisionMixta
            else:
                pareja "Gracias, me siento mejor en tu compañía"
                $ relacionFlags["flor_tuya"].append(NivelViolencia.NINGUNO.value)
                jump decisionNoViolenta

    # if parejaViolenta:
    #     pareja "Ay [nombreJugador], sólo te estás ahogando en un vaso de agua"
    #     jugador "(llorando)\n¡Como tú tienes todo no me puedes entender!"
    #     $ relacionFlags["flor_tuya"].append(1)
    #     jump decidirRespuestaChapultepec
    # else:
    #     # $ dialogo = "¡Que "
    #     # if generoJugador == "F":
    #     #     $ dialogo += "linda "
    #     # if generoJugador == "M":
    #     #     $ dialogo += "guapo "
    #     # else:
    #     #     $ dialogo += "linde "
    #     # $ dialogo += "te vez! Le voy a dar like"
    #     # pareja "[dialogo]"
    #     pareja "Este...\nNo entiendo lo que sientes, pero quiero que me cuentes más"
    #     $ relacionFlags["flor_tuya"].append(0)
    #     jump decidirRespuestaChapultepec 

# menu decidirRespuestaChapultepec:
#     "¿Tú respuesta?" 
#     "Tú nunca me entiendes, mejor olvídalo" if relacionFlags["flor_tuya"][-1] == 0:
#         $ relacionFlags["flor_pareja"].append(1)
#         jump decisionMixta
#     "Gracias, me siento mejor en tu compañía" if relacionFlags["flor_tuya"][-1] == 0:
#         $ relacionFlags["flor_pareja"].append(0)
#         jump decisionNoViolenta
#     "Tú nunca me entiendes, mejor olvídalo" if relacionFlags["flor_tuya"][-1] == 1:
#         $ relacionFlags["flor_pareja"].append(1)
#         jump decisionMixta
#     "Gracias, me siento mejor en tu compañía" if relacionFlags["flor_tuya"][-1] == 1:
#         $ relacionFlags["flor_pareja"].append(0)
#         jump decisionNoViolenta

label decisionNoViolenta:
    #show expression "flor_[relacionFlags.get('flor_tuya')]_[relacionFlags.get('flor_pareja')]":
    #    yalign 0.5
    "¡Obtuviste agua para tu planta!"
    "También obtienes un logro por completar la primera cita"
    jump finalJuego

label decisionViolenta:
    #show expression "flor_[relacionFlags.get('flor_tuya')]_[relacionFlags.get('flor_pareja')]":
    "Oh no, esto afectará a las plantas..."
    "Aún así, obtienes un logro por completar la primera cita"
    jump finalJuego

label decisionMixta:
    #show expression "flor_[relacionFlags.get('flor_tuya')]_[relacionFlags.get('flor_pareja')]":
    "Aunque esto afectó a las plantas, pudiste darle un giro a la historia a través de la empatía"
    "Obtienes un logro por completar la primera cita"
    jump finalJuego