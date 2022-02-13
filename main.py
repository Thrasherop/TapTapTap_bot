from time import sleep

from classes.director import Director



if __name__ == "__main__":

    print("delaying for 3 seconds")
    sleep(3)


    print("Starting director")
    director = Director()
    director.start_all()
    