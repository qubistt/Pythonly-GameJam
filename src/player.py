from ursina import *

class Player(Entity):
    def __init__(self, model, position, collider, scale = (1, 1, 1), SPEED = 2, MAXSPEED = 3, velocity = (0, 0, 0), MAXJUMP = 1, gravity = 1, controls = "wasd", **kwargs):
        super().__init__(
            model = "cube", 
            position = position,
            scale = (1, 1, 1), 
            visible_self = False
        )
        self.collider = BoxCollider(self, center = Vec3(0, 1, 0), size = Vec3(1, 2, 1))
        mouse.locked = True
        camera.parent = self
        camera.position = (0, 2, 0)
        camera.rotation = (0, 0, 0)
        camera.fov = 100
        self.velocity_x, self.velocity_y, self.velocity_z = velocity
        self.SPEED = SPEED
        self.MAXJUMP = MAXJUMP
        self.jump_count = 0
        self.gravity = gravity
        self.jump_height = 0.3
        self.slope = 40
        self.controls = controls
        self.sensibility = 70
        self.momentum = 0