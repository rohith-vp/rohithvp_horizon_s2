# Author : Rohith V P
# Program for calculating ditsance rover must travel
# when going from (x1,y1) to (x2, y2)

from math import sqrt


def distance_calculate():

    try:
        # Input coordinate values
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
    except ValueError:
        # If user enters an invalid character
        print("Invalid value entered")
        return

    # Calculate distance using distance formula
    d = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    # ROund the floatingpoint
    d = round(d, 2)

    print(f"Distance to destination: {d} m")


# Run only if program is run directly, for modularity
if __name__ == "__main__":
    distance_calculate()
