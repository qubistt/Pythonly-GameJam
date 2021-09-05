
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar

# Initialise the engine
app = Ursina(vsync=True)

#Create the sky, most basic thing
sky = Sky()



#Add audio assets
jump = Audio(
  '../assets/audio/jump.mp3',
  loop = False,
  autoplay = False
)

walk = Audio(
  '../assets/audio/walk.mp3',
  loop = False,
  autoplay = False
)


#Create the ground
ground = Entity(
    model='plane', 
    scale=(100,1,100), 
    color=color.yellow.tint(-.2), 
    texture='white_cube', 
    texture_scale=(100,100), 
    collider='box'
    )

#Two walls at spawn
# Plus some texture rescaling
wall1 = Entity(
    model='cube', scale=(1,5,50), 
    x=2, y=.01, 
    rotation_y=45, 
    collider='box', 
    texture='white_cube'
    )
wall1.texture_scale = (
    wall1.scale_z, 
    wall1.scale_y
    )

wall1 = Entity(
    model='cube', 
    scale=(1,5,50), 
    x=-2, y=.01, 
    collider='box', 
    texture='white_cube'
    )
wall1.texture_scale = (
    wall1.scale_z, 
    wall1.scale_y
    )

# Initialise the player with a few simple properties
player = FirstPersonController(
    y=2, 
    origin_y=-.5,
    collider = 'box'
    )
player.gun = None

# Lighting
light = PointLight(parent = camera, position = (0, 15, -1.5), color = color.white, scale = (100,1,100))
AmbientLight(color = color.rgba(100, 100, 100, 0.1))

# The health bar
health_bar = HealthBar(
    bar_color=color.lime.tint(-.25), 
    roundness=0.5, 
    value=50, 
    animation_duration = .1
    )

#The enemy, with an AI script to follow you and kill you
enemy = Entity(
    model = '../assets/textures/lion.obj',
    position = (5,1,0),
    collider = 'box',
    color = color.red,
    scale = 0.3
)
enemy.add_script(
    SmoothFollow(
        target=player, 
        offset=[0,1,0], 
        speed=0.5)
        )

# Create a basic gun and assign it to player on click
gun = Button(
    parent=scene, 
    model='../assets/textures/gun.obj', 
    color=color.blue, 
    origin_y=-.5, 
    position=(3,2,3), 
    scale = 0.3,
    collider='box'
    )

gun.on_click = Sequence(Func(setattr, gun, 'parent', camera), Func(setattr, player, 'gun', gun))
gun_2 = duplicate(gun, z=7, x=8)



# the reddish-brown block which you can use to launch yourself into the air
hookshot_target = Button(parent=scene, model='cube', color=color.brown, position=(4,5,5))
hookshot_target.on_click = Func(player.animate_position, hookshot_target.position, duration=.5)





def input(key):
    if key == '-':
        health_bar.value -= 10

    if key == 'q':
        quit()
    if key == 'space':
        if not jump.playing:
            jump.play()

    if key == 'left mouse down' and player.gun:
        gun.blink(color.orange)
        global bullet
        bullet = Entity(parent=gun, model='cube', scale=.1, color=color.black, collider='box')
        bullet.world_parent = scene
        bullet.animate_position(bullet.position+(bullet.forward*50),duration=1)
        if bullet.intersects(enemy):
            destroy(enemy, delay=1)

        destroy(bullet, delay=1)

def update():

    if player.intersects(enemy):
        health_bar.value -= 1

    else:
        health_bar.value += 1 

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
    

window.title = 'My Game'                # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Go Fullscreen
window.exit_button.visible = False      # Show the in-game red X that loses the window
window.fps_counter.enabled = False      # Remove the FPS counter, not required unless you are debugging

app.run()
