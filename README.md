# NLP_Webapp
Book recommendation engine application

# INSTALLATION AND EXECUTION MANUAL

To be able to run the Book Recommendation System, it is required to: 

- Create a GitHub account. 
- Download and install Git (already installed on Mac). 
- Download and install Django. 

## Start Django Webb App for NLP

### How to prepare your local machine

#### Virtual Environment

On your command line, to see if you have virtual environment installed:

_For MAC_:
```command
virtualenv --version
```
_For Microsoft_:
```command
venv --version
```

If there appears an error, run:

_For MAC_:
```command
pip install virtualenv
```

_For Microsoft_:
```command
pip install venv
pip install virtualenv
```

To start the virtual environment:

_For MAC_ and _Microsoft_ normally:

```command
python -m venev env
```
This will create a folder in your local repository that contains the following folders, by default:

_For MAC_:
* bin
* lib
* include

_For Microsoft_:
* Script
* Lib
* Include

So being **in** the folder _env_ you can now **activate** the environment:

_For MAC_:
```command
source env/bin/activate
```

_For Microsoft_:
```command
Script/activate
```

<img src ="https://github.com/Hupperich-Manuel/NLP_Webapp/blob/main/img/Screenshot_1.png"/>
<img src ="https://github.com/Hupperich-Manuel/NLP_Webapp/blob/main/img/Screenshot_2.png"/>

_Note: in this case I named my virtual environment **coursera**_

#### Git and Visual Studio Code

```command
git --version
```

If you havent installed it, download git on your machine.

Install [_Visual Studio Code_](https://code.visualstudio.com/download)

##### Git

Firstly, you need to clone the repository on your local machine. This is done on a terminal of your desired folder using the following command line:

```command
git clone <link to the repository>
````

Now you are ready to move on.

In case you are making any change in the files through Visual Studio Code, in order to push the changes you will have to do the following.

```command
git status
````
Notice that the changes you made are marked in red

```command
git add .
```
If you run again the status you will see how the red files turned into green.

```command
git commit -m "<Comment briefly the changes you made>"
```

```command
git push origin main
```

Now go into your git repository and create the _pull request_.

<img src ="https://github.com/Hupperich-Manuel/NLP_Webapp/blob/main/img/Screenshot_3.png"/>


This section of your forked repository will keep you updated on the changes that have been made in the original repo.

IMPORTANT: **Never forget to git pull**

Once done this, every time you want to work on the project make sure to open the terminal on your cloned folder and run a:
```command
git pull
```
To update your folder before any change (not doing this might lead to future errors).

**Now you are ready to start working on the django NLP repository**


#### Django

Now having cloned the repo and having run the virtual environment.

```command
cd NLP_Webapp
```
and run

```command
pip install django==3.2.5
```

To install the requirements _mac_
```command
pip install -r requirements.txt
```

Then do 

```command
cd mysite
```
Now you can run:
```command
python manage.py check
```
If all the code is checked and there are no errors, you will be able to run

```command
python manage.py runserver
```
You are running the webapp on your computer. Feel free to visit the host http://127.0.0.1:8000/nlp_app/ to use the Book Recommendation System. 
