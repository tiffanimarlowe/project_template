# IDS6145(SimTech 2018) - Research Plan

> * Group Name: Ama-Drone
> * Group participants names: Markus Loennig, Marc Mailloux, Tiffani Marlowe
> * Project Title: Viability of Drone Delivery in Orlando Fl

### Pitch

1.What is the topic?

Technology and online shopping continues to advance at an instantaneous rate. Consumers are now capable of ordering most anything via the web and therefore, have become reliant on quick and dependable home delivery services. With the online shopping market increasing at a steadfast rate, businesses are now investigating and improving new forms of delivery and their overall efficiency. One of the most recent forms of delivery are via aviation, in particular, by the use of drones.  Through the operation of drone delivery, there could be potential for reduced delivery costs, improved customer service and more importantly, accelerated delivery times. Which leads us to believe drones will be a more efficient form of consumer goods home delivery in the targeted city of Orlando.

![SAMPLE IMAGE 2](images/Huge.jpg)

2.What do you want to do?

By modeling and simulating a specific portion of the city of Orlando we hope to compare ground based (trucks) delivery methods against air based (drones) delivery methods. Our main effort is to determine the differences among the two delivery methods in regard to speed of delivery, efficiency and overall performance of the system. By doing so, we could further determine the quantity and locations it would take to provide an efficient air based delivery system for the city of Orlando.

![SAMPLE IMAGE 1](images/DHL.jpg)

3.Why is important?

Current consumer behaviors indicates the active buying patterns are becoming more decentralized (ordering online) and we want to see if the concept of delivery is valid and how we can integrate this into the exisiting infracture.

(TEASER IMAGE HERE - should wow me to read your work)

* (this Readme should "evolve" over time as you add and edit it)
* (once you are happy with it - copy it into the proposal directory, and remove the obvious sections that should be removed - Future work, etc)

## General Introduction

(States your motivation clearly: why is it important / interesting to solve this problem?)
(Add real-world examples, if any)

The problem we want to have a deeper look at will be part of our lives in the not-so-far future. Depending on technical development and adaptation of regulations (airspace, legal, insurance claim in case drone fall on your head/property) there are certain companies  (Amazon, DHL, etx.) already looking into fast delivery of goods via an unmanned aerial system (aka drone). In our opinion, this will become the next level of consumer delivery.

(Put the problem into a historical context, from what does it originate? Are there already some proposed solutions?)
Historical context: 


  Before the digital age of time (Internet) oders where placed by phnoe (landline) and/or by a written order (letter). The mailman delivered your package. The needs of consumers could usually be satisfied by local and specialty stores. Uncommon goods were ordered out of catalogues, all delivered from some distribution center somewhere in the country. Delivery time was usually high (compared to today) but it was considered normal.
  
  
  With the coming of the digital age of time, consumers dont have to go to stores or use catalogues, they can literally every good in the world at their will. And they want it rather sooner than later. The company Amazon has managed to changed the worlddwide behavior. Everything is connected, every good available. Delivery times were and are still shortened to an extend that certain goods can be delivered "Next Day" or eben within "1 Hour". This is possible by smart distribution of locations of Distribution centers and the implementation of highly intelligent delivery processes. Without a sound and sophisticated delivery infrastructure, this world wide success would not be possible. 
  
  
  Amazon and others are looking into the next step: overcoming the delivery infrastucture and service (like American Postal Service or UPS/DHL) with their own, efficient and fast system. The logical solution lays within air transport. Its direct, not depending on street infrastructure and unmanned, potentially saving and cutting costs on the number of employees.


  Drone technolgy has become more advanced over the past few years from better batteries to more efficient brushless motors. Thus the capabilities are of drones are expanding like in the delivery industry. Additionally consumer trends are becoming more decentralized with the need for faster and more efficient delivery methods. For example Amazon has a service called Amazon Prime Air which allows the users to order items and have them deliverd in under an hour. A service like this will open up the markets for drone delivery resulting in less overhead for both the customer and drone delivery company. Lastly Uber is a company that is experimenting with using drones as a taxi service, which is very similar to a package delivery system. This shows that drone delivery systems are scalable for different scenarios. 
  

Standard ground based delivery systems will eventually be out dated for certain areas and through this simulation we hope to evaluate  the pros and cons and the overall effort needed to (partly) replace current ground based methods of delivery.
It is apparent that drone technology is something we can expect to see in the future. Delivery/logistics companies are currently testing drone capabilites to determine the effectivness of drone delivery.


(You should begin by introducing your topic. In this section, you should define the core terminology specific to the field, introduce the problem statement, and make clear the benefits (motivate!) of resolving that problem statement. The main difference between the ABSTRACT and Introduction sections is that the abstract summarizes the entire project, including results, whereas the introduc-tion only provides the motivation of the problem and an overview of the proposed solution.)

(I tell sutdents to answer the questions, one paragaph each to start if you are lost)

(Problem Statement. One paragraph to describe the prob-lem that you are tackling.)

We will answer following questions with our project:

+ How long does it take (on average) to deliver a package to a certain location by ground and by air?

+ How will that change with increasing number of orders and diversified locations?

+ At what point will the ground based solution be better than the air based solution (and vice versa)?

+ Taking technical development into account, which (overall) measurable effects will have changes in delivery speed, battery efficiency and increased payload for air based solutions (e.g. increase of possible flight time of 10% / 20%, shortended recharging time, etc.) ?

+ How can "Hubs" like package pick-up stations with an slightly increased delivery time influence the service, e.g. by allowing ground based delivery to become more efficient for this scenario.


(Motivation. Why is this problem interesting and relevant to the research community?)

The porposed questions and areas of research will help us to see how Amazon and other companies will forge the future of delivery. It can contribute to making predictions for efficiency and help to construct the overall layout of such a system. 

(Proposed Solution. How do we propose to tackle this problem (that has been identified in the previous para-graphs, is interesting to the community, and has yet to be tackled by other researchers)?)

We will tackle this problem by modeling a part of the City of Orlando and simulate 
+ the truck and 
+ the drone delivery methods 
+ to home locations and/or 
+ to delivery hubs. 
Our intention is to use Agent Based Simulation techniques.

(Contributions. An enumeration of the contributions of the senior design project)

I dont know that we will have any contributions..-marc

(This project makes the following contributions:)(you must have this!!)
•	(Contribution 1)
•	(Contribution 2)



## The Model

![Structural Diagram](images/obj_dia.jpg)

(Provide structural and behavior diagrams of the system you wish to study.) (Why is your model a good abtraction of the problem you want to study?) (Are you capturing all the relevant aspects of the problem?) (Use the model to tell us what is going on.)

![Behavior Diagram](images/beh_dia.jpg)

(explicitly list your requirements of what the model will have and simulate for the proposal)

## Fundamental Questions
(At the end of the project you want to find the answer to these questions) (Formulate a few, clear questions. Articulate them in sub-questions, from the more general to the more specific. )

1. Are drones more efficient than standard ground based delivery methods?

  1.1 How many drones does it take to out perfrom one delivery truck with 50 packages?
  
  1.2 How long does it take to deliver 50 packages via ground based system?
  
  1.3 How long does it take to deliver 50 packages via air based system?
  
 2. How does increased battery, max speed, and carrying capacity effect the number of drones needed?
 3. Can the drones reduce average delivery time by 30%? 
 4. 

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
