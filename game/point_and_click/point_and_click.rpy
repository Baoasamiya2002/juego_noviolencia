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
            imagebutton idle (
                "point_and_click/image/" + str(i[0]) + ".webp"
            ) pos i[1] action Return(i[2])

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
    narrador "Un domingo por la tarde, Ximena y Carlos decidieron salir a una 
        cita." 
    narrador "Caminaban entre los árboles, no habían tenido tiempo de salir, 
        estaban en entregas finales y la carrera de cada uno comenzaba a ser 
        cada vez más demandante."
    jugador "Ay no amor. Hablé con mi equipo y quieren trabajar en la escuela. 
        Ya les dije que es más fácil que cada quien llegue a su casa y luego 
        ponernos a trabajar en línea."
    pareja "Sí."
    jugador "Y pues, salir de Santa Fe después de las 3 de la tarde y con 
        lluvias es una sentencia de muerte, ¿sabes a qué horas voy a llegar a mi 
        casa? Como a las 7."
    pareja "Ajá..."
    $ palabraGenero = "seria" if nombrePareja == "Ximena" else "serio"
    jugador "¿Y tú qué tienes? Estás muy [palabraGenero]."
    $ palabraGenero = "preocupada" if nombrePareja == "Ximena" else "preocupado"
    pareja "No, nada, solo estoy un poco [palabraGenero] por mi entrega del lunes."
    jugador "¿Sí? Pero a ti te sale todo a la primera… yo soy quien tiene que 
        preocuparse, casi no le entiendo a la UEA."
    pareja "Bueno, pero yo quiero preocuparme, ¿ok?"
    jugador "No me gusta cuando me hablas así, tan cortante."
    pareja "¿No será que más bien tú estás muy sensible?"
    jugador "¿Ves? Te estoy diciendo que algo tienes."
    pareja "Siempre quieres un pretexto para pelear."
    jugador "No, de verdad que no, solo quiero saber."
    pareja "Es que siento que eres muy absorbente, me hostigas."

    menu:
        "¿Tú respuesta?"
        "Qué confusión":
            jugador "¿Cómo? No entiendo, si según yo estábamos bien."
            pareja "Es que yo quiero estar bien, y tú empiezas a hacer preguntas 
                para que haya una discusión. ¿Sabes? Tú eres el que empieza a 
                sacar sus inseguridades."
        "Alguien más le metió la idea":
            jugador "¿Y eso de dónde lo sacas? Seguro tus amigos te volvieron a 
                hablar mal de mí."
            pareja "Al menos mis amigos me conocen mejor que tú, ¿ya viste que 
                en lugar de preguntar por qué pienso eso, hiciste que todo se 
                tratara sobre ti? Por eso siempre estoy mal contigo."
        "¡Qué drama!":
            jugador "Ay, siempre con tus dramas, la estábamos pasando bien, 
                siempre haces algo para hacerme sentir mal."
            pareja "Si quieres ya no te digo nada y cuando yo me vaya ni vas a 
                saber porqué."

    narrador "Hay un breve silencio entre Carlos y Ximena. Llevan tiempo 
        intentando sacar la relación a flote a pesar de sus compromisos con la 
        escuela, familia y amigos."
    jugador "Mejor, ya vámonos."
    pareja "¿Ves como tú eres la persona tóxica? No se puede hablar bien contigo."

    menu:
        "¿Tú respuesta?"
        "No quiero pelear":
            jugador "No quiero pelear, pero la verdad es que a veces siento 
                inseguridad. He llegado a pensar que te sientes mejor con tus 
                amigos que conmigo. Creo que te aburro o no sé..."
            pareja "Pues sí, me aburres con tus dramas e inseguridades. Ya no 
                puedo salir a gusto porque me vas a reclamar después."
        "Me estoy incomodando":
            jugador "Te digo que nos vayamos, ya no quiero estar aquí, todos nos 
                están viendo discutir..."
            pareja "Es tu culpa, si no hubieras preguntado nada, no me hubieras 
                hecho enojar. Eres bien, pinche imprudente."
        "Ya fue suficiente":
            jugador "Ya no te voy a seguir el juego. Cuando quieras hablar bien, 
                me mandas un mensaje."
            jump retroalimentacion_c3

    menu:
        "¿Tú respuesta?"
        "Disculparse":
            jugador "Bueno, tienes razón, discúlpame. Ya no hay que hablar de 
                eso, vamos a intentar pasarla bien."
            jump retroalimentacion_c1
        "Mantengo calma":
            $ palabraGenero = (
                "tranquila" if nombrePareja == "Ximena" else "tranquilo")
            jugador "Haber cálmate, quería hablarlo porque es importante que 
                sepas lo que siento, pero no llegamos a nada. Piénsalo y cuando 
                estés [palabraGenero], lo hablamos."
            jump retroalimentacion_c2
        "Terminar cita":
            jugador "¿Sabes qué? Ya echaste a perder la salida, mejor ya me voy."
            jump retroalimentacion_c3

label opcionNoDisponible:
    narrador "Disculpa, esta cita todavía no está disponible.\nDa click o toca 
        cualquier otra parte de la pantalla para poder volver a elegir"
    jump eleccionCita

label retroalimentacion_c1:
    narrador "¿Decidiste terminar la discusión porque de verdad quieres dejarlo 
        pasar, o porque no quieres que tu pareja continúe molesta?" 
    narrador "En una relación es importante sentirnos con la seguridad de 
        manifestar nuestras inconformidades sin miedo a que nuestra pareja se 
        moleste."
    jump finalJuego

label retroalimentacion_c2:
    narrador "Decidiste postergar la discusión, manteniendo tu postura y 
        planteando tus necesidades afectivas." 
    narrador "Es importante siempre cuidar de nosotros y nuestras emociones, y 
        establecer límites sobre lo que no vamos a permitir."
    jump finalJuego

label retroalimentacion_c3:
    narrador "Planteaste tus límites, sin embargo, cortaste la discusión sin 
        darle la oportunidad a la otra persona de expresar cómo se siente."
    jump finalJuego

label logro_aspersor:
    show logro_aspersor:
        xalign .05
    narrador "Con tu respuesta reflejaste empatía. Obtuviste un aspersor de agua 
        limpia para tu planta.\nDa click en el elemento para recogerlo y guardar."
    jump planta_florece

label penalizacion_aspersor:
    show penalizacion_aspersor:
        xalign .05
    narrador "¡Oh no! La mejor opción hubiera sido hablarlo. Obtuviste un 
        aspersor de agua sucia para tu planta. Da click en el elemento para 
        recogerlo y guardar."
    jump planta_marchita

label planta_florece:
    scene chapultepec_fondo
    show planta_florece:
        yalign .3
        xalign .5
    narrador "Tu planta ha comenzado a florecer."
    jump finalJuego

label planta_marchita:
    scene chapultepec_fondo
    show planta_marchita:
        yalign .3
        xalign .5
    narrador "Tu planta se siente un poco enferma."
    jump finalJuego