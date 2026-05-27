from utils import Utils
from shape_manager import ShapeManager

SHAPES = {
        'Square': ['side'],
        'Rectangle': ['length',
                      'width'
                      ],
        'Circle': ['radius']
    }

MENU = """
    1. Add shape 
    2. Show all shapes
    3. Update shape
    4. Delete shape
    5. Exit
    """

def handle_create_shape():
    shape = Utils.validation_input('shape', 'Enter your shape: ').capitalize()
    data = {}
    if shape.lower() == 'square':
        side = Utils.validation_input('number', 'Enter the side square: ')
        data['side'] = side
        
    elif shape.lower() == 'rectangle':
        length = Utils.validation_input('number', 'Enter the length rectangle: ')
        width = Utils.validation_input('number', 'Enter the width rectangle: ')
        data['length'], data['width'] = length, width

    elif shape.lower() == 'circle':
        radius = Utils.validation_input('number', 'Enter the radius circle: ')
        data['radius'] = radius

    return shape, data

def get_shape_update():
    id = Utils.validation_input('number', 'Enter shape id: ')
    new_data = {}
    shape = ShapeManager.get_shape_by_id(id)
    for value in shape['values']:
        new_value = Utils.validation_input('number', f'Enter new {value}: ')
        new_data[value] = new_value
    return id, new_data

