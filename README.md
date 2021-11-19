# METRICS SERVICE API

## HOW TO RUN MS
- Execute this in terminal: docker-compose up --build
- After the build is completed the user can start making requests at its localhost:8000


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
{
"result": "DATA RESPONSE"
}
```
    
# IMPORTANT NOTES
- The meaning of each column in logs.txt file is: [DATE, TIME, SERVERNAME, [USER_ID:CLIENT_ID, MSG]]
- After analyzing this file a new one is created as .csv and its columns are: [DATETIME, SERVERNAME, USER_ID, CLIENT_ID, MSG]

