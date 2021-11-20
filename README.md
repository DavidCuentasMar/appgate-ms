# METRICS SERVICE API

## HOW TO RUN MS
- Execute this in terminal: docker-compose up --build
- Open new terminal windows and execute: docker-compose exec api ash
- Run this command: FLASK_APP=flask_app FLASK_ENV=development flask run --host=0.0.0.0 --port
=8000
- Now the user can start making requests at its localhost:8000

# ENDPOINTS
    This service provides 7 endpoints:
        - [POST] - http://localhost:8000/log
        - [GET]  - http://localhost:8000/metrics
        - [GET]  - http://localhost:8000/metrics/isuserknown
        - [GET]  - http://localhost:8000/metrics/isclientknown
        - [GET]  - http://localhost:8000/metrics/isipknown
        - [GET]  - http://localhost:8000/metrics/isipinternal
        - [GET]  - http://localhost:8000/metrics/failedlogincountlastweek

Each endpoint has this response structure as JSON:

```JSON
{ "result": "DATA RESPONSE" }
```

1. http://localhost:8000/log
    - **HTTP METHOD:** 
        - POST
    - **QUERY PARAMS:**
        - NONE
    - **BODY PARAMS:**
        - KEY: "file", VALUE: FILE
    - **DESCRIPTION:**
        - This endpoints recives a txt file and creates or updates the current historical service logs txt file

2. http://localhost:8000/metrics
    - **HTTP METHOD:** 
        - GET
    - **QUERY PARAMS:**
        - isuserknown
        - isclientknown
        - isipknown
    - **BODY PARAMS:**
        - NONE
    - **DESCRIPTION:**
        - Returns boolean, checks in the historical logs file if the given creteria match at least 1 log with strictly all 3 given values
    - **URI Example:**
        - http://localhost:8000/metrics?isuserknown=4f8a7f94?isclientknown=533e226f?isipknown=0.0.0.1

3. http://localhost:8000/metrics/isuserknown
    - **HTTP METHOD:** 
        - GET
    - **QUERY PARAMS:**
        - username
    - **BODY PARAMS:**
        - NONE
    - **DESCRIPTION:**
        - Retruns boolean, Cheks if given username has aready connections attemps 
    - **URI Example:**
        - http://localhost:8000/metrics/isuserknown?username=4f8a7f94        

4. http://localhost:8000/metrics/isclientknown
    - **HTTP METHOD:** 
        - GET
    - **QUERY PARAMS:**
        - client
    - **BODY PARAMS:**
        - NONE
    - **DESCRIPTION:**
        - Retruns boolean, Cheks if given client has aready connections attemps 
    - **URI Example:**
        - http://localhost:8000/metrics/isclientknown?client=533e226f

5. http://localhost:8000/metrics/isipknown
    - **HTTP METHOD:** 
        - GET
    - **QUERY PARAMS:**
        - ip
    - **BODY PARAMS:**
        - NONE
    - **DESCRIPTION:**
        - Retruns boolean, Cheks if given ip has aready connections attemps 
    - **URI Example:**
        - http://localhost:8000/metrics/isipknown?ip=0.0.0.0

6. http://localhost:8000/metrics/isipinternal
    - **HTTP METHOD:** 
        - GET
    - **QUERY PARAMS:**
        - ip
    - **BODY PARAMS:**
        - NONE
    - **DESCRIPTION:**
        - Retruns boolean, Cheks if given ip is in internal ip list
    - **URI Example:**
        - http://localhost:8000/metrics/isipinternal?ip=0.0.0.0
    
7. http://localhost:8000/metrics/failedlogincountlastweek
    - **HTTP METHOD:** 
        - GET
    - **QUERY PARAMS:**
        - NONE
    - **BODY PARAMS:**
        - NONE
    - **DESCRIPTION:**
        - Returns Integer, Count of all connections attemps that contains "SUSPEC"

# TESTING:
    - In order to run tests use the following command: python -m pytest -vv

# IMPORTANT NOTES:
    - The values that match this pattern [value1:value2] in logs file are considered as [user_id:client_id]
    - In this basic implementation when tests are executed the historical metris logs stores test data
    - Failedlogincountlastweek checks from current date to 7 days before
    - There's no complexity in searching proceess if a given value is just found in a specific column that's considered a positive result
    - Since alpine image is been used, it slows down the docker image building process (5 to 15 mins)
    - Logs file structure: DATE, TIME, SERVERNAME, [USER:CLIENT], MESSAGE


