# DRF Cartoonize API

![Logo](https://raw.githubusercontent.com/tinshade/cartoonize-api/main/SS/Cartoonize.png)


## Description
This is a simple API made with [Django's REST Framework](https://www.django-rest-framework.org/) module.
As the name suggests, this API returns a link to a *cartoonized* image of the given input image. I have used my own [gist](https://gist.github.com/tinshade/49262f7b9093192d145e0e7fb5cd0fe2) for this task.

This API is live [here](http://cartoonize-api.herokuapp.com/) at endpoint ```/api/cartoonize/```, served on [Heroku](https://heroku.com/). Since Heroku does not allow for dynamically created files to be permanently stored, the file you create using this API must be downloaded as soon as possible, or at least before the dyno restarts.

## Working

#### Original Image
![Original Image](https://raw.githubusercontent.com/tinshade/cartoonize-api/main/media/user-images/uploads/tinshade.jpg)

#### Cartoonized Image
![Cartoonized Image](https://raw.githubusercontent.com/tinshade/cartoonize-api/main/media/user-images/served/Abhishek.png)


## Parameters

#### All of the parameters are mandatory!

	1. *name* : Give it any name you want!
	2. *ext* : Set the desired extension for the output file. Like PNG or JPG!
	3. *file* : Upload the input image!

## Usage
The local version can be used via ```curl``` or an API testing suite such as [Postman](https://www.postman.com/). If you want to hit the live API, swap out ```https://127.0.0.1:8000``` for ```http://cartoonize-api.herokuapp.com/``` and move to step 6.

	1. Clone this repo: ```git clone https://github.com/tinshade/cartoonize-api.git```
	2. Change into the directory: ```cd cartoonize-api```
	3. Initialize a virtual environment of your choice. My runtime is Python 3.8.0 with *venv*
	4. Install dependencies: ```pip install -r requirements.txt```
	5. Start the server : ```python manage.py runserver```
	6. Hit the server endpoint with the three parameters as shown below:

![Parameters with POSTMAN](https://raw.githubusercontent.com/tinshade/cartoonize-api/main/SS/postmanop.PNG)


Here's what your terminal will look like:
![CMD output](https://raw.githubusercontent.com/tinshade/cartoonize-api/main/SS/cmdop.PNG)


Here's the output on the browser via the link given in Postman's response:
![File on browser](https://raw.githubusercontent.com/tinshade/cartoonize-api/main/SS/browserop.PNG)


## Known Annoyances

	1. The server times out if the image is over 1Mb.
	2. Only accepts JPG, however that should not be the case. Error handling still works.
	3. No detailed description of the required parameters anywhere except this page.
	4. Not optimized/tested for scaling!