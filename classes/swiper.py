from types import NoneType
import pyautogui as py
import threading
from time import sleep
import random

from configs import config


class Swiper:

    def __init__(self, reference_image: str, direction_str: str, direction_list: list):

        self.reference_image = config.TAP_CIRCLE_PATH
        self.__direction_str = direction_str
        self.__direction_list = direction_list

        self.__running = False

        self.thread = None


         

    def start_deamon(self):

        print(f"Starting swiper for {self.__direction_str}")

        self.__running = True

        self.thread = threading.Thread(target=self.__run)
        self.thread.start()

 

    def stop_daemon(self):
            
            self.__running = False
    

            self.thread.kill()
            self.thread.join()



    def __run(self):

        print(f"Checking for swipe {self.__direction_str}")

        while self.__running:

            # Swipe all directions

            offset = 20
            duration = 0.2
            button = 'left'

            py.drag(0, offset, duration=duration, button=button)
            py.drag(0, -offset, duration=duration, button=button)
            py.drag(offset, 0, duration=duration, button=button)
            py.drag(-offset, 0, duration=duration, button=button)
            sleep(0.1)


            # location = py.locateOnScreen(self.reference_image, grayscale=True, confidence=0.9)


            # if location is None:
            #     pass 

            # elif len(location) > 0:

            #     print(f"Swiping {self.__direction_str}")

            #     py.drag(self.__direction_list[0], self.__direction_list[1], duration=0.01, button='left')

            # sleep(random.randint(config.MIN_RANDOM_WAIT, config.MAX_RANDOM_WAIT)/config.RANDOM_WAIT_DENOMINATOR) #sleeps random amount to help offset from other threads