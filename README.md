# Twitter Analytics
Second project for the subject IMGIDS (Masters in Computer Engineering, UMA) where we will develop a web application that shows Twitter analytics implementing agile methodologies.

### Installation
This project requires [Python] v3+ to run.
First clone the repository:
```sh
$ git clone https://github.com/samuelhl/twitteranalytics.git
$ cd twitteranalytics
```

You need virtualenv installed to work in a virtual environment:
```sh
$ pip3 install virtualenv
# Create virtual environment
$ virtualenv -p python3 venv
# Activate virtual environment
$ source venv/bin/activate
# Install the required Python packages
$ pip3 install -r requirements.txt
```

Optional commands for virtualenv:
```sh
# Disable Python virtualenv
$ deactivate
# Add a requirement to the virtualenv requirements
$ pip freeze > requirements.txt
```

### How to run
```sh
$ cd twitteranalytics
$ python3 manage.py runserver
```

[Python]: <https://www.python.org/>
