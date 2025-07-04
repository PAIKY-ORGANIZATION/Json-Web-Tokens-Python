from sqlalchemy import create_engine, Column, String, Integer


from sqlalchemy.ext.declarative import declarative_base #$ This is the class that we're going to extend.
from sqlalchemy.orm import sessionmaker
import os 
import time



Base = declarative_base()

class User(Base):
    __tablename__ = "users" #$ This is the name of the table IN THE DATABASE 
    user_id = Column("userId", Integer, primary_key=True)
    username = Column("username", String, unique=True)
    favorite_food = Column("favorite_food", String)

    #$ Seems like this __init__ is not needed
    # def __init__(self, user_id: int, username: str, favorite_food: str):
    #     self.user_id = user_id
    #     self.username = username
    #     self.favorite_food = favorite_food

    def __repr__(self) -> str: # Here we specify how we want the object to be printed
        return f"({self.user_id}, {self.username}, {self.favorite_food})"




host = os.environ.get('DB_HOST')
                            #¡ Don't USE "?schema=public"
engine = create_engine(f"postgresql://postgres:postgres@{host}/python-users") #? GET THESE FROM ENV


def init_db():
    #* Try to initialize the database every 2 seconds. The database docker service might have already started but not accepting connections yet
    while True:
        try:
            Base.metadata.create_all(bind=engine)  #$ This applies the changes to the database (adds the tables) based on the "Base" class
            #$ bind=engine means: “Use this engine to run the SQL commands that create the tables.”
            print("Database initialized successfully or was already initialized")
            break
        except Exception as e:
            print(f"Error initializing database: {e}")
            time.sleep(2)


def get_session():
    session = sessionmaker(bind=engine)()
    return session


