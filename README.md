# NLP_Webapp
Book recommendation engine application


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
source bin/activate
```

_For Microsoft_:
```command
Script/activate
```

<img src ="img/Screenshot_1"/>
<img src ="img/Screenshot_2"/>

_Note: in this case I named my virtual environment **coursera**_

#### Git and Visual Studio Code

```command
git --version
```

If you havent installed it, download git on your machine.

Install [_Visual Studio Code_](https://code.visualstudio.com/download)

##### Git

The **Number 1 rule is to always git pull**

But, since you havent your repo in your local machine you first need to do some steps.

1. Go to the [NLP_Webapp](https://github.com/Hupperich-Manuel/NLP_Webapp) and **fork** it.
2. Clone the forked inside of **your repositories** on your local machine. This is done on a terminal of your desired folder.

```command
git clone <link to your forked repository>
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
pip install django
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

You are running the webapp on your computer. Feel free to visit the host http://127.0.0.1:8000/nlp_app/ that django uses on your machine to see how the changes you did or the ones from your colleages are reflected on the UI.


In case you have further questions, reach me out.