init python:

    import time
    
    def callbackJugador(ctc, **kwargs):
        if ctc == "begin":
            renpy.music.play("audio/phone/send.mp3", channel="sound")

    def callbackPareja(ctc, **kwargs):
        if ctc == "begin":
            renpy.music.play("audio/phone/receive.mp3", channel="sound")
    
    def definirPersonaje(personajeJugador, apodoJugador, personajePareja, apodoPareja):

        global jugador, pareja, viejoAmigue

        jugador = Persona(
            personajeJugador.name, 
            apodoJugador, 
            Character(
                personajeJugador.name, 
                window_background=Frame("gui/jugador_textbox_trans.png"),
                callback=callbackJugador))
        pareja = Persona(
            personajePareja.name, 
            apodoPareja, 
            Character(
                personajePareja.name, 
                window_background=Frame("gui/pareja_textbox_trans.png"),
                callback=callbackPareja))
        
        if apodoJugador == APODO_NOVIA:

            viejoAmigue = Persona(
                "Sofia", 
                "", 
                Character(
                    "Sofia", 
                    window_background=Frame("gui/jugador_textbox_trans.png")))
        else:

            viejoAmigue = Persona(
                "Armando", 
                "", 
                Character(
                    "Armando", 
                    window_background=Frame("gui/jugador_textbox_trans.png")))
 
    #texto introductorio
    with renpy.file('misc/intro.txt', encoding='utf8') as f:
        texto_intro = f.read()

#personajes
define narrador = Character(
    None, what_color="#ffffff", 
    window_background=Frame("gui/narrador_textbox.png"))
define novia = Character("Fernanda", 
    window_background=Frame("gui/pareja_textbox_trans.png"))
define novio = Character("Carlos", 
    window_background=Frame("gui/pareja_textbox_trans.png"))
define oncahui = Character("Oncahui", 
    window_background=Frame("gui/oncahui_textbox.png"))
define narrator = nvl_narrator

#constantes
define APODO_NOVIA = "Fer"
define APODO_NOVIO = "Charly"
define LISTA_ESTADO_PLANTA = ["marchita", "levemente_marchita", 
    "levemente_florece", "florece"]
define NOMBRE_CAPA = ["Primera capa", "Segunda capa", "Tercera capa", 
    "Cuarta capa"]
define LISTA_MENSAJE_ALEATORIO = [
    ("Oye, acabo de llegar, pero creo que lo tendremos que cancelar..."+
    "<emoji_lagrima> es que me siento mal... de que no estás aquí conmigo "+
    "<emoji_risa> jaja"),
    ("Holaa amor, ya estoy aquí, pero tú tranqui. Te espero con gusto, así que"+
    " no te apures <emoji_corazon>"),
    ("Ya llegué. Me dices si vas a tardar y me doy una vuelta jeje"+
    "<emoji_risa_nerviosa>. Es que me da amsiedad jaj")]
define TEXTO_CPS_PREVIEW = PreviewSlowText(
    "{color=#000000}¡Bienvenide! Este juego se centra en la lectura. Modifica "
    "estas opciones para tener la mejor experiencia.{/color}")
define LISTA_FINAL_PRIMERA_OPCION = [
    [False, True, False, True],
    [True, False],
    [False, True, True],
    [False, False, False],
    [False, True, True, True],
    [True, True],
    [False, False, True, False]]
define LISTA_FINAL_SEGUNDA_OPCION = [
    [True, True], 
    [False], 
    [True, False]]

#variables
default coleccionables = []
default listaEstereotipo = []
default listaViolenciaJugador = []
default listaViolenciaPareja = []
default listaPresion = []
default listaMito = []
default jugador = Persona(nombre="???")
default pareja = Persona(nombre="???")
default viejoAmigue = Persona(nombre="???")
default palabraGenero = ""
default codigoCompartido = ""
default info_descriptiva = ""
default retroalimentacion = False
default persistent.Config = True
default capa_seleccionada = ""
default color_var = Color((0, 0, 0))
default persistent.final_tercera_opcion = True
default persistent.final_segunda_opcion = [True, False]
default persistent.final_primera_opcion = False
default persistent.ocultar = False



#videos
image fondo_inicio = Movie(
    size=(2561,1600), play="images/fondo_inicio.webm", 
    start_image = "images/fondo_inicio_frame.jpg",
    loop = True) 
image seleccion_personaje = Movie(
    size=(2560,1600), play="images/seleccion_personaje.webm", loop = False, 
    image="images/seleccion_personaje.png")
image cine_fondo = Movie(
    size=(2560,1600), play="images/cine fondo.webm", loop = True)
image caminata_chapultepec = Movie(
    size=(2560,1600), play="images/caminata_chapultepec.webm", loop = False, 
    image="images/caminata_chapultepec.png")
image emocion_seriedad_Carlos = Movie(
    size=(2560,1600), play="images/emocion/Carlos/seriedad.webm",
    start_image = "images/emocion/Carlos/seriedad_frame.jpg",
    loop = True)
image emocion_enojo_Carlos = Movie(
    size=(2560,1600), play="images/emocion/Carlos/enojo.webm",
    start_image = "images/emocion/Carlos/enojo_frame.jpg", 
    loop = True)
image emocion_felicidad_Carlos = Movie(
    size=(2560,1600), play="images/emocion/Carlos/felicidad.webm",
    start_image = "images/emocion/Carlos/felicidad_frame.jpg", 
    loop = True)
image emocion_tristeza_Carlos = Movie(
    size=(2560,1600), play="images/emocion/Carlos/tristeza.webm",
    start_image = "images/emocion/Carlos/tristeza_frame.jpg", 
    loop = True)
image emocion_seriedad_Fernanda = Movie(
    size=(2560,1600), play="images/emocion/Fernanda/seriedad.webm",
    start_image = "images/emocion/Fernanda/seriedad_frame.jpg", 
    loop = True)
image emocion_enojo_Fernanda = Movie(
    size=(2560,1600), play="images/emocion/Fernanda/enojo.webm",
    start_image = "images/emocion/Fernanda/enojo_frame.jpg", 
    loop = True)
image emocion_felicidad_Fernanda = Movie(
    size=(2560,1600), play="images/emocion/Fernanda/felicidad.webm",
    start_image = "images/emocion/Fernanda/felicidad_frame.jpg", 
    loop = True)
image emocion_tristeza_Fernanda = Movie(
    size=(2560,1600), play="images/emocion/Fernanda/tristeza.webm",
    start_image = "images/emocion/Fernanda/tristeza_frame.jpg", 
    loop = True)
image planta_capullo = Movie(play="images/planta/capullo.webm", loop = True)
image planta_marchita = Movie(play="images/planta/marchita.webm", loop = True)
image planta_levemente_marchita = Movie(
    play="images/planta/levemente_marchita.webm", loop = True)
image planta_levemente_florece = Movie(
    play="images/planta/levemente_florece.webm", loop = True)
image planta_florece = Movie(play="images/planta/florece.webm", loop = True)
image oncahui_zoomout = Movie(
    size=(2560,1600), play="images/Caminata uamito.webm", loop = False, 
    image="uamito.png")
image oncahui_zoomin = Movie(
    size=(2560,1600), play="images/Salida.webm", loop = False)
image creditos_iniciales = Movie(
    size=(2560,1600), play="images/creditos_iniciales.webm", loop = False)
image creditos_finales = Movie(
    size=(2560,1600), play="images/creditos_finales.webm", loop = False)
image tutorial_guardar = Movie(
    size=(1572,987), play="images/tutorial/guardar.webm", 
    start_image = "images/tutorial/guardar_focus_1.png")
image tutorial_cargar = Movie(
    size=(1572,987), play="images/tutorial/cargar.webm", 
    start_image = "images/tutorial/cargar_focus_1.png")
image tutorial_cargar_capa = Movie(
    size=(1572,987), play="images/tutorial/cargar_capa.webm", 
    start_image = "images/tutorial/cargar_capa_1.png")
image tutorial_guardar_auto = Movie(
    size=(1572,987), play="images/tutorial/guardar_auto.webm", 
    start_image = "images/tutorial/guardar_auto_1.png")
image tutorial_recursos = Movie(
    size=(1572,987), play="images/tutorial/recursos.webm", 
    start_image = "images/tutorial/recursos_focus_1.png")
image tutorial_configuracion = Movie(
    size=(1572,987), play="images/tutorial/configuracion.webm", 
    start_image = "images/tutorial/configuracion_focus_1.png")

#imagenes estaticas
image boton_opciones = "gui/button/dialogo/opciones.png" 
image boton_config = "gui/button/dialogo/config.png"
image boton_progreso = "gui/button/dialogo/progreso.png"
image boton_quitar = "gui/button/dialogo/quitar.png"
image boton_cargar = "gui/button/dialogo/cargar.png"
image boton_guardar = "gui/button/dialogo/guardar.png"
image boton_opciones_quick = "gui/button/dialogo/opciones_quick.png"
image boton_mas_info = "gui/button/dialogo/mas_info.png"
image boton_tutorial = "gui/button/dialogo/tutorial.png"
image boton_recursos = "gui/button/dialogo/recursos.png"
image chapultepec_fondo = "images/chapus fondo.png"
image planta_conjunto = "images/planta/capullo_conjunto.png"
image planta_fondo = "images/planta/fondo.png"
image chapultepec_primer_plano = "images/chapus fondo primer plano.png"
image logro_aspersor = "images/coleccionables/logro_aspersor.png"
image penalizacion_aspersor = "images/coleccionables/penalizacion_aspersor.png"
image tarjeta_intacta = "images/coleccionables/tarjeta_intacta.png"
image tarjeta_rota = "images/coleccionables/tarjeta_rota.png"
image pantalla_bloqueo_Carlos = "images/phone/media/pantalla_bloqueo_Carlos.png"
image pantalla_bloqueo_Fernanda = "images/phone/media/pantalla_bloqueo_Fernanda.png"
image oncahui = "uamito.png"
image maceta_dorado = "images/planta/maceta_dorado.png"
image capa_1 = "images/cortinilla_capa/capa_1.png"
image capa_2 = "images/cortinilla_capa/capa_2.png"
image capa_3 = "images/cortinilla_capa/capa_3.png"
image capa_4 = "images/cortinilla_capa/capa_4.png"
image marco_tutorial = "images/tutorial/marco_tutorial.png"
image white = "images/white.png"

#introducción
label splashscreen:

    play music musica_fondo loop fadein 2.0 volume 1.0
    scene fondo_inicio
    
    if persistent.Config:

        show screen text_preview
        pause
        hide screen text_preview

        if renpy.variant("mobile"):

            $ instruccion = "Toca la pantalla"
        else:

            $ instruccion = "Da click"
        
        narrador "Ahora, ¡[instruccion] para continuar! Puede ser 
            en cualquier parte de la pantalla."

        show tutorial_configuracion:
            yalign .35
            xalign .5
        show marco_tutorial:
            yalign .35
            xalign .5
        
        if _preferences.self_voicing:

            narrador "Puedes volver a modificar las opciones en el menú de 
                Configuración dentro de Opciones."
        else:

            narrador "Puedes volver a modificar las opciones en el menú de  
                {image=boton_config} dentro de {image=boton_opciones}."
        
        hide tutorial_configuracion
        hide marco_tutorial
    
    if persistent.ocultar:

        show tutorial_guardar_auto:
            yalign .16
            xalign .5
        show marco_tutorial:
            yalign .15
            xalign .5

        if _preferences.self_voicing:

            narrador "¡Juego ocultado exitosamente! Continúa donde te quedaste 
                desde Guardado automático en el menú de Cargar dentro de Opciones."
        else:

            narrador "¡Juego ocultado exitosamente! Continúa donde te quedaste 
                desde Guardado automático en el menú de {image=boton_cargar} 
                dentro de {image=boton_opciones}."
        
        hide tutorial_guardar_auto
        hide marco_tutorial
        $ persistent.ocultar = False

    show creditos_iniciales
    pause 4.0
    hide creditos_iniciales
    show black onlayer master
    show screen intro with fade    
    hide black with {"master": fade}
    pause
    hide screen intro
    hide screen boton_quitar
    return


label start:

    $ save_name = _("Introducción")
    scene black

    if persistent.Config:
        call tutorial_ocultar

    scene fondo_inicio with fade
    show planta_fondo:
        yalign .4
        xalign .27
    show planta_fondo as fondo_pareja:
        yalign .4
        xalign .69
    show planta_capullo:
        yalign .4
        xalign .27        
        xsize 950
        ysize 900
    if persistent.desbloqueo:
        show maceta_dorado:
            yalign .4
            xalign .27        
            xsize 950
            ysize 900
    show planta_capullo as planta_pareja:
        yalign .4
        xalign .69        
        xsize 950
        ysize 900
    
    narrador "(cantando) {bt=a2-s2.0-p3.0}Ella sabía que él sabía, que algún día 
        pasaría.{/bt}"    

    if renpy.variant("mobile"):

        $ instruccion = "Toca"
    else:

        $ instruccion = "Da click en"
    
    menu:

        narrador "¿Tu decisión? ([instruccion] una opción)"
        "¿Flores cantando? ¿Qué p...":
            narrador "Tampoco es para tanto ¿eh?"
        "¡Me sé la canción! Me les uno.":
            narrador "{bt=a2-s2.0-p3.0}Que vendría a buscarla con sus flooores 
                amariiillaas.{/bt}"
    if preferences.text_cps > 0:

        if renpy.variant("mobile"):

            $ instruccion = "toque"
        else:

            $ instruccion = "click"
        narrador "Espera, ¿de verdad nos entendió? Confirmemos hablando en 
            mamífero."(multiple=2)
        narrador "Eso parece..."(multiple=2)
        narrador "{cps=1.0}Hola mamífero, si nos entiendes parpadea dos 
            veces.{/cps}"(multiple=2)
        narrador "Ya va a empezar... Da un [instruccion] en pantalla para que 
            termine de mostrarse el otro diálogo. Después da otro para 
            continuar."(multiple=2)
        narrador "¡Claramente entendió porque le hable en mamífero!"(multiple=2)
        narrador "¿Ves? Nos entiende tan bien que sigue nuestras 
            instrucciones."(multiple=2)
    else:

        narrador "Jeje perdón, no te habíamos visto."

    narrador "Nosotras somos las flores que representamos el estado de la 
        relación de [novia.name] y [novio.name]. Pronto podrás elegir a uno de 
        los dos para jugar."

    if persistent.desbloqueo:
        
        narrador "Aunque ya veo que desbloqueaste la maceta {atl=bounce}dorada{/atl}. 
            ¡En esa está tu planta! Y gracias por compartir nuestro juego."
            
    narrador "Y no, no estamos así de tapaditas por el frío de Cuajis, es que 
        todavía no florecemos."
    show logro_aspersor:
            yalign .1
    narrador "Con ayuda del agua y otros cuidados podremos seguir creciendo."
    hide logro_aspersor

    $ info_descriptiva = ""

    if _preferences.self_voicing:

        $ info_descriptiva = "(primer botón superior izquierda)"
    
    narrador "Nos puedes visitar en el menú de 
        Progreso [info_descriptiva]{image=boton_progreso}."
    narrador "{cps=100}(mensaje rapidísimo) ¡Hola desde el menú de Progreso!{/cps}{nw}"
    narrador "En el menú de Progreso {image=boton_progreso} también puedes 
        volver a leer diálogos pasados (como el anterior que estuvo rapidísimo)
        . \n\n¡Te invitamos a probarlo!"
    narrador "Y recuerda, no hay puntos extra por ser queda bien. 
        Toma la decisión que realmente es tuya, va?"
    narrador "Bueno, suficiente de nosotras. [novia.name] y [novio.name] están 
        en el cine, vamos a conocerlos."
    jump conocerPersonaje

label tutorial_ocultar:

    if renpy.variant("mobile"):

        $ instruccion = "tocando"
    else:

        $ instruccion = "dando click"

    narrador"Antes de empezar, ¿Estás en un lugar privado y en confianza?"

    menu:
        narrador "Selecciona una respuesta [instruccion] sobre ella."
        "Si":

            if _preferences.self_voicing:

                $ info_descriptiva = "(último botón superior derecha)"
                                    
            narrador "¡Bien! Pero si eso cambia, el botón de 
                ¡Ocultar! [info_descriptiva]{image=boton_quitar} oculta el 
                juego y muestra el calendario escolar. Úsalo como salida 
                de emergencia de miradas ajenas."    
        "No":

            narrador "¿Quieres jugar ahorita? El juego toca temas 
                    que piden tu reflexión en privado."

            $ info_descriptiva = ""
            
            if _preferences.self_voicing:
                
                $ info_descriptiva = "(último botón superior derecha)"
            
            narrador "El botón de 
                    ¡Ocultar! [info_descriptiva]{image=boton_quitar} oculta 
                    el juego y muestra el calendario de la UAM. Úsalo como 
                    salida de emergencia de miradas ajenas."
    
    narrador "Queremos que juegues con comodidad y honestidad."
    $ persistent.Config = False
    return


label conocerPersonaje:
    
    scene cine_fondo
    narrador "En el cine dentro de una sala, están Fernanda (Fer) y Carlos 
        (Charly) esperando a que empiece la película."
    novia "Ay amor, ¡gracias por los boletos! Seguro te costó un buen 
        conseguirlos, escuché que había pocos."
    novio "Es que estuve pegado a la compu desde la preventa, sabía que tenías 
        muchas ganas de verla. Lo único malo es que vino mucha gente y solo 
        alcanzamos unas palomitas chicas..."
    novia "No te preocupes, me encanta compartir las palomitas y más si es 
        contigo."
    novio "Gracias amor, me haces muy feliz."
    call eleccionPersonaje    
    jump prologo_personaje


label eleccionPersonaje:

    hide screen phone_ui
    hide screen color_fondo_final
    scene seleccion_personaje with fade   
    narrador "Ya que los conoces un poco, elige el personaje con el que 
        quieres jugar."

    show screen boton_eleccion_personaje    
    pause
    $ forzarAutosave()
    hide screen boton_eleccion_personaje

    if not capa_seleccionada:

        $ capa_seleccionada = NOMBRE_CAPA[0].lower()
    else:

        $ capa_seleccionada = capa_seleccionada.lower()

    narrador "¡Hola [jugador.nombre]! Estás a punto de atravesar la 
        [capa_seleccionada] de Latencia."
    
    show tutorial_guardar:
        yalign .35
        xalign .5
    show marco_tutorial:
        yalign .35
        xalign .5

    if _preferences.self_voicing:

        narrador "Puedes guardar tu partida en cualquier momento en el menú de 
            Guardar dentro de Opciones (segundo botón superior izquierda)."
        hide marco_tutorial
        show tutorial_cargar:
            yalign .35
            xalign .5
        show marco_tutorial:
            yalign .35
            xalign .5
        narrador "Y puedes cargar una partida o jugar directo en otra capa en 
            el menú de Cargar dentro de Opciones (segundo botón superior izquierda)."
    else:

        narrador "Puedes guardar tu partida en cualquier momento en el menú de 
            {image=boton_guardar} dentro de Opciones {image=boton_opciones_quick}."
        hide marco_tutorial
        show tutorial_cargar:
            yalign .35
            xalign .5
        show marco_tutorial:
            yalign .35
            xalign .5
        narrador "Y puedes cargar una partida o jugar directo en otra capa en 
            el menú de {image=boton_cargar} dentro de 
            Opciones {image=boton_opciones_quick}."

    hide marco_tutorial
    hide tutorial_cargar
    hide tutorial_guardar
    hide seleccion_personaje
    return


label eleccionCapa1:

    if persistent.Config:
        call tutorial_ocultar
    call eleccionPersonaje    
    jump prologo_personaje


label eleccionCapa2:

    if persistent.Config:
        call tutorial_ocultar
    call eleccionPersonaje    
    jump cita_chapultepec

label eleccionCapa3:

    if persistent.Config:
        call tutorial_ocultar
    call eleccionPersonaje    
    jump telefono_conversacion

label eleccionCapa4:

    if persistent.Config:
        call tutorial_ocultar
    call eleccionPersonaje    
    jump telefono_amigue

label finalJuego:

    scene fondo_inicio
    narrador "¡Muchas gracias por jugar esta primera versión del juego!"
    narrador "Si tienes comentarios, por favor compártelos con nosotros y 
        ayúdanos a mejorar."
    jump evaluacion


label evaluacion:

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
        esfuerzo de todos los involucrados."

    hide oncahui_zoomout
    show oncahui_zoomin
    pause 9.0
    hide oncahui_zoomin
    show creditos_finales with fade
    pause 10.0
    return