# IDS6145(SimTech 2018) - Research Plan

> * Group Name: Ama-Drone
> * Group participants names: Markus Loennig, Marc Mailloux, Tiffani Marlowe
> * Project Title: Viability of Drone Delivery in Orlando Fl

### Pitch

1.What is the topic?

The topic is dealing with the issue of delivering consumer goods in our target city Orlando

![SAMPLE IMAGE 2](images/Huge.jpg)

2.What do you want to do?

We want to model a part of the city of Orlando and simulate the differences between ground based (trucks) and air based (drones) delivery methods. Our main effort is the air based delivery method in regards to speed of delivery, efficiency and overall effort of the system (quantity of drones, quantity and location of hubs).

![SAMPLE IMAGE 1](images/DHL.jpg)

3.Why is important?

Current consumer behaviors indicates the active buying patterns are becoming more decentralized (ordering online) and we want to see if the concept of delivery is valid and how we can integrate this into the exisiting infracture.


## General Introduction

Technology and online shopping continues to advance at an instantaneous rate. Consumers are now capable of ordering most anything via the web and therefore, have become reliant on quick and dependable home delivery services. With the online shopping market increasing at a steadfast rate, businesses are now investigating and improving new forms of delivery and their overall efficiency. One of the most recent forms of delivery are via aviation, in particular, by the use of drones.

A drone refers to unmanned aerial vehicle (UAV) that is controlled remotely by an operator on the ground. Traditionally, drones have been utilized within the military for dangerous operations. However, they are beginning to apply to civil applications such as firefighting and even now, package delivery.  Through the operation of drone delivery, there could be potential for reduced delivery costs, improved customer service and more importantly, accelerated delivery times. Which leads us to believe drones will be a more efficient form of consumer goods package delivery in the targeted city of Orlando.

The problem we wish to investigate will no doubt be part of the worlds day-to-day living in the foreseeable future. The ability to keep up with developing technology and the adaption of regulations (airspace, legal, insurance, etc.) are already in the works. Many large online retailers such as Amazon and DHL are currently experimenting with unmanned aerial systems (Drones) in order to provide fast delivery of consumer goods. Based on current technology and consumer needs, we feel this form of delivery will quickly become the next level of packaged delivery.

#### Historical Background:

Before the digital era (Internet) consumer needs were usually satisfied by local department and specialty stores. Uncommon goods were ordered from catalogues either via phone (landline) and/or via a written order (letter). Once the packaged has been processed by the retailer, a distribution center somewhere in the country would further process the order and a mailman would later deliver the package to its destination. Consumers could expect to receive their order within two weeks which was considered normal at the time.

With the coming of the digital era, consumers no longer have to physically go into stores or use catalogues to purchase goods. Instead, they are capable of ordering most anything via online shopping. With these evolving abilities, consumer behaviors and expectations have also changed. They now demand their orders sooner rather than later. This impatience and expectation has only worsened over time. Larger retailers are now forced to manage this decentralized demand by providing quicker and more efficient delivery methods.

One of that largest online retailers, Amazon, has managed to change the worldwide behavior and meet consumer expectations by ensuring everything is connected. Therefore, everything is accessible by the click of a button. Amazon, has continued to decrease delivery times from weeks to now days. They have even gone further enough to shorten the delivery time of certain goods to "Next Day" and most recently to "1 Hour" delivery. They have made this possible by building smart distribution centers in various locations and implementing a highly intelligent delivery process. Without a sound and sophisticated delivery infrastructure, this worldwide success would not be possible.

Amazon and others major retailers are investigating the next step: overcoming the delivery infrastructure and service (like American Postal Service or UPS/DHL) with their own, more efficient and fast system. The newest logical solution lays within air transportation. Its direct and is not dependent upon on street infrastructure or the control of a human. Therefore, the number of employees and the time between package processing and delivery will be decreased. Potentially allowing for greater savings for both the retailer and the consumer.

Drone technology has become more advanced over the past few years from better batteries to more efficient brushless motors. Thus, the capabilities of drones are influencing and expanding the delivery industry. Proving that drone delivery systems are scalable for different scenarios. For example, Amazon has recently launched a service called Amazon Prime Air which allows consumers to order items and have them delivered in under an hour. In addition, Uber is experimenting with drones in terms of a taxi service, which is very similar to a package delivery system. Services similar to these will introduce the market to drone delivery and will likely contribute to the out datedness of standard ground based delivery systems.

#### Problem Statement
Delivery and logistics companies are currently testing drone capabilities to determine the efficiency and effectiveness of drone package delivery. Therefore, it is apparent that drone technology is something we can expect to see in the future. We propose that the city of Orlando Florida could benefit from a delivery system such as this and could provide relevant insight into this area of rising research. Between the combination of a large population, congested roadways, and a fast-past style of living, the city of Orlando is a perfect area to simulate the impact of drone delivery. Therefore, we hypothesize:

1)	Drone delivery will be more cost efficient in Orlando compared to ground based delivery.

2)	Drone delivery will improve delivery time at a leading rate during the times of the day with increased congestion and traffic compared to ground based delivery systems.

In order to address these problems, we will develop and execute an Agent Based Simulation using Anylogic that represents specific areas of the city of Orlando. Throughout this simulation we hope to evaluate the overall effort needed to partly replace current ground based methods of delivery and meet consumer expectations.
In addition, by applying Agent Based Simulation techniques to model and simulate a specific portion of the city of Orlando we hope to compare the pros and cons of ground based (trucks) delivery methods against air based (drones) delivery methods. Our main effort is to determine the differences among the two delivery methods in regard to speed of delivery, efficiency, and overall performance of the systems. By doing so, we could further determine the quantity of drones and locations it would take to provide an efficient air based delivery system for the city of Orlando.

For the purpose of this experiment, we will focus our attention on simulating the specific input and output variables listed below: 
+ ground transportation (truck) 
+ drone delivery methods 
+ location of drop off destinations (homes) 
+ speed of delivery
+ various number of delivery hubs

#### Contributions 
•	We have modeled and developed a simulation that further identifies a novel problem.
•	We have provided a comparison of both air based delivery systems and ground based delivery systems to advance current understanding of more efficient delivery systems.  
•	We have drawn on previous research to provide an empirical analysis to the research community and larger online retailers such as Amazon. Which additionally provides insight into the true potential of the future delivery system and a greater understanding on consumer needs and expectations. 


## The Model

![Structural Diagram](images/obj_dia.jpg)

(Provide structural and behavior diagrams of the system you wish to study.) (Why is your model a good abtraction of the problem you want to study?) (Are you capturing all the relevant aspects of the problem?) (Use the model to tell us what is going on.)

![Behavior Diagram](images/beh_dia.jpg)

(explicitly list your requirements of what the model will have and simulate for the proposal)

## Fundamental Questions
By focusing on these specific variables within the simulation, we aim to answer the following questions below: 

1) Is drone delivery more efficient than standard ground based delivery methods? If so,
+ How long does it take (on average) to deliver a package to a certain location by ground and by air?
+ How will efficiency change with increasing number of orders and diversified locations?
+ At what point will the ground based solution be better than the air based solution and vice versa?
+ How long does it take to deliver 50 packages via ground based system?
+ How long does it take to deliver 50 packages via air based system?

2) How does increased battery, max speed, and carrying capacity effect the number of drones needed?
+ How can "Hubs”-like package pick-up stations with a slightly increased delivery time influence the delivery service industry?

3) Can the drones reduce average delivery time by 30%? If so, 
+ Taking technical development into account, which overall measurable effects will have changes in delivery speed, battery efficiency and increased payload for air based solutions (e.g. increased possible flight time of 10% / 20%, shortened recharging time, etc.)?
  



## Expected Results
(What are the answers to the above questions that you expect to find before starting your research?) (This changes from Expected (Proposal) to just Results (final report)) (you should verbally define them) (sketch a few graphs of what you are roughly going for - not the data but histogram of this, line graph of that, screenshot of an agent - use paper and pencil sketches)

We are expecting to see that air based methods will be more efficient compared to ground based delivery. 

## Research Methods
(Cellular Automata, Agent-Based Model, Discrete Event Continuous Modeling...)(Python or Anylogic) (If you are not sure here: 1. Consult your colleagues, 2. ask the teachers, 3. remember that you can change it afterwards) (Steps in the process)

The research methods we plan to use are Agent-Based modeling paired with the simulation software anylogic. We plan to have our air or ground based agents delivery x amount of packages with respect to time to determine which is more efficient. Additionally changing certain parameters on the drone(like battery, max speed, carrying capacity) predict completion estimates with newer technology. 

## (Other)
(change the title and amount of headers as needed) (mention datasets you are going to use) (mention base code or examples you)

## Discussion
(final only - remove whole section for proposal Readme) (What would you have done differently) (What are the contributions summerize)(what is the big take away)(what did you learn)

## Future Work
(final only - remove whole section for proposal Readme) (if you had 6 more months what would be the next steps in this project.) (What are a few questions you have now)

## References
(Add the bibliographic references you intend to use)  (Code / Projects / blogs / websites / papers...)
=======
