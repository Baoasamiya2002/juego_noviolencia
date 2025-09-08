init python:
    def filtro():
        if recuerdo:
            return SaturationMatrix(0.0)
        else:
            return SaturationMatrix(1.0)


screen show_buttons:
    for i in buttons:
        if (i[3] is None) or (eval(i[3])):
            imagebutton idle (
                "point_and_click/image/" + str(i[0]) + ".webp"
            ) pos i[1] action Return(i[2])


style pnc_image_button:
    anchor (0.5, 0.5)


define diss = {"screens" : Dissolve(0.15)} # this allows the textbox to be hidden and shown without any pause


define buttons = [
    (("chapultepec"),(0.312, 0.27),"citaChapultepec", None),
    (("zocalo"),(0.49, 0.21),"opcionNoDisponible", None),
    (("casa"),(0.53, 0.47),"opcionNoDisponible", None)
]


label citasMapa:
    $ quick_menu = False
    window hide diss
    call screen show_buttons 
    window show diss
    $ quick_menu = True
    jump expression _return


label citaChapultepec:

    scene caminata_chapultepec at Transform(matrixcolor=filtro())
    narrador "Un domingo por la tarde, Ximena y Carlos decidieron salir a una cita."
    narrador "Caminaban entre los árboles, tenían tiempo de no salir juntos, estaban en entregas finales y la carrera de cada uno comenzaba a ser cada vez más demandante."
    narrador "Aunque a veces se veían entre clases en la universidad, están en ambientes muy distintos y cada vez sus diferencias y expectativas se hacían más evidentes..."
    jugador.personaje "Ay no amor. Hablé con mi equipo y quieren trabajar en la escuela. Ya les dije que es más fácil que cada quien llegue a su casa y luego ponernos a trabajar en línea."
    pareja.personaje "Sí."
    jugador.personaje "Y pues, salir de Santa Fe después de las 3 de la tarde y con lluvias está mortal, ¿sabes a qué horas voy a llegar a mi casa? Mínimo a las 7."
    pareja.personaje "Ajá..."
    $ palabraGenero = "seria" if jugador.nombre == "Carlos" else "serio"
    scene expression "emocion_seriedad_[jugador.nombre]"
    jugador.personaje "¿Y tú qué tienes? Estás muy [palabraGenero]."
    $ palabraGenero = "estresada" if jugador.nombre == "Carlos" else "estresado"
    scene expression "emocion_seriedad_[pareja.nombre]"
    pareja.personaje "No, nada amor, solo estoy un poco [palabraGenero] por mi entrega del lunes."
    scene expression "emocion_seriedad_[jugador.nombre]"
    jugador.personaje "¿Sí? Pero a ti te sale todo a la primera… yo sí que debo preocuparme, apenas y le entiendo a la UEA."
    scene expression "emocion_enojo_[pareja.nombre]"
    pareja.personaje "Bueno, pero yo quiero preocuparme, ¿ok?, más bien tu andas de sensible."
    scene expression "emocion_seriedad_[jugador.nombre]"
    jugador.personaje "O tú de cortante."
    
    if jugador.nombre == novia.name:
        
        call mito_bienestar_1
        call mito_ocultar_1
    
    scene expression "emocion_seriedad_[pareja.nombre]"
    pareja.personaje "Sólo sacas un pretexto para pelear."
    scene expression "emocion_seriedad_[jugador.nombre]"
    jugador.personaje "No, de verdad que no, solo quiero saber..."
    scene expression "emocion_enojo_[pareja.nombre]"
    pareja.personaje "¿La verdad? Pues yo... siento que eres muy absorbente, hostigas."

    menu:

        "¿Tú respuesta?"
        "¿Por?":

            $ decisionesJugador.append("¿Por?") 
            scene expression "emocion_tristeza_[jugador.nombre]"
            jugador.personaje "¿Cómo? No entiendo, si según yo estábamos bien."
            $ jugador.estadoPlanta = "marchita"
            call violencia_culpabilizar_1

            if pareja.nombre == novia.name:

                call mito_atencion_1
                call violencia_mito_humillar_1

        "Alguien más le metió la idea":

            $ decisionesJugador.append("Alguien más le metió la idea") 
            $ pareja.estadoPlanta = "marchita"
            call violencia_celar_1
            scene expression "emocion_enojo_[pareja.nombre]"
            pareja.personaje "¿Eso quéee?, ¿ya viste que en lugar de preguntar por qué pienso eso, hiciste que todo se tratara sobre ti?"
            
            if pareja.nombre == novio.name:

                call mito_respeto_1

        "Tal vez no debí sacar el tema":

            $ decisionesJugador.append("Tal vez no debí sacar el tema")
            scene expression "emocion_tristeza_[jugador.nombre]"
            jugador.personaje "..."
            scene expression "emocion_tristeza_[jugador.nombre]"
            jugador.personaje "Eh... yo no quería molestarte. A veces soy así por que me importas. Por que te amo."
            $ jugador.estadoPlanta = "marchita"
            call violencia_humillar_1
            call presion_humillar

    scene caminata_chapultepec
    narrador "Hay un breve silencio entre Carlos y Ximena. Llevan tiempo intentando sacar la relación a flote a pesar de sus compromisos con la escuela, familia y amigos."
    narrador "Su relación nunca ha sido perfecta, pero siguen intentando que lo sea. Piensan que así es el amor."
    scene expression "emocion_tristeza_[jugador.nombre]"
    jugador.personaje "Mejor ya vámonos [pareja.apodo]."
    $ jugador.estadoPlanta = "marchita"
    call violencia_humillar_2

    menu:

        "¿Tú respuesta?"
        "Sincerar mi inseguridad":

            $ decisionesJugador.append("Sincerar mi inseguridad")
            scene expression "emocion_tristeza_[jugador.nombre]"
            jugador.personaje "La verdad no quiero pelear amor, pero a veces te siento distante. He llegado a pensar que te sientes mejor con tus amistades que conmigo. Creo que te aburro o no sé..."
            call violencia_culpabilizar_2

        "Cambiar de tema":

            $ decisionesJugador.append("Cambiar de tema")
            if jugador.nombre == novia.name:

                call mito_bienestar_2
            else:

                call mito_ocultar_2
                
            call violencia_culpabilizar_3
            
            if pareja.nombre == novia.name:
                
                call mito_atencion_2
            else:                
        
                call violencia_mito_humillar_2

            scene expression "emocion_seriedad_[pareja.nombre]"
            pareja.personaje "Así que ya, vámonos, y perdón por lo que te dije. A veces digo cosas que no quiero decir..."
            scene expression "emocion_felicidad_[jugador.nombre]"
            $ palabraGenero = "tranquila" if jugador.nombre == "Carlos" else "tranquilo"
            jugador.personaje "Si, [palabraGenero]."
            jump retroalimentacion_pareja_chapultepec
        
        "Distanciarme y terminar esto":
            
            $ decisionesJugador.append("Distanciarme y terminar esto")
            scene expression "emocion_tristeza_[jugador.nombre]"
            jugador.personaje "Ya no te voy a seguir el juego. Ahí te mando un mensaje."
            
            if pareja.nombre == novio.name:
                
                call mito_sensible_1
            else:                
        
                call mito_atencion_3

            scene expression "emocion_seriedad_[jugador.nombre]"
            jugador.personaje "(suspiro) Bueno. Chao"
            scene expression "emocion_tristeza_[pareja.nombre]"
            pareja.personaje "'¡No, espera!, es que yo... lo siento, a veces digo cosas que no quiero decir..."
            $ pareja.estadoPlanta = "marchita"
            call violencia_ignorar_1
            jump retroalimentacion_pareja_chapultepec

    menu:

        "¿Tú respuesta?"
        "Evitar más pelea":

            $ decisionesJugador.append("Evitar más pelea")
            call presion_culpabilizar
            call violencia_culpabilizar_4

            if pareja.nombre == novia.name:
                
                call mito_atencion_4
            else:                
        
                call mito_proveedor_1

            jump retroalimentacion_pareja_chapultepec

        "¡Ya basta!":

            $ decisionesJugador.append("¡Ya basta!")
            $ pareja.estadoPlanta = "marchita"
            call violencia_culpabilizar_4

            if pareja.nombre == novia.name:
                
                call violencia_celar_2
            else:                
        
                call violencia_mito_culpabilizar_1

            jump retroalimentacion_pareja_chapultepec

        "Mantengo la calma":
            
            $ decisionesJugador.append("Mantengo la calma")
            scene expression "emocion_seriedad_[jugador.nombre]"
            $ palabraGenero = "tranquila" if jugador.nombre == "Carlos" else "tranquilo"
            jugador.personaje "A ver cálmate, quería hablarlo porque no te veía, pero así no llegamos a nada. Caminemos y cuando estés [palabraGenero], lo hablamos."
            scene expression "emocion_seriedad_[pareja.nombre]"
            pareja.personaje "¿Que yo me calme? Te llevas pero no te aguantas... Y yo que te tenía una sorpresa..."
            scene expression "emocion_seriedad_[jugador.nombre]"
            jugador.personaje "¿Sorpresa?"
            scene expression "emocion_enojo_[pareja.nombre]"
            pareja.personaje "Aaa ahora ya quieres hablar..."
            scene expression "emocion_felicidad_[pareja.nombre]"
            $ palabraGenero = "hermano" if jugador.nombre == "Carlos" else "hermana"
            pareja.personaje "Era una tarjeta de Spotify que te enviaba mi [palabraGenero]."
            scene expression "emocion_felicidad_[jugador.nombre]"
            jugador.personaje "¡Hay si! Me dijo [emocionado/a] que me tenía una."
            scene expression "emocion_seriedad_[pareja.nombre]"
            pareja.personaje "Pero con tus dramas no sé..."
            call violencia_chantaje_1

            menu:

                "¿Tú respuesta?"
                "Si":

                    $ decisionesJugador.append("Si")
                    scene expression "emocion_felicidad_[jugador.nombre]"
                    jugador.personaje "(suspiro) Ok... lo podemos hablar otro día. ¿De cuántos meses es la tarjeta?"
####
                    narrador "¡Obtuviste una tarjeta de Spotify! Click o toca para continuar."
                    jump retroalimentacion_pareja_chapultepec                
                
                "No":

                    $ decisionesJugador.append("No")
                    scene expression "emocion_seriedad_[jugador.nombre]"
                    $ palabraGenero = "dispuesta" if jugador.nombre == "Carlos" else "dispuesto"
                    jugador.personaje "Sólo si estás [palabraGenero] a hablar de lo que pasó... ¿Ya platicamos en buen plan?"
                    call violencia_destruir_1
                    #####
                    narrador "¡Obtuviste una tarjeta rota de Spotify! Click o toca para continuar."
                    jump retroalimentacion_pareja_chapultepec


label opcionNoDisponible:

    narrador "Disculpa, esta cita todavía no está disponible.\nDa click o toca 
        cualquier otra parte de la pantalla para poder volver a elegir"
    jump eleccionCita


label retroalimentacion_pareja_chapultepec:

    scene chapultepec_fondo
    narrador "Bueno... no creo que esa haya sido la cita que planearon, ¿verdad?"
    show planta_marchita:
        yalign .3
        xalign .1
    narrador "Lamentablemente [pareja.nombre] dañó tu planta, veamos cuándo pasó:"
    hide planta_marchita
    $ recuerdo = True

    if "¿Por?" in decisionesJugador:

        call violencia_culpabilizar_1
        $ palabraGenero = "ella" if jugador.nombre == "Carlos" else "él"
        narrador "[pareja.nombre] te hizo {b}gaslighting{/b} y {b}culpabilizó{/b} por la discusión, cuando [palabraGenero] fue quien te dijo absorbente."
        
        if pareja.nombre == novia.name:

            call violencia_mito_humillar_1
            narrador "Ahí te intentó {b}humillar{/b} por mostrar tus sentimientos."

    elif "Tal vez no debí sacar el tema" in decisionesJugador:
        
        call violencia_humillar_1
        narrador "[pareja.nombre] se {b}burló{/b} de tu preocupación demeritandote y queriendo que te callaras."
    
    call violencia_humillar_2
    narrador "[pareja.nombre] te intentó {b}humillar{/b} por querer irte, en vez de platicarlo."

    if "Sincerar mi inseguridad" in decisionesJugador:

        call violencia_culpabilizar_2
        narrador "[pareja.nombre] te {b}culpabilizó{/b} de crear peleas por expresar cómo te sentías y quitándose responsabilidad en la discusión."
    
    elif "Cambiar de tema" in decisionesJugador:

        call violencia_culpabilizar_3
        narrador "[pareja.nombre] te {b}culpabilizó{b} de hacerla enojar y te insultó."

        if pareja.nombre == novio.name:

            narrador "Además, cuando él te dijo:"
            call violencia_mito_humillar_2 
            narrador "[pareja.nombre] te intentó {b}humillar{/b} por tus preguntas, descalificándolas."

    elif "Evitar más pelea" in decisionesJugador:
        
        call violencia_culpabilizar_3
        narrador "[pareja.nombre] te hizo {b}gaslighting{/b} y {b}culpabilizó{/b} de su reacción, justificando que decías mentiras cuando no hubo ninguna."

    elif "¡Ya basta!" in decisionesJugador:

        if pareja.nombre == novia.name:

            call violencia_celar_2
            narrador "[pareja.nombre] te {b}celó{/b} por tus amistades, justificando que peleaste para terminar la cita."
        else:
            
            call violencia_mito_culpabilizar_1
            narrador "[pareja.nombre] te {b}culpabilizó{/b} de la discusión y lo redujo a un \"drama\"."

    elif "Mantengo la calma" in decisionesJugador:

        call violencia_chantaje_1
        $ palabraGenero = "hermano" if jugador.nombre == "Carlos" else "hermana"
        narrador "[pareja.nombre] te intentó {b}chantajear{/b} para hacer pasar la violencia anterior, lo hizo con el regalo de su [palabraGenero] para tí."

    elif "No" in decisionesJugador:

        call violencia_destruir_1
        $ palabraGenero = "hermano" if jugador.nombre == "Carlos" else "hermana"        
        narrador "[pareja.nombre] te {b}humilló{/b} con su insulto y {b}destruyó{/b} el regalo de su [palabraGenero] por no caer en su chantaje."

    narrador "Y con toda esta violencia, acabó afectada tu planta."
    narrador "Pero recuerda, {b}no es tu culpa{/b}. [pareja.nombre] es responsable de los daños que causó, no tú."
    jump retroalimentacion_jugador_chapultepec


label retroalimentacion_jugador_chapultepec:
    
    scene chapultepec_fondo
    narrador "Ahora, veamos el estado de la planta de [pareja.nombre]."
    
    if pareja.estadoPlanta == "marchita":
                
        show penalizacion_aspersor:
            xalign .05
        $ coleccionables.append("penalizacion_aspersor")
        narrador "¡Oh! Con tus respuestas obtuviste un aspersor de agua sucia para tu planta."
        hide penalizacion_aspersor
        show planta_marchita:
            yalign .3
            xalign .5
        narrador "La planta de [pareja.nombre] se siente un poco enferma., veamos cuándo pasó:"
        hide planta_marchita

        if "Alguien más le metió la idea" in decisionesJugador:

            call violencia_celar_1
            narrador "Decidiste {b}celar{/b} a [pareja.nombre] por alguien más, en vez de preguntarle por sus sentimientos."

        elif "Distanciarme y terminar esto" in decisionesJugador:

            call violencia_ignorar_1
            narrador "Decidiste {b}ignorar{/b} a [pareja.nombre] cuando se empezaba a abrir contigo y no darle importancia."

        elif "¡Ya basta!" in decisionesJugador:
            
            call violencia_culpabilizar_5
            narrador "Decidiste {b}culpabilizar{/b} a [pareja.nombre] y cortar la comunicación. Además de intentar {b}humillar{/b} por no aceptar tus preocupaciones."
    
        narrador "Y por esta violencia, acabó afectada la planta de [pareja.nombre]."
        narrador "Es normal querer defenderse o terminar la discusión, pero la violencia nos puede alejar de lo que queremos decir."
        narrador "Con las emociones en lo alto podemos hacer cosas de las que nos arrepentimos después. Tomemos un respiro y con respeto se entiende la gente."
    else:
        
        $ pareja.estadoPlanta = "florece"
        show logro_aspersor:
            xalign .05
        $ coleccionables.append("logro_aspersor")
        narrador "¡Felicidades! Con tus respuestas ganaste un aspersor con agua limpia."
        hide logro_aspersor
        show planta_florece:
            yalign .3
            xalign .5
        narrador "Tu planta ha comenzado a florecer."
        hide planta_florece

        if any(d in decisionesJugador for d in (
            "Tal vez no debí sacar el tema", "Cambiar de tema", 
            "Evitar más pelea", "Si")):
            
            narrador "Pero hubo momentos en los que caíste en la presión de [pareja.nombre]:"

            if "Tal vez no debí sacar el tema" in decisionesJugador:

                call violencia_humillar_1
                call presion_humillar
                narrador "[pareja.nombre] te {b}humilló{/b} y decidiste seguirle la corriente."
            
            elif "Cambiar de tema" in decisionesJugador:

                if pareja.nombre == novia.name:
                    
                    call mito_bienestar_2
                else:

                    call mito_ocultar_2
                
                narrador "Buscaste cambiar el tema ante el enojo de [pareja.nombre] y poner su bienestar primero."

            elif "Evitar más pelea" in decisionesJugador:
            
                call presion_culpabilizar
                narrador "Quisiste hacer pasar la violencia ocurrida para terminar el conflicto."

            elif "Si" in decisionesJugador:
                ####
                narrador "¿Recuerdas esa tarjeta de Spotify? Era un regalo para tí, pero la aceptaste a través de un {b}chantaje{/b}."
            
            narrador "Cuidado, estas violencias pueden {b}continuar{/b} o {b}escalar{/b} si no se detienen y sólo las aceptas."

    jump retroalimentacion_mito_chapultepec

label retroalimentacion_mito_chapultepec:
    
    scene chapultepec_fondo
    narrador "Además, algunos de los diálogos de Carlos y Ximena reproducen mitos sobre los roles de género, ¿Te diste cuenta?"
    narrador "Por ejemplo:"
    
    if jugador.nombre == novia.name:
        
        call mito_bienestar_1
        if "Cambiar de tema" in decisionesJugador:
            call mito_bienestar_2
        narrador "Está bien reconocer tus errores, pero ¿fue por un error o porque Ximena cree estar encargada de hacer sentir bien a su pareja?"
    
    if pareja.nombre == novia.name:

        if "¿Por?" in decisionesJugador:
            call violencia_mito_humillar_1
            narrador "Te intentó {b}humillar{\b} por mostrar tus emociones, ¿Eso es algo de verguenza?"
            call mito_atencion_1
            narrador "¿Será que quiere ser el tema de conversación, o cree que así debe ser en una relación?"

        if "Cambiar de tema" in decisionesJugador:
            call mito_atencion_2
            narrador "¿Será que quiere ser el tema de conversación, o cree que así debe ser en una relación?"

        if "Distanciarme y terminar esto" in decisionesJugador:
            call mito_atencion_3
            narrador "¿Será que quiere ser el tema de conversación, o cree que así debe ser en una relación?"

        if "Evitar más pelea" in decisionesJugador:
            call mito_atencion_4
            narrador "¿Será que quiere ser el tema de conversación, o cree que así debe ser en una relación?"

    if pareja.nombre == novio.name:

        call mito_ocultar_1
        narrador "Puede ser cierto, pero la respuesta fue a la defensiva, ¿puede ser que cree tener que ocultar sus emociones?"

        if "Alguien más le metió la idea" in decisionesJugador:
            call mito_respeto_1
            narrador "Aunque Ximena haya \"empezado\", si hay una agresión, ¿quién es el responsable?"

        if "Cambiar de tema" in decisionesJugador:
            call violencia_mito_humillar_2
            narrador "Además de la {b}humillación{/b}, ¿será que cree que en la relación debe de dar órdenes?"

        if "Distanciarme y terminar esto" in decisionesJugador:
            call mito_sensible_1
            narrador "Puede que Ximena se enoje facilmente, ¿pero por qué piensa que así son todas las mujeres?"

        if "Evitar más pelea":
            call mito_proveedor_1
            narrador "¿Los regalos son una muestra de amor o cree que es una responsabilidad?"

    if jugador.nombre == novio.name:

        if "Cambiar de tema" in decisionesJugador:
                call mito_ocultar_2
                narrador "Puede ser cierto, pero la respuesta fue a la defensiva, ¿puede ser que cree tener que ocultar sus emociones?"

    if "¡Ya basta!" in decisionesJugador:

        if pareja.nombre == novio.name:

            call violencia_mito_culpabilizar_1
            narrador "Además de la {b}culpabilización{/b}, ¿la mejor solución será ser reservado?"

    narrador "Tal vez alguno de estos diálogos no los habías visto con este punto de vista."
    narrador "Por eso es bueno cuestionarnos si ¿es un gesto propio o lo hago porque \"así debe ser\"?"
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

label violencia_culpabilizar_1:

    scene expression "emocion_seriedad_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Es que yo quiero estar bien, o sea si te acuerdas yo solo 
        te estaba escuchando, pero pues empezaste a hecharme bronca por algúna razón..."
    return


label violencia_culpabilizar_2:

    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Pues sí, aburres con tus dramas e inseguridades. Yo de verdad quiero salir a gusto contigo, pero por cualquier cosa andas reclamando."
    return


label violencia_culpabilizar_3:

    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Es tu culpa, si no estuvieras castrando, no me hubieras hecho enojar. Eres bien pinche imprudente."
    return


label violencia_culpabilizar_4:

    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "(suspiro) Pero eso no depende de mí ¿ok? Si me inventas cosas, me tengo que defender."
    return


label violencia_culpabilizar_5:

    scene expression "emocion_enojo_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "¿Sabes qué? Ya echaste a perder la salida, mejor ya me voy. A ver quién se preocupa por tí."
    return


label violencia_celar_1:

    scene expression "emocion_enojo_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "¿Y eso de dónde lo sacas? Tus “amigues” te volvieron a hablar mal de mí, ¿verdad?"
    return        


label violencia_humillar_1:

    scene expression "emocion_felicidad_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    $ palabraGenero = "tontito" if jugador.nombre == "Carlos" else "tontita"
    pareja.personaje "Si, yo también amor, pero procura ya no hostigar tanto ¿eh?, o voy a tenerte que poner un diurex en la boca [palabraGenero]."
    return


label violencia_humillar_2:

    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    $ palabraGenero = "tóxico" if jugador.nombre == "Carlos" else "tóxica"
    pareja.personaje "Pero si acabamos de llegar, ¿ves como eres bien [palabraGenero]?"
    return


label violencia_ignorar_1:

    scene expression "emocion_enojo_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "Que ya te dije que me voy. Mándame mensaje o lo que sea."
    return


label violencia_celar_2:

    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Pues vete con tus \"amigues\", porque seguro querías un pretexto para eso, ¿verdad?"
    return


label violencia_chantaje_1:

    scene expression "emocion_seriedad_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Entonces... ¿Pasamos página y te la doy?"
    return


label violencia_destruir_1:

    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    $ palabraGenero = "traumado" if jugador.nombre == "Carlos" else "traumada"
    pareja.personaje "¡Hay pinche [palabraGenero]! Ya mejor me voy, ¿y la tarjeta? Aquí la tienes."
    return


label violencia_mito_humillar_1:

    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Aunque luego no aguantas cuando te respondo y andas de frágil..."
    return   


label violencia_mito_humillar_2:

    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Bueno, vámonos ahorita. Y no más preguntas estúpidas, quiero que se me pase el enojo. "
    return


label violencia_mito_culpabilizar_1:

    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Entonces me hiciste venir hasta acá para otro de tus dramas... Eres increíble. No vuelvo a abrir mi bocota."
    return


label mito_bienestar_1:
    
    scene expression "emocion_tristeza_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "...Perdón, sólo me preocupaba por tí."
    return


label mito_bienestar_2:

    scene expression "emocion_seriedad_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "Mejor hablamos de esto cuando estés más relajado, después de tu entrega."
    return


label mito_atencion_1:

    scene expression "emocion_seriedad_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Y me hablas de tus cosas de la uni, sin preguntarme por las mías... Pero si me insistes en lo que siento, te respondo."
    return


label mito_atencion_2:

    scene expression "emocion_tristeza_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Sólo tienes que estar para mí, no interrogarme, ¿puedes?"
    return


label mito_atencion_3:

    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Claaro, si yo soy la que tengo que estar enviandote mensajes..."
    return


label mito_atencion_4:

    scene expression "emocion_seriedad_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Amor, mejor pregúntame de mi semana, que esta tuve un buen de exposiciones."
    return


label mito_ocultar_1:

    scene expression "emocion_seriedad_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Yo ando normal, no tengo nada."
    return


label mito_ocultar_2:
    
    scene expression "emocion_seriedad_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "Ya olvidé mi preocupación, era una tontería."
    return


label mito_respeto_1:

    scene expression "emocion_seriedad_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Con tus inseguridades me quieres provocar, pero no te daré lo que quieres."
    return

label mito_sensible_1:

    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Mmmta. Igual que las demás, a la primera te enojas."
    return


label mito_proveedor_1:

    scene expression "emocion_felicidad_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Mira amor, ahora sí traje dinero para comprarte de los helados que te gustan, ¿vamos?"
    return

label presion_humillar:
    
    scene expression "emocion_tristeza_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "(risa nerviosa) Haha si..."
    return

label presion_culpabilizar:

    scene expression "emocion_seriedad_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "Bueno, tienes razón, discúlpame. Ya no hay que hablar de eso, vamos a intentar pasarla bien."
    return