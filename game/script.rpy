init python:

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
define TEXTO_CPS_PREVIEW = PreviewSlowText(
    "{color=#000000}¡Bienvenide! Este juego se centra en la lectura. Modifica "
    "estas y otras opciones para tener la mejor experiencia.{/color}")

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
        
        show screen boton_quitar
        if _preferences.self_voicing:

            narrador "Estas opciones las puedes volver a modificar en el menú de 
                Configuración en Opciones en cualquier momento."
        else:

            narrador "Estas opciones las puedes volver a modificar en el menú de 
                {image=boton_config} en {image=boton_opciones} en cualquier 
                momento."
        narrador "Ahora, ¡[instruccion] siempre que quieras continuar! Puede ser 
            en cualquier parte de la pantalla"
    else:
        
        show screen boton_quitar
        if _preferences.self_voicing:
            
            narrador "Si olvidas cómo hacer una acción ¡no te preocupes!, 
                en el menú de Más información se encuentra el Tutorial."
        else:

            narrador "Si olvidas cómo hacer una acción ¡no te preocupes!, 
                en el menú de {image=boton_mas_info} se encuentra el 
                {image=boton_tutorial}."
    
    show screen intro    
    show screen boton_quitar
    pause
    hide screen intro
    hide screen boton_quitar
    return


label start:

    scene black

    if persistent.Config:

        narrador"Antes de empezar, ¿Estás en un lugar privado y en confianza?"

        menu:
            "Si":
                if _preferences.self_voicing:

                    narrador "¡Bien! Aunque si quieres una salida de emergencia 
                        de miradas ajenas, el botón de ¡Quitar! (último botón 
                        superior derecha) está para ayudarte."
                else:
                                        
                    narrador "¡Bien! Aunque si quieres una salida de emergencia 
                        de miradas ajenas, el botón de {image=boton_quitar} 
                        está para ayudarte."    
            "No":
                if _preferences.self_voicing:

                    narrador "¿Quieres jugar ahora? El juego toca temas 
                        sensibles y necesita tu atención, así que es mejor 
                        jugarlo en privado.\n\nSi quieres una salida de emergencia 
                        de miradas ajenas, el botón de ¡Quitar! (último botón 
                        superior derecha) está para ayudarte."
                else:
                                        
                    narrador "¿Quieres jugar ahora? El juego toca temas 
                        sensibles y necesita tu atención, así que es mejor 
                        jugarlo en privado.\n\nSi quieres una salida de emergencia 
                        de miradas ajenas, el botón de {image=boton_quitar} está 
                        para ayudarte."
        
        narrador "Queremos que juegues con comodidad y honestidad. Ahora sí, 
            puedes continuar jugando si así lo decides."
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

    narrador "(cantando) Ella sabía que él sabía, que algún día pasaría."

    menu:

        narrador "Selecciona una respuesta."
        "¿Flores cantando? ¿Qué p...":
            narrador "Tampoco es para tanto ¿eh?"
        "¡Me sé la canción! Me les uno.":
            narrador "Que vendría a buscarla con sus flooores amariiillaas."

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

    if _preferences.self_voicing:

        narrador "Nos puedes visitar en el menú de Progreso (primer botón 
            superior izquierda). 
            Ahí también puedes recordar lo que [novia.name] y [novio.name] 
            hablen, ¡incluso esta conversación!"
    else:

        narrador "Nos puedes visitar en el menú de {image=boton_progreso}. 
            Ahí también puedes recordar lo que [novia.name] y [novio.name] 
            hablen, ¡incluso hasta esta conversación!"

    narrador "Que hablando de los reyes de roma, [novia.name] y [novio.name] están 
        en el cine, vamos a conocerlos."
    jump eleccionPersonaje


label eleccionPersonaje:
    
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
    scene seleccion_personaje
    show screen boton_eleccion_personaje    
    $ forzarAutosave()
    narrador "Ahora que los conoces un poco, elige el personaje con el que 
        quieres jugar."


label seleccionPersonaje:

    hide screen boton_eleccion_personaje
    
    if _preferences.self_voicing:

        narrador "¡Hola [jugador.nombre]! Esto se acaba de guardar en automático. 
            Si después quieres jugar como [pareja.nombre] o guardar tu progreso, 
            Cargar y Guardar se encuentran en el menú de Opciones (segundo botón 
            superior izquierda)."
    else:

        narrador "¡Hola [jugador.nombre]! Esto se acaba de guardar en automático. 
            Si después quieres jugar como [pareja.nombre] o guardar tu progreso, 
            {image=boton_cargar} y {image=boton_guardar} se encuentran en el 
            menú de {image=boton_opciones_quick}."

    hide seleccion_personaje
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