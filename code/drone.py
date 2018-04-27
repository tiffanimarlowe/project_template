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

            x = np.random.uniform(0,8.5*5280)
            y = np.random.uniform(0,8.5*5280)
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
            else:
                speeed = 50
                veloctity.insert(i,speeed)
        return veloctity

    def drone(num_drones):
        quad = {}
        for i in range(0, num_drones):

            quad[i+1] = 5400


        '''   
        quad = []
        for i in range(0,num_drones):
            battery_life = 3600
            quad.insert(i,battery_life)
        '''

        return quad
    d = drone(3)
    print(d[3])

    def flight(amount_of_orders, num_drones):

        drones = drone(num_drones)
        #if the first drone is charged go!
        needtocharge = 5400 / 2 #half how
        bat_capacity = 5400 #hour 50mins to charge fully
        charging = .5 * 5400 #20 percent charge in 1 hour
        time = []
        total_flight_time = 0
        whichdrone = []
        current_step = 0

        #####START HERE NEXT TIME need to figure out switching drones


        velocity = speed(amount_of_orders)
        print(len(velocity), "VELCOCITY")
        dist , xhomes, yhomes = distance(amount_of_orders)

        time = [int(dist) / int(velocity) for dist, velocity in zip(dist, velocity)]

        for i in range(0, len(time)):
            total_flight_time = time[i] + total_flight_time
            #drone 1 is flying
            print("running 123.....", i)
            print("time", time[i])
            times = 2 * time[i] #accounting for time to and from

            #drone 1 active, checking if its battery capacity is greater than the distance too
            if drones[1] > (times/1800)*5400:
                whichdrone.insert(i, 1)

                #total_flight_time = sum(time)
                #print(total_flight_time, 'drone 1: flight time')

                drones[1] = drones[1] - (times/1800)*5400
                print("drone 1", drones[1])


                #if the first drone needs to charge
                if drones[1] < needtocharge:
                    #using first drone
                    current_step= total_flight_time


                #Charging
                if drones[2] < 5400:
                    drones[2] =  (times/1800*5400) + drones[2]
                    if drones[2] > 5400:
                        drones[2] = 5400
                    print("charging 2 ")

                if drones[3] < 5400:
                    drones[3] = (times/1800*5400)  + drones[3]
                    if drones[3]  > 5400:
                        drones[2] = 5400
                    print("charging 3")


            #drone two is now flying
            elif drones[2] > (times/1800)*5400:
                whichdrone.insert(i, 2)

                print(total_flight_time, 'drone 2: flight time')

                drones[2] = drones[2] - (times/1800)*5400
                print("drone 2", drones[2])
                print("current step", current_step)

                #if drone 2 needs to charge
                if drones[2] < needtocharge:
                    # using first drone
                    current_step = total_flight_time

                    # Charging everyone else
                if drones[1] < 5400:
                    drones[1] = (times/1800*5400)  + drones[1]
                    if drones[1] > 5400:
                        drones[1] = 5400
                        print("charging 2 ")

                    if drones[3] < 5400:
                        drones[3] = (times/1800*5400)  + drones[3]
                        if drones[3] > 5400:
                            drones[3] = 5400
                        print("charging 3")
            #activate drone 3
            elif drones[3] > (times/1800)*5400:
                whichdrone.insert(i, 3)

                print(total_flight_time, 'drone 2: flight time')

                drones[3] = drones[3] - (times/1800)*5400
                print("drone 3", drones[3])
                print("current step", current_step)

                # if drone 3 needs to charge
                if drones[3] < needtocharge:
                    # using first drone
                    current_step = total_flight_time

                    # Charging everyone else
                if drones[1] < 5400:
                    drones[1] = (times/1800*5400)+ drones[1]
                    if drones[1] > 5400:
                        drones[1] = 5400
                        print("charging 2 ")

                    if drones[2] < 5400:
                        drones[2] = (times/1800*5400) + drones[3]
                        if drones[2] > 5400:
                            drones[2] = 5400
                        print("charging 3")



        # setting time into hours

        time = [x / 3600  for x in time]

        #print(time)

        average = sum(time) / len(time)
        maxtime = max(time)
        mintime = min(time)
        STD = np.std(time)
        beta = whichdrone
        print(beta, 'beta')
        print(len(beta), 'length of beta')

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





        #plt.plot(t, norm.pdf(t))
        #print(t, 'running')
    plt.subplot(3, 1, 3)
    plt.plot(beta)
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