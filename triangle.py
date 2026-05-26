from shape import Shape

class Triangle(Shape):
    def __init__(self, shape_id, shape_type, side1, side2, side3):
        super().__init__(shape_id, shape_type)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self):
        return self.side1 + self.side2 + self.side3
    
    def get_perimeter(self):
        pass
    
    def to_dict(self):
        pass