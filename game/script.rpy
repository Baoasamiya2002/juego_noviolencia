init python:

    import time

    def modificarPosImage(ruta):

        imagen_ancho, imagen_alto = renpy.image_size(ruta)
        return Composite(
            (imagen_ancho, imagen_alto),
            (0, -15),
            Image(ruta)
        )
    
    def definirPersonaje(personajeJugador, apodoJugador, personajePareja, apodoPareja):

        global jugador, pareja

        jugador = Persona(
            personajeJugador.name, 
            apodoJugador, 
            Character(
                personajeJugador.name, 
                window_background=Frame("gui/jugador_textbox_trans.png")))
        pareja = Persona(
            personajePareja.name, 
            apodoPareja, 
            Character(
                personajePareja.name, 
                window_background=Frame("gui/pareja_textbox_trans.png")))
    
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
    window_background=Frame("gui/pareja_textbox_trans.png"))#
define oncahui = Character("Oncahui", 
    window_background=Frame("gui/oncahui_textbox.png"))

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
    "<emoji_risa>"),
    ("Holaa amor, ya estoy aquí, pero tú tranqui. Te espero con gusto, así que"+
    " no te apures <emoji_corazon>"),
    ("Ya llegué. Me dices si vas a tardar y me doy una vuelta jeje"+
    "<emoji_risa_nerviosa>")]
define TEXTO_CPS_PREVIEW = PreviewSlowText(
    "{color=#000000}¡Bienvenide! Este juego se centra en la lectura. Modifica "
    "estas opciones para tener la mejor experiencia.{/color}")

#variables
default coleccionables = []
default listaEstereotipo = []
default listaViolenciaJugador = []
default listaViolenciaPareja = []
default listaPresion = []
default jugador = Persona(nombre="???")
default pareja = Persona(nombre="???")
default palabraGenero = ""
default codigoCompartido = ""
default info_descriptiva = ""
default retroalimentacion = False
default persistent.Config = True

#videos
image fondo_inicio = Movie(
    size=(2560,1600), play="images/fondo_inicio.webm", loop = True) 
image seleccion_personaje = Movie(
    size=(2560,1600), play="images/seleccion_personaje.webm", loop = False, 
    image="images/seleccion_personaje.png")
image cine_fondo = Movie(
    size=(2560,1600), play="images/cine fondo.webm", loop = True)
image caminata_chapultepec = Movie(
    size=(2560,1600), play="images/caminata_chapultepec.webm", loop = False, 
    image="images/caminata_chapultepec.png")
image emocion_seriedad_Carlos = Movie(
    size=(2560,1600), play="images/emocion/Carlos/seriedad.webm", loop = True)
image emocion_enojo_Carlos = Movie(
    size=(2560,1600), play="images/emocion/Carlos/enojo.webm", loop = True)
image emocion_felicidad_Carlos = Movie(
    size=(2560,1600), play="images/emocion/Carlos/felicidad.webm", loop = True)
image emocion_tristeza_Carlos = Movie(
    size=(2560,1600), play="images/emocion/Carlos/tristeza.webm", loop = True)
image emocion_seriedad_Fernanda = Movie(
    size=(2560,1600), play="images/emocion/Fernanda/seriedad.webm", loop = True)
image emocion_enojo_Fernanda = Movie(
    size=(2560,1600), play="images/emocion/Fernanda/enojo.webm", loop = True)
image emocion_felicidad_Fernanda = Movie(
    size=(2560,1600), play="images/emocion/Fernanda/felicidad.webm", loop = True)
image emocion_tristeza_Fernanda = Movie(
    size=(2560,1600), play="images/emocion/Fernanda/tristeza.webm", loop = True)
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
image creditos = Movie(
    size=(2560,1600), play="images/creditos.webm", loop = False)

#imagenes estaticas
image boton_opciones = modificarPosImage("gui/button/dialogo/opciones.png") 
image boton_config = modificarPosImage("gui/button/dialogo/config.png")
image boton_progreso = modificarPosImage("gui/button/dialogo/progreso.png")
image boton_quitar = modificarPosImage("gui/button/dialogo/quitar.png")
image boton_cargar = modificarPosImage("gui/button/dialogo/cargar.png")
image boton_guardar = modificarPosImage("gui/button/dialogo/guardar.png")
image boton_opciones_quick = modificarPosImage("gui/button/dialogo/opciones_quick.png")
image boton_mas_info = modificarPosImage("gui/button/dialogo/mas_info.png")
image boton_tutorial = modificarPosImage("gui/button/dialogo/tutorial.png")
image boton_recursos = modificarPosImage("gui/button/dialogo/recursos.png")
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
        
        if _preferences.self_voicing:

            narrador "Puedes volver a modificar las opciones en el menú de 
                Configuración dentro de Opciones."
        else:

            narrador "Puedes volver a modificar las opciones en el menú de 
                {image=boton_config} dentro de {image=boton_opciones}."
    else:
        
        show screen boton_quitar
        if _preferences.self_voicing:
            
            narrador "¿Dudas sobre el juego? Consulta el menú de Más información."
        else:

            narrador "¿Dudas sobre el juego? Consulta el menú 
                de {image=boton_mas_info}."
    
    show screen intro    
    pause
    hide screen intro
    hide screen boton_quitar
    return


label start:

    $ save_name = _("Introducción")
    scene black

    if persistent.Config:

        narrador"Antes de empezar, ¿Estás en un lugar privado y en confianza?"

        menu:
            "Si":

                if _preferences.self_voicing:

                    $ info_descriptiva = "(último botón superior derecha)"
                                        
                narrador "¡Bien! Pero si eso cambia, el botón de 
                    ¡Ocultar! [info_descriptiva]{image=boton_quitar} oculta el 
                    juego y muestra el calendario de la UAM. Úsalo como salida 
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

        $ instruccion = "tocando"
    else:

        $ instruccion = "dando click"

    menu:

        narrador "Selecciona una respuesta [instruccion] sobre ella."
        "¿Flores cantando? ¿Qué p...":
            narrador "Tampoco es para tanto ¿eh?"
        "¡Me sé la canción! Me les uno.":
            narrador "{bt=a2-s2.0-p3.0}Que vendría a buscarla con sus flooores 
                amariiillaas.{/bt}"

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
    narrador "{cps=100}¡Hola desde el menú de Progreso!{/cps}{nw}"
    narrador "En el menú de Progreso {image=boton_progreso} también puedes 
        volver a leer diálogos pasados (como el anterior que estuvo rapidísimo)
        . \n\n¡Te invitamos a probarlo!"
    narrador "Bueno, suficiente de nosotras. [novia.name] y [novio.name] están 
        en el cine, vamos a conocerlos."
    jump conocerPersonaje


label conocerPersonaje:
    
    scene cine_fondo
    narrador "En el cine dentro de una sala, están Fernanda y Carlos esperando a 
        que empiece la película."
    novia "Ay amor, ¡gracias por los boletos! Seguro te costó un buen 
        conseguirlos, escuché que había pocos."
    novio "Es que estuve pegado a la compu desde la preventa, sabía que tenías 
        muchas ganas de verla. Lo único malo es que vino mucha gente y solo 
        alcanzamos unas palomitas chicas..."
    novia "No te preocupes, me encanta compartir las palomitas y más si es 
        contigo."
    novio "Gracias amor, me haces muy feliz Fer."
    call eleccionPersonaje    
    jump prologo_personaje


label eleccionPersonaje:

    hide screen phone_ui
    scene seleccion_personaje    
    narrador "Ya que los conoces un poco, elige el personaje con el que 
        quieres jugar."

    show screen boton_eleccion_personaje    
    pause
    $ forzarAutosave()
    hide screen boton_eleccion_personaje

    narrador "¡Hola [jugador.nombre]! Estás a punto de atravesar la primera 
        capa de Latencia."

    if _preferences.self_voicing:

        narrador "Puedes guardar tu partida en cualquier momento en el menú de 
            Guardar dentro de Opciones (segundo botón superior izquierda)."
        narrador "Y puedes cargar una partida o jugar directo en otra capa en 
            el menú de Cargar dentro de Opciones (segundo botón superior izquierda)."
    else:

        narrador "Puedes guardar tu partida en cualquier momento en el menú de 
            {image=boton_guardar} dentro de Opciones {image=boton_opciones_quick}."
        narrador "Y puedes cargar una partida o jugar directo en otra capa en 
            el menú de {image=boton_cargar} dentro de 
            Opciones {image=boton_opciones_quick}."

    hide seleccion_personaje
    return


label eleccionCapa1:

    call eleccionPersonaje    
    jump prologo_personaje


label eleccionCapa2:

    call eleccionPersonaje    
    jump cita_chapultepec

label eleccionCapa3:

    call eleccionPersonaje    
    jump telefono_conversacion

label eleccionCapa4:

    call eleccionPersonaje    
    jump cita_chapultepec

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
    show creditos with fade
    pause 6.0
    return