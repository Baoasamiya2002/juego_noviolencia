init python:
    def reiniciar_celular():
        reset_phone_data()
        phone_start()

label telefono_conversacion:

    $ retroalimentacion = False

    scene black

    narrador "Estás en una fiesta y escuchas una notificación en tu celular."

    $ reiniciar_celular()

    show screen phone_ui

    $ send_phone_message(pareja.nombre, "Hola amor <emoji_corazon>, qué haces? <emoji_pensativo>", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Hablando contigo haha", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Y tú??", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "x2 zkxjaj<emoji_risa>", "pareja_dm", 3)
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

        $ send_phone_message(pareja.nombre, "Luego me encabrono bien rápido pero no soy así", "pareja_dm", 3)
        $ send_phone_message(pareja.nombre, "Del sólo pensar que te grité quiero llorar", "pareja_dm", 3)

        $ present_phone_choices([
            ("Él y sus \"sentimientos\"...", Call("telefono_humillar_vulnerabilidad")), 
            ("Pero fue mi culpa...", Call("telefono_culparse")), 
            ("Mmm y en otro tema...", Call("telefono_ignorar_violencia")), 
            ("Disculpas aceptadas", Call("telefono_perdonar_violencia"))], "pareja_dm")
    else:

        $ present_phone_choices([
            ("Pero fue mi culpa...", Call("telefono_culparse")), 
            ("Mmm y en otro tema...", Call("telefono_ignorar_violencia")), 
            ("Disculpas aceptadas", Call("telefono_perdonar_violencia"))], "pareja_dm")
    
    $ send_phone_message(pareja.nombre, "De verdad te amo mucho [jugador.apodo]", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Muchomucho?", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Muchomuchomuchomucho muasdfasdcasodcxk!", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "<emoji_risa>", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "HAHAH", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "<emoji_hablando><emoji_corazon_fuego><emoji_corazon_fuego>", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "<emoji_corazon>Oie amor, donde andas?", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "En un lugar con 4 paredes hah<emoji_risa><emoji_risa>", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "jaja y de casualidad no tiene 1 techo??, pero ya encerio, me mandas ubicación pls?", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Todavía te acuerdas cómo verdad??", "pareja_dm", 3)

    $ palabraGenero = "amigo" if pareja.nombre == novio.name else "amiga"     
    
    $ present_phone_choices([
        (
            "Mando mi ubicación en casa de su [palabraGenero]...", 
            Call("telefono_aceptar_ubicacion")), 
        (
            "¿Mi ubicación? ¡Ni en pedo!", 
            Call("telefono_negar_ubicacion"))], "pareja_dm")
    
    call telefono_ignorar_reclamo
    
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
    $ send_phone_message(phone_config["phone_player_name"], "?? y eso qué tiene que ver<emoji_indiferente><emoji_indiferente>", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Es que te quiero enviar una imagen", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Y si estabas en la calle, el internetcdmx luego taarda en descargar algo", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Ya te había dicho que estaba en lugar pero ok, manda la imagen", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "<emoji_pensativo>", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Voy", "pareja_dm", 3)

    $ palabraGenero = "prima" if pareja.nombre == novio.name else "primo"

    $ send_phone_message(pareja.nombre, "images/phone/media/instagram_[jugador.nombre].png", "pareja_dm", 2, summary_alt="Captura de pantalla del instagram de [palabraGenero] de [jugador.nombre]")
    $ send_phone_message(phone_config["phone_player_name"], "Ah no sabía que había subido la foto<emoji_feliz>", "pareja_dm", 3)
    
    call telefono_captura_instagram

    $ palabraGenero = "cercanas" if pareja.nombre == novio.name else "cercanos"

    $ send_phone_message(pareja.nombre, "Aunque se ven como muy [palabraGenero] no?", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Pues maso, fue de la reunión familiar pasada, te acuerdas?", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Aaa si, si me contaste, que se reunió un buen de tu familia", "pareja_dm", 3)
    
    call telefono_celos_foto

    $ palabraGenero = "otro" if pareja.nombre == novio.name else "otra"       
    $ send_phone_message(phone_config["phone_player_name"], "Haha<emoji_risa> quien insinua es [palabraGenero], si sólo estamos hombro con hombro", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "No mira yo entiendo que tu familia sea muy cariñosa", "pareja_dm", 3)
    $ palabraGenero = "prima" if pareja.nombre == novio.name else "primo"       
    $ send_phone_message(pareja.nombre, "Pero quien no conozca a tu [palabraGenero], puede pensar cosas...<emoji_pensativo>", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Sobre todo tu amiga esa la chismosa...", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Mejor pídele que la elimine va?<emoji_rezando>", "pareja_dm", 3)

    if jugador.nombre == novia.name:

        call telefono_proteccion_masculina

    $ present_phone_choices([
        ("Buscar eliminar la foto y agradecer", Call("telefono_eliminar_foto")), 
        ("Dejar la foto y terminar el tema, como sea", Call("telefono_mantener_foto"))], "pareja_dm")
    
    jump retroalimentacion_pareja_telefono


label retroalimentacion_pareja_telefono:
    
    hide screen phone_ui
    scene black
    show fondo_inicio
    narrador "Ellos sí que escribían rápido, aunque no sabemos si al hacerlo, dijeron cosas sin pensarlo..."
    $ jugador.estadoPlanta == "marchita"
    show planta_marchita:
        yalign .3
        xalign .1
    narrador "Lamentablemente [pareja.nombre] volvió a dañar tu planta, veamos cuándo pasó:"
    hide planta_marchita
    hide fondo_inicio

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
    narrador "E, igual que la vez pasada, esta violencia afectó a tu planta."
    narrador "Parece un ciclo, ¿no lo crees?"
    narrador "Las plantas, como los humanos, merecen cuidados. {b}Merecemos cuidados{/b}"
    jump retroalimentacion_jugador_telefono


label retroalimentacion_jugador_telefono:
    
    narrador "Ahora, veamos el estado de la planta de [pareja.nombre]."
    
    if listaViolenciaJugador:

        $ pareja.estadoPlanta == "marchita"

        show penalizacion_aspersor:
            xalign .05
        $ coleccionables.append("penalizacion_aspersor")
        narrador "¡Oh! Con tus respuestas obtuviste un aspersor de agua sucia para su planta."
        hide penalizacion_aspersor
        show planta_marchita:
            yalign .3
            xalign .5
        narrador "La planta de [pareja.nombre] se siente un poco enferma, veamos cuándo pasó:"
        hide planta_marchita
        hide fondo_inicio

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
        narrador "A veces los efectos de la violencia no son tan perceptibles, pero de que hacen daño, lo hacen."
        narrador "¿Es eso lo que quieres en una relación?"
    else:

        $ pareja.estadoPlanta == "florece"

        show logro_aspersor:
            xalign .05
        $ coleccionables.append("logro_aspersor")
        narrador "¡Felicidades! Con tus respuestas ganaste un aspersor con agua limpia."
        hide logro_aspersor
        show planta_florece:
            yalign .3
            xalign .5
        narrador "La planta de [pareja.nombre] ha comenzado a florecer."
        hide planta_florece

        if listaPresion:
             
            narrador "Pero hubo momentos en los que caíste en la presión de [pareja.nombre]:"

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
            narrador "Seguir los deseos del otro puede parecer la mejor opción, pero ¿dónde quedas tú?"

    jump retroalimentacion_mito_telefono


label retroalimentacion_mito_telefono:

    if listaMito:

        menu:

            narrador "Y, como en la cita en Chapultepec, algunos de los diálogos de Carlos y Ximena reproducen mitos sobre los roles de género, ¿Esta vez tuviste mejor suerte detectándolos?"
            
            "Sí":
            
                narrador "¡Muy bien!, vamos a comprobarlo:"
            "No":
                
                narrador "No te preocupes, veamos juntos:"

        hide fondo_inicio
        $ reiniciar_celular()
        show screen phone_ui

        $ i = 0
        while i < len(listaMito):
            $ renpy.call(listaMito[i])
            $ reiniciar_celular()
            $ i += 1
            
        hide screen phone_ui
        scene black
        show fondo_inicio
        narrador "Las palabras pueden esconder más que su significado literal."
        narrador "¿Cuántas de estas y otras frases haz utilizado sin saber lo que {b}realmente{/b} significan?"

    jump finalJuego


label telefono_humillar_vulnerabilidad:
        
    $ send_phone_message(phone_config["phone_player_name"], "Mm llorar? <emoji_alarma><emoji_robot>falla en el sistema, peligro peligro haha", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Entiendo lo del enojo pero tampoco inventes <emoji_risa_nerviosa>", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Si jaj.. fue mucho verdad?<emoji_medio_triste> lo siento...", "pareja_dm", 3)

    if retroalimentacion:

        narrador "Decidiste {b}humillar{/b} a [pareja.nombre] por querer llorar, invalidándolo, ¿Los hombres no pueden llorar?"
    else:

        $ listaViolenciaJugador.append("telefono_humillar_vulnerabilidad")

    return


label telefono_culparse:
    
    $ send_phone_message(phone_config["phone_player_name"], "Noo amor no te disculpes, yo soy quien se debería disculpar", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Perdóname por hacerte sentir así<emoji_rezando><emoji_rezando>", "pareja_dm", 3)

    if retroalimentacion:

        narrador "Decidiste aceptar toda la culpa cuando [pareja.nombre] también te violentó, aunque [pareja.nombre] se estaba disculpando."
    else:
        
        $ listaPresion.append("telefono_culparse")
        call telefono_merece_violencia
    return


label telefono_merece_violencia:
    
    if jugador.nombre == novia.name:

        $ send_phone_message(phone_config["phone_player_name"], "Si me gritaste, pero porque te hice enojar, me pasé<emoji_lagrima>", "pareja_dm", 3)

        if retroalimentacion:

            narrador "Aunque [jugador.nombre] haya \"provocado\" su enojo, ¿debe tomar responsabilidad por las acciones de [pareja.nombre]?"
        else:

            $ listaMito.append("telefono_merece_violencia")

    return


label telefono_ignorar_violencia:
        
    $ send_phone_message(phone_config["phone_player_name"], "Bueno pero el clima en Chapu estuvo padre no? Así soleadito pero fresco<emoji_feliz>", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "?? si jaj eso creo...", "pareja_dm", 3)

    if retroalimentacion:

        narrador "Decidiste {b}ignorar{/b} a [pareja.nombre] cuando se disculpó contigo. Aunque el tema te sea incómodo, ignorarlo puede hacer más daño."
    else:

        $ listaViolenciaJugador.append("telefono_ignorar_violencia")

    return


label telefono_perdonar_violencia:

    $ palabraGenero = "grosera" if pareja.nombre == novio.name else "grosero"       
    $ send_phone_message(phone_config["phone_player_name"], "Ayy<emoji_rogando> yo también fui un poco [palabraGenero], disculpa", "pareja_dm", 3)
    $ palabraGenero = "abierta" if pareja.nombre == novio.name else "abierto"       
    $ send_phone_message(phone_config["phone_player_name"], "Te perdono amor<emoji_corazon>, y yo también estaré más [palabraGenero] va?", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "sisisis", "pareja_dm", 3)
    return

label telefono_aceptar_ubicacion:

    $ send_phone_message(phone_config["phone_player_name"], "Si.. me acuerdo", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "images/phone/media/gps.png", "pareja_dm", 2, summary_alt="GPS de casa de [palabraGenero] [pareja.nombre]")
    $ send_phone_message(phone_config["phone_player_name"], "Pero no te", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "<emoji_groserias>", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Enojes...", "pareja_dm", 3)
    
    call telefono_celos_amigue
    
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

        narrador "[pareja.nombre] te {b}celó{/b} por estar en casa de una de sus amistades, siendo su primera reacción el enojo y reclamo."
    else:

        $ listaViolenciaPareja.append("telefono_celos_amigue")
        
    return


label telefono_negar_ubicacion:
    
    $ send_phone_message(phone_config["phone_player_name"], "Y si no qué? Te vas a teletransportar hasta acá? Si el único truco que conoces es pedirme ayuda a mí por tu torpeza tecnológica!!<emoji_voltea_ojos>", "pareja_dm", 3)#####################
    $ send_phone_message(phone_config["phone_player_name"], "Haber, pásame tú tu ubicación", "pareja_dm", 3)

    if pareja.nombre == novio.name:

        call telefono_insinuar_mujeriego

    if retroalimentacion:

        narrador "Decidiste {b}humillar{/b} a [pareja.nombre], aunque estás en tu derecho de no compartir tu ubicación, puedes hacerlo sin violentar al otro."
    else:

        $ listaViolenciaJugador.append("telefono_negar_ubicacion")
        
    return


label telefono_ignorar_reclamo:
        
    $ send_phone_message(pareja.nombre, "Contigo no se puede, bye", "pareja_dm", 3)

    if retroalimentacion:

        narrador "A partir de ahí [pareja.nombre] te {b}ignoró{/b} a causa de su enojo, cortando el diálogo sin mayor explicación."
    else:

        $ listaViolenciaPareja.append("telefono_ignorar_reclamo")
        
    return


label telefono_insinuar_mujeriego:
        
    $ send_phone_message(phone_config["phone_player_name"], "Pero ahí no te atreves porque seguro andas en la casa de una amiga<emoji_indiferente>...", "pareja_dm", 3)

    if retroalimentacion:

        narrador "[jugador.nombre] {b}celó{/b} a [pareja.nombre], porque ¿cómo sabe eso?, ¿por una experiencia previa o porque cree que así son los hombres?"
    else:

        $ listaMito.append("telefono_insinuar_mujeriego")
        
    return


label telefono_captura_instagram:
        
    $ palabraGenero = "prima" if pareja.nombre == novio.name else "primo"

    $ send_phone_message(phone_config["phone_player_name"], "Y sigues a mi [palabraGenero]?", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Apenas, es que te acababa de seguir jeje", "pareja_dm", 3)

    if retroalimentacion:

        narrador "[pareja.nombre] te {b}stalkeó{/b}, porque si siguió a alguien que te acaba de seguir, es que está pendiente de tus seguidores."
    else:
        
        $ listaViolenciaPareja.append("telefono_captura_instagram")
        
    return


label telefono_celos_foto:
    
    $ palabraGenero = "prima" if pareja.nombre == novio.name else "primo"
    
    $ send_phone_message(pareja.nombre, "Pero como que tu [palabraGenero] está un poco encima de ti no?", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Parece que te le insinuas", "pareja_dm", 3)

    if retroalimentacion:

        narrador "[pareja.nombre] te {b}celó{/b} por una foto familiar, por su inseguridad."
    else:
        
        $ listaViolenciaPareja.append("telefono_celos_foto")
        
    return


label telefono_proteccion_masculina:
        
    $ send_phone_message(pareja.nombre, "Tal vez tú no te das cuenta de cómo te ves", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Pero no te preocupes, tu novio te cuida<emoji_guinio>", "pareja_dm", 3)

    if retroalimentacion:

        narrador "Está bien que te quiera proteger, pero su \"protección\" eran celos, además, ¿lo está haciendo por seguir un rol de protector, sin considerar que puede ser algo mutuo?"
    else:
        
        $ listaMito.append("telefono_proteccion_masculina")
        
    return


label telefono_eliminar_foto:
        
    $ send_phone_message(phone_config["phone_player_name"], "No lo había pensado de esa forma amor...", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Le voy a pedir el favor de eliminar la foto", "pareja_dm", 3)

    if retroalimentacion:

        narrador "Decidiste caer en la presión de [pareja.nombre] impulsada por sus celos."
    else:
    
        $ listaPresion.append("telefono_eliminar_foto")

        $ send_phone_message(phone_config["phone_player_name"], "Gracias<emoji_corazon>", "pareja_dm", 3)
        $ send_phone_message(pareja.nombre, "No es nada <emoji_corazon><emoji_feliz>", "pareja_dm", 3)

        $ present_phone_choices([
            (
                "Bueno, me voy despidiendo y hablo con mi [palabraGenero]", 
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

        narrador "Decidiste {b}mentir{/b} para calmar sus inseguridades, pero como viste, eso puede empeorar las cosas"
    else:
    
        $ listaViolenciaJugador.append("telefono_mentir_relacion")

        $ send_phone_message(pareja.nombre, "Perdon, qué??<emoji_groserias>", "pareja_dm", 3)
        $ send_phone_message(pareja.nombre, "Por qué me mientes??", "pareja_dm", 3)
    
        call telefono_checar_chat
    
        $ send_phone_message(pareja.nombre, "No puedo creer que me mentiste", "pareja_dm", 3)
        $ send_phone_message(pareja.nombre, "<emoji_lagrima>", "pareja_dm", 3)
        $ send_phone_message(phone_config["phone_player_name"], "Nono espera! yo sólo quería quitar tus preocupaciones", "pareja_dm", 3)
        $ send_phone_message(phone_config["phone_player_name"], "[pareja.apodo]", "pareja_dm", 3)
        $ send_phone_message(phone_config["phone_player_name"], "<emoji_lagrima><emoji_corazon>", "pareja_dm", 3)
        $ send_phone_message(phone_config["phone_player_name"], "[pareja.apodo]!", "pareja_dm", 3)
    return


label telefono_checar_chat:
    
    $ palabraGenero = "cercanas" if pareja.nombre == novio.name else "cercanos"       
    $ send_phone_message(pareja.nombre, "Yo ya sé que son [palabraGenero]!, si veo en tus mensajes que hablan seguido", "pareja_dm", 3)
    if retroalimentacion:

        narrador "[pareja.nombre] te {b}stalkeó{/b}, porque de otra forma no conocería tus mensajes privados."
    else:
        
        $ listaViolenciaPareja.append("telefono_checar_chat")
        
    return


label telefono_mantener_foto:

    $ send_phone_message(phone_config["phone_player_name"], "Pero es su insta...", "pareja_dm", 3)

    call telefono_pretexto

    $ send_phone_message(pareja.nombre, "<emoji_grito>", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Nnonononoo", "pareja_dm", 3)
    $ send_phone_message(pareja.nombre, "Mejor así lo dejamos, verdad amor?", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Si, mejor", "pareja_dm", 3)
    return


label telefono_pretexto:

    $ send_phone_message(phone_config["phone_player_name"], "Y si le digo, tendré que decirle que me obligaste<emoji_medio_triste>", "pareja_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Y cuando sepan mis padres... nos van a querer separar, y no queremos eso verdad?", "pareja_dm", 3)

    if retroalimentacion:

        narrador "Decidiste {b}engañar{/b} para terminar con el tema, pero ¿esa es la mejor solución?"
    else:
        
        $ listaViolenciaJugador.append("telefono_pretexto")
        
    return
