from shape import Shape

class Hexagon(Shape):
    def __init__(self, shape_id, shape_type, side):
        super().__init__(shape_id, shape_type)
        self.side = side

    def get_area(self):
        return (self.side ** 2) * (3 * 3**0.5) / 2
    
    def get_perimeter(self):
        return (self.side * 6) 
    
    def to_dict(self):
        return {
            "shape_id": self.shape_id,
            "shape_type": self.shape_type,
            "shape_values": {
                "side": self.side
            }
        }