from shapes.square import Square
from shapes.rectangle import Rectangle
from shapes.circle import Circle
from shapes.hexagon import Hexagon
from shapes.triangle import Triangle
import json

class ShapeManager:
    FILE_NAME = 'shapes.json'
    SHAPES = {
    'Square': Square,
    'Rectangle': Rectangle,
    'Circle': Circle,
    'Hexagon': Hexagon,
    'Triangle': Triangle,
    }

    def __init__(self):
        self.shapes = []
        self.load_from_json(self.FILE_NAME)
    
    def get_new_id(self):
        if not self.shapes:
                return 1
        
        return max(shape.shape_id for shape in self.shapes) + 1
    
    def create_shape(self, shape: str, data: dict):
        data['shape_id'], data['shape_type'] = self.get_new_id(), shape
        try:
            new_shape = self.SHAPES[shape](**data)
        except ValueError:
            return False
        
        self.shapes.append(new_shape)
        self.save_to_json(self.FILE_NAME)

        return True
    def show_shape(self, shape):
        shape_dict = shape.to_dict()['shape_values']
        dict_str = '\n'.join([f"{k.capitalize()}: {v}" for k, v in shape_dict.items()])
        shape_str = f"""
                Shape #{shape.shape_id} [{shape.shape_type}]
                ----------
                {dict_str}
                Area: {shape.get_area():.2f}
                Parimeter: {shape.get_perimeter():.2f}
                """
        return shape_str
    
    def get_all_shapes(self):
        output_list = []
        if not self.shapes:
            return None
        
        for shape in self.shapes:
            shape_str = self.show_shape(shape)
            output_list.append(shape_str)
        return output_list
    
    def update_shape(self, shape_id: int, new_data: dict):
        shape = self.get_shape_by_id(shape_id)
        if shape:
            for k, v in new_data.items():    
                setattr(shape, k, v)
            self.save_to_json(self.FILE_NAME)
            return True
        
    def delete_shape(self, shape_id):
        shape = self.get_shape_by_id(shape_id)
        if shape:
            self.shapes.remove(shape)
            self.save_to_json(self.FILE_NAME)
            return True
    
    def save_to_json(self, file_name):
        if self.shapes:
            data = [shape.to_dict() for shape in self.shapes]
        else:
            data = []
            
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_json(self, file_name):
        
        try:
            with open(file_name, 'r') as f:
                data = json.load(f)
            
            self.shapes = []
            for item in data:
                shape_type = item.get('shape_type')
                shape_args = item.get('shape_values', {})

                if 'shape_id' in item:
                    shape_args['shape_id'], shape_args['shape_type'] = item['shape_id'], item['shape_type']
                
                if shape_type in self.SHAPES:
                    shape = self.SHAPES[shape_type](**shape_args)
                    self.shapes.append(shape)
            
        except FileNotFoundError, json.JSONDecodeError:
            self.shapes = []

    def get_shape_by_id(self, shape_id: int):
        for shape in self.shapes:
            if shape.shape_id == shape_id:
                return shape
            
    def remove_all_shapes(self):
        self.shapes = []
        self.save_to_json(self.FILE_NAME)