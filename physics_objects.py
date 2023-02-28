import pygame

total_circles_created = 0
all_circles = []

class circle:
    def __init__(self,
                 position: pygame.math.Vector2,
                 initial_acceleration: pygame.math.Vector2 = pygame.Vector2(),
                 radius: float = 20,
                 color = (255, 255, 255)):
        self.curPos = position
        self.oldPos = position
        self.acc = initial_acceleration
        self.radius = radius
        self.color = color
        
        # Increase total circles, assign ID, append to array of all circles.
        global total_circles_created
        self.id = total_circles_created
        total_circles_created += 1
        global all_circles
        all_circles.append(self)
        
    def __str__(self) -> str:
        returnString = f'<Circle {self.id} = '
        returnString += f'curPos: {self.curPos}, '
        returnString += f'oldPos: {self.oldPos}, '
        returnString += f'acc: {self.acc}, '
        returnString += f'radius: {self.radius}, '
        returnString += f'color: {self.color}>'
        return returnString
    
    def print_all():
        for circ in all_circles:
            print(circ)
        
    def accelerate(self, gravity_vector: pygame.math.Vector2):
        self.acc = self.acc + gravity_vector
    
    def update_pos(self, dt: float):
        velocity = self.curPos - self.oldPos
        self.oldPos = self.curPos
        self.curPos = self.curPos + velocity + self.acc * (dt**2)


class solver:
    gravity = pygame.Vector2(0, 0.00001)
    constraint_center = pygame.Vector2(600, 350)
    constraint_radius = 350
    
    def update(dt: float):
        solver.apply_gravity()
        solver.apply_constraint()
        solver.solve_collisions()
        solver.update_pos(dt)
    
    def apply_gravity():
        for circ in all_circles:
            circ.accelerate(solver.gravity)
    
    def update_pos(dt: float):
        for circ in all_circles:
            circ.update_pos(dt)

    def apply_constraint():
        for circ in all_circles:
            circ_rad = circ.radius
            circ_pos = circ.curPos
            dis_to_cent = (circ_pos - solver.constraint_center).length()
            farthest_point_away = dis_to_cent + circ_rad
            if (farthest_point_away > solver.constraint_radius):
                # The distance outside the contraint circle that the circle is.
                dis_outside = farthest_point_away - solver.constraint_radius
                # Gets a vector from the circle to the contraint circle's center,
                # then scales it to be the length of dis_outside
                move_vec = solver.constraint_center - circ_pos
                move_vec.scale_to_length(dis_outside)
                # Moves the circle towards the constraint circle's center. 
                circ.curPos = circ.curPos + move_vec
    
    def solve_collisions():
        for current_id in range(len(all_circles)):
            circ1 = all_circles[current_id]
            pos1 = circ1.curPos
            rad1 = circ1.radius
            
            for check_id in range(current_id+1, len(all_circles)):
                circ2 = all_circles[check_id]
                pos2 = circ2.curPos
                rad2 = circ2.radius
                
                dis = (pos1 - pos2).length() - rad1 - rad2
                if (dis < 0):                    
                    move_vec = pos1 - pos2
                    move_vec.scale_to_length(dis/2)
                    all_circles[current_id].curPos = all_circles[current_id].curPos - move_vec
                    all_circles[check_id].curPos = all_circles[check_id].curPos + move_vec


if __name__ == "__main__":
    # Create a few circles. 
    for i in range(1, 4):
        circle(pygame.Vector2(), radius=i*10)

    circle.print_all()
    solver.update(5.0)
    circle.print_all()