from square import Square
from rectangle import Rectangle
from circle import Circle
from utils import Utils
import json

class ShapeManager:

    def __init__(self):
        self.shapes = []
        self.load_from_json()
    
    def get_new_id(self):
        return len(self.shapes) + 1
    
    def create_shape(self, shape: str, data: dict):
        data['shape_id'], data['shape_type'] = self.get_new_id(), shape
        new_shape = shape(**data)
        self.shapes.append(new_shape)
        
    def get_all_shapes(self):
        output_list = []
        for shape in self.shapes:
            shape_dict = shape.todict()
            shape_str = '\n'.join([f"{k.capitalize()}: {v}" for k, v in shape_dict.items()])
            output_list.append(shape_str)
        return output_list
    
    def update_shape(self, shape_id: str, new_data: dict, file_name):
        shape = self.get_shape_by_id(shape_id)
        if shape:
            for value in new_data:    
                shape.value = new_data[value]
            self.shapes.append(shape)
            self.save_to_json(file_name)
            return True
        
    def delete_shape(self, shape_id):
        shape = self.get_shape_by_id(shape_id)
        if shape:
            self.shapes.remove(shape)
            return True
    
    def save_to_json(self, file_name):
        with open(file_name, 'w') as f:
            json.dump(self.shapes, f)

    def load_from_json(self, file_name):
        with open(file_name, 'r') as f:
            self.shapes = json.load(f)

    def get_shape_by_id(self, id):
        for shape in self.shapes:
            if shape['id'] == id:
                return shape
            