# pygame-website

Repository for Pygame orientated website

Githib link: https://github.com/maximinus/pygame-website


To set up and run on Linux:
===========================

Start a virtual environment. This will create a directory called pygame:

	virtualenv pygame

Start the environment:

	source pygame/bin/activate

Now you need to download the repository:

	git clone https://github.com/maximinus/pygame-website.git
	cd pygame-website

Now we need to download all python packages:

	pip install -r requirements.txt

Now we can run the django server:

	cd pygamesite
	./serve

Now load up a web browser and go to:

	127.0.0.1:8000

And you should see a welcome screen.

The directory structure in the pygamesite is as follows:

	/media			- this is for uploads from users
	/static			- this is for static files
		/images
		/css
		/js
	/templates		- this is the templates used to build the HTML. These files are 95% HTML and a little bit of Django templates

The other folders all relate to Django internals.


Referencing static media
========================

If there is a file on the server such as:

	/static/some_folder/some_file.png

And we wish to use on the HTML as:

	<img src="/static/some_folder/some_file.png">
	
Then to use in the templates we have to do:

	<img src="{% static "/some_folder/some_file.png" %}">

See the source code for main.html under /templates for the example.


