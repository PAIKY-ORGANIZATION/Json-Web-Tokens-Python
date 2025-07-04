
    #* Why do we need to create the server object ("app") in a different file ("app_setup")?

#$ Believe me one day I understood why I need to import the app from another file if I am going to be importing "router". 
#% It has to do with this vial being ran as "__main__" when you do python3 app.py 
#¡ It DOESN'T have anything to do with this line "if __name__ == "__main__":"

#% The behavior issue is that THIS file runs when you 1- import router AND 2- router imports app.
#!  It is ⚠️NOT⚠️ a "Circular dependency issue"  tho. It has to do with __name__

#! Again, also:   It DOESN'T have anything to do with this line "if __name__ == "__main__":"

#% Why does it run twice?
    #$ WRITTEN BY ME WITH  GPT HELP:
    #% Because when you run this file using "python3", this  file gets registered  into "sys.modules" with  the  "__main__"
    #%"sys.modules" is a Python-internal dictionary that keeps track of all modules that have been imported so far in the current process.

    #% Now HERE IS THE CAKE LOL: When you import "router" and "router" finds this line: "from app_listens import app" It will ask sys.modules: 
        #% Have you registered a file with the name  "app"?
    #% Since it has not it will run THIS file again.
    #% That is why you need to avoid creating the server object (app = Flask(__name__)) in this file.
    #% Instead create the serv





from src.bootsrap import load_env_files
import os

load_env_files()
from src.db.db_init import init_db



init_db() #* Load the database. 
port = os.environ.get('PORT') or 3004



from src.app_setup import app
import src.router # type: ignore


app.run(host="0.0.0.0", port=int(port), use_reloader=False, debug=False)