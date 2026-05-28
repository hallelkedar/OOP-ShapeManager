from shape import Shape

class Rectangle(Shape):
    def __init__(self, shape_id, shape_type, length, width):
        super().__init__(shape_id, shape_type)
        self.length = length
        self.width = width

    def get_area(self):
        return (self.length * self.width)
    
    def get_perimeter(self):
        return (self.length*2) + (self.width*2)
    
    def to_dict(self):
        return {
            "shape_id": self.shape_id,
            "shape_type": self.shape_type,
            "shape_values": {
                "length": self.length,
                "width": self.width,
            },
        }