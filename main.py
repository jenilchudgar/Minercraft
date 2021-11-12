from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Load
app = Ursina()

# Textures
grass_tex = load_texture("Assests/grass_block.png")
stone_tex = load_texture("Assests/stone_block.png")
brick_tex = load_texture("Assests/brick_block.png")
dirt_tex = load_texture("Assests/dirt_block.png")
sky_tex = load_texture("Assests/skybox.png")
hand_tex = load_texture("Assests/arm_texture.png")
sound = Audio("Assests/punch_sound.wav",loop=False,autoplay=False)

# Remove FPS and exit btn
window.fps_counter.enabled = False
window.exit_button.enabled = False

# Textures List
textures = []
textures.append(grass_tex)
textures.append(stone_tex)
textures.append(brick_tex)
textures.append(dirt_tex)

block_pic = 1

def update():
    global block_pic

    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()

    if held_keys['escape']: 
        sys.exit()
    if held_keys['1']: block_pic = 1
    if held_keys['2']: block_pic = 2
    if held_keys['3']: block_pic = 3
    if held_keys['4']: block_pic = 4

class Voxel(Button):
    def __init__(self,pos=(0,0,0),texture=grass_tex):
        super().__init__(
            parent = scene,
            position = pos,
            model = 'Assests/block.obj',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            scale = 0.5
        )
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                sound.play()
                Voxel(pos=self.position + mouse.normal,texture=textures[block_pic-1])
            if key == 'right mouse down':
                sound.play()
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_tex,
            scale = 150,
            double_sided = True
        )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'Assests/arm',
            texture = hand_tex,
            scale = 0.2,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.4,-0.6)
        )

    def active(self):
        self.position = Vec2(0.3,-0.5)
    
    def passive(self):
        self.position = Vec2(0.4,-0.6)

for z in range(40):
    for x in range(40):
        voxel = Voxel(pos=(x,0,z))

def main():
    if __name__ == "__main__":
        global hand
        player = FirstPersonController()
        sky = Sky()
        hand = Hand()
        app.run()

main()