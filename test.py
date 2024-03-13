from pynput import mouse
import time

class GetMousePos(mouse.Listener):
    __my_pos = []

    def __init__(self):
        mouse.Listener.__init__(self, on_click=self.__on_click, on_move=self.__on_move)
        self.start()
    
    def __on_click(self, x, y, button, pressed):
        if(pressed == False):
            self.__my_pos.append([x,y])

    def __on_move(self, x, y):
        print("[{0}, {1}]".format(x,y))
        # time.sleep(0.5)
    
    def get_pos(self):
        return self.__my_pos.copy()
    
a = GetMousePos()
a.join()

    