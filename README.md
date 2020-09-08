# weather-station
Software part of RPI/Arduino based weather station 

## To setup application with environment variables  

Deactivate active virtualenv and install **autoenv** 
```sh
$ deactivate
$ pip install autoenv
$ touch .env
```

Edit .env (should be in the project directory) 
```
source env/bin/activate
export APP_SETTINGS="config.DevelopmentConfig"
```
env - directory where is virtualenv files are located

Edit bashrc(~/.bashrc) directly or via echo
```sh
$ echo "source  ~/.local/bin/activate.sh"
$ source ~/.bashrc
```

Now the environment will automatically be started when you move to the project directory
