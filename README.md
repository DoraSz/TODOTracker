How to start the TODO-Tracker


1. Installation


1.1 Virtual Environment

This article is written for Ubuntu. Most of it will run on any system, but the use of virtualenv might be different. Luckily, it has a good documentation online.

First, create a virtual python3 environment. This can possibly be skipped, but it is highly recommended as it will assure that a working version of the TODO Tracker will work forever and especially can't be destroyed by a libary update or anything like that.

We use virtualenv for this, if you don't have it installed, do so with the following command:

	pip3 install virtualenv

Now open a directory in a terminal that shall contain the TODO Tracker.
Here, create a new virtual python3 environment with the following command:
	virtualenv --python=python3 NAME_OF_YOUR_CHOICE
This will create a new directory with your chosen name. Change to that directory with
	cd NAME_OF_YOUR_CHOICE

Activate the environment with

	source bin/activate

You should see something like (NAME_OF_YOUR_CHOICE) at the beginning of each terminal line now.

1.2 Install django
It is important to have the virtual environment activated now, as we want django to be installed only locally. We do this with

	pip3 install Django

1.3 Clone the git repository

Now that you have you virtual environment open in your terminal, you can clone the repository with the command

	git clone https://github.com/DoraSz/TODOTracker.git

Congratulations! You have a great TODO Tracker now!



2 Starting

To start the TODOTracker, open the directory of your local repository in a terminal. If you have done the steps of the installation, do so with

	cd TODOTracker/

Now, type

	cd Djangoproject/
	
And start the webserver with

	python3 manage.py runserver

You will see something like:

		Performing system checks...

		System check identified no issues (0 silenced).
		May 12, 2016 - 21:07:44
		Django version 1.9.6, using settings 'mysite.settings'
		Starting development server at http://127.0.0.1:8000/
		
Open http://127.0.0.1:8000/ in your browser and enjoy a beatiful TODO Tracker.


