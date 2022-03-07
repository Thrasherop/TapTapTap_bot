from types import NoneType
import pyautogui as py
import threading
from time import sleep
import random

from configs import config
#from helpers.helper_functions import *


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

            locations_raw = py.locateAllOnScreen(self.reference_image, grayscale=True, confidence=config.TAP_CIRCLE_CONFIDENCE)

            
            print("Raw locations: ", list(locations_raw)) #these aren't getting passed in
            locations = parse_location(locations_raw, 8)

            

            if locations is not None:

                print(locations)

                for location in locations:
                    x, y, w, h = location
                    py.click(x + w/2, y + h/2)






            # location = py.locateOnScreen(self.reference_image, grayscale=True, confidence=config.TAP_CIRCLE_CONFIDENCE)


            # if location is None: # or type(location) is NoneType:
            #     pass

            # elif len(location) > 0:

            #     print(location)

            #     x, y, width, height = location

            #     py.click(x + config.TAP_OFFSET, y + config.TAP_OFFSET)


            #sleep(random.randint(config.MIN_RANDOM_WAIT, config.MAX_RANDOM_WAIT)/config.RANDOM_WAIT_DENOMINATOR) #sleeps random amount to help offset from other threads
            sleep(config.TAP_SLEEP)


def parse_location(locations, threshhold):
    """
    Parses a location list into corrosponding things
    """

    positions = []
   
    print(type(locations))
    print(locations)

    locations_list = list(locations)
    print(locations_list)

    print("Raw locations: (inside) ", list(locations))

    print("zero locations: " + str((locations)))


    for location in locations:
        print("location: " + str(location))


    for p in locations: #py.locateAllOnScreen( 'image.png', confidence=0.9, grayscale=False ):
        print("First: " + str(p))
        for pos in positions:

            print("Second: " + str(pos))

            if abs( pos['left'] -p['left'] ) > threshhold \
            and abs( pos['top'] -p['top'] ) > threshhold:
                positions .append( pos )

    # for pos in positions:
    #     print( pos )

    return positions