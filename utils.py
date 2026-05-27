class Utils:
    
    @staticmethod
    def validation_input(input_type, req_msg, shapes=None, choice_range=None):
        while True:
            choice = input(req_msg)
            if input_type.lower() == 'number':
                if choice.isdigit():
                    choice_num = int(choice)
                    if choice_range:
                        if 0 < choice_num < choice_range+1:
                            return choice_num
                    
                    elif choice_num > 0:
                        return choice_num
                    
            elif input_type.lower() == 'shape':
                shape_type = choice.capitalize()
                if shape_type in shapes:
                    return shape_type
            
            print("Invalid input.")