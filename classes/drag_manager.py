import threading
import pyautogui as py
import random
from time import sleep

from configs import config
from classes.drag import Drag

class Drag_Manager:

    def __init__(self):
        
        self.__running = False
        
        pass

    def start_deamon(self):

        print("Starting drag manager")

        self.__running = True

        self.thread = threading.Thread(target=self.__run)
        self.thread.start()

    def __run(self):

        print("checking for drag")

        while self.__running:

            # Finds the location of the drag circle
            locations = list(py.locateOnScreen(image=config.DRAG_CIRCLE_PATH, grayscale=True, confidence=config.DRAG_CIRCLE_CONFIDENCE))

            print(locations)
            print(type(locations))

            if locations is not None:
                
                x, y, w, h = locations

                # Gets the color of the drag circle
                color = py.pixel(x + config.DRAG_PIXEL_OFFSET, y + config.DRAG_PIXEL_OFFSET)
                print("Drag color: " + str(color))

                # Creates drag object
                this_drag = Drag(cords=[x + w/2, y + h/2], color=color)
                this_drag.drag_drop()

                print("No more drag circles")

            
            sleep(random.randint(config.MIN_RANDOM_WAIT, config.MAX_RANDOM_WAIT)/config.RANDOM_WAIT_DENOMINATOR) #sleeps random amount to help offset from other threads
