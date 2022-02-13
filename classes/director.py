import threading
import pyautogui as py
from time import sleep

from classes.basic_tap_clicker import BasicTapClicker
from classes.swiper import Swiper
from classes.drag_manager import Drag_Manager

from configs import config


class Director:

    def __init__(self):

        self.swiper = Swiper(config.SWIPE_UP_PATH, config.SWIPE_UP_DIRECTION_STR, config.SWIPE_UP_DIRECTION_LIST)
        self.basic_tap_clicker = BasicTapClicker()
        self.drag_manager = Drag_Manager()



    def start_all(self):

            # Starts all the objects
            self.swiper.start_deamon()
            self.basic_tap_clicker.start_deamon()
            self.drag_manager.start_deamon()

            
