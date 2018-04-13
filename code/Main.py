import numpy as np
from random import shuffle
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    #defining distances for 10 packages
    def distance(n):
        x = [1,2,3,4,5,6,7,8,9,10]
        shuf = shuffle(x)

        if x[n] == 1:
            dist = 5280 * 1/9
        elif x[n] == 2:
            dist = 5280 *1/8
        elif x[n] == 3:
            dist = 5280 * 1/3
        elif x[n] == 4:
            dist = 5280 * 1/2
        elif x[n] == 5:
            dist = 5280 * 1/8
        elif x[n] == 6:
            dist = 5280 * 2
        elif x[n] == 7:
            dist = 5280 * 4
        elif x[n] == 8:
            dist = 5280 * 2/3
        elif x[n] == 9:
            dist = 5280 * .1
        elif x[n] == 10:
            dist = 5280 * .2
        return dist
    #distance(0)

    def packages(num_deliv):
        package_weight = []
        area = []
        dragco = []

        for i in range(0,num_deliv):
            weight  = np.random.uniform(.5,10)
            package_weight.insert(i, weight)
            if weight > 5: #heavy and bulky
                Area_package = 10
                drag_coef = .82
                area.insert(i,Area_package)
                dragco.insert(i, drag_coef)
            else: #light and form effcient
                Area_package = 2
                drag_coef = .3
                area.insert(i, Area_package)
                dragco.insert(i, drag_coef)

        return package_weight, area , dragco


    def battery(capacity, n ,num_deliv):
        p = packages(num_deliv)
        d = distance(n)
        batlife = capacity / p[n] / d
        #print( batlife,"bat", p[n] , " Pack" , d , " distance")
        #print( p[n],p,'ppppp')

    def drone(num_deliv, Thrust):
        timelist = []
        for n in range(0,10):
            p, A ,CD  = packages(num_deliv)
            d = distance(n)
            speed = 2 / (A[n] * CD[n]) * (Thrust * (1 - (p[n] * 32.2 / Thrust) ** 2) ** .5)
            time = d / speed
            timelist.insert(n,time)

        return (timelist, sum(timelist))

    y = []
    time_sum = []
    def run():
        for i in range(0,100):
            x , z = drone(10, 1000)
            y.insert(i,x)
            time_sum.insert(i,z)
            print ('running')

        return y , time_sum


    a , b = run()
    print(b)

    sns.heatmap(a)
    plt.show()

    sorted(b)
    plt.plot(b)
    plt.show()
    print("ran")








if __name__ == "__main__":
        main()