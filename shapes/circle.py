from shape import Shape

class Circle(Shape):
    
    PI = 3.14159265359

    def __init__(self, shape_id, shape_type, radius):
        super().__init__(shape_id, shape_type)
        self.radius = radius

    def get_area(self):
        return Circle.PI * (self.radius ** 2)
    
    def get_perimeter(self):
        return 2 * Circle.PI * self.radius
    
    def to_dict(self):
        return {
            "shape_id": self.shape_id,
            "shape_type": self.shape_type,
            "values": {
                "radius": self.radius,
            },
        }