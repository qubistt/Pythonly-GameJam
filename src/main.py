# Import Ursina
# Import time util
from ursina import *
from random import uniform
from ursina.prefabs.first_person_controller import FirstPersonController
import time




# The main method/app is Ursina's Engine
# It sets up 3D, 2D scenes etc.
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
    playBtn.on_click = destroySplash() # assign a function to the button.
    playBtn.tooltip = Tooltip('exit')

# Spawning ground
def destroySplash():
    destroy(bg, delay=10)
    destroy(playBtn, delay=10)
    destroy(splashText, delay=10)
    startGame()

def startGame():
    ground = Entity(model = 'plane',
                texture = 'grass',
                collider = 'mesh',
                scale = (100,1, 100))

    sky = Sky()

    blocks = Entity(
        model = 'cube',
        texture = 'white_cube',
        position = (0,11,0),
        color = color.red,
        collider = 'box'
    )


    goal = Entity(
        color=color.gold,
        model='cube',
        texture='white_cube',
        position=(0,11,55),
        scale=(10,1,10),
        collider='box'
    )
    pillar = Entity(
        color=color.green,
        model='cube',
        position=(0,36,58),
        scale=(1,50,1)
    )

    player = FirstPersonController(collider = 'box', speed = 30)
    player.cursor.visible = False
    if held_keys == 'escape':
      mouse.visible = True
      mouse.locked = False


    if held_keys == 'q':
        quit()
    
app = Ursina(vsync=True)
window.title = 'My Game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Go Fullscreen
window.exit_button.visible = False      # Show the in-game red X that loses the window
window.fps_counter.enabled = False       # Show the FPS (Frames per second) counter

splashScreen()
app.run()





