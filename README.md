# DataRepresentation2020
Big Project for Data Representation


## 1. Files uploaded to Github

GiHub repository (public): https://github.com/SasikalaGV/DataRepresentation2020
- server: server.py
- web page: index.html
- DAO: stockDAO.py
- DB config to edit dbconfigtemplate.py
- Virtual environment requirements: requirements.txt
- Sample API File: WeatherTestAPI.py [Tried to add an API to show weather condition for a selected county]

### MySQL database & table

Database = datarepresentation  
Table = stock

MySQL command to create stock table:

CREATE TABLE Stock (id INT AUTO_INCREMENT PRIMARY KEY, category VARCHAR(50), name VARCHAR(255), quantity INT);

desc stock;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int(11)      | NO   | PRI | NULL    | auto_increment |
| category | varchar(50)  | YES  |     | NULL    |                |
| name     | varchar(255) | YES  |     | NULL    |                |
| quantity | int(11)      | YES  |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+

### Web page
- CSS Bootstrap: buttons, form
- Added host code to ajax calls

### DAO
- stockDAO.py contains stockDAO class

### Current working version:
- index.html
- server.py
- stockDAO.py

### API 
- WeatherTestAPI.py
- Subscribed to http://api.openweathermap.org/data/2.5/weather? and got the App Key to run the API to get the weather condition for the Store
- Had an issue with hosting two different hosts and couldn't connect the weather API to the main server.py.
- In order to test weather API, please run WeatherTestAPI on cmder command prompt