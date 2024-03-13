from pynput import mouse
import pyautogui
import time
import random

class ListOperation:
    @staticmethod
    def make_2d_list(row: int, col: int):
        created_list = []
        temp = [0]*col

        for i in range(0, row):
            created_list.append(temp.copy())
        return created_list


class BlockOperation:
    __counter = 0
    COL = 6
    ROW = 5
    __l_w_param = None
    __l_w_diff: ["distance_x", "distance_y"] = None
    __block5x6: ["存放每個珠子的座標"] = None

    def __init__(self, left_up_pos: ["x", "y"], right_down_pos: ["x", "y"]): 
        self.__l_w_param = [left_up_pos, right_down_pos]
        self.__distance_calculate()

        # self.__block5x6 = [[[0,0]]*self.COL]*self.ROW
        self.__block5x6 = ListOperation.make_2d_list(self.ROW, self.COL)
        self.__split_block()
    
    # def __init__(self):
    #     self.__init__([0,0], [1080,1920])
    
    def __distance_calculate(self):
        distance_x = abs(self.__l_w_param[0][0]-self.__l_w_param[1][0])
        distance_y = abs(self.__l_w_param[0][1]-self.__l_w_param[1][1])
        self.__l_w_diff = [distance_x, distance_y]

    def __split_block(self):
        half_per_block_x = self.__l_w_diff[1]/12
        half_per_block_y = self.__l_w_diff[0]/10

        for i in range(0, self.ROW):
            y = self.__l_w_param[0][1]+(2*i+1)*half_per_block_y

            for j in range(0, self.COL):
                x = self.__l_w_param[0][0]+(2*j+1)*half_per_block_x
                self.__block5x6[i][j] = [x, y]
    
    def get_block5x6(self):
        return self.__block5x6.copy()

class GetMousePos(mouse.Listener):
    __my_pos = []

    def __init__(self):
        mouse.Listener.__init__(self, on_click=self.__on_click)
        self.start()
    
    def __on_click(self, x, y, button, pressed):
        if(pressed == False):
            self.__my_pos.append([x,y])
            return False
    
    def get_pos(self):
        return self.__my_pos.copy()

class MouseControl():
    def detect_mouse_pos(self):
        mouse_pos = GetMousePos()
        mouse_pos.join()
        return mouse_pos.get_pos()
    
    def set_mouse_pos(self, pos: [[float],[float]]):
        this_mouse = mouse.Controller()
        this_mouse.position = pos
    
    def drag(self, pos: [[float], [float]]):
        pyautogui.dragTo(pos[0]+random.uniform(0.0, 10.0), pos[1]+random.uniform(0.0, 10.0), random.uniform(0.3,0.8), button="left")

    def one_turn(self, pos_start, pos_end):
        duration = random.uniform(0.3, 0.7)
        pyautogui.moveTo(pos_start[0], pos_end[1]+random.uniform(0.0,10.0), duration)
        pyautogui.moveTo(pos_end[0]+random.uniform(0.0,10.0), pos_end[1]+random.uniform(0.0,10.0), duration)

    def click(self, pos):
        pyautogui.click(pos[0], pos[1])

class Robot:
    __my_mouse: MouseControl = None
    __my_operation: BlockOperation = None
    __block5x6 = None
    __moon_pos = [1384, 431]

    def __init__(self):
        self.__my_mouse = MouseControl()
    
    def start(self):
        # self.__my_mouse.detect_mouse_pos()
        # detect_pos = self.__my_mouse.detect_mouse_pos()
        # self.__my_operation = BlockOperation(detect_pos[0], detect_pos[1])
        self.__my_operation = BlockOperation([1261, 505], [1769, 925])
        self.__block5x6 = self.__my_operation.get_block5x6()
        print(self.__block5x6)

    def play_game(self):
        # a = int(input("Floor: "))
        a = 9
        for i in range(0, a):
            print("第 {0} 回合".format(i+1))
            if(i < a-2):
                self.__my_mouse.set_mouse_pos(self.__moon_pos)
                time.sleep(0.5)
                self.move_moon()

            elif(i == a-2):
                self.moon_skill_turn_on()
            elif(i == a-1):
                self.skill_turn_on([1478, 427], None, [1411, 603])

            if(i >= a-2):
                time.sleep(2)
                self.__my_mouse.set_mouse_pos(self.__block5x6[0][4])
                self.__my_mouse.drag(self.__block5x6[0][5])

            time.sleep(random.uniform(11.0, 16.0))
            if(i == a-2 or i == a-3):
                time.sleep(5)
        print("關卡結束")
        time.sleep(15)
        print("升等確認")
        self.level_up_check()
        time.sleep(5)
        self.__my_mouse.click([1665, 600])
        time.sleep(5)
        print("再次挑戰")
        self.challenge_again()
        time.sleep(5)
        print("體力確認")
        self.stamina_check()
        time.sleep(3)
        self.__my_mouse.click(self.__block5x6[1][3])
        time.sleep(5)
        print("進入戰鬥")
        self.get_in_battle()

    def move_moon(self):
        pyautogui.mouseDown()
        time.sleep(1.5)
        self.__my_mouse.one_turn(self.__moon_pos, [1298,543])
        pyautogui.mouseUp()

    def skill_turn_on(self, cha_pos, skill_pos, check_pos):
        self.__my_mouse.click(cha_pos)
        time.sleep(0.5)

        if(skill_pos != None):
            self.__my_mouse.click(skill_pos)
            time.sleep(0.5)

        self.__my_mouse.click(check_pos)

    def moon_skill_turn_on(self):
        # self.skill_turn_on(self.__moon_pos, [1515, 719], [1410, 880])
        self.skill_turn_on(self.__moon_pos, [1506, 611], [1421, 764])
        time.sleep(2)
        self.skill_turn_on(self.__moon_pos, [1506, 611], [1421, 812])

    def challenge_again(self):
        self.__my_mouse.click([1665, 600])

    def level_up_check(self):
        self.__my_mouse.click([1665, 600])
    
    def stamina_check(self):
        self.__my_mouse.click([1554, 607])
        time.sleep(1)
        self.__my_mouse.click([1413, 861])

    def get_in_battle(self):
        self.__my_mouse.click([1694, 919])

robot = Robot()
robot.start()
counter = 0
while True:
    robot.play_game()
    counter += 1
    time.sleep(20)

    if(counter > 0):
        print("程式結束")
        break
    
# def on_click(x, y, button, pressed):
#     # print("x = {0}, y = {1}, pressed = {2}, button = {3}".format(x, y, pressed, button))
#     if(pressed == False):
#         global l_w_param, counter
#         l_w_param[counter] = [x,y]
#         counter += 1
#         print("x={0}, y={1}".format(x,y))
    
#     if(counter >= 2):
#         return False

# def mouse_listener():
#     with mouse.Listener(on_click=on_click) as listener:
#         listener.join()

# mouse_listener()
# a = [0,0]
# b = [1080, 1920]
# test = BlockOperation(a, b)
# print(test.get_block5x6())