class Utils:
    
    @staticmethod
    def validation_input(input_type, req_msg, shapes=None):
        while True:
            choice = input(req_msg)
            if input_type.lower() == 'number':
                if choice.isdigit():
                    if choice > 0:
                        return choice
                    
            elif input_type.lower() == 'shape':
                if choice in shapes:
                    return choice
            
            print("Invalid input.")