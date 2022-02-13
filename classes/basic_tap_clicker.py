from types import NoneType
import pyautogui as py
import threading
from time import sleep
import random

from configs import config


class BasicTapClicker:

    def __init__(self):

        self.reference_image = config.TAP_CIRCLE_PATH


        self.__running = False

        self.thread = None

         

    def start_deamon(self):

        print("Starting basic tap clicker")
        
        self.__running = True

        self.thread = threading.Thread(target=self.__run)
        self.thread.start()

 

    def stop_daemon(self):
            
            self.__running = False
    

            self.thread.kill()
            self.thread.join()



    def __run(self):

        print("checking basic tap")

        while self.__running:


            location = py.locateOnScreen(self.reference_image, grayscale=True, confidence=config.TAP_CIRCLE_CONFIDENCE)


            if location is None: # or type(location) is NoneType:
                pass

            elif len(location) > 0:

                print(location)

                x, y, width, height = location

                py.click(x + config.TAP_OFFSET, y + config.TAP_OFFSET)


            #sleep(random.randint(config.MIN_RANDOM_WAIT, config.MAX_RANDOM_WAIT)/config.RANDOM_WAIT_DENOMINATOR) #sleeps random amount to help offset from other threads
            sleep(config.TAP_SLEEP)


            