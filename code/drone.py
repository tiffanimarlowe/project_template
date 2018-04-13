import numpy as np
from random import shuffle
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    #needs distance, speeds, make so 100, to 1000 packages, weight displacement for packages
    #needs: time,

    def packages(amount_of_orders):
        weight = []

        #randomly creating a weight distr using .5 as a low and 8 as a high
        # and using amount of orders for the size.
        for i in range(0,amount_of_orders):
            pack_weight = np.random.uniform(.5, 8)
            weight.insert(i,pack_weight)

        return weight

    #print(packages(10)) #prints a list of weights

    def distance(amount_of_orders):

        dist = []

        for i in range(0,amount_of_orders):
            dist_distr = np.random.uniform(5280, 10 * 5280)
            dist.insert(i,dist_distr)

        return dist

    def speed(amount_of_orders):
        veloctity = []
        for i in range(0, amount_of_orders):
            speeed = 85.0667 #ft/s
            veloctity.insert(i,speeed)
        return veloctity

    def drone(num_drones):
        quad = []
        for i in range(0,num_drones):
            battery_life = 7500
            quad.insert(i,battery_life)

        return quad



    def flight(amount_of_orders, num_drones):

        drones = drone(num_drones)

        if drones[0] > 7200:


            velocity = speed(amount_of_orders)
            dist = distance(amount_of_orders)
            bat_life = drone(num_drones)

            time = dist / velocity

            total_flight_time = sum(time)

            if total_flight_time > 7200: #2hrs
                drones[0] = drones[0] - total_flight_time

                #adding more time for charging
                if drone[1] < 7200 or drone[2] < 7200:
                    drone[1] = drone[1] + 4000
                    drone[2] = drone[2] +4000

                    #setting the battery time to 7500 if it is over 7500
                    if drone[1] > 7500:
                        drone[1] = 7500:
                    if drone[2] > 7500:
                        drone[2] = 7500:

        elif drone[1] > 7200:

            velocity = speed(amount_of_orders)
            dist = distance(amount_of_orders)
            bat_life = drone(num_drones)

            time = dist / velocity

            total_flight_time = sum(time)

            if total_flight_time > 7200: #2hrs
                drones[1] = drones[1] - total_flight_time
                drones[0] = drones[0] + 4000

                if drone[0] > 7500:
                    drone[0] = 7500

        elif drone[2] > 7200:

            velocity = speed(amount_of_orders)
            dist = distance(amount_of_orders)
            bat_life = drone(num_drones)

            time = dist / velocity

            total_flight_time = sum(time)

            if total_flight_time > 7200:  # 2hrs
                drones[2] = drones[2] - total_flight_time
                drones[0] = drones[0] + 4000
                drones[1] = drones[1] + 4000

                if drone[0] > 7500:
                    drone[0] = 7500
                if drone[1] > 7500:
                    drone[1] = 7500



            if bat_life[0]
            bat_life[0] = bat_life[0] - 7200
            if bat_life[0] < 0:
                bat_life[0] = 0

            #needs to charge after next delivery





    def distance(num_orders):

        return dist

if __name__ == "__main__":
    main()