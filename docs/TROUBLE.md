# Troubleshooting Log

## 1. Virtual Environment Activation Issue  
**Problem:**  
Could not activate venv due to PowerShell script execution policy:  
```
.\.venv\Scripts\activate : File ... cannot be loaded because running scripts is disabled on this system.
```
**Fix:**  
Ran `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` to allow script execution.

---

## 2. DynamoDB GetItem ValidationException  
**Problem:**  
Error when calling GetItem:  
```
botocore.exceptions.ClientError: An error occurred (ValidationException) when calling the GetItem operation: The provided key element does not match the schema
```
**Fix:**  
Discovered the key name was in camelCase. Changed to correct key name and it worked.

---

## 4. Docker Run --env-file Issue in Travis  
**Problem:**  
Could not use `--env-file` with `docker run` in Travis CI.  
**Fix:**  
Set environment variables directly in Travis CI settings, keeping secrets secure.

---

## 5. Docker Image Not Available Across Stages  
**Problem:**  
Image built in the build stage was not available in the test stage.  
**Fix:**  
combined the stages into one stage

---

## 6. Docker Build --push Not Supported  
**Problem:**  
`docker build --push` was not available in Travis CI.  
**Fix:**  
Used separate `docker build` and `docker push` commands.
(in gitlab ci this would not happen)

---

## 7. Pytest Timeout Connecting to Container  
**Problem:**  
Pytest timed out because the FastAPI app container was not ready.  
**Fix:**  
Added a wait to ensure the app was fully loaded before running tests.

---