init python:
    def filtro():
        if retroalimentacion:
            return SaturationMatrix(0.0)
        else:
            return SaturationMatrix(1.0)


label cita_chapultepec:

    scene caminata_chapultepec
    narrador "Un domingo por la tarde, Ximena y Carlos decidieron salir a una 
        cita."
    narrador "Caminaban entre los árboles, tenían tiempo de no salir juntos, 
        estaban en entregas finales y la carrera de cada uno comenzaba a ser 
        cada vez más demandante."
    narrador "Aunque a veces se veían entre clases en la universidad, están en 
        ambientes muy distintos y cada vez sus diferencias y expectativas se 
        hacían más evidentes..."
    jugador.personaje "Ay no amor. Hablé con mi equipo y quieren trabajar en la 
        escuela. Ya les dije que es más fácil que cada quien llegue a su casa y 
        luego ponernos a trabajar en línea."
    pareja.personaje "Sí."
    jugador.personaje "Y pues, salir de Santa Fe después de las 3 de la tarde y 
        con lluvias está mortal, ¿sabes a qué horas voy a llegar a mi casa? 
        Mínimo a las 7."
    pareja.personaje "Ajá..."
    $ palabraGenero = "seria" if jugador.nombre == novio.name else "serio"
    scene expression "emocion_seriedad_[jugador.nombre]"
    jugador.personaje "¿Y tú qué tienes? Estás muy [palabraGenero]."
    $ palabraGenero = "estresada" if jugador.nombre == novio.name else "estresado"
    scene expression "emocion_seriedad_[pareja.nombre]"
    pareja.personaje "No, nada amor, solo estoy un poco [palabraGenero] por mi 
        entrega del lunes."
    scene expression "emocion_seriedad_[jugador.nombre]"
    jugador.personaje "¿Sí? Pero a ti te sale todo a la primera… yo sí que debo 
        preocuparme, apenas y le entiendo a la UEA."
    scene expression "emocion_enojo_[pareja.nombre]"
    pareja.personaje "Bueno, pero yo quiero preocuparme, ¿ok? Más bien tu andas 
        de sensible."
    scene expression "emocion_seriedad_[jugador.nombre]"
    jugador.personaje "O tú de cortante."

    if jugador.nombre == novia.name:
        
        call chapultepec_preocupacion_pareja
        call chapultepec_ocultar_emocion
    
    scene expression "emocion_seriedad_[pareja.nombre]"
    pareja.personaje "Sólo sacas un pretexto para pelear."
    scene expression "emocion_seriedad_[jugador.nombre]"
    jugador.personaje "No, de verdad que no, solo quiero saber..."
    scene expression "emocion_enojo_[pareja.nombre]"
    pareja.personaje "¿La verdad? Pues yo... siento que eres muy absorbente, 
        hostigas."

    menu:

        narrador "¿Tu respuesta?"
        "¿Por?":

            scene expression "emocion_tristeza_[jugador.nombre]"
            jugador.personaje "¿Cómo? No entiendo, si según yo estábamos bien."
            call chapultepec_culpar_otro

            if pareja.nombre == novia.name:

                call chapultepec_pedir_foco
                call chapultepec_burlar_emociones

        "Alguien más le metió la idea":

            call chapultepec_celar_amigues
            scene expression "emocion_enojo_[pareja.nombre]"
            pareja.personaje "¿Eso quéee?, ¿ya viste que en lugar de preguntar 
                por qué pienso eso, hiciste que todo se tratara sobre ti?"
            
            if pareja.nombre == novio.name:

                call chapultepec_provocacion

        "Tal vez no debí sacar el tema":

            scene expression "emocion_tristeza_[jugador.nombre]"
            jugador.personaje "..."
            scene expression "emocion_tristeza_[jugador.nombre]"
            jugador.personaje "Eh... yo no quería molestarte. A veces soy así 
                por que me importas. Por que te amo."
            call chapultepec_aceptar_broma
    
    scene caminata_chapultepec
    narrador "Hay un breve silencio entre Carlos y Ximena. Llevan tiempo 
        intentando sacar la relación a flote a pesar de sus compromisos con la 
        escuela, familia y amigos."
    narrador "Su relación nunca ha sido perfecta, pero siguen intentando que lo 
        sea. Piensan que así es el amor."
    scene expression "emocion_tristeza_[jugador.nombre]"
    jugador.personaje "Mejor ya vámonos [pareja.apodo]."
    call chapultepec_reclamar_toxicidad

    menu:

        narrador "¿Tu respuesta?"
        "Sincerar mi inseguridad":

            scene expression "emocion_tristeza_[jugador.nombre]"
            jugador.personaje "La verdad no quiero pelear amor, pero a veces te 
                siento distante. He llegado a pensar que te sientes mejor con 
                tus amistades que conmigo. Creo que te aburro o no sé..."
            call chapultepec_culpar_drama

        "Cambiar de tema":

            if jugador.nombre == novia.name:

                call chapultepec_cambiar_tema
            else:

                call chapultepec_olvidar_preocupacion
                
            call chapultepec_culpa_imprudente
            
            if pareja.nombre == novia.name:
                
                call chapultepec_evitar_interrogar
            else:                
        
                call chapultepec_reclamar_estupidez

            scene expression "emocion_seriedad_[pareja.nombre]"
            pareja.personaje "Así que ya, vámonos, y perdón por lo que te dije. 
                A veces digo cosas que no quiero decir..."
            scene expression "emocion_felicidad_[jugador.nombre]"
            $ palabraGenero = (
                "tranquila" if jugador.nombre == novio.name else "tranquilo")
            jugador.personaje "Si, [palabraGenero]."
            jump retroalimentacion_pareja_chapultepec
        
        "Distanciarme y terminar esto":

            scene expression "emocion_tristeza_[jugador.nombre]"
            jugador.personaje "Ya no te voy a seguir el juego. Ahí te mando un 
                mensaje."
            
            if pareja.nombre == novio.name:
                
                call chapultepec_comparar_mujeres
            else:                
        
                call chapultepec_enviar_mensaje

            scene expression "emocion_seriedad_[jugador.nombre]"
            jugador.personaje "(suspiro) Bueno. Chao"
            scene expression "emocion_tristeza_[pareja.nombre]"
            pareja.personaje "¡No, espera!, es que yo... lo siento, a veces digo 
                cosas que no quiero decir..."
            call chapultepec_repetir_retirada
            jump retroalimentacion_pareja_chapultepec

    menu:

        narrador "¿Tu respuesta?"
        "Evitar más pelea":

            call chapultepec_tomar_culpa
            call chapultepec_quitarse_culpa

            if pareja.nombre == novia.name:
                
                call chapultepec_preguntar_semana
            else:                
        
                call chapultepec_comprar_helado

            jump retroalimentacion_pareja_chapultepec

        "¡Ya basta!":

            call chapultepec_reclamar_salida

            if pareja.nombre == novia.name:
                
                call chapultepec_pretexto_amigues
            else:                
        
                call chapultepec_reclamar_drama

            jump retroalimentacion_pareja_chapultepec

        "Mantengo la calma":

            scene expression "emocion_seriedad_[jugador.nombre]"
            $ palabraGenero = (
                "tranquila" if jugador.nombre == novio.name else "tranquilo")
            jugador.personaje "A ver cálmate, quería hablarlo porque no te veía, 
                pero así no llegamos a nada. Caminemos y cuando estés 
                [palabraGenero], lo hablamos."
            scene expression "emocion_seriedad_[pareja.nombre]"
            pareja.personaje "¿Que yo me calme? Te llevas pero no te aguantas... 
                Y yo que te tenía una sorpresa..."
            scene expression "emocion_seriedad_[jugador.nombre]"
            jugador.personaje "¿Sorpresa?"
            scene expression "emocion_enojo_[pareja.nombre]"
            pareja.personaje "Aaa ahora ya quieres hablar..."
            scene expression "emocion_felicidad_[pareja.nombre]"
            $ palabraGenero = (
                "hermano" if jugador.nombre == novio.name else "hermana")
            pareja.personaje "Era una tarjeta de Spotify que te enviaba mi 
                [palabraGenero]."
            scene expression "emocion_felicidad_[jugador.nombre]"
            $ palabraGenero = (
                "emocionado" if jugador.nombre == novio.name else "emocionada")
            jugador.personaje "¡Hay si! Me dijo [palabraGenero] que me tenía una."
            scene expression "emocion_seriedad_[pareja.nombre]"
            pareja.personaje "Pero con tus dramas no sé..."
            call chapultepec_condicionar_regalo

            menu:

                narrador "¿Tu respuesta?"
                "Sí":

                    $ listaPresion.append("chapultepec_aceptar_chantaje")
                    scene expression "emocion_felicidad_[jugador.nombre]"
                    jugador.personaje "(suspiro) Ok... lo podemos hablar otro 
                        día. ¿De cuántos meses es la tarjeta?"
                    $ coleccionables.append("tarjeta_spotify_intacta")
                    show tarjeta_spotify_intacta:
                        yalign .3
                        xalign .5
                    narrador "¡Obtuviste una tarjeta de Spotify! Click o toca 
                        para continuar."
                    hide tarjeta_spotify_intacta
                    jump retroalimentacion_pareja_chapultepec                
                
                "No":

                    scene expression "emocion_seriedad_[jugador.nombre]"
                    $ palabraGenero = (
                        "dispuesta" if jugador.nombre == novio.name 
                        else "dispuesto")
                    jugador.personaje "Sólo si estás [palabraGenero] a hablar de 
                        lo que pasó... ¿Ya platicamos en buen plan?"
                    call chapultepec_romper_tarjeta
                    $ coleccionables.append("tarjeta_spotify_rota")
                    show tarjeta_spotify_rota:
                        yalign .3
                        xalign .5
                    narrador "¡Obtuviste una tarjeta rota de Spotify! Click o 
                        toca para continuar."
                    hide tarjeta_spotify_rota
                    jump retroalimentacion_pareja_chapultepec


label retroalimentacion_pareja_chapultepec:
    
    scene chapultepec_fondo
    narrador "Bueno... no creo que esa haya sido la cita que planearon, ¿verdad?"    
    $ jugador.estadoPlanta == "marchita"
    show planta_marchita:
        yalign .3
        xalign .1
    narrador "Lamentablemente [pareja.nombre] dañó tu planta, veamos cuándo pasó:"
    hide planta_marchita
    $ retroalimentacion = True

    $ i = 0
    while i < len(listaViolenciaPareja):
        $ renpy.call(listaViolenciaPareja[i])
        $ reiniciarCelular()
        $ i += 1
        
    scene chapultepec_fondo
    narrador "Y con toda esta violencia, acabó afectada tu planta."
    narrador "Pero recuerda, {b}no es tu culpa{/b}. [pareja.nombre] es 
        responsable de los daños que causó, no tú."
    jump retroalimentacion_jugador_chapultepec


label retroalimentacion_jugador_chapultepec:
    
    narrador "Ahora, veamos el estado de la planta de [pareja.nombre]."
    
    if listaViolenciaJugador:

        $ pareja.estadoPlanta == "marchita"

        show penalizacion_aspersor:
            xalign .05
        $ coleccionables.append("penalizacion_aspersor")
        narrador "¡Oh! Con tus respuestas obtuviste un aspersor de agua sucia 
            para su planta."
        hide penalizacion_aspersor
        show planta_marchita:
            yalign .3
            xalign .5
        narrador "La planta de [pareja.nombre] se siente un poco enferma, 
            veamos cuándo pasó:"
        hide planta_marchita

        $ i = 0
        while i < len(listaViolenciaJugador):
            $ renpy.call(listaViolenciaJugador[i])
            $ reiniciarCelular()
            $ i += 1
        
        scene chapultepec_fondo
        narrador "Y por esta violencia, acabó afectada la planta de [pareja.nombre]."
        narrador "Es normal querer defenderse o terminar la discusión, pero la 
            violencia nos puede alejar de lo que queremos decir."
        narrador "Con las emociones en lo alto podemos hacer cosas de las que 
            nos arrepentimos después. Tomemos un respiro y con respeto se 
            entiende la gente."
    else:

        $ pareja.estadoPlanta == "florece"

        show logro_aspersor:
            xalign .05
        $ coleccionables.append("logro_aspersor")
        narrador "¡Felicidades! Con tus respuestas ganaste un aspersor con agua 
            limpia."
        hide logro_aspersor
        show planta_florece:
            yalign .3
            xalign .5
        narrador "La planta de [pareja.nombre] ha comenzado a florecer."
        hide planta_florece

        if listaPresion:
             
            narrador "Pero hubo momentos en los que caíste en la presión de 
                [pareja.nombre]:"

            $ i = 0
            while i < len(listaPresion):
                $ renpy.call(listaPresion[i])
                $ reiniciarCelular()
                $ i += 1
                
            scene chapultepec_fondo
            narrador "Cuidado, estas violencias pueden {b}continuar{/b} o 
                {b}escalar{/b} si no se detienen y sólo las aceptas."

    jump retroalimentacion_mito_chapultepec


label retroalimentacion_mito_chapultepec:

    if listaMito:

        menu:

            narrador "Además, algunos de los diálogos de Carlos y Ximena 
                reproducen mitos sobre los roles de género, ¿Te diste cuenta?"
        
            "Sí":
            
                narrador "¡Muy bien!, vamos a comprobarlo:"
            "No":
                
                narrador "No te preocupes, veamos juntos:"
        
        $ i = 0
        while i < len(listaMito):
            $ renpy.call(listaMito[i])
            $ reiniciarCelular()
            $ i += 1
            
        scene chapultepec_fondo
        narrador "Tal vez alguno de estos diálogos no los habías visto con este punto de vista."
        narrador "Por eso es bueno cuestionarnos si ¿es un gesto propio o lo hago porque \"así debe ser\"?"
    
    jump telefono_conversacion


label chapultepec_preocupacion_pareja:
    
    scene expression "emocion_tristeza_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "...Perdón, sólo me preocupaba por tí."

    if retroalimentacion:

        narrador "Está bien reconocer tus errores, pero ¿fue por un error o 
            porque Ximena cree estar encargada de hacer sentir bien a su pareja?"
    else:

        $ listaMito.append("chapultepec_preocupacion_pareja")
    
    return


label chapultepec_ocultar_emocion:
    
    scene expression "emocion_seriedad_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Yo ando normal, no tengo nada."

    if retroalimentacion:

        narrador "Puede ser cierto, pero la respuesta fue a la defensiva, ¿puede 
            ser que cree tener que ocultar sus emociones?"
    else:

        $ listaMito.append("chapultepec_ocultar_emocion")
    
    return


label chapultepec_culpar_otro:
    
    scene expression "emocion_seriedad_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Es que yo quiero estar bien, o sea si te acuerdas yo solo 
        te estaba escuchando, pero pues empezaste a hecharme bronca por algúna 
        razón..."

    if retroalimentacion:

        $ palabraGenero = "ella" if jugador.nombre == novio.name else "él"
        narrador "[pareja.nombre] te hizo {b}gaslighting{/b} y 
            {b}culpabilizó{/b} por la discusión, cuando [palabraGenero] fue 
            quien te dijo absorbente."
    else:

        $ listaViolenciaPareja.append("chapultepec_culpar_otro")
    
    return


label chapultepec_pedir_foco:
    
    scene expression "emocion_seriedad_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Y me hablas de tus cosas de la uni, sin preguntarme por 
        las mías... Pero si me insistes en lo que siento, te respondo."

    if retroalimentacion:

        narrador "¿Será que quiere ser el tema de conversación, o cree que 
            así debe ser en una relación?"
    else:

        $ listaMito.append("chapultepec_pedir_foco")
    
    return 



label chapultepec_burlar_emociones:
    
    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Aunque luego no aguantas cuando te respondo y andas de 
        frágil..."

    if retroalimentacion:

        narrador "[pareja.nombre] te intentó {b}humillar{/b} por mostrar tus 
            sentimientos. ¿Eso es algo de verguenza?"
    else:

        $ listaViolenciaPareja.append("chapultepec_burlar_emociones")
    
    return 



label chapultepec_celar_amigues:
    
    scene expression "emocion_enojo_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "¿Y eso de dónde lo sacas? Tus “amigues” te volvieron a 
        hablar mal de mí, ¿verdad?"

    if retroalimentacion:

        narrador "Decidiste {b}celar{/b} a [pareja.nombre] por alguien más, en 
            vez de preguntarle por sus sentimientos."
    else:

        $ listaViolenciaJugador.append("chapultepec_celar_amigues")
    
    return


label chapultepec_provocacion:
    
    scene expression "emocion_seriedad_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Con tus inseguridades me quieres provocar, pero no te 
        daré lo que quieres."

    if retroalimentacion:

        narrador "Aunque [pareja.nombre] haya \"empezado\", si hay una agresión, 
            ¿quién es el responsable?"
    else:

        $ listaMito.append("chapultepec_provocacion")
    
    return


label chapultepec_broma_diurex:
    
    scene expression "emocion_felicidad_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    $ palabraGenero = "tontito" if jugador.nombre == novio.name else "tontita"
    pareja.personaje "Si, yo también amor, pero procura ya no hostigar tanto 
        ¿eh?, o voy a tenerte que poner un diurex en la boca [palabraGenero]."

    if retroalimentacion:

        narrador "[pareja.nombre] se {b}burló{/b} de tu preocupación 
            demeritandote y queriendo que te callaras."
    else:

        $ listaViolenciaPareja.append("chapultepec_broma_diurex")
    
    return


label chapultepec_aceptar_broma:
    
    call chapultepec_broma_diurex
    scene expression "emocion_tristeza_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "(risa nerviosa) Haha si..."

    if retroalimentacion:

        narrador "[pareja.nombre] te {b}humilló{/b} y decidiste seguirle la 
            corriente."
    else:

        $ listaPresion.append("chapultepec_aceptar_broma")
    
    return


label chapultepec_reclamar_toxicidad:
    
    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    $ palabraGenero = "tóxico" if jugador.nombre == novio.name else "tóxica"
    pareja.personaje "Pero si acabamos de llegar, ¿ves como eres bien 
        [palabraGenero]?"

    if retroalimentacion:

        narrador "[pareja.nombre] te intentó {b}humillar{/b} por querer irte, 
            en vez de platicarlo."
    else:

        $ listaViolenciaPareja.append("chapultepec_reclamar_toxicidad")
    
    return


label chapultepec_culpar_drama:
    
    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Pues sí, aburres con tus dramas e inseguridades. Yo de 
        verdad quiero salir a gusto contigo, pero por cualquier cosa andas 
        reclamando."

    if retroalimentacion:

        narrador "[pareja.nombre] te {b}culpabilizó{/b} de crear peleas por 
            expresar cómo te sentías y quitándose responsabilidad en la discusión."
    else:

        $ listaViolenciaPareja.append("chapultepec_culpar_drama")
    
    return


label chapultepec_cambiar_tema:
    
    scene expression "emocion_seriedad_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "Mejor hablamos de esto cuando estés más relajado, después 
        de tu entrega."

    if retroalimentacion:

        narrador "Buscaste cambiar el tema ante el enojo de [pareja.nombre] y 
            poner su bienestar primero."
    else:

        $ listaMito.append("chapultepec_cambiar_tema")
    
    return


label chapultepec_olvidar_preocupacion:
    
    scene expression "emocion_seriedad_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "Ya olvidé mi preocupación, era una tontería."

    if retroalimentacion:

        narrador "Buscaste cambiar el tema ante el enojo de [pareja.nombre] y 
            poner su bienestar primero."
    else:

        $ listaMito.append("chapultepec_olvidar_preocupacion")
    
    return


label chapultepec_culpa_imprudente:
    
    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Es tu culpa, si no estuvieras castrando, no me hubieras 
        hecho enojar. Eres bien pinche imprudente."

    if retroalimentacion:

        narrador "[pareja.nombre] te {b}culpabilizó{b} de hacerla enojar y 
            te insultó."
    else:

        $ listaViolenciaPareja.append("chapultepec_culpa_imprudente")
    
    return


label chapultepec_evitar_interrogar:
    
    scene expression "emocion_tristeza_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Sólo tienes que estar para mí, no interrogarme, ¿puedes?"

    if retroalimentacion:

        narrador "¿Será que quiere ser el tema de conversación, o cree que así 
            debe ser en una relación?"
    else:

        $ listaMito.append("chapultepec_evitar_interrogar")
    
    return


label chapultepec_reclamar_estupidez:
    
    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Bueno, vámonos ahorita. Y no más preguntas estúpidas, 
        quiero que se me pase el enojo."

    if retroalimentacion:

        narrador "[pareja.nombre] te intentó {b}humillar{/b} por tus preguntas, 
            descalificándolas. ¿Será que cree que en la relación debe de dar 
            órdenes?"
    else:

        $ listaViolenciaPareja.append("chapultepec_reclamar_estupidez")
    
    return


label chapultepec_comparar_mujeres:
    
    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Mmmta. Igual que las demás, a la primera te enojas."

    if retroalimentacion:

        narrador "Puede que [pareja.nombre] se enoje facilmente, ¿pero por qué 
            piensa que así son todas las mujeres?"
    else:

        $ listaMito.append("chapultepec_comparar_mujeres")
    
    return


label chapultepec_enviar_mensaje:
    
    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Claaro, si yo soy la que te anda enviando mensajes..."

    if retroalimentacion:

        narrador "¿Será que [jugador.nombre] casi no envía mensajes, o ella cree
            estar encargada de la comunicación?"
    else:

        $ listaMito.append("chapultepec_enviar_mensaje")
    
    return


label chapultepec_repetir_retirada:
    
    scene expression "emocion_enojo_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "Que ya te dije que me voy. Mándame mensaje o lo que sea."

    if retroalimentacion:

        narrador "Decidiste {b}ignorar{/b} a [pareja.nombre] cuando se empezaba 
            a abrir contigo y no darle importancia."
    else:

        $ listaViolenciaJugador.append("chapultepec_repetir_retirada")
    
    return


label chapultepec_tomar_culpa:
    
    scene expression "emocion_seriedad_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "Bueno, tienes razón, discúlpame. Ya no hay que hablar de 
        eso, vamos a intentar pasarla bien."

    if retroalimentacion:

        narrador "Quisiste hacer pasar la violencia ocurrida para terminar el 
            conflicto."
    else:

        $ listaPresion.append("chapultepec_tomar_culpa")
    
    return


label chapultepec_quitarse_culpa:
    
    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "(suspiro) Pero eso no depende de mí ¿ok? Si me inventas 
        cosas, me tengo que defender."

    if retroalimentacion:

        narrador "[pareja.nombre] te hizo {b}gaslighting{/b} y {b}culpabilizó{/b} 
            de su reacción, justificando que decías mentiras cuando no hubo ninguna."
    else:

        $ listaViolenciaPareja.append("chapultepec_quitarse_culpa")
    
    return


label chapultepec_preguntar_semana:
    
    scene expression "emocion_seriedad_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Amor, mejor pregúntame de mi semana, que esta tuve un buen 
        de exposiciones."

    if retroalimentacion:

        narrador "¿Será que quiere ser el tema de conversación, o cree que así 
            debe ser en una relación?"
    else:

        $ listaMito.append("chapultepec_preguntar_semana")
    
    return


label chapultepec_comprar_helado:
    
    scene expression "emocion_felicidad_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Mira amor, ahora sí traje dinero para comprarte de los 
        helados que te gustan, ¿vamos?"

    if retroalimentacion:

        narrador "¿Los regalos son una muestra de amor o cree que es una 
            responsabilidad?"
    else:

        $ listaMito.append("chapultepec_comprar_helado")
    
    return


label chapultepec_reclamar_salida:
    
    scene expression "emocion_enojo_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "¿Sabes qué? Ya echaste a perder la salida, mejor ya me 
        voy. A ver quién se preocupa por tí."

    if retroalimentacion:

        narrador "Decidiste {b}culpabilizar{/b} a [pareja.nombre] y cortar la 
            comunicación. Además de intentar {b}humillar{/b} por no aceptar tus 
            preocupaciones."
    else:

        $ listaViolenciaJugador.append("chapultepec_reclamar_salida")
    
    return


label chapultepec_pretexto_amigues:
    
    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Pues vete con tus \"amigues\", porque seguro querías un 
        pretexto para eso, ¿verdad?"

    if retroalimentacion:

        narrador "[pareja.nombre] te {b}celó{/b} por tus amistades, justificando 
            que peleaste para terminar la cita."
    else:

        $ listaViolenciaPareja.append("chapultepec_pretexto_amigues")
    
    return


label chapultepec_reclamar_drama:
    
    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Entonces me hiciste venir hasta acá para otro de tus 
        dramas... Eres increíble. No vuelvo a abrir mi bocota."

    if retroalimentacion:

        narrador "[pareja.nombre] te {b}culpabilizó{/b} de la discusión y lo 
            redujo a un \"drama\". ¿La mejor solución era ser reservado?"
    else:

        $ listaViolenciaPareja.append("chapultepec_reclamar_drama")
    
    return


label chapultepec_condicionar_regalo:
    
    scene expression "emocion_seriedad_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Entonces... ¿Pasamos página y te la doy?"

    if retroalimentacion:

        $ palabraGenero = "hermano" if jugador.nombre == novio.name else "hermana"
        narrador "[pareja.nombre] te intentó {b}chantajear{/b} para hacer pasar 
            la violencia anterior, lo hizo con el regalo de su [palabraGenero] 
            para tí."
    else:

        $ listaViolenciaPareja.append("chapultepec_condicionar_regalo")
    
    return


label chapultepec_romper_tarjeta:
    
    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    $ palabraGenero = "traumado" if jugador.nombre == novio.name else "traumada"
    pareja.personaje "¡Hay pinche [palabraGenero]! Ya mejor me voy, ¿y la 
        tarjeta? Aquí la tienes."

    if retroalimentacion:

        $ palabraGenero = "hermano" if jugador.nombre == novio.name else "hermana"
        show tarjeta_spotify_rota:
                        yalign .3
                        xalign .5        
        narrador "[pareja.nombre] te {b}humilló{/b} con su insulto y 
            {b}destruyó{/b} el regalo de su [palabraGenero] por no caer en su 
            chantaje."
        hide tarjeta_spotify_rota
    else:

        $ listaViolenciaPareja.append("chapultepec_romper_tarjeta")
    
    return


label chapultepec_aceptar_chantaje:
    
    show tarjeta_spotify_intacta:
        yalign .3
        xalign .5
    narrador "¿Y recuerdas esa tarjeta de Spotify? Era un regalo para tí, pero la 
        aceptaste a través de un {b}chantaje{/b}."
    hide tarjeta_spotify_intacta

    return