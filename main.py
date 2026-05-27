from utils import Utils
from shape_manager import ShapeManager

SHAPES = {
        'Square': ['side'],
        'Rectangle': ['length',
                      'width'
                      ],
        'Circle': ['radius']
    }

WELCOME = """
 __      __       .__                                  __          
/  \    /  \ ____ |  |   ____  ____   _____   ____   _/  |_  ____  
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \ 
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/ 
       \/       \/          \/            \/     \/                

 $$$$$$\   $$$$$$\  $$$$$$$\          $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$\  $$$$$$$$\      $$\      $$\  $$$$$$\  $$\   $$\  $$$$$$\   $$$$$$\  $$$$$$$$\ $$$$$$$\  
$$  __$$\ $$  __$$\ $$  __$$\        $$  __$$\ $$ |  $$ |$$  __$$\ $$  __$$\ $$  _____|     $$$\    $$$ |$$  __$$\ $$$\  $$ |$$  __$$\ $$  __$$\ $$  _____|$$  __$$\ 
$$ /  $$ |$$ /  $$ |$$ |  $$ |       $$ /  \__|$$ |  $$ |$$ /  $$ |$$ |  $$ |$$ |           $$$$\  $$$$ |$$ /  $$ |$$$$\ $$ |$$ /  $$ |$$ /  \__|$$ |      $$ |  $$ |
$$ |  $$ |$$ |  $$ |$$$$$$$  |$$$$$$\\$$$$$$\  $$$$$$$$ |$$$$$$$$ |$$$$$$$  |$$$$$\ $$$$$$\ $$\$$\$$ $$ |$$$$$$$$ |$$ $$\$$ |$$$$$$$$ |$$ |$$$$\ $$$$$\    $$$$$$$  |
$$ |  $$ |$$ |  $$ |$$  ____/ \______|\____$$\ $$  __$$ |$$  __$$ |$$  ____/ $$  __|\______|$$ \$$$  $$ |$$  __$$ |$$ \$$$$ |$$  __$$ |$$ |\_$$ |$$  __|   $$  __$$< 
$$ |  $$ |$$ |  $$ |$$ |             $$\   $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |           $$ |\$  /$$ |$$ |  $$ |$$ |\$$$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |
 $$$$$$  | $$$$$$  |$$ |             \$$$$$$  |$$ |  $$ |$$ |  $$ |$$ |      $$$$$$$$\      $$ | \_/ $$ |$$ |  $$ |$$ | \$$ |$$ |  $$ |\$$$$$$  |$$$$$$$$\ $$ |  $$ |
 \______/  \______/ \__|              \______/ \__|  \__|\__|  \__|\__|      \________|     \__|     \__|\__|  \__|\__|  \__|\__|  \__| \______/ \________|\__|  \__|
                                                                                                                                                                     
                                                                                                                                                                                                                                                                                                                                       
"""
MENU = """
    1. Add shape 
    2. Show all shapes
    3. Update shape
    4. Delete shape
    5. Exit
    """

MENU_RANGE = 5

def get_menu_choice():
    choice = Utils.validation_input('number', f'Enter your choice (1-{MENU_RANGE})', choice_range=MENU_RANGE)
    return choice

def get_id_from_user():
    id = Utils.validation_input('number', 'Enter shape id: ')
    return id

def handle_create_shape():
    
    shape = Utils.validation_input('shape', 'Enter your shape: ', SHAPES)

    data = {}

    for field in SHAPES[shape]:
        data[field] = Utils.validation_input(
            'number',
            f'Enter {field}: '
        )

    return shape, data

def get_shape_update(shape_manager):
    
    shape_id = get_id_from_user()
    
    shape = shape_manager.get_shape_by_id(shape_id)
    if not shape:
        return None, None
    
    new_data = {}

    for f in SHAPES[shape.shape_type]:
        new_value = Utils.validation_input('number', f'Enter new {f}: ')
        new_data[f] = new_value
    
    return shape_id, new_data

def main():

    shape_manager = ShapeManager()

    print(WELCOME)

    while True:
        print(MENU)
        choice = get_menu_choice()

        if choice == 1:
            shape, data = handle_create_shape()
            
            new_shape = shape_manager.create_shape(shape=shape, data=data)
            if new_shape:
                print(f'{shape} created succefully')
            else:
                print('Error.')

        elif choice == 2:
            
            all_shapes = shape_manager.get_all_shapes()
            if all_shapes:
                for shape in all_shapes:
                    print(f'{shape}\n')
            else:
                print('There are no shapes.')
        
        elif choice == 3:
            shape_id, new_data = get_shape_update(shape_manager)
            
            if shape_id is None:
                print("Shape not found.")
                continue

            update = shape_manager.update_shape(shape_id=shape_id, new_data=new_data)
            if update:
                print('Shape updated successfully')
            else:
                print('Error.')

        elif choice == 4:
            
            delete = shape_manager.delete_shape(shape_id=get_id_from_user())
            if delete:
                print('Shape deleted successfully')
            else:
                print('Error.')
        
        elif choice == 5:
            print('Goodbye.')
            break
