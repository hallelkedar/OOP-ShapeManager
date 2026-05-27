from square import Square
from rectangle import Rectangle
from circle import Circle
import json

class ShapeManager:
    FILE_NAME = 'shapes.json'
    SHAPES = {
    'Square': Square,
    'Rectangle': Rectangle,
    'Circle': Circle
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
        
    def get_all_shapes(self):
        output_list = []
        for shape in self.shapes:
            shape_dict = shape.to_dict()['values']
            dict_str = '\n'.join([f"{k.capitalize()}: {v}" for k, v in shape_dict.items()])
            shape_str = f"""
                    Shape #{shape.shape_id} [{shape.shape_type}]
                    ----------
                    {dict_str}
                    """
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
        
        data = [shape.to_dict() for shape in self.shapes]

        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_json(self, file_name):
        
        try:
            with open(file_name, 'r') as f:
                data = json.load(f)
            
            self.shapes = []
            for item in data:
                shape_type = item.get('shape_type')
               
                shape_args = item.get('values', {})

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
            