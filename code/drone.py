import numpy as np
from random import shuffle
import seaborn as sns
import matplotlib.pyplot as plt
import math
from scipy.stats import norm
import matplotlib.mlab as mlab
import pandas as pd
from collections import Counter
import random
from itertools import cycle, islice

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

            x = np.random.uniform(0,6*5280)
            y = np.random.uniform(0,6*5280)
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
                speeed = 50 #ft/s
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

    def battery_life(num_drones):
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
    #d = drone(3)
    #print(d[3])

    def flight(amount_of_orders, num_drones):

        drones = battery_life(num_drones)
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
        #print(len(velocity), "VELCOCITY")
        dist , xhomes, yhomes = distance(amount_of_orders)

        time = [int(dist) / int(velocity) for dist, velocity in zip(dist, velocity)]

        for i in range(0, len(time)):
            total_flight_time = time[i] + total_flight_time
            #drone 1 is flying
            #print("running 123.....", i)
            #print("time", time[i])
            times = 2 * time[i] #accounting for time to and from

            #drone 1 active, checking if its battery capacity is greater than the distance too
            if drones[1] > needtocharge:
                whichdrone.insert(i, 1)

                #total_flight_time = sum(time)
                #print(total_flight_time, 'drone 1: flight time')

                drones[1] = drones[1] - (times/1800)*5400
                #print("drone 1", drones[1])


                #if the first drone needs to charge
                if drones[1] < needtocharge:
                    #using first drone
                    current_step= total_flight_time


                #Charging
                if drones[2] < 5400:
                    drones[2] =  (times/1800*5400) + drones[2]
                    if drones[2] > 5400:
                        drones[2] = 5400
                    #print("charging 2 ")

                if drones[3] < 5400:
                    drones[3] = (times/1800*5400)  + drones[3]
                    if drones[3]  > 5400:
                        drones[3] = 5400
                    #print("charging 3")


            #drone two is now flying
            elif drones[2] > needtocharge:
                whichdrone.insert(i, 2)

                #print(total_flight_time, 'drone 2: flight time')

                drones[2] = drones[2] - (times/1800)*5400
                #print("drone 2", drones[2])
                #print("current step", current_step)

                #if drone 2 needs to charge
                if drones[2] < needtocharge:
                    # using first drone
                    current_step = total_flight_time

                    # Charging everyone else
                if drones[1] < 5400:
                    drones[1] = (times/1800*5400)  + drones[1]
                    if drones[1] > 5400:
                        drones[1] = 5400
                        #print("charging 1 ")

                    if drones[3] < 5400:
                        drones[3] = (times/1800*5400)  + drones[3]
                        if drones[3] > 5400:
                            drones[3] = 5400
                        #print("charging 3")
            #activate drone 3
            elif drones[3] > needtocharge:
                whichdrone.insert(i, 3)

                #print(total_flight_time, 'drone 2: flight time')

                drones[3] = drones[3] - (times/1800)*5400
                #print("drone 3", drones[3])
                #print("current step", current_step)

                # if drone 3 needs to charge
                if drones[3] < needtocharge:
                    # using first drone
                    current_step = total_flight_time

                    # Charging everyone else
                if drones[1] < 5400:
                    drones[1] = (times/1800*5400)+ drones[1]
                    if drones[1] > 5400:
                        drones[1] = 5400
                        #print("charging 1 ")

                    if drones[2] < 5400:
                        drones[2] = (times/1800*5400) + drones[3]
                        if drones[2] > 5400:
                            drones[2] = 5400
                        #print("charging 3")



        # setting time into hours

        time = [x / 3600  for x in time]
        dist = [2 * x / 5280 for x in dist]

        #doubling to take in the trip back into account
        time = time * 2

        #print(time)

        average = sum(time) / len(time)
        maxtime = max(time)
        mintime = min(time)
        STD = np.std(time)
        beta = whichdrone
        all = Counter(beta)
        uno = beta.count(1)
        dos = beta.count(2)
        tres = beta.count(3)

        #print(beta, 'beta')
        #print(len(beta), 'length of beta')

        return time , dist, average, maxtime, mintime, STD, xhomes, yhomes, beta, uno, dos, tres, all

    uno_list = []
    dos_list = []
    tres_list = []
    delivery_distance = []
    def monte(num_runs):

        #running Monte-Carlo Simulation
        for i in range(0,num_runs):
            print(i, "running")

            t, d, avg, maxim, minim, STD, xhomes, yhomes, beta,uno, dos, tres, all = flight(200,3)
            uno_list.insert(i,uno)
            dos_list.insert(i, dos)
            tres_list.insert(i, tres)
            delivery_distance.insert(i,d)

            plt.subplot(3,1,1)
            plt.scatter(i, avg, alpha = .5,c = "green")
            plt.scatter(i, maxim, alpha = .5, c= "blue")
            plt.scatter(i, minim, alpha=.5, c="red")

            plt.legend([" Average", "Max", "Min"], loc=1, bbox_to_anchor=(1, 0.4))
            plt.title("Average, Max, and Min Delivery Times over Simulated Iterations")
            plt.ylabel("Time in hours")
            plt.xlabel("Iterations")


            dist_avg = np.average(delivery_distance)
            dist_std = np.std(delivery_distance)

            avg_1 = sum(uno_list) / len(uno_list)
            avg_2 = sum(dos_list) / len(dos_list)
            avg_3 = sum(tres_list) / len(tres_list)

            std_1 = np.std(uno_list)
            std_2 = np.std(dos_list)
            std_3 = np.std(tres_list)
        return avg_1,avg_2,avg_3,std_1,std_2,std_3,t, d, avg, maxim, minim, STD, xhomes, yhomes, beta,uno, dos, tres, all, dist_avg,dist_std

    num_runs = 1000
    avg_1, avg_2, avg_3, std_1, std_2, std_3, t, d, avg, maxim, minim, STD, xhomes, yhomes, beta, uno, dos, tres, all,dist_avg,dist_std = monte(num_runs)
    #Monte-carlo plots AVG,MIN,MAX and PDF of Completetion times
    plt.subplot(3, 1, 2)
    num_bins = 10
    n, bins, patches = plt.hist(t, num_bins, normed=1, alpha=0.5)
    y = mlab.normpdf(bins, avg, STD)
    plt.plot(bins, y, 'r--')
    plt.ylabel("Probability")
    plt.title(" Delivery Completion Times PDF")
    plt.xlabel("Time in hours")

    plt.subplot(3,1,3)
    num_bins = 10
    n, bins, patches = plt.hist(t, num_bins, normed=1, alpha=0.5, cumulative = True)
    y = mlab.normpdf(bins, avg, STD).cumsum()
    plt.title('CDF of Delivery Completion Times')
    plt.xlabel("Times in Hours")
    plt.ylabel("Probabilty")
    plt.plot(bins, y, 'r--')

    plt.show()



    #print("drone 1", uno)

    plt.subplot(3, 1, 1)
    num_bins = 10
    n, bins, patches = plt.hist(uno_list, num_bins, normed=1, alpha=0.5)
    y = mlab.normpdf(bins, avg_1, std_1)
    plt.title('PDF of Drone 1 Usage')
    plt.ylabel("Times Used")
    plt.xlabel("Probabilty")
    plt.plot(bins, y, 'r--')

    plt.subplot(3, 1, 2)
    num_bins = 10
    n, bins, patches = plt.hist(dos_list, num_bins, normed=1, alpha=0.5)
    y = mlab.normpdf(bins, avg_2, std_2)
    plt.title('PDF of Drone 2 Usage')
    plt.ylabel("Times Used")
    plt.xlabel("Probabilty")
    plt.plot(bins, y, 'r--')

    plt.subplot(3, 1, 3)
    num_bins = 10
    n, bins, patches = plt.hist(tres_list, num_bins, normed=1, alpha=0.5)
    y = mlab.normpdf(bins, avg_3, std_3)
    plt.title('PDF of Drone 3 Usage')
    plt.ylabel("Times Used")
    plt.xlabel("Probabilty")
    plt.plot(bins, y, 'r--')
    plt.show()

    plt.subplot(3,1,1)
    n, bins, patches = plt.hist(uno_list, num_bins, normed=1, alpha=0.5, cumulative=True)
    y = mlab.normpdf(bins, avg_1, std_1).cumsum()
    y /= y[-1]
    plt.plot(bins, y)
    plt.title('CDF of Drone 1 Utilization')
    plt.xlabel("Times Used")
    plt.ylabel("Probabilty")

    plt.subplot(3, 1, 2)
    n, bins, patches = plt.hist(dos_list, num_bins, normed=1, alpha=0.5, cumulative=True)
    y = mlab.normpdf(bins, avg_2, std_2).cumsum()
    y /= y[-1]
    plt.plot(bins, y)
    plt.title('CDF of Drone 2 Utilization')
    plt.xlabel("Times Used")
    plt.ylabel("Probabilty")

    plt.subplot(3, 1, 3)
    n, bins, patches = plt.hist(tres_list, num_bins, normed=1, alpha=0.5, cumulative=True)
    y = mlab.normpdf(bins, avg_3, std_3).cumsum()
    y /= y[-1]
    plt.plot(bins, y)
    plt.title('CDF of Drone 3 Utilization')
    plt.xlabel("Times Used")
    plt.ylabel("Probabilty")
    plt.show()

    plt.subplot(2, 1, 1)
    plt.plot(beta)
    plt.xlabel("Packages/Orders", )
    plt.title("Drone Frequency Usage")

    plt.ylabel("Drones")

    plt.subplot(2,1,2)
    plt.bar(1,avg_1)
    plt.bar(2,avg_2)
    plt.bar(3,avg_3)
    plt.legend([(' Drone 1 ', uno), (' Drone 2 ', dos), (' Drone 3 ',tres)])
    plt.title('Drone Delivery Utilization')
    plt.xlabel('DRONES')
    plt.ylabel('Times Used')


    plt.show()



    plt.subplot(1,1,1)
    xLocation = [a / 5280 for a in xhomes]
    yLocation = [b / 5280 for b in yhomes]

    plt.scatter(0, 0, color='cyan')
    plt.plot(xLocation, yLocation, 'ro')
    plt.legend(["Customer Homes", "Delivery Facility"], loc=1, bbox_to_anchor=(1, 0.4))

    plt.ylabel('Miles')
    plt.title("Customer Grid Map for the last RUN")
    plt.xlabel('Miles')
    plt.show()


    plt.subplot(1,1,1)
    n, bins, patches = plt.hist(delivery_distance, num_bins, normed=1, alpha=0.5)
    y = mlab.normpdf(bins, dist_avg, dist_std)
    plt.title('PDF of Total Trip Distance')
    plt.ylabel("Probabilty")
    plt.xlabel("Distance in Miles")
    plt.plot(bins, y, 'r--')
    plt.show()

    n, bins, patches = plt.hist(delivery_distance, num_bins, normed=1, alpha=0.5,cumulative=True)
    y = mlab.normpdf(bins, dist_avg, dist_std).cumsum()
    y /= y[-1]
    plt.plot(bins,y)
    plt.title("CDF of Total Trip Distance")
    plt.xlabel("Distance in Miles")
    plt.ylabel("Probabilty")


    plt.show()


    '''   
    df1 = pd.DataFrame.from_dict(all,orient = 'index')
    df1.plot(kind = 'bar')


    plt.legend(['Drones'])
    plt.title('Drone Delivery Utilization')
    plt.xlabel('DRONES')
    plt.ylabel('Times Used')
    plt.show()
    '''



if __name__ == "__main__":
    main()