from shapes.rectangle import Rectangle

class Triangle(Rectangle):
    def __init__(self, shape_id, shape_type, base, height, side_a, side_b, side_c):
        super().__init__(shape_id, shape_type)
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        return (self.base * self.height) / 2

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
    
    def to_dict(self):
        return {
            "shape_id": self.shape_id,
            "shape_type": self.shape_type,
            "shape_values": {
                'base': self.base,
                'height': self.height,
                'side_a': self.side_a,
                'side_b': self.side_b,
                'side_c': self.side_c,
            },
        }