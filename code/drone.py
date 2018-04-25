import numpy as np
from random import shuffle
import seaborn as sns
import matplotlib.pyplot as plt
import math
from scipy.stats import norm
import matplotlib.mlab as mlab

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
        pythagorean = []
        xhomes = []
        yhomes = []
        x1 = y1 = 0
        start = [x1, y1]
        for i in range(0,amount_of_orders):
            #dist_distr = np.random.uniform(5280, 10 * 5280)
            #dist.insert(i,dist_distr)

            x = np.random.uniform(0,20*5280)
            y = np.random.uniform(0,20*5280)
            xhomes.insert(i,x)
            yhomes.insert(i,y)

            mrEuclid =np.sqrt( (x-x1)**2 + (y-y1)**2 )
            pythagorean.insert(i,mrEuclid)

        return pythagorean , xhomes, yhomes

    def speed(amount_of_orders):
        veloctity = []
        for i in range(0, amount_of_orders):

            dist , x, y = distance(amount_of_orders)
            #print(dist)

            if dist[i] < 7*5280:
                #low range
                speeed = 60 #ft/s
                veloctity.insert(i, speeed)
            elif 7*5280 < dist[i] < 14*5280:
                #Med Range
                speeed = 50 #ft/s
                veloctity.insert(i, speeed)
                #High Range
            elif 14*5280 > dist[i]:
                speeed = 50 #ft/s
                veloctity.insert(i, speeed)
        return veloctity

    def drone(num_drones):
        quad = []
        for i in range(0,num_drones):
            battery_life = 3600
            quad.insert(i,battery_life)

        return quad

    def flight(amount_of_orders, num_drones):

        drones = drone(num_drones)
        #if the first drone is charged go!
        avgflighttime = 3200 #little less than 1 hour
        maxcapacity = 3600 #maxhour
        charging = .2 * 3600 #20 percent charge in 1 hour
        time = []
        total_flight_time = 0
        whichdrone = []

        #####START HERE NEXT TIME need to figure out switching drones
        if drones[0] > avgflighttime:

            velocity = speed(amount_of_orders)
            dist , xhomes, yhomes = distance(amount_of_orders)

            time = [int(dist) / int(velocity) for dist, velocity in zip(dist, velocity)]
            for i in range(0, len(time)):

                total_flight_time = time[i] + total_flight_time

                #total_flight_time = sum(time)
                print(total_flight_time, ' flight time')

                drones[0] = drones[0] - total_flight_time
                print("drone 0", drones[0])


                if drones[0] < avgflighttime:
                    #using first drone
                    whichdrone.append(1)

                elif drones[0] > avgflighttime:
                    #switching drone
                    whichdrone.append(2)




                if total_flight_time < avgflighttime:
                    drones[0] = drones[0] - total_flight_time
                    print("drone 0", drones[0])

                    #adding more time for charging
                    if drones[1] < avgflighttime:
                        drones[1] = drone[1] + charging
                        # setting the battery time to 7500 if it is over 7500
                        if drones[1] > maxcapacity:
                            drones[1] = maxcapacity

                    if drones[2] < avgflighttime:
                        drones[2] = drones[2] +charging
                        if drones[2] > maxcapacity:
                            drones[2] = maxcapacity





        elif drones[1] > avgflighttime:
            whichdrone.append( 2)
            velocity = speed(amount_of_orders)
            dist, xhomes, yhomes = distance(amount_of_orders)

            time = [int(dist) / int(velocity) for dist, velocity in zip(dist, velocity)]

            total_flight_time = sum(time)

            if total_flight_time > avgflighttime: #2hrs
                drones[1] = drones[1] - total_flight_time
                drones[0] = drones[0] + charging

                if drones[0] > maxcapacity:
                    drones[0] = maxcapacity

        elif drones[2] > avgflighttime:
            whichdrone.append(2)
            velocity = speed(amount_of_orders)
            dist, xhomes, yhomes = distance(amount_of_orders)


            time =[int(dist) / int(velocity) for dist, velocity in zip(dist, velocity)]

            total_flight_time = sum(time)

            if total_flight_time > avgflighttime:  # 2hrs
                drones[2] = drones[2] - total_flight_time
                drones[0] = drones[0] + charging
                drones[1] = drones[1] + charging

                if drones[0] > maxcapacity:
                    drones[0] = maxcapacity
                if drones[1] > maxcapacity:
                    drones[1] = maxcapacity

        # setting time into hours

        time = [x / 3600  for x in time]

        #print(time)

        average = sum(time) / len(time)
        maxtime = max(time)
        mintime = min(time)
        STD = np.std(time)
        beta = whichdrone[0]
        print(beta)

        return time , dist, average, maxtime, mintime, STD, xhomes, yhomes, beta


    #running Monte-Carlo Simulation
    for i in range(0,100):

        t, d, avg, maxim, minim, STD, xhomes, yhomes, beta = flight(100,3)

        plt.subplot(3,1,1)
        plt.scatter(i, avg, alpha = .5,c = "green")
        plt.scatter(i, maxim, alpha = .5, c= "blue")
        plt.scatter(i, minim, alpha=.5, c="red")

        plt.legend([" Average", "Max", "Min"], loc=1, bbox_to_anchor=(1, 0.4))
        plt.ylabel("Time in hours")
        plt.xlabel("Iterations")

        plt.subplot(3, 1, 2)
        num_bins = 10
        n, bins, patches = plt.hist(t, num_bins, normed=1, alpha=0.5)
        y = mlab.normpdf(bins, avg, STD)
        plt.plot(bins, y, 'r--')
        plt.ylabel("Probability")
        plt.xlabel("Delivery Completion Times")


        plt.subplot(3, 1, 3)
        plt.plot(i, beta)


        #plt.plot(t, norm.pdf(t))
        #print(t, 'running')

    plt.show()

    xLocation = [a / 5280 for a in xhomes]
    yLocation = [b / 5280 for b in yhomes]

    plt.scatter(0, 0, color='cyan')
    plt.plot(xLocation, yLocation, 'ro')
    plt.legend(["Customer Homes", "Delivery Facility"], loc=1, bbox_to_anchor=(1, 0.4))

    plt.ylabel('Miles')
    plt.title("Customer Grid Map for the last RUN")
    plt.xlabel('Miles')

    plt.show()


if __name__ == "__main__":
    main()