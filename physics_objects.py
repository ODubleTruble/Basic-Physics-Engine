import pygame

total_circles_created = 0
all_circles = {}

class circle:
    def __init__(self,
                 position: pygame.math.Vector2,
                 initial_acceleration: pygame.math.Vector2 = pygame.Vector2(),
                 radius: float = 50,
                 color = (255, 255, 255)):
        self.curPos = position
        self.oldPos = position
        self.acc = initial_acceleration
        self.radius = radius
        self.color = color
        
        # Increase total circles, assign ID, append to array of all circles.
        global total_circles_created
        total_circles_created += 1
        self.id = total_circles_created
        global all_circles
        all_circles[self.id] = self
        
    def __str__(self) -> str:
        returnString = f'<Circle {self.id} = '
        returnString += f'curPos: {self.curPos}, '
        returnString += f'oldPos: {self.oldPos}, '
        returnString += f'acc: {self.acc}, '
        returnString += f'radius: {self.radius}, '
        returnString += f'color: {self.color}>'
        return returnString
    
    def print_all():
        for id in all_circles:
            print(all_circles[id])
        
    def accelerate(self, gravity_vector: pygame.math.Vector2):
        self.acc = self.acc + gravity_vector
    
    def update_pos(self, dt: float):
        velocity = self.curPos - self.oldPos
        self.oldPos = self.curPos
        self.curPos = self.curPos + velocity + self.acc * (dt**2)


class solver:
    gravity = pygame.Vector2(0, 0.00001)
    
    def update(dt: float):
        solver.apply_gravity()
        solver.update_pos(dt)
    
    def apply_gravity():
        for id in all_circles:
            all_circles[id].accelerate(solver.gravity)
    
    def update_pos(dt: float):
        for id in all_circles:
            all_circles[id].update_pos(dt)


if __name__ == "__main__":
    # Create a few circles. 
    for i in range(1, 4):
        circle(pygame.Vector2(), radius=i*10)

    circle.print_all()
    solver.update(5.0)
    circle.print_all()