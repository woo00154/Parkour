class InputHandler:
    
    def __init__(self):
        self.button_list = {}

    def clicked(self,button):
        return True
    
    def pressed(self,button):
        return True
    
    def released(self,button):
        return True
    
    def add_button(self,button):
        self.button_list.setdefault(button,False)
