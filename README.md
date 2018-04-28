# IDS6145(SimTech 2018) - Research Plan

> * Group Name: Ama-Drone
> * Group participants names: Markus Loennig, Marc Mailloux, Tiffani Marlowe
> * Project Title: Viability of Drone Delivery in Orlando Fl


## General Introduction

![SAMPLE IMAGE 2](images/Huge.jpg)

Technology and online shopping continues to advance at an instantaneous rate. Consumers are now capable of ordering most anything via the web and therefore, have become reliant on quick and dependable home delivery services. With the online shopping market increasing at a steadfast rate, businesses are now investigating and improving new forms of delivery and their overall efficiency. One of the most recent forms of delivery are via aviation, in particular, by the use of drones.

A "drone" refers to unmanned aerial vehicle (UAV) or unmanned arial system (UAS) that is or can be controlled remotely by an operator on the ground. Currently technology is shifting from controlling to giving it an UAS a task and just monitor it, so no positive control is maintained at all times. This greatly reduces workload o the operators and enables them to operate multiple systems at any given time.  

Traditionally, drones have been utilized within the military for dangerous operations or missions that can be done by soldiers due constrains like flight-time/endurance. However, they are beginning to apply to civil applications such as firefighting and even now, package delivery.  Through the operation of drone delivery, there could be potential for reduced delivery costs, improved customer service and more importantly, accelerated delivery times. 

Which leads us to believe that drones will be a more efficient and especially speedier form of consumer goods package delivery in a exemplary city like Orlando.

The problem we wish to investigate will no doubt be part of the worlds day-to-day living in the foreseeable future. The ability to keep up with developing technology and the adaption of regulations (airspace, legal, insurance, etc.) are already in the works. Many large online retailers such as Amazon and DHL are currently experimenting with unmanned aerial systems in order to provide faster delivery of consumer goods. Amazon plans to implement "Amazon Prime Air" with a targeted delivery time for certain goods in under 1 hour. Based on current technology and consumer needs, we feel this form of delivery will quickly become the next level of packaged delivery.

#### Historical Background:

Before the digital era (Internet) consumer needs were usually satisfied by local department and specialty stores. Uncommon goods were ordered from catalogues either via phone (landline) and/or via a written order (letter). Once the packaged has been processed by the retailer, a distribution center somewhere in the country would further process the order and a mailman would later deliver the package to its destination. Consumers could expect to receive their order within two weeks which was considered normal at the time.

With the coming of the digital era, consumers no longer have to physically go into stores or use catalogues to purchase goods. Instead, they are capable of ordering most anything via online shopping. With these evolving abilities, consumer behaviors and expectations have also changed. They now demand their orders sooner rather than later. This impatience and expectation has only worsened over time. Larger retailers are now forced to manage this decentralized demand by providing quicker and more efficient delivery methods.

One of that largest online retailers, Amazon, has managed to change the worldwide behavior and meet consumer expectations by ensuring everything is connected. Therefore, everything is accessible by the click of a button. Amazon, has continued to decrease delivery times from weeks to now days. They have even gone further enough to shorten the delivery time of certain goods to "Next Day" and most recently to "1 Hour" delivery. They have made this possible by building smart distribution centers in various locations and implementing a highly intelligent delivery process. Without a sound and sophisticated delivery infrastructure, this worldwide success would not be possible.

Amazon and others major retailers are investigating the next step: overcoming the delivery infrastructure and service (like American Postal Service or UPS/DHL) with their own, more efficient and fast system. The newest logical solution lays within air transportation. Its direct and is not dependent upon on street infrastructure or the control of a human. Therefore, the number of employees and the time between package processing and delivery will be decreased. Potentially allowing for greater savings for both the retailer and the consumer.

Drone technology on the other hand has also become more advanced over the past few years, especially better batteries with higher density, improved charging times, more efficient brushless motors and a certain degree of independence to perform a variety of tasks. 

Thus, the capabilities of drones are influencing and expanding the delivery industry. Drone delivery systems are already scalable for different scenarios. Uber is experimenting with drones in terms of a taxi service, which is, from a logistical stand point of view, very similar to a on-time package delivery system. 


#### Problem Statement
Delivery and logistics companies are currently testing drone capabilities to determine the efficiency and effectiveness of drone package delivery. Therefore, it is apparent that delivery (among other areas) via drone technology is something we can expect to see in the future. We propose that a delivery system such as this for at least parts of the city of Orlando Florida could be realistic and the city overall could benefit from this. 

Our research could provide relevant insight into how such a system would have to be designed and how many drones would be neccessary (scale of effort) to service a given area. Additionally, we want to have a look into the future by predicting lower charging times and higher flight speeds. We will simulate the effects this would have on the number of drones and therefore on costs.  want to 


Therefore, we hypothesize:

1.)	Drone delivery will be able to improve delivery time to under one hour (e.g. Amazon Prime Air), given the customer lives within a certain distance to a "delivery hub" and is able to receive a package from a drone. 

2.) Progress in battery development and design for improved speed will significantly reduce the overall number of drones and therefore reduce the logistical footprint and costs for the respective logistical company, making it easier, cheaper and more probable to implement. 


#### Contributions 
•	We have modeled and developed 2 simulations. We use Python and AnyLogic to adress the abovementioned hypothesis.
•	We will provide a comparison of statistics with deliveries with current technologies to those with improved (future) capabilities and their efects on delivery and scale of effort.  
•	We will provide an empirical analysis to further highlight the potential of a future drone based delivery system.
•	We will provide answers to the urgent questions and consumer expectationson on delivery time.


## The Model

After working on both Python and AnyLogic and feedback given by Dr. Kider and the Teaching Assistant (TA), the intended model as depicted below will no longer be used. It seemed like a natural evolution, while working on the actual respective models that easier and better to implement solutions were found. So what is shown here was the intention, which has developed into the adapted models shown below. 
 
![Structural Diagram](images/obj_dia.jpg)

As you can see, for the purpose of this experiment we will focus our attention on simulating various input and output variables. For a greater understanding, they are also listed below:
+ transportation type (truck vs drone)
+ drone delivery methods
+ battery life
+ location of drop off destinations (homes)
+ speed of delivery
+ various number of delivery hubs


![Behavior Diagram](images/beh_dia.jpg)

The purpose of Figure 1 (Transportation Simulation Model – Object Diagram) and Figure 2 (Transportation Simulation Method – Behavioral Diagram) is to provide a depiction of the current problem we are trying to address.

As shown above, Figure 1 describes the various objects in the simulation (delivery system, customer, etc.) and their attributes in which we will be focusing our attention (battery life, location, etc.). Within Figure 2, you can clearly understand the interactions between the variables and how the simulation will be executed. Gathered from the models, you can see that the initial state starts with the customer. They first place an order; the order is then sent to a distribution center where the package will be delivered based on two forms of delivery (drone and/or truck).


The new diagrams focus solely on the drone aspect of the simulation. We have created each a Python and an AnyLogic simulation, each with a different approach to the below stated fundamental questions. Here is the AnyLogic part:

![NEW Object Diagram - AnyLogic](images/Diagrams2.jpg)

![NEW Behavior Diagram - AnyLogic](images/Diagrams.jpg)


## Fundamental Questions
By focusing on these specific variables and prerequisites (see also below) within the simulation, we aim to answer the following questions below:

1) Is drone delivery efficient as a air based delivery methods? If so,
+ How long does it take (on average) to deliver a package to a certain location by air?
+ How will efficiency change with increasing number of orders and diversified locations?
+ How long does it take to deliver 50 packages via air based system?

2) How does increased battery, max speed, and carrying capacity effect utilization, arrival time and the number of drones needed?

3) Can drones reduce average delivery time to 1 hour (as intended by Amazon Prime Air), how much drones are neccessary? 


## Expected Results
After creating and analyzing the delivery system simulation, we expect to find air based delivery methods will be more efficient compared to ground based delivery methods. In particular, we believe that drone delivery will be significantly faster and more efficient compared to ground based delivery; perhaps even 30% more efficient. With that being said, we are not sure at what point and what conditions it will take for ground based delivery systems to exceed drone delivery abilities.  Lastly, we expect that battery life and the weight of the packages will have an overall effect on the air delivery systems capabilities.

## Research Methods

AnyLogic:

- In order to address these problems, we developed and executed an Agent Based Simulation with the simulation software Anylogic, based on GIS data of a specific areas of the city of Orlando. Throughout this simulation we hope to evaluate the overall effort needed to partly replace or at least improve current ground based methods of delivery and meet future consumer expectations.

We want to demonstrate how and which scale of effort is needed, the quality and quantity of drones and to a certain degree the intended area it would take to provide an efficient air based delivery system.

Changing certain parameters on the drone (like battery density/endurance, max speed, charging time) predict completion estimates with newer technology.

## (Other)
(change the title and amount of headers as needed) (mention datasets you are going to use) (mention base code or examples you)

Tiffani: 

I put everything, (and as much of I write up I can give you) here: I dont really know where iit would fit best, so feel free to improve my writing and put it where it belongs. Images, links for movies and text....


On order to model a simulation, and therefore to answer the questions that we have formulated, we had to define certain prerequisites and assumptions to calculate from a valid and repeatable standpoint. Since this is a drone based simulation, we have done a market screening and decided for a product of the DJI company which offers the best compromise between (carrying) power, in other words how much weight it can transport and lift, and endurance. Endurance is important as it ensures the neccessary reach of the drone and therefore a higher radius. 

The drone is the DJI Matrice 600 (matrice multiplication which is by pure coincidence the mathematics behind our Python simulation, no pun intended). It is build and used for professional users, offers a high amount of documentation, is highly exact in flying to coordinates (a prerequiste in unmanned/unmonitored flying) due to its sensor layout, could carry up to 5.5kg (12.1 lbs) and has a speed of up to 40 knots (which translates to 40 mph when there is no wind). Due to its retractable landing gear, it could also carry light, oversized packages. 

For drone technical stats: https://www.dji.com/matrice600 from April 27, 2018

![Matrice 600](images/drone.png)

Here are our our prerequsites and assumptions for the AnyLogic simulation:

Prerequisites taken from the documentation and flight experience 

- our drone flies with an average of 50 ft/second (15m/sec), which includes acceleration and decelleration.
- we chose the TB48S battery configuration with a higher endurance of of 30 minutes with a 4.4 lbs payload/package.  
- this translates to a maximum range of 17 miles, with an efective radius of 8.5 miles (for a forth and back trip).
- the batteries have a recharging time for a complete charge (from 0% to 100%) of 90 minutes. 
- no transmission range implemented as it will be programmed at the start with the adress coordinates and the flight profile (e.g. obstacles). In other words, it will fly "uncontrolled".

Assumptions:

- the effective time from order to loading the drone is a triangular distribution with a minimum 3 minutes, an average 7 minutes and a maximum of 12 minutes. 
- unloading the package at the destination is a uniform distribution between 20 and 45 seconds. 
- the distribution center is responsible for the depicted area, which has a diameter of 14.2 miles. We have chosen a smaller than possible (17 miles) diameter as we have to include some measures for wind (even minor wind speeds can have huge effects) and possible higher drag for the packages. 
- no package is heavier than 4 lbs total.

![Chosen Delivery Area ](images/Delivery_Area.png)

For the simulation, we have used only a quarter of the depicted area above as it is of no difference for the drone in which direction it has to fly. An adrees has only one important parameter, which is the distance. This will translate into flight time, which is the limiting factor for the drone and results in the respective recharging time.  

Simulation:

We have started with 



## Discussion
(final only - remove whole section for proposal Readme) (What would you have done differently) (What are the contributions summerize)(what is the big take away)(what did you learn)

## Future Work
(final only - remove whole section for proposal Readme) (if you had 6 more months what would be the next steps in this project.) (What are a few questions you have now)

## References

Campbell, J. F., Sweeney, D. C., & II, Z. J. (2017). Strategic design for delivery with trucks and drones. In Technical Report.

Gulden, T. R. (2017). The Energy Implications of Drones for Package Delivery: A Geographic Information System Comparison.

Thiels, C. A., Aho, J. M., Zietlow, S. P., & Jenkins, D. H. (2015). Use of unmanned aerial vehicles for medical product transport. Air medical journal, 34(2), 104-108.


