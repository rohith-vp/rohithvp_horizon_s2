# Author : Rohith V P
# Program for calculating total time taken by rover
# when going from (x1,y1) to (x2, y2)

from math import sqrt


def calculate_time_taken():

    try:
        # Input coordinate values
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        
        # Input motion parametrs
        vin = float(input("Enter initial velocity: "))
        acc = float(input("Enter acceleration: "))
        max_speed = float(input("Enter maximum allowd top speed: "))

    except ValueError:
        # If user enters an invalid character
        print("Invalid value entered")
        return

    # Calculate distance using distance formula
    dist_total = sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Print the total distance, using round() for rounding the floating point
    print(f"Distance the rover must travel: {round(dist_total,2)} units")

    # Logic:
    # if there is acceleration, then we have to calculate distance rover travels before reaching top speed
    # if total dist > acc dist, then add acc time and remaining time to get total time
    # if no acceleration, then total time is total distance / initial vel

    # If acceleration is there
    if acc != 0:
        # Calculate time to reach top speed
        time_acc = (max_speed - vin) / acc
        # Calculate distnace covered during acceleration
        dist_acc = vin * time_acc + 0.5 * acc * (time_acc ** 2)

        # If rover reaches top speed before reaching destination
        if dist_total > dist_acc:
            remaining_dist = dist_total - dist_acc
            time_total = time_acc + remaining_dist / max_speed
        # If rover doesnt reach top speed
        else:
            # Using quadratic formula to solve d = vin * t + 0.5 * a * t^2
            disc = vin ** 2 + 2 * acc * dist_total
            time_total = (-vin + sqrt(disc)) / acc

    # If there is no acceeleration
    else:
        # If there is initial vel
        if vin > 0:
            time_total = dist_total / vin
        # If there is no initial vel and no acc then the rover will not move
        else:
            print("Initial vel and acc are 0. Rover will not reach.")
            return
    
    print(f"Total time taken by the rover to reach its destination: {round(time_total,2)}")


# Run only if program is run directly, for modularity
if __name__ == "__main__":
    calculate_time_taken()
