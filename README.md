# Drone Controller API
Service to mange drones
### REST API

> **Language**
>> Python

> **framework**
>> Flask

> **Database**
>> Mongodb (running locally)

> **API test platform**
>> postman

> **prerequisites & required installations**
>> Python3\
>> Mongodb\
>> Postman<br>


## About the project.
This API allows the client to.
- registering a drone.
- loading a drone with medication items.
- checking loaded medication items for a given drone.
- checking available drones for loading.
- check drone battery level for a given drone.<br><br><br>


I have used ``` random ``` a python library to generate Data for various variables used in the project. I have also used it to assign different states to newly created drone and also assigning battery charge.
This data is then consumed by the API in JSON form and fed to the database. Using Postman, the required data is fetched/updated using the same data
format(JSON)<br><br><br>


## Build instructions
**IDE used VSCODE**

- To run MongoDb open terminal and type ```mongo start```
- Open folder containing the file task_Drone.py on yout IDE(I used VSCODE)
- Open terminal on VsCode by pressing ```Ctrl+``` . (help in displaying vital information when the program is running)
- Click Run button.



## Testing
open Postman and type the following commands to test the API.

### 1. registering a drone
Select POST method then type ```http://localhost:5000/add``` on the URL bar, Click **SEND** to send the request. You shoud be ble to see a success message.\
<img src="https://raw.githubusercontent.com/charlesncn/task_Drone/master/img/add.png"><br><br><br>


### 2. loading a drone with medication items;
Select PUT method then type ```http://localhost:5000/add-load``` on the Url bar, Click **SEND** to execute the request.
Every time a drone is loaded its state changes from **IDLE** to **LOADING**.

<img src="https://raw.githubusercontent.com/charlesncn/task_Drone/master/img/addLoad.png">
fig 2.0 Loading a drone with a state IDLE with medication.<br><br><br>


<img src="https://raw.githubusercontent.com/charlesncn/task_Drone/master/img/AddMedError.png">
fig 2.1 Loading drone that is  not at IDLE state<br><br><br>


### 3. checking loaded medication items for a given drone;
Select GET method and type ```http://localhost:5000/get-med/<id>``` on the url bar. **Replace <id> with the actual id of the drone you want to check.** and 
click **SEND** The API will filter out the fields containing information about medication loaded to that drone.<br><br>
<img src="https://raw.githubusercontent.com/charlesncn/task_Drone/master/img/viewMedOnDrone.png"><br><br><br>



### 4. checking available drones for loading;<br><br>
This method filters out those drones that are IDLE and have Charge of more than 25%. Select GET method and type
```http://localhost:5000/available``` on the url bar and click **SEND**. In this case there was only one drone that was IDLE
<img src="https://raw.githubusercontent.com/charlesncn/task_Drone/master/img/avail.png"><br><br>
However after adding more drones to the fleet I got another IDLE drone with a healthy battery.<br><br>
<img src="https://raw.githubusercontent.com/charlesncn/task_Drone/master/img/available2.png"><br><br><br>


### 5. check drone battery level for a given drone.<br>
Select GET method and type ```hhttp://localhost:5000/get-battery/<id>``` on the url bar. **Replace <id> with the actual id of the drone you want to check.** and 
click **SEND**.<br><br>
<img src="https://raw.githubusercontent.com/charlesncn/task_Drone/master/img/getBatID.png"><br><br><br>

### Battery Log.<br><br>
<img src="https://github.com/charlesncn/task_Drone/blob/master/img/BatLog.png"><br><br><br>

## END
