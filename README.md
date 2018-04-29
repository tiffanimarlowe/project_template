# IDS6145(SimTech 2018) - Research Plan

> * Group Name: Ama-Drone
> * Group participants names: Markus Loennig, Marc Mailloux, Tiffani Marlowe
> * Project Title: Viability of Drone Delivery in Orlando Fl


## General Introduction

![SAMPLE IMAGE 2](images/Huge.jpg)

Technology and online shopping continues to advance at an instantaneous rate. Consumers are now capable of ordering most anything via the web and therefore, have become reliant on quick and dependable home delivery services. With the online shopping market increasing at a steadfast rate, businesses are now investigating and improving new forms of delivery and their overall efficiency. One of the most recent forms of delivery are via aviation, in particular, by the use of drones.
A "drone" refers to an unmanned aerial vehicle (UAV) or unmanned aerial system (UAS) – meaning while in flight the drone is controlled remotely by an operator on the ground. Currently aviation technology is shifting from typical within cockpit control to UAS. Pilots main task is to monitor the UAV from the ground instead of physically being in control from inside the cockpit. In doing so, the pilot is removed from manual control and systems operations in various scenarios. This ability greatly reduces operator workload and safety while also enabling pilots to operate multiples systems simultaneously.  

Traditionally, drones have been utilized within the military for dangerous operations and missions to limit solider causalities. Drones enables the military to complete missions that otherwise would not be possible due to constrains such as flight-time and endurance. More recently, drones are beginning to be utilized in many civil applications such as firefighting and even now, package delivery.  Through the operation of drone delivery, there could be potential for reduced delivery costs, improved customer service and more importantly, accelerated delivery times. 

The ability to keep up with developing technology and the adaption of regulations (airspace, legal, insurance, etc.) are already in the works. Many large online retailers such as Amazon and DHL are currently experimenting with unmanned aerial systems in order to provide faster delivery of consumer goods. Amazon plans to implement "Amazon Prime Air" with a targeted delivery time for certain goods in under 1 hour. In addition to Amazon, other delivery and logistics companies are currently testing drone capabilities to determine the efficiency and effectiveness of drone package delivery. Therefore, it is apparent that delivery (among other areas) via drone technology is something we can expect to see in the future. We feel this form of delivery will quickly become the next level of packaged delivery throughout the world due to its ability to provide faster and more efficient deliveries. 

#### Historical Background:
Before the digital era (Internet) consumer needs were usually satisfied by local department and specialty stores. Uncommon goods were ordered from catalogues either via phone (landline) and/or via a written order (letter). Once the packaged has been processed by the retailer, a distribution center somewhere in the country would further process the order and a mailman would later deliver the package to its destination. Consumers could expect to receive their order within two weeks which was considered normal at the time.

With the coming of the digital era, consumers no longer have to physically go into stores or use catalogues to purchase goods. Instead, they are capable of ordering most anything via online shopping. With these evolving abilities, consumer behaviors and expectations have also changed. They now demand their orders sooner rather than later. This impatience and expectation has only worsened over time. Larger retailers are now forced to manage this decentralized demand by providing quicker and more efficient delivery methods.

One of that largest online retailers, Amazon, has managed to change the worldwide behavior and meet consumer expectations by ensuring everything is connected. Therefore, everything is accessible by the click of a button. Amazon, has continued to decrease delivery times from weeks to now days. They have even gone further enough to shorten the delivery time of certain goods to "Next Day" and most recently to "1 Hour" delivery. They have made this possible by building smart distribution centers in various locations and implementing a highly intelligent delivery process. Without a sound and sophisticated delivery infrastructure, this worldwide success would not be possible.

Amazon and others major retailers are investigating the next step: overcoming the delivery infrastructure and service (like American Postal Service or UPS/DHL) with their own, more efficient and fast system. The newest logical solution lays within air transportation. Its direct and is not dependent upon on street infrastructure or the control of a human. Therefore, the number of employees and the time between package processing and delivery will be decreased. Potentially allowing for greater savings for both the retailer and the consumer.

Drone technology on the other hand has also become more advanced over the past few years. They are now equipped with better batteries due to higher density, improved charging times, more efficient brushless motors and a certain degree of independence to perform a variety of tasks. Thus, the capabilities of drones are influencing and expanding the delivery industry. Drone delivery systems are already scalable for different scenarios. Uber is experimenting with drones in terms of a taxi service, which is, from a logistical stand point of view, very similar to an on-time package delivery system. 

#### Problem Statement
Based on current technology and consumer needs, we believe that drones will provide a more efficient and especially faster form of consumer goods package delivery throughout the world. Therefore, in this article, we aim to investigate whether a drone delivery system could be realistic and overall beneficial to a larger city such as Orlando, Florida. 

This research contributes to the current technological advancement by providing relevant insight on how a drone delivery system would have to be designed in order to run successfully and efficiently. Our research compares statistics for both current and advanced delivery systems to determine their effects on delivery time and scale of effort. In addition, we provide an empirical analysis to further highlight the potential of a future drone based delivery system and answer to current urgent questions and consumer expectations on delivery time.

By simulating the effects of varying number of drones, charging times, and flights speeds we hope to determine 1) how many drones would be necessary (scale of effort) to service a given area and 2) how cost efficient a drone delivery system would be.

We hypothesize:

1.)	Drone delivery will be able to improve delivery time to under one hour (e.g. Amazon Prime Air), given the customer lives within a certain distance to a "delivery hub" and is able to receive a package from a drone. 

2.) Improved battery life and speed will significantly reduce the overall number of drones needed. Therefore, reducing the logistical footprint and costs for the respective logistical company - making it easier, cheaper and more probable to implement. 



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

#### 1) Is drone delivery efficient as a air based delivery methods? If so,
+ How long does it take (on average) to deliver a package to a certain location by air?
+ How will efficiency change with increasing number of orders and diversified locations?
+ How long does it take to deliver 50 packages via air based system?

#### 2) How does increased battery and max speed effect utilization, arrival time and the number of drones needed?

#### 3) Can drones reduce average delivery time to 1 hour (as intended by Amazon Prime Air), how much drones are neccessary? 


## Expected Results
After creating and analyzing the delivery system simulation, we expect to find air based delivery methods will be more efficient compared to ground based delivery methods. In particular, we believe that drone delivery will be significantly faster and more efficient compared to ground based delivery; perhaps even 30% more efficient. With that being said, we are not sure at what point and what conditions it will take for ground based delivery systems to exceed drone delivery abilities.  Lastly, we expect that battery life and the weight of the packages will have an overall effect on the air delivery systems capabilities.

## Research Methods

#### AnyLogic:

- In order to address these problems, we developed and executed an Agent Based Simulation with the simulation software Anylogic, based on GIS data of a specific areas of the city of Orlando. Throughout this simulation we hope to evaluate the overall effort needed to partly replace or at least improve current ground based methods of delivery and meet future consumer expectations.

We want to demonstrate how and which scale of effort is needed, the quality and quantity of drones and to a certain degree the intended area it would take to provide an efficient air based delivery system.

Changing certain parameters on the drone (like battery density/endurance, max speed, charging time) predict completion estimates with newer technology.

#### Python:

- 


## (Other)
(change the title and amount of headers as needed) (mention datasets you are going to use) (mention base code or examples you)

Tiffani: 

I put everything, (and as much of I write up I can give you) here: I dont really know where iit would fit best, so feel free to improve my writing and put it where it belongs. Images, links for movies and text....


On order to model a simulation, and therefore to answer the questions that we have formulated, we had to define certain prerequisites and assumptions to calculate from a valid and repeatable standpoint. Since this is a drone based simulation, we have done a market screening and decided for a product of the DJI company which offers the best compromise between (carrying) power, in other words how much weight it can transport and lift, and endurance. Endurance is important as it ensures the neccessary reach of the drone and therefore a higher radius. 

The drone is the DJI Matrice 600 (matrice multiplication which is by pure coincidence the mathematics behind our Python simulation, no pun intended). It is build and used for professional users, offers a high amount of documentation, is highly exact in flying to coordinates (a prerequiste in unmanned/unmonitored flying) due to its sensor layout, could carry up to 5.5kg (12.1 lbs) and has a speed of up to 40 knots (which translates to 40 mph when there is no wind). Due to its retractable landing gear, it could also carry light, oversized packages. 

For drone technical specs: https://www.dji.com/matrice600 

![Matrice 600](images/drone.png)

Here are our our prerequsites and assumptions for the AnyLogic simulation:

We did a survey on the last 10 Amazon orders for 4 persons and came to the conclussion that the average package is about 10x5x8 inches in size (low was 5x5x5 and high was 17x10x11) on the orders with 4lbs or below. As our drone is set to a max of 4 lbs (see below), everything above will not be offered for "Air delivery". Average time was 2.0 days. 

#### Prerequisites taken from the documentation and flight experience 

- our drone flies with an average of 50 ft/second (15m/sec), which includes acceleration and decelleration.
- we chose the TB48S battery configuration with a higher endurance of of 30 minutes with a 4.4 lbs payload/package.  
- this translates to a maximum range of 17 miles, with an efective radius of 8.5 miles (for a forth and back trip).
- the batteries have a recharging time for a complete charge (from 0% to 100%) of 90 minutes. 
- the drone will be recharged to full capacity after each flight, regardless of the travelled distance.
- recharge time is roughly the flight time by a factor of 3, so for a flight time between 3-6 minutes, there is a recharging time of 9-18 minutes. 
- no transmission range implemented as the drone will be programmed at the start with the adress coordinates and the flight profile (e.g. obstacles). In other words, it will fly "uncontrolled".

![Matrice 600 specs ](images/drone_endurance.png)

#### Assumptions:

- the effective time from order to loading the drone is a triangular distribution with a minimum 3 minutes, an average 7 minutes and a maximum of 12 minutes. 
- unloading the package at the destination is a uniform distribution between 20 and 45 seconds. 
- the distribution center is responsible for the depicted area, which has a diameter of 14.2 miles. We have chosen a smaller than possible (17 miles) diameter as we have to include some measures for wind (even minor wind speeds can have huge effects) and possible higher drag for the packages. 
- no package is heavier than 4 lbs total.
- there is one distribution center, which prepares the packages and houses the drones
- we have 13 different adresses to deliver the packages to, for the different distances to cover. 

![Chosen Delivery Area ](images/Delivery_Area.png)

For the simulation, we have used only a quarter of the depicted area above as it is of no difference for the drone in which direction it has to fly. An adrees has only one important parameter, which is the distance. This will translate into flight time, which is the limiting factor for the drone and results in the respective recharging time.  

#### Simulation:

![Model AnyLogic Sim ](images/Model_AnyLogic.png)

Based on the depicted AnyLogic Model (aboce) as the core process, we started with 5 / 8 / 11 drones and 1 order per household (HH) per hour (13 orders/hour). Runtime is 600 minutes (10 hours). 

#### Results:

Are as expected, as it even though there are only a few orders per hour, there are only a few drones. In aviation, a rule of thumb is if you need to employ one aircraft all the time, you need at least three. This is similar to our situation as the charging time is triple the flight time. 

- 1 order/household/hour  with  5 drones:  utilization 96%,  53 deliveries, of which 21 take longer than 1 hour, 6 even longer than 90 minutes
  + https://youtu.be/HbHV2XxcoAI
- 1 order/household/hour  with  8 drones:  utilization 95%,  81 deliveries, none took longer than 1 hour
  + https://youtu.be/rOAO5Jfjz04
- 1 order/household/hour  with 11 drones:  utilization 81%,  94 deliveries, none took longer than 40 minutes
  + https://youtu.be/vtBSfUZnuog

A utilization of over 85% is unrealistic, as there will always be neccessary planned and unplanned maintainace. It also leaves no reserves for a higher order on peak times. The formulated goal could not be met with 5 and 8 drones. 

Clearly the results show that due to the high utilization rate there was no time to accept sufficient orders. Only 53 deliveries (with 5 drones) compared to 94 deliveries (with 11 drones) were completed. 

We have realized that the manual search for the optimal number of drones is time consuming and were able to implement an optimization simulation. We chose a threshold of an utilization of 85% (see above) and can now let AnyLogic do the optimization process in regards to the optimal number of drones for a utilization of 85%. 

![Optimization process for 85% threshold ](images/optimization.png)

The process for 1 order/HH/hour with can be seen here: https://youtu.be/fzb6oUqDDWY


The next simulation doubles the number of orders to 2/HH/hour. The optimization process calculates 18 drones as optimum, with a threshold of 85% utilization.

As the video with 16 (not 18) shows (https://youtu.be/uKgUKagtmTc), the actual simulation reaches an utilization of 92%, which is above the given threshold for the optimization process. 

The optimization process showed an optimum number of 18 drones and a simulation runs has confirmed the data (https://youtu.be/in5Zay7Dtjw). 

All deliveries were completed within 30 minutes of the order, which shows the potential of drone based delivery systems. 


The next simulation brings the number of orders to 3/HH/hour. The respective optimization process calculates 25 drones as optimum, again with a threshold of 85% utilization. Interestingly, the number of drones doesn't just equally to the magnitude of orders. 

The result shows that the optimization is correct. Even simulations with significantly more drones (up to 45) dont show any significant differences between number of orders served or service time until delivery. The only difference is the utilization time, which drops significantly and is therefore counterproductive (as it is a cost-driver).

#### Questions answered so far:

1) Is drone delivery efficient as a air based delivery methods? If so,
+ How long does it take (on average) to deliver a package to a certain location by air?
  - depending on the number of drones and the distance to be travelled usually about 30 minutes (with the prerequisites and assumptions formulated above). That is when the optimal number of drones is found for the actual demand with a utilization rate not higher 85%.
+ How will efficiency change with increasing number of orders and diversified locations?
  - the number of orders have an immediate effect on the number of drones needed to keep the timelines under 1 hour. At a certain point, the orders can not be fulfilled in time and will lead to a cascade of unfulfilled orders (see example above with 1 order/HH/hour and 5 drones).
+ How long does it take to deliver 50 packages via air based system?
  - that depends on the rate of incoming orders and on the available drones in the distribution center. With a rate of 3 orders/HH/hour, it takes about 140 minutes, given the number of drones is about 25.
  
3) Can drones reduce average delivery time to 1 hour (as intended by Amazon Prime Air), how much drones are neccessary? 
   - Yes, they can and it is dependant on the number of orders the systems is prepared for. 


In the next simulation runs, we will change the speed (in the images below as: "fast") and shorten the charging times of the batteries ("charge"), as this is currently the limiting factor on usage. Lastly, both changes/improvements will be implemented ("both") and analyzed 

- "fast": the speed will be adapted to 60 mph (88ft/sec, 29m/sec). Modern drones can achive that speed and are foreseen to be faster, depending on the type of drones. 
- "charge": the charging time will be reduced by 1/3, so now a full charge can be done within 60 minutes (instead of 90 minutes).
- "both": both above described improvements are being implemented into the drone simulation. 

Otherwise, all other values (houses, number of drones, ...) will remain as above to be able to compare the impact of the changes.


#### Results:

The changes in the values of charging time, speed and both are described and summarized here. The first image shows the effects on 1 order/HH/hour for the given area and 11 drones. The optimization process shows slight variations in necessary drones:  

- 1_11 (normal) is 11      1_11fast is 12     1_11charge is 9      1_11both is 9      --> thats a change of 19% from normal to both

Even though the optimization run suggests to change the number of drones, I left them deliberatly at the "normal" value to see the difference in the simulation. the numbers are as follows:

![1 order with 11 drones, improvements: overview ](images/1_11_summary.png)

The first striking difference (on the right side), as to be expected, the flight time is almost reduced to half. This is logical as the speed almost doubled (34mph --> 60mph). 
- The effect of the increased speed on delivery time is also significant with a mean from 17.7 minutes to 12.5, which is a reduction of almost 30%. 
- The reduced charging time shows its effect on the max delivery time value, as it is also significantly reduced from 37.6 to 22.9 minutes. This is a reduction of 39%! Obviously, implementing both improvements reduce the mean and the max delivery time again, as both can have cumulative or subsidiary effects. 

--> Implementing both improvements reduce mean time by 37% and the max delivery time by 54%. 


The next image shows the effects on the 2 order/HH/hour for the given area and 18 drones. The optimization process shows again positive variations in necessary drones (decrease of up to 3, which equals a 17% reduction):  

2_18 (normal) is 18      2_18fast is 16     2_18charge is 17     2_18both is 15     --> thats a change of 17% from normal to both

Again, I left the number of drones at the "normal" value to see the difference in the simulation. the numbers are as follows:

![2 orders with 18 drones, improvements: overview ](images/2_18_summary.png)

As above, the flight time is almost reduced to half. This will always be the case because it is logical as the speed almost doubled (34mph --> 60mph). It will not be mentioned in further discussions. 

- The effect of the increased speed on delivery time in a higher number environment, with more drones and more orders shows again improvements on the mean delivery time from 15.6 minutes to 13.2, which is a reduction of almost 16%. The reduction is smaller, but so is the mean time to begin with. This seems to be a normal effect, as smaller numbers are less tolerant to outlying behavior or problems. (In fleet management this is the so called "curse of small numbers".) 
- The reduced charging time again shows its effect best on the max delivery time value, as it is reduced from 31 to 21.7 minutes. This is a reduction of 30%!  

--> Implementing both improvements reduce mean time by 29% and the max delivery time by 43%. 


Here are the effects on 3 order/HH/hour and 25 drones. The optimization process shows again positive variations in necessary drones (decrease of up to 7, which equals a 28% reduction) for a targeted utilization rate of 85%:  

3_25 (normal) is 25      3_25fast is 25     3_25charge is 19     3_25both is 18     --> thats a change of 28% from normal to both!

![3 orders with 25 drones, improvements: overview ](images/3_25_summary.png)

- The effect of speed increase on delivery time in an even higher number environment, with more drones and more orders shows again  improvements on the mean delivery time, here from 14.2 minutes to 11.4, which is about 20%. This reduction is somewhat higher than for the 2_18 simulation, but it seems to be a normal variation. This seems to be a normal effect, as smaller numbers are less tolerant to outlying behavior or problems. (In fleet management this is the so called "curse of small numbers".) 
- The reduced charging time again shows its effect best on the max delivery time value, as it is reduced from 25.7 to 23.3 minutes. This is only a nimor reduction of 9%.  

--> Implementing both improvements reduce mean time from 14.2 to 11.2 minutes (21%) and the max delivery time from 25.8 to 17.6minutes  (32%). 

Video with statistics for 3_25_both on:   https://youtu.be/Bg6cD1Y4d-0


#### Questions answered for this part:

2) How does increased battery and max speed effect utilization, arrival time and the number of drones needed?




Tiffani:

I have attached the complete screenshots of the simulations made for the three different settings (1, 2 and 3 orders per HH and hour) in the image section. They  are each called 1_11 (meaning: 1 order, 11 drones), 2_18 (2 orders, 18 drones) and 3_25 with the abbreviation of the included improvement ("fast" ist increased speed to 60mph, "charge" is the reduced charging time by 1/3, and "both" is the implementation of both). This needs to be analyzed and summarized some more (with a couple of images on the ReadMe here) and compared to each other. Values to look at could be max times and deviation.

Also important in the images for analyzis which I havent done so far: the number of delivered packages increased in every improvement, because it gives a good value on the capability and effects of the improvements (how much more can be handled...). 

For questions just write me...


## Discussion
(final only - remove whole section for proposal Readme) (What would you have done differently) (What are the contributions summerize)(what is the big take away)(what did you learn)

## Future Work
(final only - remove whole section for proposal Readme) (if you had 6 more months what would be the next steps in this project.) (What are a few questions you have now)

## References

Campbell, J. F., Sweeney, D. C., & II, Z. J. (2017). Strategic design for delivery with trucks and drones. In Technical Report.

Gulden, T. R. (2017). The Energy Implications of Drones for Package Delivery: A Geographic Information System Comparison.

Thiels, C. A., Aho, J. M., Zietlow, S. P., & Jenkins, D. H. (2015). Use of unmanned aerial vehicles for medical product transport. Air medical journal, 34(2), 104-108.


