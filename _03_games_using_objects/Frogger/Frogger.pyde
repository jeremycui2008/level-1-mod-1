

def setup():
    # 1. Use the size function to set the size of your sketch
    size(800,600)
    # 2. Create 2 global variables for the background and the frog
    # using the loadImage("frog.png") function. For example:
    global bg, frog, car, Car,death, guh
    bg = loadImage("froggerBackground.png")
    frog = loadImage("frog.png")
    car = Car(100, 200, 200, 5)
    death = Car(150,100,200,200)
    guh = Car(300,300,200,3)
    # 3. Use the resize method to set the size of the background variable
    # to the width and height of the sketch. Resize the frog to an
    # appropriate size.
    bg.resize(800,600)
    global frog_x, frog_y
    frog_x=400
    frog_y=550
    
    
def draw():
    global frog_x, frog_y, car, bg, Car, death, guh
    # 4. Use the background function to draw the background
    background(bg)
    # 5. Use the image function to draw the frog.
    # Run the program and check the background and frog are displayed.
    image(frog,frog_x,frog_y)
    frog.resize(50,50)
    

    print(key)
    intersects(car)
    intersects(death)
    intersects(guh)
        # 6. Create global frog_x and frog_y variables in the setup function
    # and use them when drawing the frog. You will also have to put the
    # following in the draw function:
        
    # 7. Use the Car class below to create a global car object in the
    # setup function and call the update and draw functions here.
    
    car.update()
    car.draw()
    
    death.update()
    death.draw()
    
    guh.update
    guh.draw()
    # 8. Create an intersects method that checks whether the frog collides
    # with the car. If there's a collision, move the frog back to the starting
    # point.

    # 9. Create more car objects of different lengths, speed, and size
    
def keyPressed():
    global frog_x, frog_y, car
    if key == CODED:
        print(key)
        if keyCode == UP:
            # Frog Y position goes up
            print("up")
            frog_y-=10
        elif keyCode == DOWN:
            # Frog Y position goes down
            print("down")
            frog_y+=10
        elif keyCode == RIGHT:
            # Frog X position goes right
            print("right")
            frog_x+=10
        elif keyCode == LEFT:
            # Frog X position goes left
            print("left")
            frog_x-=10

    
def intersects(car):
    global frog_x, frog_y, Car, death, guh
    if frog_y > car.Car_y and frog_y < car.Car_y + 50 and frog_x > car.Car_x and frog_x < car.Car_x + car.Car_length:
        frog_x = 400;
        frog_y = 550;
        return True;
    else:
        return False;
    
class Car:
    
    def __init__(self, Car_x, Car_y, Car_length, Car_speed):
        self.Car_x = Car_x
        self.Car_y = Car_y
        self.Car_length = Car_length
        self.Car_speed = Car_speed
        
        self.car_image = loadImage("carRight.png")
        if self.Car_speed < 0:
            self.car_image = loadImage("carLeft.png")
        
        self.car_image.resize(Car_length, Car_length / 3)
        
    def draw(self):
        image(self.car_image, self.Car_x, self.Car_y)
    
    def update(self):
        self.Car_x += self.Car_speed
        
        if self.Car_x > width:
            self.Car_x = -self.Car_length
            
        if self.Car_x < -self.Car_length:
            self.Car_x = width
