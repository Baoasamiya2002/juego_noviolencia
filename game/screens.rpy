init python:
    import random

    config.has_quicksave = False
    config.has_sync = False

    def forzarAutosave():
        renpy.force_autosave()

    #codigo aleatorio para compartir
    if not persistent.codigo_usuario:
        with renpy.file('misc/codigos_maceta.txt', encoding='utf8') as f:
            persistent.codigos_maceta = [line[:-1] for line in f]
            persistent.codigo_usuario = (
                random.choice(persistent.codigos_maceta) + str(random.randint(0, 9)))

################################################################################
## Inicialización
################################################################################

init offset = -1


################################################################################
## Estilos
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5
    xalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)
    font gui.name_text_font

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Pantallas internas del juego
################################################################################


## Pantalla de diálogo #########################################################
##
## La pantalla de diálogo muestra el diálogo al jugador. Acepta dos parámetros,
## 'who' y 'what', es decir, el nombre del personaje que habla y el texto que ha
## de ser mostrado respectivamente. (El parámetro 'who' puede ser 'None' si no
## se da ningún nombre.)
##
## Esta pantalla debe crear un texto visualizable con id "what" que Ren'Py usa
## para gestionar la visualización del texto. Puede crear también visualizables
## con id "who" y id "window" para aplicar propiedades de estilo.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    frame:
        
        id "window"
        style_prefix "window"

        vbox:
            
            if who is not None:

                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"

            text what id "what"


## Permite que el 'namebox' pueda ser estilizado en el objeto 'Character'.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    left_margin 200
    right_margin 200
    padding (0, 50)
    background Frame("gui/textbox.png")

style window_image:
    xalign 1.0

style window_vbox:
    xalign 0.5
    xsize 1906

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    ypos gui.dialogue_ypos

    adjust_spacing False

style text_preview:
    xalign 0.5
    xfill True
    ypos 0.01
    left_margin 100
    right_margin 100
    ysize 240
    padding (0, 20)
    background Frame("gui/preview_textbox.png")

style preferences_intro:
    ypos 0.17    
    left_margin 100
    right_margin 100
    ysize 1310
    background Frame("gui/preview_textbox.png")
## Pantalla de introducción de texto ###########################################
##
## Pantalla usada para visualizar 'renpy.input'. El parámetro 'prompt' se usa
## para pasar el texto presentado.
##
## Esta pantalla debe crear un displayable 'input' con id "input" para aceptar
## diversos parámetros de entrada.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Pantalla de menú ############################################################
##
## Esta pantallla presenta las opciones internas al juego de la sentencia
## 'menu'. El parámetro único, 'items', es una lista de objetos, cada uno los
## campos 'caption' y 'action'.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 540
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Pantalla de menú rápido #####################################################
##
## El menú rápido se presenta en el juego para ofrecer fácil acceso a los menus
## externos al juego.

screen quick_menu():

    ## Asegura que esto aparezca en la parte superior de otras pantallas.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.0

            #textbutton _("Atrás") action Rollback() size_group "menu"
            imagebutton: 
                idle "gui/button/menu_quick/progreso.png"
                hover "gui/button/menu_quick/progreso_hover.png"
                alt "Progreso"
                action ShowMenu("history")

            imagebutton: 
                idle "gui/button/menu_quick/opciones.png"
                hover "gui/button/menu_quick/opciones_hover.png"
                alt "Opciones"
                action ShowMenu("options")

            imagebutton: 
                idle "gui/button/menu_quick/recursos.png"
                hover "gui/button/menu_quick/recursos_hover.png"
                alt "Recursos de ayuda"
                action ShowMenu("resources")

            if renpy.variant("pc"):

                ## El botón de salida está prohibido en iOS y no es necesario en
                ## Web.
                imagebutton: 
                    idle "gui/button/menu_quick/salir.png"
                    hover "gui/button/menu_quick/salir_hover.png"
                    alt "Salir"
                    action [forzarAutosave,
                            Quit(confirm=True)] 
            
            imagebutton:
                idle "gui/button/menu_quick/quitar.png"
                hover "gui/button/menu_quick/quitar_hover.png"
                alt "¡Quitar!"
                action [forzarAutosave, 
                        OpenURL("https://www.uam.mx/calendario/index.html"), 
                        Quit(confirm=False)]


## Este código asegura que la pantalla 'quick_menu' se muestra en el juego,
## mientras el jugador no haya escondido explícitamente la interfaz.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

#image testimg = Frame("gui/button/quick_idle_background.png")

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")
    #xsize 250

style quick_button_text:
    properties gui.text_properties("quick_button")

style quick_image_button:
    xsize 230


################################################################################
## Principal y Pantalla de menu del juego.
################################################################################

## Pantalla de navegación ######################################################
##
## Esta pantalla está incluída en el menú principal y los menús del juego y
## ofrece navegación a los otros menús y al inicio del juego.

screen navigation():

    hbox:

        xfill True

        if (renpy.get_screen("main_menu") and renpy.variant("pc")):
            ## El botón de salida está prohibido en iOS y no es necesario en
            ## Web.
            imagebutton:
                idle "gui/button/menu_principal/salir.png"
                hover "gui/button/menu_principal/salir_hover.png"
                alt "Salir"
                action Quit(confirm=True)
        elif not renpy.get_screen("main_menu"):

            imagebutton:
                idle "gui/button/menu_opciones/volver.png"
                hover "gui/button/menu_opciones/volver_hover.png"
                alt "Volver"
                action Return()

        imagebutton:
            xalign 1.0
            idle "gui/button/menu_principal/ocultar.png"
            hover "gui/button/menu_principal/ocultar_hover.png"
            alt "¡Ocultar!"
            action [forzarAutosave, 
                    OpenURL("https://www.uam.mx/calendario/index.html"), 
                    Quit(confirm=False)]

    if renpy.get_screen("main_menu"):

        hbox:

            style_prefix "navigation"

            xalign 0.5
            yalign 0.90

            spacing gui.navigation_spacing

            vbox:

                yalign 0.5

                imagebutton:                
                    idle "gui/button/menu_principal/jugar.png" 
                    hover "gui/button/menu_principal/jugar_hover.png"
                    alt "Jugar"
                    action Start()
                
                if not persistent.desbloqueo:
                    imagebutton:
                        xalign 0.5
                        idle "mejora_button"
                        alt "Mejora"
                        action ShowMenu("desbloquear")

            null height (1.5 * gui.pref_spacing)

            vbox:

                imagebutton:
                    idle "gui/button/menu_principal/cargar.png"
                    hover "gui/button/menu_principal/cargar_hover.png"
                    alt "Cargar"
                    action ShowMenu("load")

                imagebutton: 
                    idle "gui/button/menu_principal/mas_info.png"
                    hover "gui/button/menu_principal/mas_info_hover.png"
                    alt "Más información"
                    action ShowMenu("more_info")

                imagebutton: 
                    idle "gui/button/menu_principal/opciones.png"
                    hover "gui/button/menu_principal/opciones_hover.png"
                    alt "Opciones"
                    action ShowMenu("options")


image mejora_button:
    "gui/button/menu_principal/mejora.png"
    pause 0.5
    "gui/button/menu_principal/mejora_hover.png"
    pause 0.5
    repeat

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")

style selected_button:
    background "#ff0000cf"

## Pantalla del menú principal #################################################
##
## Usado para mostrar el menú principal cuando Ren'Py arranca.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## Esto asegura que cualquier otra pantalla de menu es remplazada.
    tag menu

    add gui.main_menu_background

    ## La sentencia 'use' incluye otra pantalla dentro de esta. El contenido
    ## real del menú principal está en la pantalla de navegación.
    use navigation

    hbox:

        xalign 0.5
        yalign 0.25

        image "images/titulo.png":
            fit "contain" 
            xsize 1700 
            alt "Latencia. Toma el control... o la decisión correcta"


style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text


style main_menu_vbox:
    xalign 1.0
    xoffset -40
    xmaximum 1600
    yalign 1.0
    yoffset -40

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Pantalla del menú del juego #################################################
##
## Esto distribuye la estructura de base del menú del juego. Es llamado con el
## título de la pantalla y presenta el fondo, el título y la navegación.
##
## El parámetro 'scroll' puede ser 'None', "viewport" o "vpgrid". Se usa esta
## pantalla con uno o más elementos, que son transcluídos (situados) en su
## interior.

screen game_menu(title=None, scroll=None, yinitial=0.0, spacing=0):
    
    style_prefix "game_menu"
    
    if main_menu:
        add "fondo_inicio"

    frame:
        
        if title != None:

            style "game_menu_outer_frame"
        
        else:

            style_prefix "history_menu"
        
        hbox:

            frame:

                style "game_menu_content_frame"
                
                if scroll == "viewport":

                    viewport:

                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                elif scroll == "config_viewport":


                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        viewport_yfill False
                
                else:
                    
                    transclude

    if title != None:

        use navigation
    
        label title

        if main_menu:
            key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 20
    top_padding 200
    left_padding 0
    xfill True    
    yfill True
    background "#ffffffcf"#ffffffcf

style history_menu_frame:
    xfill True    
    yfill True
    background "#0015ff00"

style history_menu_viewport:
    ysize 1020

style game_menu_navigation_frame:
    xsize 560
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 40
    top_margin 20
    ysize 1280

style game_menu_viewport:
    xsize 1840

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_label:
    xalign 0.5
    ysize 240

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -60


screen more_info():

    tag menu

    use game_menu("Más información"):

        hbox:

            xfill True
        vbox:

            align (0.5, 0.45)
            spacing 100
            imagebutton:
                idle "gui/button/menu_mas_info/recursos.png"
                hover "gui/button/menu_mas_info/recursos_hover.png"
                alt "Recursos de ayuda"
                action ShowMenu("resources")
            imagebutton:
                xalign 0.5
                idle "gui/button/menu_mas_info/tutorial.png"
                hover "gui/button/menu_mas_info/tutorial_hover.png"
                alt "Tutorial"
                action ShowMenu("tutorial")
            imagebutton:
                xalign 0.5
                idle "gui/button/menu_mas_info/creditos.png"
                hover "gui/button/menu_mas_info/creditos_hover.png"
                alt "Creditos"
                action ShowMenu("about")


screen resources():

    tag menu

    use game_menu("Recursos de ayuda"):

        label ("En construcción")

screen tutorial():

    tag menu

    use game_menu("Tutorial"):

        label ("En construcción")

## Pantalla 'acerca de' ########################################################
##
## Esta pantalla da información sobre los créditos y el copyright del juego y de
## Ren'Py.
##
## No hay nada especial en esta pantalla y por tanto sirve también como ejemplo
## de cómo hacer una pantalla personalizada.

screen about():

    tag menu

    ## Esta sentencia 'use' incluye la pantalla 'game_menu' dentro de esta. El
    ## elemento 'vbox' se incluye entonces dentro del 'viewport' al interno de
    ## la pantalla 'game_menu'.
    use game_menu(("Créditos"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Versión [config.version!t]\n")

            ## 'gui.about' se ajusta habitualmente en 'options.rpy'.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Hecho con {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Pantallas de carga y grabación ##############################################
##
## Estas pantallas permiten al jugador grabar el juego y cargarlo de nuevo. Como
## comparten casi todos los elementos, ambas están implementadas en una tercera
## pantalla: 'file_slots'.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Guardar"))


screen load():

    tag menu

    use file_slots(_("Cargar"))


screen file_slots(title):

    use game_menu(title):

        fixed:

            ## Botones de acceso a otras páginas
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 0.05

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    if config.has_autosave:
                        textbutton _("Guardado automático") action FilePage("auto")

                    if title == "Cargar":
                        text "|"
                        textbutton "Capas" action FilePage("quick")

                    ## range(1, 3) da los números del 1 al 2.
                    for page in range(1, 3):
                        text "|"
                        textbutton "Partida propia ([page])" action FilePage(page)

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 1.0

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    if persistent._file_page != "quick":

                        button:
                            action FileAction(slot)

                            has vbox

                            add FileScreenshot(slot) xalign 0.5

                            spacing 22

                            text FileTime(
                                slot, 
                                format=_("{#file_time}%A, %d/%m/%Y - %H:%M"), 
                                empty=_("vacío")):
                                style "slot_time_text"

                            text FileSaveName(slot):
                                style "slot_name_text"

                            key "save_delete" action FileDelete(slot)
                    else:

                        $ nombreLabel = "eleccionCapa" + str(slot)
                        $ nombreImagen = "capa_" + str(slot)

                        button:
                            action Start(nombreLabel)

                            has vbox

                            add DynamicImage(nombreImagen): 
                                ysize config.thumbnail_height 
                                xsize config.thumbnail_width

                            spacing 22

                            text NOMBRE_CAPA[i]:
                                style "slot_time_text"
            

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 100
    ypadding 6

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_text:
    yalign 0.5

style page_button_text:
    properties gui.text_properties("page_button")   
    font gui.name_text_font
    size 70

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")

default flag = False
screen options():
    
    tag menu
    
    use game_menu("Opciones"):
    
        vbox:

            hbox:

                xfill True
                yfill True
                vbox:

                    align (0.5, 0.45)
                    spacing 100
                    imagebutton:
                        idle "gui/button/menu_opciones/cargar.png"
                        hover "gui/button/menu_opciones/cargar_hover.png"
                        alt "Cargar"
                        action ShowMenu("load")
                    imagebutton: 
                        idle "gui/button/menu_opciones/guardar.png"
                        hover "gui/button/menu_opciones/guardar_hover.png"
                        insensitive "gui/button/menu_opciones/guardar_insensitive.png"
                        sensitive not main_menu
                        alt "Guardar"
                        action ShowMenu("save")
                vbox:

                    align (0.5, 0.45)
                    spacing 100
                    imagebutton: 
                        idle "gui/button/menu_opciones/mas_info.png"
                        hover "gui/button/menu_opciones/mas_info_hover.png"
                        alt "Más información"
                        action ShowMenu("more_info")
                    imagebutton: 
                        idle "gui/button/menu_opciones/config.png"
                        hover "gui/button/menu_opciones/config_hover.png"
                        alt "Configuración"
                        action ShowMenu("preferences")

            if renpy.variant("pc"):

                ## El botón de salida está prohibido en iOS y no es necesario en
                ## Web.
                hbox:

                    align (0.5, 0.5)
                    imagebutton: 
                        ypos -230
                        idle "gui/button/menu_opciones/salir.png"
                        hover "gui/button/menu_opciones/salir_hover.png"
                        alt "Salir"                        
                        if main_menu:
                            action Quit(confirm=True)
                        else:
                            action [forzarAutosave,
                                    Quit(confirm=True)]

## Pantalla de preferencias ####################################################
##
## La pantalla de preferencias permite al jugador configurar el juego a su
## gusto.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences(view="Menu"):
    
    tag menu

    use game_menu(title=("Configuración" if view == "Menu" else None), scroll=(
        "vpgrid" if 300 else "viewport")):
        
        vbox:
                
            hbox:
                
                xfill True
                box_wrap True

                vbox:

                    style_prefix "slider"
                    label _("Velocidad del texto")

                    bar:
                        value Preference("text speed") 
                        xsize 610
                        released Function(TEXTO_CPS_PREVIEW.update_cps)

                    if view == "Menu":
                        
                        vbox:
                            
                            ysize 100
                            xsize 600
                            add PreviewSlowText(
                                "{size=-14}Muestra de velocidad{/size}")

                vbox:

                    style_prefix "radio"
                    label _("Tamaño")

                    textbutton _("Por defecto") action Preference(
                        "font size", 1.0)
                    textbutton _("Grande") action Preference("font size", 1.25)
                
                vbox:

                    style_prefix "radio"
                    label _("Font Override")

                    textbutton _("Default") action Preference(
                        "font transform", None)
                    textbutton _("DejaVu Sans") action Preference(
                        "font transform", "dejavusans")
                    textbutton _("Opendyslexic") action Preference(
                        "font transform", "opendyslexic")   
                
                vbox:

                    style_prefix "radio"
                    label _("High Contrast Text")

                    textbutton _("Enable") action Preference(
                        "high contrast text", "enable")
                    textbutton _("Disable") action Preference(
                        "high contrast text", "disable")
                    
            hbox:
                xfill True
                box_wrap True

                if (renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile"))):
                    vbox:   

                        style_prefix "radio"
                        
                        label _("Pantalla")
                        
                        textbutton _("Ventana") action Preference(
                            "display", "window")
                        textbutton _("Pantalla completa") action Preference(
                            "display", "fullscreen")
                
                vbox:

                    style_prefix "slider"
                    label _("Volumen música")
                    
                    bar value Preference("music volume") xsize 610
                
                vbox:
                    
                    style_prefix "radio"
                    label _("Espacio de línea")

                    textbutton _("Reducido") action Preference(
                        "font line spacing", 0.85)
                    textbutton _("Por defecto") action Preference(
                        "font line spacing", 1.0)
                    textbutton _("Amplio") action Preference(
                        "font line spacing", 1.25)

                vbox:

                    style_prefix "radio"
                    label _("Kerning")

                    textbutton _("Reducido") action Preference(
                        "font kerning", -0.5)
                    textbutton _("Por defecto") action Preference(
                        "font kerning", 0.0)
                    textbutton _("Amplio") action Preference(
                        "font kerning", 0.75)
                
                if not (renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile"))):

                    vbox:
                    
                        style_prefix "radio"
                            
            hbox:

                xfill True
                box_wrap True

                vbox:

                    style_prefix "radio"
                    #xsize 425
                    label _("Self-Voicing")

                    textbutton _("Off") action Preference(
                        "self voicing", "disable")
                    textbutton _("Text-to-speech") action Preference(
                        "self voicing", "enable")

                vbox:
                    
                    style_prefix "slider"
                    label _("Volumen  voz automática")
                    
                    bar value Preference("voice volume") xsize 610
                
                vbox:

                    
                    xsize 1000
                    null height (4 * gui.pref_spacing)

                    textbutton ("{u}Regresar a configuración inicial{/u}") action [
                        Preference("font kerning", 0.0), 
                        Preference("font line spacing", 1.0), 
                        Preference("font size", 1.0), 
                        Preference("high contrast text", "disable"), 
                        Preference("font transform", None), 
                        Preference("voice volume", 1.0), 
                        Preference("self voicing", "disable"), 
                        Preference("music volume", 1.0), 
                        Preference("text speed", 40)]:
                        
                        xalign 0.5

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 4

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 450

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    ypos 0.18

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 700

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 20

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 700


## Pantalla de historial #######################################################
##
## Esta pantalla presenta el historial de diálogo al jugador, almacenado en
## '_history_list'.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Evita la predicción de esta pantalla, que podría ser demasiado grande.
    predict False

    use game_menu(_("Progreso")):

        hbox:

            vbox:

                hbox:

                    vbox:

                        label _("Planta de [jugador.nombre]") xsize 550
                        null height (4 * gui.pref_spacing)
                        align(0.5, 0.5)
                        add DynamicImage("planta_[jugador.estadoPlanta]") ysize 450 xsize 400
                    vbox:

                        label _("Planta de [pareja.nombre]") xsize 450
                        null height (4 * gui.pref_spacing)
                        align(0.5, 0.5)
                        add DynamicImage("planta_[pareja.estadoPlanta]"): 
                            ysize 450 
                            xsize 400
                hbox:

                    vbox:

                        style_prefix "horizontal_scroll"
                        label _("Coleccionables")
                        
                        hbox:

                            frame:

                                viewport:
                                    scrollbars "horizontal"
                                    mousewheel True
                                    draggable True

                                    hbox:

                                        if coleccionables:
                                            for c in coleccionables:
                                                add "images/coleccionables/[c].png": 
                                                    fit "contain"
                                                    ysize 450
                                        else:
                                            vbox:
                                                style "slider" 
                  
            
            vbox:

                label _("Historial de diálogos")
                
                use game_menu(scroll=(
                    "vpgrid" if gui.history_height else "viewport"), yinitial=1.0, 
                    spacing=gui.history_spacing):

                    style_prefix "history"

                    for h in _history_list:

                        window:

                            ## Esto distribuye los elementos apropiadamente si
                            ## 'history_height' es 'None'.
                            has fixed:
                                yfit True

                            if h.who:
                                
                                label h.who:
                                    style "history_name"
                                    substitute False

                                    ## Toma el color del texto 'who' de 'Character', si ha
                                    ## sido establecido.
                                    if "color" in h.who_args:
                                        text_color h.who_args["color"]
                                    
                            $ what = renpy.filter_text_tags(h.what, 
                            allow=gui.history_allow_tags)
                            truncate_text what:
                                substitute False

                    if not _history_list:
                        label _("No se ha iniciado el juego.")


                        


## Esto determina qué etiquetas se permiten en la pantalla de historial.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height
    top_padding 50

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    font gui.text_font

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

style horizontal_scroll_vbox:
    xsize 860
    ysize 580
    
style horizontal_scroll_frame:
    background "#ff000000"
    
    



## Pantalla de ayuda ###########################################################
##
## Una pantalla que da información sobre el uso del teclado y el ratón. Usa
## otras pantallas con el contenido de la ayuda ('keyboard_help', 'mouse_help',
## y 'gamepad_help').

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Ayuda"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 30

            hbox:

                textbutton _("Teclado") action SetScreenVariable("device", "keyboard")
                textbutton _("Ratón") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Mando") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Intro")
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("Espacio")
        text _("Avanza el diálogo sin seleccionar opciones.")

    hbox:
        label _("Teclas de flecha")
        text _("Navega la interfaz.")

    hbox:
        label _("Escape")
        text _("Accede al menú del juego.")

    hbox:
        label _("Ctrl")
        text _("Salta el diálogo mientras se presiona.")

    hbox:
        label _("Tabulador")
        text _("Activa/desactiva el salto de diálogo.")

    hbox:
        label _("Av. pág.")
        text _("Retrocede al diálogo anterior.")

    hbox:
        label _("Re. pág.")
        text _("Avanza hacia el diálogo siguiente.")

    hbox:
        label "H"
        text _("Oculta la interfaz.")

    hbox:
        label "S"
        text _("Captura la pantalla.")

    hbox:
        label "V"
        text _("Activa/desactiva la asistencia por {a=https://www.renpy.org/l/voicing}voz-automática{/a}.")

    hbox:
        label "Shift+A"
        text _("Abre el menú de accesibilidad.")


screen mouse_help():

    hbox:
        label _("Clic izquierdo")
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("Clic medio")
        text _("Oculta la interfaz.")

    hbox:
        label _("Clic derecho")
        text _("Accede al menú del juego.")

    hbox:
        label _("Rueda del ratón arriba")
        text _("Retrocede al diálogo anterior.")

    hbox:
        label _("Rueda del ratón abajo")
        text _("Avanza hacia el diálogo siguiente.")


screen gamepad_help():

    hbox:
        label _("Gatillo derecho\nA/Botón inferior")
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("Gatillo izquierdo\nBotón sup. frontal izq.")
        text _("Retrocede al diálogo anterior.")

    hbox:
        label _("Botón sup. frontal der.")
        text _("Avanza hacia el diálogo siguiente.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navega la interfaz.")

    hbox:
        label _("Inicio, Guía, B/Botón Derecho")
        text _("Accede al menú del juego.")

    hbox:
        label _("Y/Botón superior")
        text _("Oculta la interfaz.")

    textbutton _("Calibrar") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 16

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 500
    right_padding 40

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Pantallas adicionales
################################################################################


## Pantalla de confirmación ####################################################
##
## Ren'Py llama la pantalla de confirmación para presentar al jugador preguntas
## de sí o no.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action=None):

    ## Asegura que otras pantallas no reciban entrada mientras se muestra esta
    ## pantalla.

    if message == layout.QUIT:
            
        $ message = ("¿Quieres salir?")
        if not main_menu:

            $ message += "\nYa se guardó tu partida hasta este punto en automático."

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 60

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 200

                textbutton _("Sí") action [yes_action, Hide("confirm")]

                if no_action:
                    textbutton _("No") action no_action

    ## Clic derecho o escape responden "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame(["gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Pantalla del indicador de salto #############################################
##
## La pantalla de indicador de salto se muestra para indicar que se está
## realizando el salto.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 12

            text _("Saltando")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Esta transformación provoca el parpadeo de las flechas una tras otra.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Es necesario usar un tipo de letra que contenga el glifo BLACK RIGHT-
    ## POINTING SMALL TRIANGLE.
    font "DejaVuSans.ttf"


## Pantalla de notificación ####################################################
##
## La pantalla de notificación muestra al jugador un mensaje. (Por ejemplo, con
## un guardado rápido o una captura de pantalla.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Pantalla NVL ################################################################
##
## Esta pantalla se usa para el diálogo y los menús en modo NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Presenta el diálogo en una 'vpgrid' o una 'vbox'.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Presenta el menú, si lo hay. El menú puede ser presentado
        ## incorrectamente si 'config.narrator_menu' está ajustado a 'True'.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Esto controla el número máximo de entradas en modo NVL que pueden ser
## mostradas de una vez.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Pantalla de globos ##########################################################
##
## La pantalla de burbujas se utiliza para mostrar el diálogo al jugador cuando
## se utilizan burbujas de diálogo. La pantalla de burbujas toma los mismos
## parámetros que la pantalla "say", debe crear un visualizable con el id de
## "what", y puede crear visualizables con los ids "namebox", "who", y "window".
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Variantes móviles
################################################################################

style pref_vbox:
    variant "medium"
    xsize 900

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style game_menu_outer_frame:
    variant "small"
    background "#ffffffcf"

style game_menu_navigation_frame:
    variant "small"
    xsize 680

style game_menu_content_frame:
    variant "small"
    top_margin 0

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize 700

style slider_slider:
    variant "small"
    xsize 1200


screen text_preview():

    dismiss action NullAction()
    
    frame:
        style "text_preview"
        vbox:
            xalign 0.5
            yalign 0.5
            xsize 2300
            style "say_dialogue"
            add TEXTO_CPS_PREVIEW

    frame:
        style "preferences_intro"
        use preferences("Intro")

    vbox:
        ypos 0.85
        xpos 0.68
        imagebutton:                
            idle "gui/button/menu_principal/continuar.png" 
            hover "gui/button/menu_principal/continuar_hover.png"
            alt "Continuar" 
            action Return()


screen intro():

    frame:
        xalign 0.6
        yalign 0.8
        xsize 2300
        ysize 1300
        padding (100, 60)
        background Frame("gui/narrador_textbox.png")
        truncate_text (texto_intro):
            shrink_to_fit 10 adjust_line_spacing_to_fit -10
            shrink_before_spacing False
            yalign 0.5

screen boton_quitar():

    hbox:

        xfill True

        imagebutton:
            xalign 1.0
            idle "gui/button/menu_principal/ocultar.png"
            hover "gui/button/menu_principal/ocultar_hover.png"
            alt "¡Ocultar!"
            action [forzarAutosave, 
                    OpenURL("https://www.uam.mx/calendario/index.html"), 
                    Quit(confirm=False)]

screen boton_eleccion_personaje():

    zorder 1

    dismiss action NullAction()
    
    imagebutton:
        xalign .19
        yalign .4
        idle "gui/button/boton_seleccion_fernanda.png"
        hover "gui/button/boton_seleccion_fernanda_hover.png"
        action [
            Function(lambda: definirPersonaje(
                novia, APODO_NOVIA, 
                novio, APODO_NOVIO)), 
            Return()]
    imagebutton:
        xalign .75
        yalign .4
        idle "gui/button/boton_seleccion_carlos.png"        
        hover "gui/button/boton_seleccion_carlos_hover.png"
        action [
            Function(lambda: definirPersonaje(
                novio, APODO_NOVIO, 
                novia, APODO_NOVIA)), 
            Return()]

screen desbloquear():
    
    default mostrarInput = False

    tag menu

    use game_menu("Desbloquear", scroll=(
        "vpgrid" if 300 else "viewport")):

        vbox:
            
            xfill True
            null height (6 * gui.pref_spacing)

            text "¡Muchas gracias por querer jugar nuestro juego!"
            null height (4 * gui.pref_spacing)
            text "¿Quieres desbloquear algo especial?"
            null height (4 * gui.pref_spacing)
            text "¡Invita a alguien a jugar y compartan sus códigos!"
            null height (5 * gui.pref_spacing) 

            style_prefix "codigo"
            hbox:

                vbox:

                    label (" Comparte este código")
                    textbutton (persistent.codigo_usuario)
                vbox:

                    label (" Escribe aquí el código compartido")
                    textbutton ("") action SetScreenVariable("mostrarInput",True)
                    
                    if mostrarInput:
                                                
                        input default "":
                            color "#000"
                            size gui.interface_text_size + 50
                            pos(280, -211)
                            length(6)
                            value VariableInputValue("codigoCompartido")
                        
                        if len(codigoCompartido) == 6:
                            
                            if codigoCompartido == persistent.codigo_usuario:

                                text "Tiene que ser un código distinto al tuyo"
                            else:

                                if codigoCompartido[:-1] in persistent.codigos_maceta:
                                    
                                    timer 0.1 action Hide("desbloquear")
                                    timer 0.1 action Show(
                                        "confirm", 
                                        message=(
                                            "¡Desbloqueo exitoso!" + 
                                            "\nJuega para verlo"), 
                                        yes_action=Return())

                                    $ persistent.desbloqueo = True

            null height (4 * gui.pref_spacing)
            text "Así, reciben un objeto sorpresa que podrán ver al jugar..."

style codigo_hbox:
    xalign 0.5

style codigo_button:
    xysize (924,305)
    background "gui/button/codigo.png"

style codigo_button_text:
    size gui.interface_text_size + 50
    color "#000" 

style codigo_text:
    xalign 0.5