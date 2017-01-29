# Course Project - Virtual Lifestyle Coach 

**Introduction to Service Design and Engineering | University of Trento**

**Client | Telegram**

**Student**: Gianvito Taneburgo (182569)

This file aims to provide a short documentation for the course project. Further details can be found in the report [here](https://github.com/virtual-life-coach/common/blob/master/report.pdf).
The original instructions can be found [here](https://docs.google.com/document/u/1/d/1kU66KOoprmdypDEE1W1bs1iQsX-Vf7_SXH7gAm5UYMU/edit?usp=sharing).

The project was developed individually.


## Project structure

The project repository is made up of the following *files* and **folders**:
* **handlers**: handlers for client requests
    * *handlers.py*: handler for bot commands
    * *hook_handler.py*: handler for incoming messages
* **lib**: bot dependencies (must be deployed to avoid problems on GAE)
* *app.yaml*: GAE deployment descriptor
* *appengine_config.py*: required to include custom libraries into GAE environment
* *bot.py*: bot entry point
* *message_handler.py*: dispatch every bot request to the appropriate handler
* *README.md*: this file
* *request.py*: perform API calls to back end
