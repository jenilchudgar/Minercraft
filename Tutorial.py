from ursina import *

class MyCube(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            color = color.white,
            texture = 'white_cube',
            rotation = Vec3(45,45,45)
        )

class MyButton(Button):
    def __init__(self):
        super().__init__(
            model = 'cube',
            texture = 'brick',
            color = color.yellow,
            highlight_color = color.blue,
            pressed_color = color.green,
            parent = scene
        )
    
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                print("btn pressed")
        return super().input(key)

app = Ursina()

# Update
def update():
    if held_keys['a']:
        test_square.x -= 3 * time.dt

# Entities
test_square = Entity(model="quad",color=color.red,scale=(1,4),position=(5,1))

# sans = Entity(model="quad",texture="icon.png")
my_btn = MyButton()
app.run()