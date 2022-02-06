# Task Drone
### REST API

### Language
> Python
### framework
> Flask
### Database
> Mongodb running locally

### API test platform
> postman


## About the project.
This API allows the client to:
- registering a drone;
- loading a drone with medication items;
- checking loaded medication items for a given drone;
- checking available drones for loading;
- check drone battery level for a given drone;


I have used ``` random ``` a python library to generate Data for various variables used in the project.
This data is then consumed by the API in JSON form and fed to the database. Using Postman, the required data is fetched an the same format.



## Building instructions
- IDE used VSCODE.
1. Open folder containing the file task_Drone.py on yout IDE(I used VSCODE)
2. Open terminal on VsCode by pressing ```Ctrl+``` . (help in displaying vital information when the programm is running)
3. Click Run button.


## Testing
open Postman and type the following commands to test the api.

### egistering a drone

Select POST method then type ```http://localhost:5000/add``` on the Url bar, Click **SEND** to send the request. You shoud be ble to see a success message.

### loading a drone with medication items;
Select PUT method then type ```http://localhost:5000/add-load``` on the Url bar, Click **SEND** to execute the request.

### checking loaded medication items for a given drone;
Select GET method and type ```http://localhost:5000/get-med/<id>``` on the url bar. **Replace <id> with the actual id of the drone you want to check.** and 
click **SEND** The API will filter out the fields containing information about medication loaded to that drone.

### checking available drones for loading;
This method filters out those drones that are IDLE and have Charge of more than 25%.
Select GET method and type ```http://localhost:5000/available``` on the url bar and click **SEND**

### heck drone battery level for a given drone.
Select GET method and type ```hhttp://localhost:5000/get-battery/<id>``` on the url bar. **Replace <id> with the actual id of the drone you want to check.** and 
click **SEND**.
