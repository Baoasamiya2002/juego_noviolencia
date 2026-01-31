init python:

    def aclararColorFondo(cont, valor_incremento):
        
        global color_var

        rgb_var = cont * valor_incremento
        color_var = Color((rgb_var, rgb_var, rgb_var, 121))

        
label telefono_amigue:

    $ save_name = _("Cuarta capa")
    play musica_ambiental musica_capa_4 loop fadein 1.0 volume 1.0
    show capa_4 with fade
    show screen accion_cronometrada
    pause
    hide screen accion_cronometrada
    
    $ retroalimentacion = False
    $ listaEstereotipo = []
    $ listaViolenciaJugador = []
    $ listaViolenciaPareja = []
    $ listaPresion = []
    $ palabraGenero = ""

    scene fondo_inicio at Transform(matrixcolor=TintMatrix("#505050"))

    $ reiniciar_celular()
    $ switch_channel_view("amigue_dm")

    show screen phone_ui

    if jugador.apodo == APODO_NOVIA:

        $ send_phone_message(viejoAmigue.nombre, "Hola amigx! Me ayudas con un like para mi hermanito? <emoji_rezando> Es para el concurso \"El futuro ingeniero\" de su kinder. Muchas gracias! <emoji_feliz> https://www.feizbook.com/share/17j8FUnxfu/", "amigue_dm", 3)
    else:
        
        $ send_phone_message(viejoAmigue.nombre, "Hola amigx! Me ayudas con un like para mi hermanita? <emoji_rezando> Es para el concurso \"La futura enfermera\" de su kinder. Muchas gracias! <emoji_feliz> https://www.feizbook.com/share/17j8FUnxfu/", "amigue_dm", 3)
    
    $ palabraGenero = "hermana" if jugador.nombre == novio.name else "hermano"
    $ send_phone_message(phone_config["phone_player_name"], "Si! con gusto apoyo a tu [palabraGenero] <emoji_feliz>", "amigue_dm", 3)
    
    if jugador.apodo == APODO_NOVIA:

        $ send_phone_message(phone_config["phone_player_name"], "Un poco raro lo de futuro ingeniero<emoji_risa_nerviosa>, no pudo ser de cualquier carrera?", "amigue_dm", 3)
    else:

        $ send_phone_message(phone_config["phone_player_name"], "Un poco raro lo de futura enfermera<emoji_risa_nerviosa>, no pudo ser de cualquier carrera?", "amigue_dm", 3)
    
    $ palabraGenero = "la" if jugador.nombre == novio.name else "lo"
    $ send_phone_message(phone_config["phone_player_name"], "Y ya creció un buen! <emoji_grito><emoji_grito> Recuerdo cuando [palabraGenero] cargué...", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "weeey! tiempo de no hablar. Sii ya está bien grande", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "cómo estás? ya tampoco te he visto jugar básquet en las canchas", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "<emoji_pensativo>", "amigue_dm", 3)
    $ palabraGenero = "amiga" if jugador.nombre == novio.name else "amigo"
    $ send_phone_message(phone_config["phone_player_name"], "Si... [pareja.apodo] tuvo problemitas con un [palabraGenero] que jugaba y pues ya no tengo ganas de básquet...", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "no mames, pero si a ti te encantaba jugar!<emoji_indiferente>", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "en la prepa casi todos los días jugabas", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Pues la gente cambia <emoji_risa_nerviosa>heh", "amigue_dm", 3)
    $ palabraGenero = "la" if jugador.nombre == novio.name else "el"
    $ send_phone_message(viejoAmigue.nombre, "no pues si... y entonces sigues con [palabraGenero] [pareja.nombre]?", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "tampoco se me ha aparecido en los pasillos<emoji_pensativo>", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Haha ni que fuera un fantasma! haha. Es que se fue de movilidad a...", "amigue_dm", 3)

    $ send_phone_message("", "{color=#ffffff}¿Tu decisión?{/color}", "amigue_dm", 1, do_pause=False)
    $ present_phone_choices([
        (
            "Italia", 
            Call("movilidad_Italia")), 
        (
            "Perú",
            Call("movilidad_Peru")),
        (
            "China",
            Call("movilidad_China"))], "amigue_dm")
    
    $ send_phone_message(viejoAmigue.nombre, "<emoji_risa>", "amigue_dm", 3)
    $ palabraGenero = "listo" if jugador.nombre == novio.name else "lista"
    $ send_phone_message(phone_config["phone_player_name"], "Pero ya mero regresa y estoy [palabraGenero] para su bienvenida<emoji_guinio><emoji_guinio>", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "uuy, no me des detalles jajaj<emoji_risa> Y qué chido que tiene varo para ir allá jaj", "amigue_dm", 3)
    $ palabraGenero = "solo" if jugador.nombre == novio.name else "sola"
    $ send_phone_message(viejoAmigue.nombre, "y en este tiempo de \"solteria\", hiciste algo [palabraGenero] o con tus compas?", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "a mí me gustaría, pero vivo bien lejos y le ayudo a mi mamá en su jale...<emoji_risa_nerviosa>", "amigue_dm", 3)
    $ palabraGenero = "ocupado" if jugador.nombre == novio.name else "ocupada"
    $ send_phone_message(phone_config["phone_player_name"], "Ay tu tranqui! si me acuerdo que estabas muy [palabraGenero], me saludas a tu mami!", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Y la verdad<emoji_risa_nerviosa> no sabría con quién salir...", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "poooor?<emoji_pensativo> si tienes un buen de seguidores en insta", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Mucho dizque like, pero ninguno aprobaba mi relación con mi [pareja.apodo]<emoji_voltea_ojos>", "amigue_dm", 3)
    
    if "telefono_eliminar_foto" in listaMito:
        
        $ send_phone_message(phone_config["phone_player_name"], "Cuando pedí que borraran fotos conmigo por consejo de [pareja.apodo], mi familia y amigos reaccionaron súper mal", "amigue_dm", 3)
    elif "telefono_pretexto" in listaMito:

        $ send_phone_message(phone_config["phone_player_name"], "Me reprochaban mis mentirillas a [pareja.apodo] para que pudieran tener fotos conmigo", "amigue_dm", 3)
    
    $ palabraGenero = "estresarla" if jugador.nombre == novio.name else "estresarlo"
    $ send_phone_message(phone_config["phone_player_name"], "Así que decidí subir fotos sólo con [pareja.apodo] para no [palabraGenero]", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "<emoji_grito>", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Pues si, los demás no entendían que acciones como esa...", "amigue_dm", 3)

    $ send_phone_message("", "{color=#ffffff}¿Tu decisión?{/color}", "amigue_dm", 1, do_pause=False)
    $ present_phone_choices([
        (
            "Nos mantienen unidos", 
            Call("media_naranja_telefono")), 
        (
            "Pasan en todas las relaciones",
            Call("emparejamiento_telefono")),
        (
            "Son por amor",
            Call("amor_todo_puede_telefono"))], "amigue_dm")
    
    $ send_phone_message(viejoAmigue.nombre, "hmm... entiendo que quieras hacer cosas por tu pareja...", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "<emoji_corazon_fuego>", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "pero lo que dices suena a que justificas comportamientos tóxicos...", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Ah <emoji_indiferente>, tal vez no me expliqué bien, pero te juro que estamos bien", "amigue_dm", 3)
    
    if jugador.apodo == APODO_NOVIA:

        $ send_phone_message(phone_config["phone_player_name"], "De hecho cuando podemos, me invita al cine o a Chapu", "amigue_dm", 3)
    else:
        $ send_phone_message(phone_config["phone_player_name"], "De hecho cuando podemos, la invito al cine o a Chapu", "amigue_dm", 3)
    
    $ send_phone_message(viejoAmigue.nombre, "ah si, recuerdo que me contaste una vez, ya tiene un bueeen jaja", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Si verdad? haha, extrañaba hablar contigo<emoji_rogando>", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "<emoji_feliz><emoji_feliz>", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Y recordando, una vez en Chapu estuvo escuchando mis tontas preocupaciones<emoji_corazon>", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Aunque también ese mismo día me dijo absorbente y me gritó, pero fue porque..", "amigue_dm", 3)

    $ send_phone_message("", "{color=#ffffff}¿Tu decisión?{/color}", "amigue_dm", 1, do_pause=False)
    $ present_phone_choices([
        (
            "Me estaba probando", 
            Call("amor_todo_puede_chapultepec")), 
        (
            "Estábamos empezando la relación",
            Call("emparejamiento_chapultepec")),
        (
            "Apenas entendía que somos uno",
            Call("media_naranja_chapultepec"))], "amigue_dm")
    
    $ send_phone_message(viejoAmigue.nombre, "mmm...<emoji_medio_triste> me parece que hay un poco de noviazgo en tu relación violenta...<emoji_risa_nerviosa>", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "??? haha creo que exageras", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Sí peleamos a veces, ni que fuéramos perfectos, es pasajero", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "si... pero por lo que dices, tienen muchas peleas y tú lo ves como normal<emoji_pensativo>", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "Y probablemente sigan teniendo peleas y cada vez más fuertes...", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Pues... <emoji_medio_triste> a veces", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "la vdd creo que deben buscar un cambio", "amigue_dm", 3)
    $ palabraGenero = "experto" if jugador.nombre == novio.name else "experta"
    $ send_phone_message(phone_config["phone_player_name"], "Ay y cuándo te volviste [palabraGenero] en relaciones de pareja o qué?", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "yo?? nunca! si hasta me engañaron jaja <emoji_risa_nerviosa>. Pero ya en serio, me preocupo por ti", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "y he visto que luego se acostumbran a estar con gente bien mierda", "amigue_dm", 3)    
    $ send_phone_message(phone_config["phone_player_name"], "<emoji_risa_nerviosa>", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "al chile no te quiero incomodar, pero cuando algo no me late, te lo tengo que decir", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Ay nono, tú tranqui, de verdad estamos bien...", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "mira, como dices, [palabraGenero] no soy, pero neta que deberías pensar en platicárselo a alguien más", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "en la UAM hay atención psicológica o hasta puedes buscar por fuera", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "y gracias por la confianza <emoji_rezando>, pero también hablalo con otra persona de confianza va?", "amigue_dm", 3)
    $ palabraGenero = "seguro" if jugador.nombre == novio.name else "segura"
    $ send_phone_message(phone_config["phone_player_name"], "Este... gracias por preocuparte, sigo sin estar [palabraGenero] de que haya algo mal", "amigue_dm", 3)
    
    $ send_phone_message("", "{color=#ffffff}¿Tu decisión?{/color}", "amigue_dm", 1, do_pause=False)
    $ present_phone_choices([
        (
            "Le diré a [pareja.apodo] que tomemos atención psicológica", 
            Call("tomar_atencion_en_pareja")), 
        (
            "Tomaré por mi cuenta atención psicológica ",
            Call("tomar_atencion_individual")),
        (
            "No te preocupes, estamos bien",
            Call("no_tomar_atencion"))], "amigue_dm")
    
    jump palabras_finales


label movilidad_Italia:

    $ send_phone_message(phone_config["phone_player_name"], "Italia Italia, se me estaba olvidando el nombre", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Fue a visitar a Mario y su hermano. Ah no que esos son japoneses hahah", "amigue_dm", 3)
    
    return


label movilidad_Peru:

    $ send_phone_message(phone_config["phone_player_name"], "Perú Perú, se me estaba olvidando el nombre", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Es que Perú es clave haha y fue a visitar a los capibaras", "amigue_dm", 3)
    return


label movilidad_China:

    $ send_phone_message(phone_config["phone_player_name"], "China China, se me estaba olvidando el nombre", "amigue_dm", 3)
    $ palabraGenero = "hecha" if jugador.nombre == novio.name else "hecho"
    $ send_phone_message(phone_config["phone_player_name"], "Seguro fue a ver si no estaba [palabraGenero] allá haha", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Con eso de que le gusta mucho el pollo a la naranja hah", "amigue_dm", 3)
    return


label media_naranja_telefono:

    $ send_phone_message(phone_config["phone_player_name"], "Muestran cómo nos importa la relación y estamos en sintonía", "amigue_dm", 3)
    $ palabraGenero = "ella" if jugador.nombre == novio.name else "él"
    $ send_phone_message(phone_config["phone_player_name"], "Porque ni yo ni [palabraGenero] me pide algo<emoji_feliz>, ya sabémos lo que el otro necesita", "amigue_dm", 3)
    
    if "telefono_eliminar_foto" in listaMito:
        $ send_phone_message(viejoAmigue.nombre, "lit te pidió que los demás eliminaran fotos contigo...", "amigue_dm", 3)
    
    return


label emparejamiento_telefono:

    $ send_phone_message(phone_config["phone_player_name"], "Son parte de cualquier relación! Es normal", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Y varios criticones ni tenían pareja <emoji_groserias>, si no sabes no hables, verdad?", "amigue_dm", 3)
    return


label amor_todo_puede_telefono:

    $ send_phone_message(phone_config["phone_player_name"], "Son muestras de que nos amamos<emoji_corazon>", "amigue_dm", 3)
    $ palabraGenero = "insegura" if jugador.nombre == novio.name else "inseguro"
    $ send_phone_message(phone_config["phone_player_name"], "Tal vez [pareja.apodo] es un poco [palabraGenero], pero lo superamos", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "oh ok, supongo que lo superaron hablando al respecto no?", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Eso no fue necesario, lo demostramos con gestos románticos<emoji_guinio><emoji_guinio>", "amigue_dm", 3)
    return


label amor_todo_puede_chapultepec:

    $ palabraGenero = "la" if jugador.nombre == novio.name else "lo"
    $ send_phone_message(phone_config["phone_player_name"], "Era una prueba, quería ver si [palabraGenero] amaba de verdad", "amigue_dm", 3)
    
    if "chapultepec_insistir_hablar" in listaMito:
        
        $ send_phone_message(phone_config["phone_player_name"], "Sé que en el amor hay momentos difíciles, así que continúe con mi empatía como si nada<emoji_corazon>", "amigue_dm", 3)
    elif "chapultepec_tomar_culpa" in listaMito:
        
        $ send_phone_message(phone_config["phone_player_name"], "Cambié el tema y después seguimos como si nada. Cuando se quiere de verdad, es así de simple<emoji_corazon>", "amigue_dm", 3)
    elif "chapultepec_reclamar_salida" in listaMito:
        
        $ send_phone_message(phone_config["phone_player_name"], "Así que [palabraGenero] ignoré y no caí en la provocación. Con el amor todo se supera fácilmente<emoji_corazon>", "amigue_dm", 3)
    
    return


label emparejamiento_chapultepec:

    $ palabraGenero = "ella" if jugador.nombre == novio.name else "él"
    $ send_phone_message(phone_config["phone_player_name"], "El noviazgo era algo nuevo para [palabraGenero], pero con el tiempo entendió su papel", "amigue_dm", 3)
    
    if "chapultepec_insistir_hablar" in listaMito:
        
        $ send_phone_message(phone_config["phone_player_name"], "Mi interés es mi inversión en la relación, sólo se tuvo que acostumbrar a estar para mí", "amigue_dm", 3)
    elif "chapultepec_tomar_culpa" in listaMito:
        
        $ send_phone_message(phone_config["phone_player_name"], "Así que lo dejé pasar, después de todo esto tiempo, no iba a rendirme en la relación", "amigue_dm", 3)
    elif "chapultepec_reclamar_salida" in listaMito:
        
        $ palabraGenero = "sola" if jugador.nombre == novio.name else "solo"
        $ send_phone_message(phone_config["phone_player_name"], "Le hice sentir lo que es estar [palabraGenero] otra vez y se arrepintió, era obvio", "amigue_dm", 3)
    
    return


label media_naranja_chapultepec:

    $ send_phone_message(phone_config["phone_player_name"], "Todavía no se daba cuenta que eramos uno para el otro", "amigue_dm", 3)
    
    if "chapultepec_insistir_hablar" in listaMito:
        
        $ send_phone_message(phone_config["phone_player_name"], "Y yo sólo estaba pendiente de que estuvieramos sintiendo lo mismo, debíamos de hacerlo<emoji_feliz>", "amigue_dm", 3)
    elif "chapultepec_tomar_culpa" in listaMito:
        
        $ send_phone_message(phone_config["phone_player_name"], "Pero le di por su lado y poco a poco entendió que estamos destinados<emoji_feliz>", "amigue_dm", 3)
    elif "chapultepec_reclamar_salida" in listaMito:
        
        $ palabraGenero = "solita" if jugador.nombre == novio.name else "solito"
        $ send_phone_message(phone_config["phone_player_name"], "Entonces no le hablé por un tiempo y [palabraGenero] vino a mi, sabía que me necesitaba<emoji_feliz>", "amigue_dm", 3)
    return


label tomar_atencion_en_pareja:

    $ send_phone_message(phone_config["phone_player_name"], "Lo hablaré con [pareja.apodo], porque esto es algo de los dos no?", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Veré si los dos podemos tomar atención psicológica", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Creo que al final, vale la pena intentar y ver qué tal", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "ese es el espíritu! pruebenlo y cualquier cosa, me puedes enviar un mensaje o llamar", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "porfa ya no perdamos el contacto<emoji_corazon>", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Noo claro que no! Gracias. Bye", "amigue_dm", 3)
    hide screen phone_ui
    stop musica_ambiental fadeout 1.0
    stop music fadeout 1.0
    jump final_tomar_atencion_en_pareja
    return


label tomar_atencion_individual:

    $ palabraGenero = "solo" if jugador.nombre == novio.name else "sola"
    $ send_phone_message(phone_config["phone_player_name"], "Primero lo haré yo [palabraGenero]. No quiero presionar a [pareja.apodo] a cosas que ni yo entiendo", "amigue_dm", 3)
    $ palabraGenero = "ella" if jugador.nombre == novio.name else "él"
    $ send_phone_message(phone_config["phone_player_name"], "Porque si, muchas veces las cosas no se sienten bien entre nosotros... pero [palabraGenero] ya es parte de mí", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Primero quiero entender qué está pasando y luego veo cómo se lo comento a [palabraGenero], va?", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "ese es el espíritu! intentalo y cualquier cosa, me puedes enviar un mensaje o llamar.", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "porfa ya no perdamos el contacto<emoji_corazon>", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Noo claro que no! Gracias. Bye", "amigue_dm", 3)
    hide screen phone_ui
    stop musica_ambiental fadeout 1.0
    stop music fadeout 1.0
    jump final_tomar_atencion_individual
    return


label no_tomar_atencion:

    $ send_phone_message(phone_config["phone_player_name"], "Por el momento no necesitamos nada, pero gracias por tu preocupación!", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Ya me dí cuenta que tú y yo andamos en distintos lugares haha y no ves las cosas como yo", "amigue_dm", 3)
    $ palabraGenero = "el mismo" if jugador.nombre == novio.name else "la misma"
    $ send_phone_message(phone_config["phone_player_name"], "Cuando [pareja.apodo] regrese, va a querer que sea [palabraGenero] de siempre. No quiero meter ruido en eso ok?", "amigue_dm", 3)
    $ send_phone_message(viejoAmigue.nombre, "disculpa, no te quería ofender ni nada, sólo que algo no me cuadra, mira, hablar con un experto no te hará daño", "amigue_dm", 3)
    $ send_phone_message(phone_config["phone_player_name"], "Tal vez no, pero ahorita no tengo tiempo y creo que me llegó un mensaje de [pareja.apodo]", "amigue_dm", 3)
    $ palabraGenero = "hermana" if jugador.nombre == novio.name else "hermana"
    $ send_phone_message(phone_config["phone_player_name"], "Así que... suerte a tu [palabraGenero] en su concurso. Bye", "amigue_dm", 3)
    narrador "Bloqueaste a [viejoAmigue.nombre]"
    hide screen phone_ui
    stop musica_ambiental fadeout 1.0
    stop music fadeout 1.0
    jump final_no_tomar_atencion
    return


label final_tomar_atencion_en_pareja:
    
    scene black
    nvl clear

    if not persistent.final_primera_opcion:

        $ final_random = random.choice([1, 5])
        $ persistent.final_primera_opcion = LISTA_FINAL_PRIMERA_OPCION[final_random]
    else:

        $ idx = LISTA_FINAL_PRIMERA_OPCION.index(persistent.final_primera_opcion)
        $ siguiente_final = (idx + 1) % len(LISTA_FINAL_PRIMERA_OPCION)
        $ persistent.final_primera_opcion = LISTA_FINAL_PRIMERA_OPCION[siguiente_final]

    $ color_var = Color((0, 0, 0, 121))
    if persistent.final_primera_opcion[0]:

        $ tamanio_final = 4  
    elif (
        (len(persistent.final_primera_opcion) == 4) 
        and not persistent.final_primera_opcion[3]):

        $ tamanio_final = 7
    else:

        $ tamanio_final = 6
    show screen color_fondo_final

    "[jugador.nombre] le dijo a [pareja.nombre] sobre tomar atención psicológica."
    
    $ valor_incremento = 255 / tamanio_final
    $ aclararColorFondo(1, valor_incremento)    
    if persistent.final_primera_opcion[0]:
        
        "[pareja.nombre] aceptó ir."
        $ aclararColorFondo(2, valor_incremento)
        "Los dos identificaron la violencia y buscaron resolver sus problemas 
            más allá de sus suposiciones del otro."

        $ aclararColorFondo(3, valor_incremento)
        if persistent.final_primera_opcion[1]:

            "[jugador.nombre] y [pareja.nombre] siguen siendo novios. Todavía 
                llegan a tener desacuerdos, pero buscan resolverlos con respeto."
        else:

            "Se dieron cuenta de que no eran la mejor persona para el otro 
                y terminaron su relación en buenos términos."
        
        $ aclararColorFondo(4, valor_incremento)
        nvl clear       
        show white
        hide screen color_fondo_final with Fade(0.5, 0, 0.5, color="#FFFFFF")
        show planta_fondo:
            yalign .4
            xalign .27
        show planta_fondo as fondo_pareja:
            yalign .4
            xalign .69

        $ planta_jugador = (
            "planta_florece_dorado" if persistent.desbloqueo 
            else "planta_florece")

        show expression planta_jugador:
            yalign .4
            xalign .27        
            xsize 950
            ysize 900
        show planta_florece as planta_pareja:
            yalign .4
            xalign .69        
            xsize 950
            ysize 900
        narrador "Sus plantas siguen marchitándose."
    else:

        "[pareja.nombre] no aceptó ir."

        $ aclararColorFondo(2, valor_incremento)
        if persistent.final_primera_opcion[1]:

            "[jugador.nombre] se desanimó y tampoco fué."
            $ aclararColorFondo(3, valor_incremento)
            "Pero después de platicar sobre sus problemas, 
                reflexionaron un poco sobre su relación."
            
            $ aclararColorFondo(4, valor_incremento)
            if persistent.final_primera_opcion[2]:

                "[jugador.nombre] y [pareja.nombre] se dieron cuenta de algunas 
                    violencias que estaban ejerciendo e intentaron evitarlas."
                $ aclararColorFondo(5, valor_incremento)
                "[jugador.nombre] y [pareja.nombre] siguen siendo novios. Su 
                    relación mejoró, pero todavía hay violencia normalizada y a 
                    veces ha escalado."
                $ aclararColorFondo(6, valor_incremento)
                nvl clear       
                show white
                hide screen color_fondo_final with Fade(0.5, 0, 0.5, color="#FFFFFF")
                show planta_fondo:
                    yalign .4
                    xalign .5

                $ planta_jugador = (
                    "planta_[jugador.estadoPlanta]_dorado" if persistent.desbloqueo 
                    else "planta_[jugador.estadoPlanta]")

                show expression planta_jugador:
                    yalign .4
                    xalign .5        
                    xsize 950
                    ysize 900
                narrador "La planta que cuidas sanó un poco."
            else:

                "[pareja.nombre] se dió cuenta de algunas violencias que estaba 
                    ejerciendo e intentó evitarlas."
                
                $ aclararColorFondo(5, valor_incremento)
                if persistent.final_primera_opcion[3]:

                    "[jugador.nombre] y [pareja.nombre] siguen siendo novios. 
                        Su relación mejoró, pero todavía hay violencia normalizada 
                        y a veces ha escalado."
                    $ aclararColorFondo(6, valor_incremento)
                    nvl clear       
                    show white
                    hide screen color_fondo_final with Fade(0.5, 0, 0.5, color="#FFFFFF")
                    show planta_fondo:
                        yalign .4
                        xalign .5

                    $ planta_jugador = (
                        "planta_[jugador.estadoPlanta]_dorado" if persistent.desbloqueo 
                        else "planta_[jugador.estadoPlanta]")

                    show expression planta_jugador:
                        yalign .4
                        xalign .5        
                        xsize 950
                        ysize 900
                    narrador "La planta que cuidas sanó un poco."
                else:

                    "Su relación no pudo continuar con los nuevos límites que puso 
                        [jugador.nombre] y terminó su relación. [jugador.nombre] 
                        sigue intentando superar las cicatrices de la relación."
                    $ aclararColorFondo(6, valor_incremento)
                    "Pero ahora ya no están dañando a sus plantas."
                    $ aclararColorFondo(7, valor_incremento)
                    nvl clear       
                    show white
                    hide screen color_fondo_final with Fade(0.5, 0, 0.5, color="#FFFFFF")
                    show planta_fondo:
                        yalign .4
                        xalign .5

                    $ planta_jugador = (
                        "planta_florece_dorado" if persistent.desbloqueo 
                        else "planta_florece")

                    show expression planta_jugador:
                        yalign .4
                        xalign .5        
                        xsize 950
                        ysize 900
                    narrador "La planta que cuidas está floreciendo."

        else:

            "[jugador.nombre] aceptó tomar atención psicológica."
            $ aclararColorFondo(3, valor_incremento)
            "[jugador.nombre] identificó la violencia y buscó resolver sus 
                problemas más allá de sus suposiciones del otro."
            
            $ aclararColorFondo(4, valor_incremento)
            if persistent.final_primera_opcion[2]:

                "[pareja.nombre] se dió cuenta de algunas violencias que estaba 
                    ejerciendo e intentó evitarlas."

                $ aclararColorFondo(5, valor_incremento)
                if persistent.final_primera_opcion[3]:

                    "[jugador.nombre] y [pareja.nombre] siguen siendo novios. 
                        Su relación mejoró, pero todavía hay violencia normalizada 
                        y a veces ha escalado."
                    $ aclararColorFondo(6, valor_incremento)
                    nvl clear       
                    show white
                    hide screen color_fondo_final with Fade(0.5, 0, 0.5, color="#FFFFFF")
                    show planta_fondo:
                        yalign .4
                        xalign .5

                    $ planta_jugador = (
                        "planta_[jugador.estadoPlanta]_dorado" if persistent.desbloqueo 
                        else "planta_[jugador.estadoPlanta]")
                    
                    show expression planta_jugador:
                        yalign .4
                        xalign .5        
                        xsize 950
                        ysize 900
                    narrador "La planta que cuidas sanó un poco."
                else:

                    "Su relación no pudo continuar con los nuevos límites que puso 
                        [jugador.nombre] y terminó su relación. [jugador.nombre] 
                        sigue intentando superar las cicatrices de la relación."
                    $ aclararColorFondo(6, valor_incremento)
                    "Pero ahora ya no están dañando a sus plantas."
                    $ aclararColorFondo(7, valor_incremento)
                    nvl clear       
                    show white
                    hide screen color_fondo_final with Fade(0.5, 0, 0.5, color="#FFFFFF")
                    show planta_fondo:
                        yalign .4
                        xalign .5

                    $ planta_jugador = (
                        "planta_florece_dorado" if persistent.desbloqueo 
                        else "planta_florece")

                    show expression planta_jugador:
                        yalign .4
                        xalign .5        
                        xsize 950
                        ysize 900
                    narrador "La planta que cuidas está floreciendo."
            else:

                "Su relación no pudo continuar con los nuevos límites que puso 
                    [jugador.nombre] y terminó su relación. [jugador.nombre] 
                    sigue intentando superar las cicatrices de la relación."
                $ aclararColorFondo(5, valor_incremento)
                "Pero ahora ya no están dañando a sus plantas."
                $ aclararColorFondo(6, valor_incremento)
                nvl clear       
                show white
                hide screen color_fondo_final with Fade(0.5, 0, 0.5, color="#FFFFFF")
                show planta_fondo:
                    yalign .4
                    xalign .5

                $ planta_jugador = (
                    "planta_florece_dorado" if persistent.desbloqueo 
                    else "planta_florece")

                show expression planta_jugador:
                    yalign .4
                    xalign .5        
                    xsize 950
                    ysize 900
                narrador "La planta que cuidas está floreciendo."
                
    return


label final_tomar_atencion_individual:

    scene black
    nvl clear
    
    $ idx = LISTA_FINAL_SEGUNDA_OPCION.index(persistent.final_segunda_opcion)
    $ siguiente_final = (idx + 1) % len(LISTA_FINAL_SEGUNDA_OPCION)
    $ persistent.final_segunda_opcion = LISTA_FINAL_SEGUNDA_OPCION[siguiente_final]
    
    $ color_var = Color((0, 0, 0, 121))
    if persistent.final_segunda_opcion[0]:

        $ tamanio_final = 5  
    if ((len(persistent.final_segunda_opcion) == 2)
        and persistent.final_segunda_opcion[1]):

        $ tamanio_final = tamanio_final - 1
    else:

        $ tamanio_final = 4
    show screen color_fondo_final
    
    "[jugador.nombre] aceptó tomar atención psicológica."
    $ valor_incremento = 255 / tamanio_final
    $ aclararColorFondo(1, valor_incremento)
    "[jugador.nombre] identificó la violencia y buscó resolver sus problemas 
        más allá de sus suposiciones del otro."

    $ aclararColorFondo(2, valor_incremento)
    if persistent.final_segunda_opcion[0]:

        "[pareja.nombre] se dió cuenta de algunas violencias que estaba 
            ejerciendo e intentó evitarlas."        
        $ aclararColorFondo(3, valor_incremento)
        if persistent.final_segunda_opcion[1]:

            "[jugador.nombre] y [pareja.nombre] siguen siendo novios. Su 
                relación mejoró, pero todavía hay violencia normalizada y a veces 
                ha escalado."
            $ aclararColorFondo(4, valor_incremento)
            nvl clear       
            show white
            hide screen color_fondo_final with Fade(0.5, 0, 0.5, color="#FFFFFF")
            show planta_fondo:
                yalign .4
                xalign .5

            $ planta_jugador = (
                "planta_[jugador.estadoPlanta]_dorado" if persistent.desbloqueo 
                else "planta_[jugador.estadoPlanta]")

            show expression planta_jugador:
                yalign .4
                xalign .5        
                xsize 950
                ysize 900
            narrador "La planta que cuidas sanó un poco."
        else:

            "Su relación no pudo continuar con los nuevos límites que puso 
                [jugador.nombre] y terminó su relación. [jugador.nombre] sigue 
                intentando superar las cicatrices de la relación."
            $ aclararColorFondo(4, valor_incremento)
            "Pero ahora ya no están dañando a sus plantas."
            $ aclararColorFondo(5, valor_incremento)
            nvl clear       
            show white
            hide screen color_fondo_final with Fade(0.5, 0, 0.5, color="#FFFFFF")
            show planta_fondo:
                yalign .4
                xalign .5

            $ planta_jugador = (
                "planta_florece_dorado" if persistent.desbloqueo 
                else "planta_florece")

            show expression planta_jugador:
                yalign .4
                xalign .5        
                xsize 950
                ysize 900
            narrador "La planta que cuidas está floreciendo."
    else:

        "Su relación no pudo continuar con los nuevos límites que puso 
            [jugador.nombre] y terminó su relación. [jugador.nombre] sigue 
            intentando superar las cicatrices de la relación."
        $ aclararColorFondo(3, valor_incremento)
        "Pero ahora ya no están dañando a sus plantas."
        $ aclararColorFondo(4, valor_incremento)
        nvl clear       
        show white
        hide screen color_fondo_final with Fade(0.5, 0, 0.5, color="#FFFFFF")
        show planta_fondo:
            yalign .4
            xalign .5

        $ planta_jugador = (
            "planta_florece_dorado" if persistent.desbloqueo 
            else "planta_florece")

        show expression planta_jugador:
            yalign .4
            xalign .5        
            xsize 950
            ysize 900
        narrador "La planta que cuidas está floreciendo."
    
    return


label final_no_tomar_atencion:

    scene black
    nvl clear
    
    $ persistent.final_tercera_opcion = not persistent.final_tercera_opcion
    
    $ color_var = Color((0, 0, 0, 121))
    $ tamanio_final = 2
    show screen color_fondo_final
    
    "[pareja.nombre] y [jugador.nombre] continuaron con sus mismas actitudes 
        violentas."
    
    $ valor_incremento = 255 / tamanio_final
    $ aclararColorFondo(1, valor_incremento)
    if persistent.final_tercera_opcion:

        "[jugador.nombre] y [pareja.nombre] siguen siendo novios. Todavía hay 
            violencia y esta ha escalado."        
        $ aclararColorFondo(2, valor_incremento) 
        nvl clear       
        show white
        hide screen color_fondo_final with Fade(0.5, 0, 0.5, color="#FFFFFF")
        show planta_fondo:
            yalign .4
            xalign .27
        show planta_fondo as fondo_pareja:
            yalign .4
            xalign .69

        $ planta_jugador = (
            "planta_marchita_dorado" if persistent.desbloqueo 
            else "planta_marchita")

        show expression planta_jugador:
            yalign .4
            xalign .27        
            xsize 950
            ysize 900
        show planta_marchita as planta_pareja:
            yalign .4
            xalign .69        
            xsize 950
            ysize 900
        narrador "Sus plantas siguen marchitándose."
    else:

        "Su relación no pudo continuar con los problemas y terminó su relación. 
            [jugador.nombre] sigue intentando superar las cicatrices de la relación."
        $ aclararColorFondo(2, valor_incremento)    
        nvl clear    
        show white
        hide screen color_fondo_final with Fade(0.5, 0, 0.5, color="#FFFFFF")
        show planta_fondo:
            yalign .4
            xalign .27
        show planta_fondo as fondo_pareja:
            yalign .4
            xalign .69

        $ planta_jugador = (
            "planta_[jugador.estadoPlanta]_dorado" if persistent.desbloqueo 
            else "planta_[jugador.estadoPlanta]")

        show expression planta_jugador:
            yalign .4
            xalign .27        
            xsize 950
            ysize 900
        show expression "planta_[pareja.estadoPlanta]" as planta_pareja:
            yalign .4
            xalign .69        
            xsize 950
            ysize 900
        narrador "Pero ahora ya no están dañando a sus plantas."
    
    return


label palabras_finales:
    
    hide screen phone_ui
    hide screen color_fondo_final
    play music musica_fondo loop fadein 2.0 volume 1.0
    scene fondo_inicio with fade 
    
    if persistent.contador_final_visto == 12:

        narrador "¡Muchas gracias por ver todos los finales! Pensamos que nadie lo haría, pero {size=30}{b}tú{/b}{/size} nos demostraste lo contrario."
    else: 
    
        narrador "Y este fue el final {b}[persistent.contador_final_visto]{/b} de 12 posibles finales de la historia de [jugador.nombre] y [pareja.nombre]"
        $ persistent.contador_final_visto += 1
    
    narrador "Estos cambian cada vez que juegas, ¡Descubre todos los finales y prueba las distintas decisiones!"
    narrador "Porque, aunque aquí puedes intentarlo una y otra vez, en la vida real no siempre se tiene esa oportunidad..."
    narrador "No dejes que otros tomen el control de tí o de una amistad, puedes tomar la decisión y hacer un cambio. Al igual que [viejoAmigue.nombre], tus redes de apoyo te podemos ayudar."
    call instrucciones_recursos
    narrador "Esta fue la última capa de Latencia. ¡Muchas gracias por jugar!, sin tí este juego no sería posible."
    show creditos_finales with fade 
    pause 10.0    
    scene black with fade
    return