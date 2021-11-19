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
        - 
    - **BODY PARAMS:**
        - 
    - **DESCRIPTION:**
        - 

3. http://localhost:8000/metrics/isuserknown
    - **HTTP METHOD:** 
        - GET
    - **QUERY PARAMS:**
        - 
    - **BODY PARAMS:**
        - 
    - **DESCRIPTION:**
        -

4. http://localhost:8000/metrics/isclientknown
    - **HTTP METHOD:** 
        - GET
    - **QUERY PARAMS:**
        - 
    - **BODY PARAMS:**
        - 
    - **DESCRIPTION:**
        -

5. http://localhost:8000/metrics/isipknown
    - **HTTP METHOD:** 
        - GET
    - **QUERY PARAMS:**
        - 
    - **BODY PARAMS:**
        - 
    - **DESCRIPTION:**
        -
6. http://localhost:8000/metrics/isipinternal
    - **HTTP METHOD:** 
        - GET
    - **QUERY PARAMS:**
        - 
    - **BODY PARAMS:**
        - 
    - **DESCRIPTION:**
        -
7. http://localhost:8000/metrics/failedlogincountlastweek
    - **HTTP METHOD:** 
        - GET
    - **QUERY PARAMS:**
        - 
    - **BODY PARAMS:**
        - 
    - **DESCRIPTION:**
        -                       