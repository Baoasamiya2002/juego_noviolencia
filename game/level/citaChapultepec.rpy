init python:
    def filtro():
        if retroalimentacion:
            return SaturationMatrix(0.0)
        else:
            return SaturationMatrix(1.0)


label cita_chapultepec:

    $ save_name = _("Segunda capa")
    show capa_2 with fade
    show screen accion_cronometrada
    pause
    hide screen accion_cronometrada

    $ retroalimentacion = False
    $ listaEstereotipo = []

    scene caminata_chapultepec with fade
    narrador "[jugador.nombre] y [pareja.nombre] empezaron a caminar entre los 
        árboles, tenían tiempo de no salir juntos, estaban en entregas finales y 
        la carrera de cada uno comenzaba a ser cada vez más demandante."
    narrador "Aunque a veces se veían entre clases en la universidad, están en 
        ambientes muy distintos y cada vez sus diferencias y expectativas se 
        hacían más evidentes..."
    
    if jugador.nombre == novia.name:

        jugador.personaje "Ay no amor. Hablé con mi equipo y quieren trabajar en la 
            escuela. Ya les dije que es más fácil que cada quien llegue a su casa y 
            luego ponernos a trabajar en línea."
        pareja.personaje "Sí."
        jugador.personaje "Y pues, salir de Santa Fe después de las 3 de la tarde y 
            con lluvias está mortal, ¿sabes a qué horas voy a llegar a mi casa? 
            Mínimo a las 7."
        pareja.personaje "Ajá..."
        scene expression "emocion_seriedad_[jugador.nombre]"
        jugador.personaje "¿Y tú qué tienes? Estás muy serio."
        scene expression "emocion_seriedad_[pareja.nombre]"
        pareja.personaje "No, nada amor, solo estoy un poco estresado por mi 
            entrega del lunes."
        scene expression "emocion_seriedad_[jugador.nombre]"
        jugador.personaje "¿Sí? Pero a ti te sale todo a la primera… yo sí que debo 
            preocuparme, apenas y le entiendo a la UEA."
    else:

        jugador.personaje "¿Te acuerdas de mi proyecto que tengo para mañana? 
            Pues al parecer yo no... casi no he hecho nada."
        pareja.personaje "Sí."
        jugador.personaje "Y pues le puedo pedir cosas a IA ¿verdad?, 
            pero la otra vez, de ese mismo tema, me dió cosas que nada que ver..."
        pareja.personaje "Ajá..."
        scene expression "emocion_seriedad_[jugador.nombre]"
        jugador.personaje "¿Y tú qué tienes? Estás muy seria."
        scene expression "emocion_seriedad_[pareja.nombre]"
        pareja.personaje "No, nada amor, solo estoy un poco estresada por mi 
            trabajo en equipo."
        scene expression "emocion_seriedad_[jugador.nombre]"
        jugador.personaje "¿Sí? Pero te tocó con puro matadito… yo sí que debo 
            preocuparme, apenas y le entiendo a la UEA."
    scene expression "emocion_enojo_[pareja.nombre]"
    pareja.personaje "Bueno, pero yo quiero preocuparme, ¿ok? Más bien tu andas 
        de sensible."
    scene expression "emocion_seriedad_[jugador.nombre]"
    jugador.personaje "O tú de cortante."

    if jugador.nombre == novia.name:
        
        call chapultepec_preocupacion_pareja from _call_chapultepec_preocupacion_pareja
        call chapultepec_ocultar_emocion from _call_chapultepec_ocultar_emocion
    
    scene expression "emocion_seriedad_[pareja.nombre]"
    pareja.personaje "Sólo sacas un pretexto para pelear."
    scene expression "emocion_seriedad_[jugador.nombre]"
    jugador.personaje "No, de verdad que no, sólo quiero saber..."
    scene expression "emocion_enojo_[pareja.nombre]"
    pareja.personaje "¿La verdad? Pues yo... siento que no sabes qué inventar, 
        hostigas."

    menu:

        narrador "¿Tu decisión?"
        "Mostrar confusión":

            scene expression "emocion_tristeza_[jugador.nombre]"
            jugador.personaje "¿Cómo? No entiendo, si según yo estábamos bien."
            call chapultepec_culpar_otro from _call_chapultepec_culpar_otro

            if pareja.nombre == novia.name:

                call chapultepec_pedir_foco from _call_chapultepec_pedir_foco
                call chapultepec_burlar_emociones from _call_chapultepec_burlar_emociones

        "Preguntar de dónde sacó la idea":

            call chapultepec_celar_amigues from _call_chapultepec_celar_amigues
            scene expression "emocion_enojo_[pareja.nombre]"
            pareja.personaje "¿Eso quéee?, ¿ya viste que en lugar de preguntar 
                por qué pienso eso, hiciste que todo se tratara sobre ti?"
            
            if pareja.nombre == novio.name:

                call chapultepec_provocacion from _call_chapultepec_provocacion

        "Arrepentirse por hostigar":

            scene expression "emocion_tristeza_[jugador.nombre]"
            jugador.personaje "..."
            scene expression "emocion_tristeza_[jugador.nombre]"
            jugador.personaje "Eh... yo no quería molestarte. A veces soy así 
                por que me importas. Por que te amo."
            call chapultepec_aceptar_broma from _call_chapultepec_aceptar_broma
    
    scene caminata_chapultepec
    narrador "Hay un breve silencio entre [pareja.nombre] y [jugador.nombre]. Llevan tiempo 
        intentando sacar la relación a flote a pesar de sus compromisos con la 
        escuela, familia y amigos."
    narrador "Su relación nunca ha sido perfecta, pero siguen intentando que lo 
        sea. Piensan que así es el amor."
    scene expression "emocion_tristeza_[jugador.nombre]"
    $ palabraGenero = (
                "enojada" if jugador.nombre == novio.name else "enojado")
    jugador.personaje "Mira, la verdad se nota que sigues [palabraGenero], 
        ¿y si nos vamos?"
    call chapultepec_reclamar_toxicidad from _call_chapultepec_reclamar_toxicidad

    menu:

        narrador "¿Tu decisión?"
        "Cuestionar relación":

            scene expression "emocion_tristeza_[jugador.nombre]"
            jugador.personaje "La verdad no quiero pelear amor, pero a veces te 
                siento distante. He llegado a pensar que te sientes mejor con 
                tus amistades que conmigo. Creo que te aburro o no sé..."
            call chapultepec_culpar_drama from _call_chapultepec_culpar_drama

        "Cambiar de tema":

            if jugador.nombre == novia.name:

                call chapultepec_cambiar_tema from _call_chapultepec_cambiar_tema
            else:

                call chapultepec_olvidar_preocupacion from _call_chapultepec_olvidar_preocupacion
                
            call chapultepec_culpa_imprudente from _call_chapultepec_culpa_imprudente
            
            if pareja.nombre == novia.name:
                
                call chapultepec_evitar_interrogar from _call_chapultepec_evitar_interrogar
            else:                
        
                call chapultepec_reclamar_estupidez from _call_chapultepec_reclamar_estupidez

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
                
                call chapultepec_comparar_mujeres from _call_chapultepec_comparar_mujeres
            else:                
        
                call chapultepec_enviar_mensaje from _call_chapultepec_enviar_mensaje

            scene expression "emocion_seriedad_[jugador.nombre]"
            jugador.personaje "(suspiro) Bueno. Chao"
            scene expression "emocion_tristeza_[pareja.nombre]"
            pareja.personaje "¡No, espera!, es que yo... lo siento, a veces digo 
                cosas que no quiero decir..."
            call chapultepec_repetir_retirada from _call_chapultepec_repetir_retirada
            jump retroalimentacion_pareja_chapultepec

    menu:

        narrador "¿Tu decisión?"
        "Evitar más pelea":

            call chapultepec_tomar_culpa from _call_chapultepec_tomar_culpa
            call chapultepec_quitarse_culpa from _call_chapultepec_quitarse_culpa

            if pareja.nombre == novia.name:
                
                call chapultepec_preguntar_semana from _call_chapultepec_preguntar_semana
            else:                
        
                call chapultepec_comprar_helado from _call_chapultepec_comprar_helado

            jump retroalimentacion_pareja_chapultepec

        "Terminar cita":

            call chapultepec_reclamar_salida from _call_chapultepec_reclamar_salida

            if pareja.nombre == novia.name:
                
                call chapultepec_pretexto_amigues from _call_chapultepec_pretexto_amigues
            else:                
        
                call chapultepec_reclamar_drama from _call_chapultepec_reclamar_drama

            jump retroalimentacion_pareja_chapultepec

        "Insistir más":

            $ listaMito.append("chapultepec_insistir_hablar")
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
            pareja.personaje "Era una tarjeta para streaming de música que te 
                enviaba mi [palabraGenero]."
            scene expression "emocion_felicidad_[jugador.nombre]"
            $ palabraGenero = (
                "emocionado" if jugador.nombre == novio.name else "emocionada")
            jugador.personaje "¡Hay si! Me dijo [palabraGenero] que me tenía una."
            scene expression "emocion_seriedad_[pareja.nombre]"
            pareja.personaje "Pero con tus dramas no sé..."
            call chapultepec_condicionar_regalo from _call_chapultepec_condicionar_regalo
            if renpy.variant("mobile"):

                $ instruccion = "Toca la pantalla para continuar."
            else:

                $ instruccion = "Da click para continuar."

            menu:

                narrador "¿Tu decisión?"
                "Sí":

                    $ listaPresion.append("chapultepec_aceptar_chantaje")
                    scene expression "emocion_felicidad_[jugador.nombre]"
                    jugador.personaje "(suspiro) Ok... lo podemos hablar otro 
                        día. ¿De cuántos meses es la tarjeta?"
                    $ coleccionables.append("tarjeta_intacta")
                    show tarjeta_intacta:
                        yalign .4
                        xalign .5
                    narrador "¡Obtuviste una tarjeta para streaming de música! 
                        [instruccion]"
                    hide tarjeta_intacta
                    jump retroalimentacion_pareja_chapultepec                
                
                "No":

                    scene expression "emocion_seriedad_[jugador.nombre]"
                    $ palabraGenero = (
                        "dispuesta" if jugador.nombre == novio.name 
                        else "dispuesto")
                    jugador.personaje "Sólo si estás [palabraGenero] a hablar de 
                        lo que pasó... ¿Ya platicamos en buen plan?"
                    call chapultepec_romper_tarjeta from _call_chapultepec_romper_tarjeta
                    $ coleccionables.append("tarjeta_rota")
                    show tarjeta_rota:
                        yalign .4
                        xalign .5
                    narrador "¡Obtuviste una tarjeta rota para streaming de 
                        música! [instruccion]"
                    hide tarjeta_rota
                    jump retroalimentacion_pareja_chapultepec    


label retroalimentacion_pareja_chapultepec:
    
    scene fondo_inicio with fade
    narrador "Bueno... no creo que esa haya sido la cita que planeaste, ¿verdad?"    
    $ jugador.estadoPlanta = LISTA_ESTADO_PLANTA[1]
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
    narrador "Lamentablemente [pareja.nombre] dañó tu planta, veamos cuándo pasó:"
    hide planta_fondo
    hide planta
    hide maceta_dorado
    $ retroalimentacion = True

    $ i = 0
    while i < len(listaViolenciaPareja):
        $ renpy.call(listaViolenciaPareja[i])
        $ i += 1
        
    scene chapultepec_fondo
    narrador "Y con toda esta violencia, acabó afectada tu planta."
    narrador "Pero recuerda, {size=+15}{u}no es tu culpa{/u}{/size}. [pareja.nombre] es 
        responsable de los daños que causó, no tú."
    jump retroalimentacion_jugador_chapultepec


label retroalimentacion_jugador_chapultepec:
    
    narrador "Ahora, veamos el estado de la planta de [pareja.nombre]."
    
    if listaViolenciaJugador:

        $ pareja.estadoPlanta = LISTA_ESTADO_PLANTA[1]

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
        narrador "La planta de [pareja.nombre] se siente un poco enferma, 
            veamos cuándo pasó:"
        hide planta_fondo
        hide planta

        $ i = 0
        while i < len(listaViolenciaJugador):
            $ renpy.call(listaViolenciaJugador[i])
            $ i += 1
        
        scene chapultepec_fondo
        narrador "Y por esta violencia, acabó afectada la planta de [pareja.nombre]."
        narrador "Es normal que quieras defenderte o terminar la discusión, pero 
            ¿quieres una relación a base de violencia?"
        narrador "Tomar responsabilidad y buscar un cambio te llevan más cerca 
            a la relación que quieres, ¿no lo crees?"
    else:

        $ pareja.estadoPlanta = LISTA_ESTADO_PLANTA[2]

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
             
            narrador "Pero hubo momentos en los que caíste en la presión de 
                [pareja.nombre]:"

            $ i = 0
            while i < len(listaPresion):
                $ renpy.call(listaPresion[i])
                $ i += 1
                
            scene chapultepec_fondo
            narrador "{size=+15}{u}Cuidado{/u}{/size}, estas violencias pueden continuar o 
                {size=+15}{u}escalar{/u}{/size} si no se detienen y sólo las aceptas."

    jump retroalimentacion_estereotipo_chapultepec


label retroalimentacion_estereotipo_chapultepec:

    if listaEstereotipo:

        menu:

            narrador "Además, algunos de sus diálogos 
                reproducen estereotipos sobre los roles de género, ¿Te diste cuenta?"
        
            "Sí":
            
                narrador "¿Eso crees?, vamos a comprobarlo:"
            "No":
                
                narrador "Puede ser difícil ¿verdad?, veamos:"
        
        $ i = 0
        while i < len(listaEstereotipo):
            $ renpy.call(listaEstereotipo[i])
            $ i += 1
            
        scene chapultepec_fondo
        narrador "Tal vez alguno de estos diálogos no los habías visto con este 
            punto de vista."
        narrador "Por eso es bueno cuestionarnos ¿es un gesto propio o lo hago 
            porque \"así debe ser\"?"

    $ forzarAutosave()

    call instrucciones_recursos
    jump opcion_chapultepec_regresar_menu


label opcion_chapultepec_regresar_menu:

    scene black

    menu:
        
        narrador "Haz atravesado la segunda capa de Latencia ¿Quieres continuar? 
            La siguiente capa te {glitch=4.1}retará{/glitch}."
        "Sí":

            call instrucciones_cargar
            jump telefono_conversacion
        "Más tarde":

            narrador "¡Entendido! Espero que regreses pronto para atravesar más 
                capas de Latencia."
            call instrucciones_cargar
            $ renpy.full_restart() 


label chapultepec_ocultar_incomodidad:

    scene expression "emocion_felicidad_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "Así que espero no olvidar verme feliz o va a pensar que 
        no estoy agradecida por su regalo."    
    scene expression "emocion_seriedad_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "Todo sea en nombre de la moda... porque también estos mallones me 
        aprietan un buen, pero combinan y obvio en las fotos me quiere ver bonita."

    if retroalimentacion:

        narrador "Si sientes incomodidad, ¿Porqué fingir y sacrificar tu cuerpo 
            para verte como crees que [pareja.nombre] te quiere ver?"
    else:

        $ listaEstereotipo.append("chapultepec_ocultar_incomodidad")
    
    return


label chapultepec_miedo_estereotipo:

    scene expression "emocion_seriedad_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "Aunque, ¿yo darle una flor? Eso lo hacen más los chicos..."

    if retroalimentacion:

        narrador "¿Es de chicos el dar regalos a su pareja?, ¿Las flores son de 
            chicas? o ¿ninguna de las anteriores?"
    else:

        $ listaEstereotipo.append("chapultepec_miedo_estereotipo")
    
    return


label chapultepec_merecer_enojo:

    scene expression "emocion_tristeza_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "Y no quiero que [pareja.apodo] se moleste por hacer cosas 
        extrañas... Fue una idea estúpida."

    if retroalimentacion:

        narrador "Si tus acciones no le hacen daño ¿Por qué se podría molestar?, 
            ¿o es lo que esperas de él?"
    else:

        $ listaEstereotipo.append("chapultepec_merecer_enojo")
    
    return

label chapultepec_encargada_sentir_pareja:

    scene expression "emocion_seriedad_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "¿Será de la escuela? No, no creo, pero ahorita que 
        hablemos lo voy a hacer sentir bien, debo poder..."

    if retroalimentacion:

        narrador "Está bien que te preocupes por [pareja.nombre], pero ¿por 
            qué lo ves como una obligación?"
    else:

        $ listaEstereotipo.append("chapultepec_encargada_sentir_pareja")
    
    return


label chapultepec_ser_romantico:

    scene expression "emocion_enojo_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "¡Ah, el regalo de [pareja.apodo]! lo olvidé. Va a pensar 
        que estoy enojado con ella..."

    if retroalimentacion:

        narrador "A cualquiera se le puede olvidar algo, ¿O crees que 
            [pareja.nombre] se enojará porque espera que siempre le des regalos?"
    else:

        $ listaEstereotipo.append("chapultepec_ser_romantico")
    
    return


label chapultepec_ocultar_frustracion:

    scene expression "emocion_tristeza_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    narrador "[jugador.nombre] empieza a sentir frustración y ganas de llorar. 
        Sin embargo, antes de que lo invadan estos 
        sentimientos, se pellizca con fuerza."
    scene expression "emocion_enojo_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "No, ya no soy un niño, puedo con esto."
    jugador.personaje "Despierta cabrón, eres fuerte."

    if retroalimentacion:

        narrador "¿La mejor forma de tratar tus sentimientos es autolesionandote? 
            Además, ¿hay algo malo en querer llorar?"
    else:

        $ listaEstereotipo.append("chapultepec_ocultar_frustracion")
    
    return


label chapultepec_guardar_emocion_soledad:

    scene expression "emocion_enojo_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "Y que la gente me vea, sobre todo [pareja.apodo], ¿qué 
        van a pensar de mí?"

    if retroalimentacion:

        narrador "¿Te preocupa más que los demás vean tus sentimientos en vez de 
            entenderlos?"
    else:

        $ listaEstereotipo.append("chapultepec_guardar_emocion_soledad")
    
    return


label chapultepec_preocupacion_pareja:
    
    scene expression "emocion_tristeza_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "...Perdón, es que me preocupa que no te haga sentir bien."

    if retroalimentacion:

        narrador "Está bien reconocer tus errores, pero ¿fue tu culpa o crees 
            estar encargada de hacer sentir bien a [pareja.nombre]?"
    else:

        $ listaEstereotipo.append("chapultepec_preocupacion_pareja")
    
    return


label chapultepec_ocultar_emocion:
    
    scene expression "emocion_seriedad_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Yo ando normal, no tengo nada."

    if retroalimentacion:

        narrador "Puede ser cierto, pero la respuesta fue a la defensiva, ¿puede 
            ser que cree tener que ocultar sus emociones?"
    else:

        $ listaEstereotipo.append("chapultepec_ocultar_emocion")
    
    return


label chapultepec_culpar_otro:
    
    scene expression "emocion_seriedad_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Es que yo quiero estar bien, o sea si te acuerdas yo solo 
        te estaba escuchando, pero pues empezaste a echarme bronca por alguna 
        razón..."

    if retroalimentacion:

        $ palabraGenero = "ella" if jugador.nombre == novio.name else "él"
        narrador "[pareja.nombre] te hizo {atl=rotate_text}gaslighting {/atl} 
            (manipular para sembrar la duda) y {atl=rotate_text}culpabilizó {/atl} 
            por la discusión, cuando [palabraGenero] fue 
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

        $ listaEstereotipo.append("chapultepec_pedir_foco")
    
    return 



label chapultepec_burlar_emociones:
    
    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Aunque luego no aguantas cuando te respondo y andas de 
        frágil..."

    if retroalimentacion:

        narrador "[pareja.nombre] te intentó {atl=rotate_text}humillar {/atl} por mostrar tus 
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

        narrador "Decidiste {atl=rotate_text}celar {/atl} a 
            [pareja.nombre] culpando a sus amistades, sin dejar que 
            [pareja.nombre] se explicara."
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

        $ listaEstereotipo.append("chapultepec_provocacion")
    
    return


label chapultepec_broma_diurex:
    
    scene expression "emocion_felicidad_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    $ palabraGenero = "tontito" if jugador.nombre == novio.name else "tontita"
    pareja.personaje "Si, yo también amor, pero procura ya no hostigar tanto 
        ¿eh?, o voy a tenerte que poner un diurex en la boca [palabraGenero]."

    if retroalimentacion:

        narrador "[pareja.nombre] se {atl=rotate_text}burló {/atl} de tu preocupación 
            demeritandote y queriendo que te callaras."
    else:

        $ listaViolenciaPareja.append("chapultepec_broma_diurex")
    
    return


label chapultepec_aceptar_broma:
    
    call chapultepec_broma_diurex from _call_chapultepec_broma_diurex
    scene expression "emocion_tristeza_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "(risa nerviosa) Haha si..."

    if retroalimentacion:

        narrador "[pareja.nombre] te {atl=rotate_text}humilló {/atl} y decidiste seguirle la 
            corriente."
    else:

        $ listaPresion.append("chapultepec_aceptar_broma")
    
    return


label chapultepec_reclamar_toxicidad:
    
    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    $ palabraGenero = "hostigoso" if jugador.nombre == novio.name else "hostigosa"
    pareja.personaje "Acabamos de llegar y sigues chingando con lo mismo... 
        ¡Por eso te digo [palabraGenero]!"

    if retroalimentacion:

        narrador "[pareja.nombre] te intentó {atl=rotate_text}humillar {/atl} por querer irte, 
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

        narrador "[pareja.nombre] te {atl=rotate_text}culpabilizó {/atl} de crear peleas por 
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

        $ listaEstereotipo.append("chapultepec_cambiar_tema")
    
    return


label chapultepec_olvidar_preocupacion:
    
    scene expression "emocion_seriedad_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "Ya olvidé mi preocupación, era una tontería."

    if retroalimentacion:

        narrador "Buscaste cambiar el tema ante el enojo de [pareja.nombre] y 
            poner su bienestar primero."
    else:

        $ listaPresion.append("chapultepec_olvidar_preocupacion")
    
    return


label chapultepec_culpa_imprudente:
    
    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Es tu culpa, si no estuvieras castrando, no me hubieras 
        hecho enojar. Eres bien pinche imprudente."

    if retroalimentacion:

        narrador "[pareja.nombre] te {atl=rotate_text}culpabilizó {/atl} de hacerla enojar y 
            te {atl=rotate_text}insultó {/atl}."
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

        $ listaEstereotipo.append("chapultepec_evitar_interrogar")
    
    return


label chapultepec_reclamar_estupidez:
    
    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Bueno, vámonos ahorita. Y no más preguntas estúpidas, 
        quiero que se me pase el enojo."

    if retroalimentacion:

        narrador "[pareja.nombre] te intentó {atl=rotate_text}humillar {/atl} por tus preguntas, 
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

        narrador "Puede que te hayas enojado, ¿pero por qué 
            piensa [pareja.nombre] que lo haces \"a  la primera\"? ¿Y que así 
            son todas las mujeres?"
    else:

        $ listaEstereotipo.append("chapultepec_comparar_mujeres")
    
    return


label chapultepec_enviar_mensaje:
    
    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Ash pues espero, haber si con un mensaje arreglas esto ¿eh?"

    if retroalimentacion:

        narrador "¿Pensará que tú debes solucionar las peleas? ¿Es tu deber 
            siempre tomar la iniciativa?"
    else:

        $ listaEstereotipo.append("chapultepec_enviar_mensaje")
    
    return


label chapultepec_repetir_retirada:
    
    scene expression "emocion_enojo_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "Que ya te dije que me voy. Mándame mensaje o lo que sea."

    if retroalimentacion:

        narrador "Decidiste {atl=rotate_text}ignorar {/atl} a [pareja.nombre] 
            cuando se empezaba a abrir contigo y cortar la comunicación."
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
        $ listaMito.append("chapultepec_tomar_culpa")
    
    return


label chapultepec_quitarse_culpa:
    
    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "(suspiro) Pero eso no depende de mí ¿ok? Si me inventas 
        cosas, me tengo que defender."

    if retroalimentacion:

        narrador "[pareja.nombre] te hizo {atl=rotate_text}gaslighting {/atl} y {atl=rotate_text}culpabilizó {/atl} 
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

        narrador "¿De verdad le interesa contarle sobre su semana o es porque 
            cree estar encargada de llevar la conversación?"
    else:

        $ listaEstereotipo.append("chapultepec_preguntar_semana")
    
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

        $ listaEstereotipo.append("chapultepec_comprar_helado")
    
    return


label chapultepec_reclamar_salida:
    
    scene expression "emocion_enojo_[jugador.nombre]" at Transform(
        matrixcolor=filtro())
    jugador.personaje "¿Sabes qué? Ya echaste a perder la salida, mejor ya me 
        voy. A ver quién se preocupa por tí."

    if retroalimentacion:

        narrador "Decidiste {atl=rotate_text}culpabilizar {/atl} a [pareja.nombre] y cortar la 
            comunicación. Además de intentar {atl=rotate_text}humillar {/atl} por no aceptar tus 
            preocupaciones."
    else:

        $ listaViolenciaJugador.append("chapultepec_reclamar_salida")
        $ listaMito.append("chapultepec_reclamar_salida")
    
    return


label chapultepec_pretexto_amigues:
    
    scene expression "emocion_enojo_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Pues vete con tus \"amigues\", porque seguro querías un 
        pretexto para eso, ¿verdad?"

    if retroalimentacion:

        narrador "[pareja.nombre] te {atl=rotate_text}celó {/atl} por tus amistades, justificando 
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

        narrador "[pareja.nombre] te {atl=rotate_text}culpabilizó {/atl} de la 
            discusión y lo redujo a un \"drama\". ¿Su silencio de verdad sería 
            la mejor solución?"
    else:

        $ listaViolenciaPareja.append("chapultepec_reclamar_drama")
    
    return


label chapultepec_condicionar_regalo:
    
    scene expression "emocion_seriedad_[pareja.nombre]" at Transform(
        matrixcolor=filtro())
    pareja.personaje "Entonces... ¿Pasamos página y te la doy?"

    if retroalimentacion:

        $ palabraGenero = "hermano" if jugador.nombre == novio.name else "hermana"
        narrador "[pareja.nombre] te intentó {atl=rotate_text}chantajear {/atl} para hacer pasar 
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
        show tarjeta_rota:
                        yalign .4
                        xalign .5        
        narrador "[pareja.nombre] te {atl=rotate_text}humilló {/atl} con su insulto y 
            {atl=rotate_text}destruyó {/atl} el regalo de su [palabraGenero] por no caer en su 
            chantaje."
        hide tarjeta_rota
    else:

        $ listaViolenciaPareja.append("chapultepec_romper_tarjeta")
    
    return


label chapultepec_aceptar_chantaje:
    
    show tarjeta_intacta:
        yalign .4
        xalign .5
    narrador "¿Y recuerdas esa tarjeta para streaming de música? Era un regalo 
        para tí, pero la aceptaste a través de un {atl=rotate_text}chantaje {/atl}."
    hide tarjeta_intacta

    return