# Code Folder 

Below is an explanation of the Discrete Event simulation code designed in Python.


![Python Distance](images/python/howto/distance.png)

We began our simulation by creating a distance function that generates distances in miles on a constrained Grip Map. The Euclidian Distances are then calculated and stored along with a list of x and y coordinates. Additionally, we created a Speed function that is able to adjust the velocity depending on distance.

![Python Speed](images/python/howto/speed.png)

Latly, we developed a battery initializing function that creates an array of battery charge for each drone used.

![Python battery](images/python/howto/bat_life.png)

This function starts off by creating the necessary constraints. Additionally, using Time equal to distance over Velocity. Using this newly calculated array to then simulate each delivery by taking in consideration the flight time with respect to the battery life and capacity.

![Python flight](images/python/howto/flight1.png)

The equation can be seen in the photo below for drones[1].

This allowed us to monitor the battery life and if the battery life was at half capacity, another drone will be sent out for use, and the rest of the drones at home base will be charging.

![Python flight](images/python/howto/flight2.png)

Various Stats are then accounted for and collected

![Python flight](images/python/howto/flight3.png)

A Monte-Carlo Simulation is then set-up and ran for a number amount of trials for a variety number of stats. 

![Python Monte-Carlo](images/python/howto/monte.png)
![Python Monte-Carlo](images/python/howto/monte1.png)











## The used file/code for AnyLogic is in the folder "Final Project".

- the other 2 folders (AMADRONE_state and Project_AmaDrone) were attempts which were not leading in the right direction. They are left inside the folder structure simply for documentation purposes.

