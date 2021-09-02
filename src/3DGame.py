from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import uniform

app = Ursina()

ground = Entity(model = 'plane',
                texture = 'grass',
                collider = 'mesh',
                scale = (100,1, 100))

player = FirstPersonController(collider = 'box', speed = 100)

player.cursor.visible = False
mouse.visible = True

myBox = Entity(model= 'cube',
               color= color.black,
               collider= 'box',
               position= (15, 0.5, 5))
myBall = Entity(model= 'sphere',
                color= color.red,
                collider= 'sphere',
                position= (5, 0.5, 10))

sky = Sky()
lvl = 1

blocks = []
directions = []
window.fullscreen = False
for i in range(10):
  r = uniform(-2,2)
  block = Entity(
    position=(r, 1+i , 3+i*5),
    model='cube',
    texture='../assets/BannersLogos/ExtinctVerse.png',
    color=color.azure,
    scale=(3, 0.5, 3),
    collider='box',
  )
  blocks.append(block)
  if r < 0:
    directions.append(1)
  else:
    directions.append(-1)


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




def input(key):
    if key == 'escape':
        player.cursor.visible = True
        


    if key == 'q':
        quit()

    if key == 'space':
        if not jump.playing:
            jump.play()


app.run()