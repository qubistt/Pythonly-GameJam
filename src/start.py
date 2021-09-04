from ursina import *
from main import *

class main:
    def splashScreen():

        global bg
        bg = Entity(
            parent = camera.ui,
            model = 'quad',
            scale = (10,10,10),
            color = color.white
        )
        textShown = dedent(
            '''<scale: 1><azure>EXTINCT<scale: 1><black>VERSE'''
        )
        

        Text.size = 0.10
        Text.default_resolution = 1080 * Text.size
        Text.default_font = '../assets/fonts/Fonseca Rounded.otf'
        
        global splashText                           
        splashText = Text(
            text = textShown,
            origin = (0,-4),
            
        )
        global playBtn
        playBtn = Button(text='', color=color.white, icon='../assets/textures/play-button', scale=(0.5,0.25), text_origin=(0,0),origin = (0,1))
        playBtn.on_click = splashDisable() # assign a function to the button.
        playBtn.tooltip = Tooltip('exit')
    
    def splashDisable():
        bg.disable()
        splashText.disable()
        playBtn.disable()