label prologo_personaje:

    $ save_name = _("Primera capa")
    show capa_1 with fade
    pause

    $ retroalimentacion = False
    $ listaEstereotipo = []
    
    scene chapultepec_fondo with fade
    narrador "Un domingo por la tarde, [jugador.nombre] y [pareja.nombre] 
        decidieron salir a una cita."
    
    if jugador.nombre == novia.name:
        
        call prologo_novia
    else:

        call prologo_novio
    
    jump retroalimentacion_estereotipo_prologo


label prologo_novia:

    narrador "[jugador.nombre] está en Chapultepec... pero todavía no está en el 
        punto de reunión con [pareja.nombre]."
    scene expression "emocion_seriedad_[jugador.nombre]"
    jugador.personaje "Otra vez me equivoqué de parada... hasta parezco nueva, 
        pero ahorita me apuro."
    jugador.personaje "Ya ví que [pareja.apodo] me envió un mensaje, ¿le contesto?"
    
    menu:

        "Ya estoy cerca...":

            jugador.personaje "Puede esperar tantito, ya ahorita lo veo y me 
            lo puede platicar."
        "¿Y si es algo importante?":

            jugador.personaje "Pero ¿y si le pasó algo? Mejor checo ahorita."

            $ reiniciar_celular()
            show screen phone_ui
            $ switch_channel_view("pareja_dm")
            $ mensajeAleatorio = random.choice(LISTA_MENSAJE_ALEATORIO)
            $ send_phone_message(pareja.nombre, mensajeAleatorio, "pareja_dm", 3)
            
            if LISTA_MENSAJE_ALEATORIO.index(mensajeAleatorio) == 0:

                jugador.personaje "Hahaha, casi casi buscaba mi coquita para 
                    el susto."
            elif LISTA_MENSAJE_ALEATORIO.index(mensajeAleatorio) == 1:

                jugador.personaje "Aay que lindo, pero aún así no lo haré esperar 
                    mucho, estoy cerca... creo."
            else:

                jugador.personaje "Hehe anda nerviosito, pero entonces no le 
                    digo nada, capaz que llego y él tampoco está por dar esa vuelta."

            hide screen phone_ui
    
    narrador "El día está soleado y [jugador.nombre] empieza a sentir el calor a 
        comparación de cuando estaba en Cuajimalpa."
    jugador.personaje "Diablos... por andar organizando cosas con mi equipo ya 
        no chequé el clima acá en la ciudad..."
    scene expression "emocion_tristeza_[jugador.nombre]"
    jugador.personaje "Que con este solecito y las botitas que me traje, me van 
        a quedar los pies bien sudados."
    jugador.personaje "Ash ¿por qué no me traje mis tenis? Así ando más liviana."
    scene expression "emocion_seriedad_[jugador.nombre]"
    jugador.personaje "Aaah si cierto, que me las regaló mi [pareja.apodo] y 
        tiene un ratote que no las uso..."
    call chapultepec_ocultar_incomodidad from _call_chapultepec_ocultar_incomodidad
    scene expression "emocion_felicidad_[jugador.nombre]"
    jugador.personaje "Así que uff, respira y enderezate..."
    narrador "En el camino [jugador.nombre] ve que venden flores."
    jugador.personaje "Hmm unas flores... ¿y si le compro una a [pareja.apodo]?"
    call chapultepec_miedo_estereotipo from _call_chapultepec_miedo_estereotipo
    jugador.personaje "Si mejor no, me van a ver raro."
    call chapultepec_merecer_enojo from _call_chapultepec_merecer_enojo
    scene expression "emocion_seriedad_[jugador.nombre]"
    jugador.personaje "Ya debo de dejar de ser rara... sólo debo concentrarme en 
        encontrarlo."
    jugador.personaje "Y... ¿ese es [pareja.nombre]? Se ve un poco preocupado..."
    narrador "[jugador.nombre] ve que [pareja.nombre] la saluda y ella empieza a 
        caminar hacia él."
    call chapultepec_encargada_sentir_pareja from _call_chapultepec_encargada_sentir_pareja
    return


label prologo_novio:

    narrador "Carlos llegó primero a Chapultepec."
    scene expression "emocion_felicidad_[jugador.nombre]"
    jugador.personaje "Le voy a enviar un mensaje de que ya estoy aquí, espero 
        no tarde mucho."

    menu:

        "Mensaje juguetón":

            $ reiniciar_celular()
            show screen phone_ui
            $ switch_channel_view("pareja_dm")
            $ send_phone_message(
                phone_config["phone_player_name"], 
                LISTA_MENSAJE_ALEATORIO[0], "pareja_dm", 3)
        "Mensaje comprensivo":

            $ reiniciar_celular()
            show screen phone_ui
            $ switch_channel_view("pareja_dm")
            $ send_phone_message(
                phone_config["phone_player_name"], 
                LISTA_MENSAJE_ALEATORIO[1], "pareja_dm", 3)
        "Mensaje con urgencia":

            $ reiniciar_celular()
            show screen phone_ui
            $ switch_channel_view("pareja_dm")
            $ send_phone_message(
                phone_config["phone_player_name"], 
                LISTA_MENSAJE_ALEATORIO[2], "pareja_dm", 3)

    hide screen phone_ui
    narrador "Después de enviar el mensaje, [jugador.nombre] se pone a revisar 
        sus notas."

    $ reiniciar_celular()
    show screen phone_ui
    $ switch_channel_view("jugador_dm")
    $ send_phone_message(
        jugador.nombre, 
        (
            "Mañana entrega final\n\nComprar pavos Fortnite," +
            "\n\n(IMPORTANTE) regalo para [pareja.apodo]"), "jugador_dm", 3)

    jugador.personaje "El proyecto... Otra noche sin dormir para que el profe ni 
        lo lea.."
    jugador.personaje "Gastos y más gastos... ¿Y si le vuelvo a pedir prestado 
        a mi pa'?"
    jugador.personaje "Pero todavía le debo del regalo pasado de [pareja.apodo]..."
    hide screen phone_ui
    call chapultepec_ser_romantico from _call_chapultepec_ser_romantico
    scene expression "emocion_felicidad_[jugador.nombre]"
    jugador.personaje "Pero mi hermano me había dado dinero ¿no?, voy a..."
    scene expression "emocion_seriedad_[jugador.nombre]"
    jugador.personaje "..."
    jugador.personaje "También se me olvidó en la mesa."
    jugador.personaje "..."
    scene expression "emocion_enojo_[jugador.nombre]"
    jugador.personaje "Como siempre, ¡soy un pinche desastre!"
    call chapultepec_ocultar_frustracion from _call_chapultepec_ocultar_frustracion
    call chapultepec_guardar_emocion_soledad from _call_chapultepec_guardar_emocion_soledad
    scene expression "emocion_tristeza_[jugador.nombre]"
    jugador.personaje "Además se ve agitada, puede que sea por la caminata, 
        pero tal vez sea otra cosa... La voy a distraer y ver si se le pasa."
    scene expression "emocion_seriedad_[jugador.nombre]"
    narrador "[jugador.nombre] sumerge sus sentimientos y ve que [pareja.nombre] 
        ya está por llegar."
    scene expression "emocion_felicidad_[jugador.nombre]"
    jugador.personaje "Erm, aquí, ¡Aquí estoy Fer!"
    return


label retroalimentacion_estereotipo_prologo:

    scene fondo_inicio
    narrador "El amor no sólo debería ser hacia la pareja, ¿no lo crees?"    
    $ retroalimentacion = True 

    if listaEstereotipo:

        menu:

            narrador "Y algunos diálogos reproducen estereotipos sobre los roles 
                de género, ¿Lo notaste?"
        
            "Sí":
            
                narrador "¡Muy bien!, vamos a comprobarlo:"
            "No":
                
                narrador "No te preocupes, veamos:"
        
        $ i = 0
        while i < len(listaEstereotipo):
            $ renpy.call(listaEstereotipo[i])
            $ i += 1
            
        scene chapultepec_fondo
        narrador "Es distinto conocer los estereotipos a ver cómo dictan 
            nuestras acciones."
        narrador "Si estos límites nos hacen daño, ¿por qué los seguimos repitiendo?"

    $ forzarAutosave()

    call instrucciones_recursos
    jump opcion_prologo_regresar_menu


label opcion_prologo_regresar_menu:

    scene black

    menu:

        narrador "Haz atravesado la primera capa de Latencia ¿Quieres continuar? 
            La siguiente capa es la primera con 
            {gradient2=2-#93B2FD-#F792D5-20-#F792D5-#93B2FD-20}[pareja.nombre]
            {/gradient2}."
        "Si":
            
            call instrucciones_cargar
            jump cita_chapultepec
        "Más tarde":

            narrador "¡Entendido! Espero que regreses pronto para atravesar más 
                capas de Latencia."
            call instrucciones_cargar
            $ renpy.full_restart() 


label instrucciones_cargar:

    if _preferences.self_voicing:
        
        narrador "Puedes volver a jugar esta capa desde el menú de Cargar 
            dentro de Opciones (segundo botón superior izquierda)."
    else:

        narrador "Puedes volver a jugar esta capa desde el menú 
            de {image=boton_cargar} dentro de 
            Opciones {image=boton_opciones_quick}."
    
    return


label instrucciones_recursos:
      
    $ info_descriptiva = ""  

    if _preferences.self_voicing:
        
        $ info_descriptiva = "(tercer botón superior)"

    narrador "¿Te quedó alguna duda y no sabes con quién hablarlo? Checa 
        los contactos en el menú de 
        Recursos [info_descriptiva]{image=boton_recursos}."
    return