import threading
import pyautogui as py
import random
from time import sleep

from configs import config

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
            locations = list(py.locateAllOnScreen(image=config.DRAG_CIRCLE_PATH, grayscale=True, confidence=config.DRAG_CIRCLE_CONFIDENCE))

            print(locations)
            print(type(locations))

            if locations is not None:
                for location in locations:
                    print(location)
                print("No more drag circles")

            
            sleep(random.randint(config.MIN_RANDOM_WAIT, config.MAX_RANDOM_WAIT)/config.RANDOM_WAIT_DENOMINATOR) #sleeps random amount to help offset from other threads
