# General configuration for the project
WINDOW_SIZE = "1600 x 900" # This isn't actually used anywhere. It's just here for reference.

# Confidences
DRAG_CIRCLE_CONFIDENCE = 0.7
TAP_CIRCLE_CONFIDENCE = 0.7


# Global configs for classes
MIN_RANDOM_WAIT = 1 
MAX_RANDOM_WAIT = 3
RANDOM_WAIT_DENOMINATOR = 100


# Basic tap circle configuration
TAP_CIRCLE_PATH = "sample/tap_circle.png"
TAP_OFFSET = 100
TAP_SLEEP = 0.1


# Swipe up configuration
SWIPE_UP_PATH = "sample/swipe_up.png"
SWIPE_UP_DIRECTION_STR = "UP"
SWIPE_UP_DIRECTION_LIST = [0, -50]


# Swipe down configuration
SWIPE_DOWN_PATH = "sample/swipe_down.png"
SWIPE_DOWN_DIRECTION_STR = "DOWN"
SWIPE_DOWN_DIRECTION_LIST = [0, 50]

# Swipe left configuration
SWIPE_LEFT_PATH = "sample/swipe_left.png"
SWIPE_LEFT_DIRECTION_STR = "LEFT"
SWIPE_LEFT_DIRECTION_LIST = [-50, 0]

# Swipe right configuration
SWIPE_RIGHT_PATH = "sample/swipe_right.png"
SWIPE_RIGHT_DIRECTION_STR = "RIGHT"
SWIPE_RIGHT_DIRECTION_LIST = [50, 0]

# Drag drop configs
DRAG_CIRCLE_PATH = "sample/drag.png"