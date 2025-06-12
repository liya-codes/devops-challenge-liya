# Project Summary

I began by setting up all prerequisites, including new Docker Hub and GitHub accounts, and forking the provided repository. After reviewing the assignment and Travis CI documentation, I started with a simple FastAPI router to connect to DynamoDB. I encountered an issue activating my virtual environment due to PowerShell restrictions, which I resolved by updating the execution policy.

Once the environment was set up, I installed dependencies, configured environment variables, and established a connection to DynamoDB. I initially struggled to retrieve items due to a key naming mismatch, but after some help, I corrected the key to camelCase and successfully accessed the data.

Next, I created a Dockerfile and moved on to Travis CI for continuous integration. My first CI run failed because the config file was named `.travis.yaml` instead of `.travis.yml`, which I quickly fixed. I structured my CI pipeline into separate stages for linting, testing, and building/pushing the Docker image. I also ensured sensitive environment variables were securely managed in Travis CI.

During testing, I faced issues with Docker image availability between CI stages and with using `--env-file` in Travis. I resolved these by pushing temporary images and setting environment variables directly in Travis. Additionally, I encountered timeouts in pytest due to the app container not being fully ready, which I fixed by adding a wait before running tests.

Finally, I created a Docker Compose file and documented the process. Throughout, I focused on keeping the workflow secure and efficient, ensuring all stages from development to deployment were robust and well-documented.