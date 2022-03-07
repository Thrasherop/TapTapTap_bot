from email import generator
import pyautogui as py


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