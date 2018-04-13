import numpy as np
from random import shuffle
import seaborn as sns
import matplotlib.pyplot as plt
import math


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
        #if the first drone is charged go!
        if drones[0] > 7200:


            velocity = speed(amount_of_orders)
            dist = distance(amount_of_orders)

            time = [int(dist) / int(velocity) for dist, velocity in zip(dist, velocity)]

            total_flight_time = sum(time)

            if total_flight_time > 7200: #2hrs
                drones[0] = drones[0] - total_flight_time

                #adding more time for charging
                if drones[1] < 7200:
                    drones[1] = drone[1] + 4000
                    # setting the battery time to 7500 if it is over 7500
                    if drones[1] > 7500:
                        drones[1] = 7500

                if drones[2] < 7200:
                    drones[2] = drones[2] +4000
                    if drones[2] > 7500:
                        drones[2] = 7500

        elif drones[1] > 7200:

            velocity = speed(amount_of_orders)
            dist = distance(amount_of_orders)

            time = [int(dist) / int(velocity) for dist, velocity in zip(dist, velocity)]

            total_flight_time = sum(time)

            if total_flight_time > 7200: #2hrs
                drones[1] = drones[1] - total_flight_time
                drones[0] = drones[0] + 4000

                if drones[0] > 7500:
                    drones[0] = 7500

        elif drones[2] > 7200:

            velocity = speed(amount_of_orders)
            dist = distance(amount_of_orders)


            time =[int(dist)/ int(velocity) for dist, velocity in zip(dist, velocity)]

            total_flight_time = sum(time)

            if total_flight_time > 7200:  # 2hrs
                drones[2] = drones[2] - total_flight_time
                drones[0] = drones[0] + 4000
                drones[1] = drones[1] + 4000

                if drones[0] > 7500:
                    drones[0] = 7500
                if drones[1] > 7500:
                    drones[1] = 7500
        # setting time into hours
        time = [x / 120 for x in time]

        average = sum(time) / len(time)
        maxtime = max(time)
        mintime = min(time)


        return time , dist, average, maxtime, mintime


    #running Simulation
    for i in range(0,100):

        t, d, avg, maxim, minim  = flight(100,3)



        plt.scatter(i, avg, alpha = .8,c = "green")
        plt.scatter(i, maxim, alpha = .5, c= "blue")
        plt.scatter(i, minim, alpha=.5, c="red")

        #print(t, 'running')

    plt.legend([" Average" ,"Max", "Min"], loc=1, bbox_to_anchor=(1.15, 0.40))
    plt.show()







if __name__ == "__main__":
    main()