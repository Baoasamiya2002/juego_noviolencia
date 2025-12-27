init python:
    def reiniciar_celular():
        reset_phone_data()
        phone_start()

label telefono_conversacion:

    $ save_name = _("Tercera capa")
    show capa_3 with fade
    pause 8.0
    if renpy.variant("mobile"):

        $ instruccion = "Toca"
    else:

        $ instruccion = "Click"
    narrador "[instruccion] para continuar"
    
    $ retroalimentacion = False
    $ listaEstereotipo = []
    $ listaViolenciaJugador = []
    $ listaViolenciaPareja = []
    $ listaPresion = []
    $ palabraGenero = ""

    scene fondo_inicio at Transform(matrixcolor=TintMatrix("#505050")) with fade
    show expression "pantalla_bloqueo_[jugador.nombre]":
        anchor(0.5, 0.5) 
        pos(0.5, 0.57)

    narrador "Estás en una fiesta y escuchas una notificación en tu celular."

    $ reiniciar_celular()
    $ switch_channel_view("pareja_dm")

    hide expression "pantalla_bloqueo_[jugador.nombre]"
    show screen phone_ui
    
    $ send_phone_message(
        pareja.nombre, 
        (
            "Hola amor <emoji_corazon>, qué haces? "
            "<emoji_pensativo>"), "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Hablando contigo haha", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Y tú??", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "x2 zkxjaj<emoji_risa>", "pareja_dm", 3)

    if jugador.nombre == novia.name:

        $ send_phone_message(pareja.nombre, "Y te funciona bien el nuevo cel??", "pareja_dm", 3)
        $ send_phone_message(phone_config["phone_player_name"], "Sii todo perfecto amor <emoji_corazon>, gracias por el regalo", "pareja_dm", 3)
        $ send_phone_message(pareja.nombre, "Eso espero <emoji_guinio>", "pareja_dm", 3)
    else:

        $ send_phone_message(pareja.nombre, "Haaay [pareja.apodo], otra vez Ceballos nos dejó un proyecto súper difícil", "pareja_dm", 3)
        $ send_phone_message(pareja.nombre, "Y ya sabes que me cuesta mucho<emoji_rogando>, lo checas porfa?", "pareja_dm", 3)
        $ send_phone_message(phone_config["phone_player_name"], "Claro amor, tú tranquila<emoji_corazon><emoji_corazon>", "pareja_dm", 3)
        $ send_phone_message(pareja.nombre, "Te juro que es la última vez<emoji_guinio>", "pareja_dm", 3)

    $ send_phone_message(pareja.nombre, "Oye", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Te extrañooo <emoji_rogando>", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Yo también amor <emoji_corazon><emoji_corazon>", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Tiene rato que no nos mensajeamos...", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Te acuerdas en pandemia? Hablabamos todo el día... ahora bien poquis", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Es que también ya nos vemos en la uni", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Pues ni tanto...", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "<emoji_lagrima>", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Y... disculpa por lo dle otro día", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "del*", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "No debí enojarme contigo...", "pareja_dm", 3)

    if pareja.nombre == novio.name:

        $ send_phone_message(pareja.nombre, "Luego me encabrono bien rápido, pero no soy así", "pareja_dm", 3)
        $ send_phone_message(pareja.nombre, "Del sólo pensar que te grité quiero llorar", "pareja_dm", 3)

        $ send_phone_message("", "{color=#ffffff}¿Tu decisión?{/color}", "pareja_dm", 1, do_pause=False)
        $ present_phone_choices([
            (
                "Cuestionar su reacción", 
                Call("telefono_humillar_vulnerabilidad")), 
            (
                "Cargar culpa", 
                Call("telefono_culparse")), 
            (
                "Enfocarse en lo positivo", 
                Call("telefono_ignorar_violencia")), 
            (
                "Quitarle importancia", 
                Call("telefono_perdonar_violencia"))], "pareja_dm")
    else:

        $ send_phone_message("", "{color=#ffffff}¿Tu decisión?{/color}", "pareja_dm", 1, do_pause=False)
        $ present_phone_choices([
            (
                "Cargar culpa", 
                Call("telefono_culparse")), 
            (
                "Enfocarse en lo positivo", 
                Call("telefono_ignorar_violencia")), 
            (
                "Quitarle importancia", 
                Call("telefono_perdonar_violencia"))], "pareja_dm")
    
    $ send_phone_message(pareja.nombre, "De verdad te amo mucho [jugador.apodo]", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Mucho mucho?", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Mucho muchomu chomuch o muasd fasdca sodcxk!", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "<emoji_risa>", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "HAHAH", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "<emoji_hablando><emoji_corazon_fuego><emoji_corazon_fuego>", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "<emoji_corazon>Oie amor, donde andas?", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "En un lugar con 4 paredes hah<emoji_risa><emoji_risa>", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Jaja y de casualidad no tiene 1 techo??, pero ya encerio, me mandas ubicación pls?", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Todavía te acuerdas cómo verdad??", "pareja_dm", 3)

    $ palabraGenero = "amigo" if pareja.nombre == novio.name else "amiga"     
    
    $ send_phone_message("", "{color=#ffffff}¿Tu decisión?{/color}", "pareja_dm", 1, do_pause=False)
    $ present_phone_choices([
        (
            "Mando mi ubicación en casa de su [palabraGenero]...", 
            Call("telefono_aceptar_ubicacion")), 
        (
            "¿Mi ubicación? ¡Ni en pedo!", 
            Call("telefono_negar_ubicacion"))], "pareja_dm")
    
    call telefono_ignorar_reclamo from _call_telefono_ignorar_reclamo
    
    $ send_phone_message(phone_config["phone_player_name"], "Me pides cosas y te molestas???", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Hey", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Ni se te ocurra", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "<emoji_indiferente>", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "[pareja.apodo]", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "[pareja.apodo]", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "[pareja.nombre]!", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "<emoji_indiferente>", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "<emoji_indiferente>", "pareja_dm", 3)
    $ send_phone_message("", "15 minutos despúes", "pareja_dm", 1)
    $ send_phone_message(pareja.nombre, "Bueno, a mi ni me importaba dónde estás", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Sólo preguntaba porque sé que nunca tienes datos", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "?? y eso qué tiene que ver??<emoji_indiferente><emoji_indiferente>", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Es que te quiero enviar una imagen", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Y si estabas en la calle, tus datos luego taardan en descargar algo", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Pues si tengo wifi, manda la imagen", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "<emoji_pensativo>", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Voy", "pareja_dm", 3)

    $ palabraGenero = "prima" if pareja.nombre == novio.name else "primo"

    $ send_phone_message(pareja.nombre, "images/phone/media/instagram_[jugador.nombre].png", "pareja_dm", 2, summary_alt="Captura de pantalla del instagram de [palabraGenero] de [jugador.nombre]")

    $ palabraGenero = "prima" if pareja.nombre == novio.name else "primo"

    $ send_phone_message(phone_config["phone_player_name"], "Hehe nos vemos bien<emoji_feliz>, no sabía que seguías a mi [palabraGenero]", "pareja_dm", 3)
    
    $ palabraGenero = "prima" if pareja.nombre == novio.name else "primo"

    $ palabraGenero = "cercanas" if pareja.nombre == novio.name else "cercanos"

    $ send_phone_message(pareja.nombre, "No lo hago, son muy [palabraGenero]?", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Pues maso, fue de la reunión familiar pasada, te acuerdas?", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Aaa si, si me contaste, que se reunió un buen de tu familia", "pareja_dm", 3)
    
    call telefono_celos_foto from _call_telefono_celos_foto

    $ palabraGenero = "otro" if pareja.nombre == novio.name else "otra"       
    $ send_phone_message(phone_config["phone_player_name"], "Haha<emoji_risa> quien insinua es [palabraGenero], si sólo estamos hombro con hombro", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "No mira yo entiendo que tu familia sea muy cariñosa", "pareja_dm", 3)
    $ palabraGenero = "prima" if pareja.nombre == novio.name else "primo"       
    $ send_phone_message(pareja.nombre, "Pero quien no conozca a tu [palabraGenero], puede pensar cosas...<emoji_pensativo>", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Sobre todo tu amiga esa la chismosa...", "pareja_dm", 3)

    call telefono_control_publicacion

    if jugador.nombre == novia.name:

        call telefono_proteccion_masculina from _call_telefono_proteccion_masculina

    $ send_phone_message("", "{color=#ffffff}¿Tu decisión?{/color}", "pareja_dm", 1, do_pause=False)
    $ present_phone_choices([
        (
            "Pedir que elimine la foto y agradecer", 
            Call("telefono_eliminar_foto")), 
        (
            "Dejar la foto y terminar el tema, como sea", 
            Call("telefono_mantener_foto"))], "pareja_dm")
    
    jump retroalimentacion_pareja_telefono


label retroalimentacion_pareja_telefono:
    
    hide screen phone_ui
    scene fondo_inicio with fade 
    show fondo_inicio
    narrador "Sí que ustedes \"escribieron\" rápido, aunque al hacerlo, 
        ¿dijeron cosas sin pensarlo?"
    
    if jugador.estadoPlanta == "capullo":

        $ jugador.estadoPlanta = LISTA_ESTADO_PLANTA[1]
    else:

        $ pos = LISTA_ESTADO_PLANTA.index(jugador.estadoPlanta)
        $ jugador.estadoPlanta = LISTA_ESTADO_PLANTA[pos - 1]    

    show planta_fondo:
        yalign .4
        xalign .5
    show expression "planta_[jugador.estadoPlanta]" as planta:
        yalign .4
        xalign .5
        xsize 950
        ysize 900
    if persistent.desbloqueo:
        show maceta_dorado:
            yalign .4
            xalign .5        
            xsize 950
            ysize 900
    narrador "Lamentablemente [pareja.nombre] volvió a dañar tu planta, veamos 
        cuándo pasó:"
    hide planta_fondo
    hide planta
    hide maceta_dorado
    hide fondo_inicio
    scene fondo_inicio at Transform(matrixcolor=TintMatrix("#505050"))

    $ reiniciar_celular()
    show screen phone_ui
    $ retroalimentacion = True

    $ i = 0
    while i < len(listaViolenciaPareja):
        $ renpy.call(listaViolenciaPareja[i])
        $ reiniciar_celular()
        $ i += 1
        
    hide screen phone_ui
    scene black
    show fondo_inicio
    narrador "Así que, igual que la vez pasada, esta violencia afectó a tu planta."
    narrador "Parece un ciclo, ¿no lo crees?"
    narrador "Las plantas, como los humanos, merecen cuidados. {size=+15}{u}Merecemos 
        cuidados{/u}{/size}."
    jump retroalimentacion_jugador_telefono


label retroalimentacion_jugador_telefono:
    
    narrador "Ahora, veamos el estado de la planta de [pareja.nombre]."
    
    if listaViolenciaJugador:

        if pareja.estadoPlanta == "capullo":

            $ pareja.estadoPlanta = LISTA_ESTADO_PLANTA[1]
        else:

            $ pos = LISTA_ESTADO_PLANTA.index(pareja.estadoPlanta)
            $ pareja.estadoPlanta = LISTA_ESTADO_PLANTA[pos - 1]
        
        show penalizacion_aspersor:
            xalign .05
            yalign 0.3
        $ coleccionables.append("penalizacion_aspersor")
        narrador "¡Oh! Con tus respuestas obtuviste un aspersor de agua sucia 
            para su planta."
        hide penalizacion_aspersor
        show planta_fondo:
            yalign .4
            xalign .5
        show expression "planta_[pareja.estadoPlanta]" as planta:
            yalign .4
            xalign .5
            xsize 950
            ysize 900
        narrador "La planta de [pareja.nombre] se siente un poco enferma, veamos 
            cuándo pasó:"
        hide planta_fondo
        hide planta
        hide fondo_inicio
        scene fondo_inicio at Transform(matrixcolor=TintMatrix("#505050"))

        $ reiniciar_celular()
        show screen phone_ui

        $ i = 0
        while i < len(listaViolenciaJugador):
            $ renpy.call(listaViolenciaJugador[i])
            $ reiniciar_celular()
            $ i += 1
        
        hide screen phone_ui
        scene black
        show fondo_inicio
        narrador "Y por esta violencia, acabó afectada la planta de [pareja.nombre]."
        narrador "Aún con la mejor intención, nuestra respuesta no siempre es la 
            mejor. Prefiere comunicar con claridad, que \"regresándole\" la ofensa."
        narrador "Y lo que quieres recibir, {size=+15}{u}¿También lo ofreces?{/u}{/size}"
    else:

        if pareja.estadoPlanta == "capullo":

            $ pareja.estadoPlanta = LISTA_ESTADO_PLANTA[2]
        else:
        
            $ pos = LISTA_ESTADO_PLANTA.index(pareja.estadoPlanta)
            $ pareja.estadoPlanta = LISTA_ESTADO_PLANTA[pos + 1]

        show logro_aspersor:
            xalign .05
            yalign 0.3
        $ coleccionables.append("logro_aspersor")
        narrador "¡Felicidades! Con tus respuestas ganaste un aspersor con agua 
            limpia."
        hide logro_aspersor
        show planta_fondo:
            yalign .4
            xalign .5
        show expression "planta_[pareja.estadoPlanta]" as planta:
            yalign .4
            xalign .5
            xsize 950
            ysize 900
        narrador "La planta de [pareja.nombre] ha comenzado a florecer."
        hide planta_fondo
        hide planta

        if listaPresion:
             
            narrador "Pero hubo momentos en los que caíste en la presión 
                de [pareja.nombre]:"

            hide fondo_inicio
            $ reiniciar_celular()
            show screen phone_ui

            $ i = 0
            while i < len(listaPresion):
                $ renpy.call(listaPresion[i])
                $ reiniciar_celular()
                $ i += 1
                
            hide screen phone_ui
            scene black
            show fondo_inicio
            narrador "Seguir sus deseos puede parecer la mejor opción, pero 
                ¿dónde quedas tú en la relación?"

    jump retroalimentacion_estereotipo_telefono


label retroalimentacion_estereotipo_telefono:

    if listaEstereotipo:

        menu:

            narrador "Y, como en capas anteriores, algunos diálogos 
                reproducen estereotipos sobre los roles de género, ¿Esta vez 
                tuviste mejor suerte detectándolos?"
            
            "Sí":
            
                narrador "Esperamos que no sólo sea suerte, vamos a comprobarlo:"
            "No":
                
                narrador "Tal vez no tuviste suerte, pero ahorita los conoceremos:"

        hide fondo_inicio
        scene fondo_inicio at Transform(matrixcolor=TintMatrix("#505050"))
        $ reiniciar_celular()
        show screen phone_ui

        $ i = 0
        while i < len(listaEstereotipo):
            $ renpy.call(listaEstereotipo[i])
            $ reiniciar_celular()
            $ i += 1
            
        hide screen phone_ui
        scene black
        show fondo_inicio
        narrador "Las palabras pueden esconder más que su significado literal."
        narrador "¿Cuántas de estas y otras frases haz dicho sin pensar lo 
            que {size=+15}{u}realmente{/u}{/size} significan?"

    $ forzarAutosave()

    call instrucciones_recursos
    jump opcion_telefono_regresar_menu


label opcion_telefono_regresar_menu:

    scene black

    menu:
        
        narrador "Haz atravesado la tercera capa de Latencia ¿Quieres continuar? 
            La siguiente capa es la {atl=drop_text~#~ 2.5}última{/atl}."
        "Si":

            call instrucciones_cargar
            jump telefono_amigue
        "Más tarde":

            narrador "¡Entendido! Espero que regreses pronto para atravesar más 
                capas de Latencia."
            call instrucciones_cargar
            $ renpy.full_restart() 


label telefono_humillar_vulnerabilidad:
        
    $ send_phone_message(
        phone_config["phone_player_name"], 
        (
            "Mmm llorar? <emoji_alarma><emoji_robot>falla en el sistema, peligro " 
            "peligro haha"), "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Entiendo lo del enojo pero tampoco inventes <emoji_risa_nerviosa>", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Si jaj.. fue mucho verdad?<emoji_medio_triste> lo siento...", "pareja_dm", 3)

    if retroalimentacion:

        narrador "Decidiste {atl=rotate_text}humillar {/atl} a [pareja.nombre] por querer llorar, invalidándolo, ¿Los hombres no pueden llorar?"
    else:

        $ listaViolenciaJugador.append("telefono_humillar_vulnerabilidad")

    return


label telefono_culparse:
    
    $ send_phone_message(phone_config["phone_player_name"], "Noo amor, no te disculpes, yo soy quien se debería disculpar", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Perdóname por hacerte sentir así<emoji_rezando><emoji_rezando>", "pareja_dm", 3)

    if retroalimentacion:

        narrador "Decidiste aceptar toda la culpa cuando [pareja.nombre] también te violentó, aunque [pareja.nombre] se estaba disculpando."
    else:
        
        $ listaPresion.append("telefono_culparse")
        call telefono_merece_violencia from _call_telefono_merece_violencia
    return


label telefono_merece_violencia:
    
    if jugador.nombre == novia.name:

        $ send_phone_message(phone_config["phone_player_name"], "Sí, me gritaste, pero porque te hice enojar, me pasé<emoji_lagrima>", "pareja_dm", 3)

        if retroalimentacion:

            narrador "Aunque tú hayas \"provocado\" su enojo, ¿debes tomar 
                responsabilidad por sus acciones??"
        else:

            $ listaEstereotipo.append("telefono_merece_violencia")

    return


label telefono_ignorar_violencia:
        
    $ send_phone_message(phone_config["phone_player_name"], "Pero ni pasó nada, y el clima en Chapu estuvo padre, no? Así soleadito pero fresco<emoji_feliz>", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "?? Sí jaj eso creo...", "pareja_dm", 3)

    if retroalimentacion:

        narrador "Decidiste {atl=rotate_text}ignorar {/atl} a [pareja.nombre] cuando se disculpó contigo. Aunque el tema te sea incómodo, ignorarlo puede hacer más daño."
    else:

        $ listaViolenciaJugador.append("telefono_ignorar_violencia")

    return


label telefono_perdonar_violencia:

    $ send_phone_message(phone_config["phone_player_name"], "Ayy pues equis, ni me acuerdo de lo que pasó y seguro no vuelve a pasar", "pareja_dm", 3)
    $ palabraGenero = "abierta" if pareja.nombre == novio.name else "abierto"       
    $ send_phone_message(phone_config["phone_player_name"], "Pero si te hace sentir mejor, si, claro que te perdono amor<emoji_corazon>, y yo también estaré más [palabraGenero] va?", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "sisisis", "pareja_dm", 3)
    return

label telefono_aceptar_ubicacion:

    $ send_phone_message(phone_config["phone_player_name"], "Si.. me acuerdo", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "images/phone/media/gps.png", "pareja_dm", 2, summary_alt="GPS de casa de [palabraGenero] [pareja.nombre]")
    $ send_phone_message(phone_config["phone_player_name"], "Pero no te", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "<emoji_groserias>", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Enojes...", "pareja_dm", 3)
    
    call telefono_celos_amigue from _call_telefono_celos_amigue
    
    $ send_phone_message(phone_config["phone_player_name"], "Es el cumple de su hermana, de mi clase, ella invitó al salón", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Claaro que si<emoji_voltea_ojos>", "pareja_dm", 3)
    $ palabraGenero = "al otro ni lo" if pareja.nombre == novio.name else "a la otra ni la"       
    $ send_phone_message(phone_config["phone_player_name"], "Pues sí, es la fiesta de mi compañera, [palabraGenero] topo", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Ok?", "pareja_dm", 3)
    return


label telefono_celos_amigue:
 
    $ palabraGenero = "Armando" if pareja.nombre == novio.name else "Sofia"       
    $ send_phone_message(pareja.nombre, "Qué haces en la casa de [palabraGenero]??", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Eh????", "pareja_dm", 3)

    if retroalimentacion:

        narrador "[pareja.nombre] te {atl=rotate_text}celó {/atl} por estar en casa de una de sus amistades, siendo su primera reacción el enojo y reclamo."
    else:

        $ listaViolenciaPareja.append("telefono_celos_amigue")
        
    return


label telefono_negar_ubicacion:
    
    $ send_phone_message(phone_config["phone_player_name"], "Y si no qué? Tú me vas a ayudar? Si yo soy quien te ayuda cuando no le sabes al cel!!<emoji_voltea_ojos>", "pareja_dm", 3)#####################
    $ send_phone_message(phone_config["phone_player_name"], "A ver, pásame tú tu ubicación", "pareja_dm", 3)

    if pareja.nombre == novio.name:

        call telefono_insinuar_mujeriego from _call_telefono_insinuar_mujeriego

    if retroalimentacion:

        narrador "Decidiste {atl=rotate_text}humillar {/atl} a [pareja.nombre], aunque estás en tu derecho de no compartir tu ubicación, puedes hacerlo sin violentar al otro."
    else:

        $ listaViolenciaJugador.append("telefono_negar_ubicacion")
        
    return


label telefono_ignorar_reclamo:
        
    $ send_phone_message(pareja.nombre, "Contigo no se puede, bye", "pareja_dm", 3)

    if retroalimentacion:

        narrador "A partir de ahí [pareja.nombre] te {atl=rotate_text}ignoró {/atl} a causa de su enojo, cortando el diálogo sin mayor explicación."
    else:

        $ listaViolenciaPareja.append("telefono_ignorar_reclamo")
        
    return


label telefono_insinuar_mujeriego:
        
    $ send_phone_message(phone_config["phone_player_name"], "Pero ahí no te atreves porque seguro andas en la casa de una amiga<emoji_indiferente>...", "pareja_dm", 3)

    if retroalimentacion:

        narrador "{atl=rotate_text}Celaste {/atl} a Carlos, porque ¿cómo sabes eso?, ¿por una 
            experiencia previa o porque crees que así son los hombres?"
    else:

        $ listaEstereotipo.append("telefono_insinuar_mujeriego")
        
    return


label telefono_celos_foto:
    
    $ palabraGenero = "prima" if pareja.nombre == novio.name else "primo"
    
    $ send_phone_message(pareja.nombre, "Pero como que tu [palabraGenero] está un poco encima de ti no?", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Parece que te le insinuas", "pareja_dm", 3)

    if retroalimentacion:

        narrador "[pareja.nombre] te {atl=rotate_text}celó {/atl} por una foto familiar, por su inseguridad."
    else:
        
        $ listaViolenciaPareja.append("telefono_celos_foto")
        
    return


label telefono_control_publicacion:
    
    $ send_phone_message(pareja.nombre, "Mejor pídele que la elimine va?<emoji_rezando>", "pareja_dm", 3)

    if retroalimentacion:

        narrador "[pareja.nombre] te quizo {atl=rotate_text}controlar {/atl} con quién puedes tener fotos."
    else:
        
        $ listaViolenciaPareja.append("telefono_control_publicacion")
        
    return


label telefono_proteccion_masculina:
        
    $ send_phone_message(pareja.nombre, "Tal vez tú no te das cuenta de cómo te ves", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Pero no te preocupes, tu novio te cuida<emoji_guinio>", "pareja_dm", 3)

    if retroalimentacion:

        narrador "Está bien que te quiera proteger, pero su \"protección\" eran celos, además, ¿lo está haciendo por seguir un rol de protector, sin considerar que puede ser algo mutuo?"
    else:
        
        $ listaEstereotipo.append("telefono_proteccion_masculina")
        
    return


label telefono_eliminar_foto:
        
    $ send_phone_message(phone_config["phone_player_name"], "No lo había pensado de esa forma amor...", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Le voy a pedir el favor de eliminar la foto", "pareja_dm", 3)

    if retroalimentacion:

        narrador "Decidiste caer en la presión de [pareja.nombre] impulsada por sus celos."
    else:
    
        $ listaPresion.append("telefono_eliminar_foto")
        $ listaMito.append("telefono_eliminar_foto")

        $ send_phone_message(phone_config["phone_player_name"], "Gracias<emoji_corazon>", "pareja_dm", 3)
        $ send_phone_message(pareja.nombre, "No es nada <emoji_corazon><emoji_feliz>", "pareja_dm", 3)
        $ send_phone_message(pareja.nombre, "Es que me preocupaba que te inventaran rumores <emoji_lagrima>", "pareja_dm", 3)

        $ send_phone_message("", "{color=#ffffff}¿Tu decisión?{/color}", "pareja_dm", 1, do_pause=False)
        $ present_phone_choices([
            (
                "Irse despidiendo de [pareja.nombre]", 
                None), 
            (
                "Reconfortar a [pareja.nombre] con una mentira blanca",
                Call("telefono_mentir_relacion"))], "pareja_dm")

        $ palabraGenero = "prima" if pareja.nombre == novio.name else "primo"

        $ send_phone_message(phone_config["phone_player_name"], "Bueno amor, voy a hablar con mi [palabraGenero] y después seguimos si??, te amoo<emoji_corazon>", "pareja_dm", 3)#################

    return


label telefono_mentir_relacion:
        
    $ palabraGenero = "prima" if pareja.nombre == novio.name else "primo"

    $ send_phone_message(phone_config["phone_player_name"], "Y la verdad, casi ni hablo con mi [palabraGenero], somos distantes", "pareja_dm", 3)

    if retroalimentacion:

        narrador "Decidiste {atl=rotate_text}mentir {/atl} para calmar sus inseguridades, pero como viste, eso puede empeorar las cosas"
    else:
    
        $ listaViolenciaJugador.append("telefono_mentir_relacion")

        $ send_phone_message(pareja.nombre, "Perdon, qué??<emoji_groserias>", "pareja_dm", 3)
        $ send_phone_message(pareja.nombre, "Por qué me mientes??", "pareja_dm", 3)
    
        call telefono_checar_chat from _call_telefono_checar_chat
    
        $ send_phone_message(phone_config["phone_player_name"], "Nono espera! Yo sólo quería quitar tus preocupaciones", "pareja_dm", 3)
        $ send_phone_message(phone_config["phone_player_name"], "[pareja.apodo]", "pareja_dm", 3)
        $ send_phone_message(phone_config["phone_player_name"], "<emoji_lagrima><emoji_corazon>", "pareja_dm", 3)
        $ send_phone_message(phone_config["phone_player_name"], "[pareja.apodo]!", "pareja_dm", 3)
    return


label telefono_checar_chat:
    
    $ palabraGenero = "cercanas" if pareja.nombre == novio.name else "cercanos"       
    $ send_phone_message(pareja.nombre, "Yo ya sé que son [palabraGenero]!, si veo en tus mensajes que hablan seguido", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "No puedo creer que me mentiste", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "<emoji_lagrima>", "pareja_dm", 3)
    
    if retroalimentacion:

        narrador "[pareja.nombre] te {atl=rotate_text}engañó {/atl}, porque 
            antes preguntó por su relación, como si no supiera la verdad."
        narrador "Además, {atl=rotate_text}invadió tu privacidad {/atl} leyendo
            tus mensajes privados de Instagram."

    else:
        
        $ listaViolenciaPareja.append("telefono_checar_chat")
        
    return


label telefono_mantener_foto:

    $ send_phone_message(phone_config["phone_player_name"], "Pero es su insta...", "pareja_dm", 3)

    call telefono_pretexto from _call_telefono_pretexto

    $ send_phone_message(pareja.nombre, "<emoji_grito>", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Nnonononoo", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Mejor así lo dejamos, verdad amor?", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Si, mejor", "pareja_dm", 3)
    return


label telefono_pretexto:

    $ send_phone_message(phone_config["phone_player_name"], "Y si le digo, tendré que decirle que me obligaste<emoji_medio_triste>", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Y cuando sepan mis padres... nos van a querer separar, y no queremos eso, verdad?", "pareja_dm", 3)

    if retroalimentacion:

        narrador "Decidiste {atl=rotate_text}engañar {/atl} y {atl=rotate_text}chantajear {/atl} para terminar con el tema, pero ¿esa es la mejor solución?"
    else:
        
        $ listaViolenciaJugador.append("telefono_pretexto")
        $ listaMito.append("telefono_pretexto")
        
    return
