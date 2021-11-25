class Circle:
    
    def __init__(self, radius = None, diameter = None):
        if radius == None and diameter == None:
            self.radius = 1
            self.diameter = self.radius * 2
            print('Radius: 1, diameter: 2')
        elif radius != None and diameter == None:
            self.radius = radius
            self.diameter = radius * 2
            print(f"Radius: {self.radius}, diameter: {self.diameter}")
        elif radius ==None and diameter != None and diameter == None:
            self.diameter = diameter
            self.radius = self.diameter // 2
            print(f"Radius: {self.radius}, diameter: {self.diameter}")
        else:
            user_input = input("Please provide valid input.")
            return Circle(user_input)
    
    @property
    def compute_are(self):
        return self.radius * self.diameter
    
    def __add__(self, circle):
        return self.compute_are + circle.compute_are
    
    def __lt__(self, circle):
        if self.compute_are < circle.compute_are:
            return True
        else:
            return False
    
    def __eq__(self, circle):
        if self.compute_are == circle.compute_are:
            return True
        else:
            return False

circle_a = Circle(diameter = 8)
circle_b = Circle(diameter = 6)

circle_a + circle_b

circle_a < circle_b
circle_a == circle_b

circle_list = [circle_a, circle_b]

sorted(circle_list)

circle.diameter
circle.radius
circle.compute_are
