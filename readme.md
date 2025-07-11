# Cookies and JWTs to store user session information.

### API Documentation and About:

[API Documentation](https://documenter.getpostman.com/view/40182356/2sB2xBEqrP)





## How to Use the Application

### Run with Docker Compose (recommended if you have Docker, includes a Postgres service and works out of the box):

### Install Dependencies:

```bash
   pip install -r requirements.txt
```


### For Linux/MacOS:
(Assuming you have a "bash" shell)
```bash
   /bin/bash script.sh dev_docker
```

How to run locally:

```bash
   /bin/bash script.sh dev
```



### Environment Configuration Overview
1. A "bootstrap.py" file is loaded automatically on startup to manage environment variables using dotenv.

2. config/{environment}.env is loaded based on os.environ.get('ENVIRONMENT') 


3. Inside of config/, MAKE SURE you rename any "example*....env" by removing the "example" part. 
         Example: example-shared.env -> shared.env

4. Also, MAKE SURE you set the required env variables in the -example files if they are not set

