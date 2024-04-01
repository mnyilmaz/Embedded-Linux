# Week 8

This week's responsibilities includes 

 - Problem solving
 - Test valus for temp
 - Subscribe code
 - Documentation
and related work to these topics can be found below.

## Publish error solving

Payload were sending using usual create_message function. Response was OK yet nothing to show on ThingsBoard app. Yet when we inspect the error closer we found out format of the payload is not proper to deliver message to ThingsBoard telemetry screeen. Related to that problem sending payload message as ***str*** solved the issue. For a better customer experience edited this inside ThingsBoard class. Payload is being sent as str to create_message function. Telemetry value updates can be seen through ThingsBoard App.

## Temp value 

After receiving values from app, integrated real-time example for ThingsBoard as temp value observation. This code receiving real-time temp values within 30 seconds and sending values to the ThingsBoard telemetry page to observe. ThingsBoard has lots of visualization components including dashboards. These components let user to understand data difference and change relativeley, based on time. 30 seconds is essential. At first attempt time between was limited in a second. This caused an error while receiving and calculating data. 10 seconds was enough for the data yet 30 seconds is the best choce for evaluating the environment not just calculating process. 


## Subscribe 
Subscribe code has been written earlier yet after errors test process for this part has been delayed. After resolving, this part re-written again. Receiving part remained unplanned due to receive method. According to usage a Telegram bot can be integrated in here. 


## Documentation
In final, a documentation must be written related to define the app that I've written. For this part our team shared an example document for us to make this app understanbele for the users. These examples had been observed and planned has been made for this documentation. Yet for the subscribe part plan is still on its way due to that preparation of this part is missing for now. Otherwise md file is being prepared.
