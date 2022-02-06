# Task Drone
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
>> Python3 
>> Mongodb
>> Postman


## About the project.
This API allows the client to:
- registering a drone;
- loading a drone with medication items;
- checking loaded medication items for a given drone;
- checking available drones for loading;
- check drone battery level for a given drone;


I have used ``` random ``` a python library to generate Data for various variables used in the project. I have also used it to assign different states to newly created drone and also assigning battery charge.
This data is then consumed by the API in JSON form and fed to the database. Using Postman, the required data is fetched an the same format.


## Building instructions
**IDE used VSCODE**

- To run MongoDb open terminal and type ```mongo start```
- Open folder containing the file task_Drone.py on yout IDE(I used VSCODE)
- Open terminal on VsCode by pressing ```Ctrl+``` . (help in displaying vital information when the program is running)
- Click Run button.



## Testing
open Postman and type the following commands to test the API.

### 1. registering a drone

Select POST method then type ```http://localhost:5000/add``` on the URL bar, Click **SEND** to send the request. You shoud be ble to see a success message.\
<img src="https://raw.githubusercontent.com/charlesncn/task_Drone/master/img/add.png">


### 2. loading a drone with medication items;
Select PUT method then type ```http://localhost:5000/add-load``` on the Url bar, Click **SEND** to execute the request.
Every time a drone is loaded its state changes from **IDLE** to **LOADING**.

<img src="https://raw.githubusercontent.com/charlesncn/task_Drone/master/img/addLoad.png">
fig 2.0 Loading a drone with a state IDLE with medication.


<img src="https://raw.githubusercontent.com/charlesncn/task_Drone/master/img/AddMedError.png">
fig 2.1 Loading drone that is  not at IDLE state


### 3. checking loaded medication items for a given drone;
Select GET method and type ```http://localhost:5000/get-med/<id>``` on the url bar. **Replace <id> with the actual id of the drone you want to check.** and 
click **SEND** The API will filter out the fields containing information about medication loaded to that drone.
<img src="https://raw.githubusercontent.com/charlesncn/task_Drone/master/img/viewMedOnDrone.png">
  

  
### 4. checking available drones for loading;
This method filters out those drones that are IDLE and have Charge of more than 25%.
Select GET method and type ```http://localhost:5000/available``` on the url bar and click **SEND**
<img src="https://raw.githubusercontent.com/charlesncn/task_Drone/master/img/avail.png">


### 5. check drone battery level for a given drone.
Select GET method and type ```hhttp://localhost:5000/get-battery/<id>``` on the url bar. **Replace <id> with the actual id of the drone you want to check.** and 
click **SEND**.
<img src="https://raw.githubusercontent.com/charlesncn/task_Drone/master/img/getBatID.png">
