import os
from dotenv import load_dotenv

def load_env_files():
    environment = os.environ.get('ENVIRONMENT')



    load_dotenv("./config/shared.env")
    load_dotenv(f"./config/{environment}.env")


    required_envs = [
        'ENVIRONMENT',
        'DB_HOST',
        'PORT',
    ]

    for env in required_envs:
        if not os.environ.get(env):
            raise Exception(f"{env} is not set ⚠️")   

