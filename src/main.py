# Import Ursina Engine
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
from random import uniform

# Initialise the engine
app = Ursina(vsync=True)


ground = Entity(
    model= 'plane',
    texture= 'grass',
    collider= 'mesh',
    position = (0,0,0),
    scale= (100,1, 100)
    )

player = FirstPersonController(
  collider='box',
  mouse_sensitivity= (40,40),
  speed = 30
  )

light = PointLight(parent = camera, position = (0, 10, -1.5), color = color.white)
AmbientLight(color = color.rgba(100, 100, 100, 0.1))

health_bar = HealthBar(bar_color=color.lime.tint(-.25), roundness=.5, value=50)

enemy = Entity(
    model = 'cube',
    position = (0,1,0),
    collider = 'box',
    color = color.red
)
enemy.add_script(SmoothFollow(target=player, offset=[0,0,0], speed=0.5))

#def damagePlayer():
   # health_bar.value -= 1
    #time.sleep(2)

#def healPlayer():
    #health_bar.value += 1
    #

sky = Sky()

jump = Audio(
  'assets\jump.mp3',
  loop = False,
  autoplay = False
)

walk = Audio(
  'assets\walk.mp3',
  loop = False,
  autoplay = False
)


def update():
    if player.intersects(enemy):
        #damagePlayer()
        health_bar.value -= 1


    else:
        health_bar.value += 0.5

    global lvl
    walking = held_keys['a'] or \
          held_keys['d'] or \
          held_keys['w'] or \
          held_keys['s']
    if walking and player.grounded:
        if not walk.playing:
            walk.play()

    else:
        if walk.playing:
            walk.stop()


def input(key):
    if key == 'q':
        quit()
    if key == 'space':
        if not jump.playing:
            jump.play()


window.title = 'My Game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Go Fullscreen
window.exit_button.visible = False      # Show the in-game red X that loses the window
window.fps_counter.enabled = False       # Show the FPS (Frames per second) counter


app.run()