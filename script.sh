case $1 in


    #¡ If the app fails to run with this command it will restart automatically without pointing to a concrete error. Example: a missing port, General syntax error.
    dev_local)
        watchmedo auto-restart \
            --patterns="*.py" \
            --recursive \
            -- bash -c "ENVIRONMENT=local python3 app_listens.py" #$ To a load the environment variable along the main command you need to wrap this in "bash -c"
    ;;

    dev_docker)
        watchmedo auto-restart \
            --patterns="*.py" \
            --recursive \
            -- bash -c "ENVIRONMENT=docker python3 -u app_listens.py" #$ -u: Unbuffered output ...... Meaning that we will see output like print() statements in the terminal. When running on Docker they are not shown by default.
             #$ To a load the environment variable along the main command you need to wrap this in "bash -c"  
    ;;

esac