<!-- header -->
<h1 style="text-align: left; margin-top:0px;">
  Shotput -Url Shortener API
</h1>

> Url shortener API with Django and django rest framework.






Project consists to allow a user to transform a long web url into a
pattern-consistent (encoded) small url easy to share and remember.

At the same time the user is allowed to transform back (decode)
the small url into the original url 

It is partly tested as only and was developed as showcase only.




How Url Shortener API Works:
- You can send (POST) a full url and retrieve a small encoded one with tier.app as the base web service url.

    Eg. POST https://stark-scrubland-55374.herokuapp.com/shorten-url/
        with https://www.newsbytesapp.com/
        result: stark-scrubland-55374.herokuapp.com/qyMX6k (6 digits id)
    
- You can get the original url with the encoded url on a GET request (done in previous step)

    Eg. GET stark-scrubland-55374.herokuapp.com/qyMX6k
        result: https://www.newsbytesapp.com/
        

<br><br>

## Index:
- #### Installation
    1. Installing Django API App

- #### Usage:
    1. Available Endpoints

- #### What's Next:
    1. thoughts on improving it.
        - Testing
        - UI
        - Database
     




<br><br>


## Installation:
#### 1.Installing Django API App

1. Clone repository and go inside the repository folder "url-shortener-api"
```sh
git clone https://github.com/shadowpint/shotput.git
```

2. Create you virtualenv and install the packages
```sh
pip install -r requirements.txt
```

3. Initialize database and create the database mapping used for persistance in the url shortener API.
```sh
python manage.py makemigrations
```

4. Apply the database mapping from the app to the database; migrate the database.
```sh
python manage.py migrate
```

5. Run the application.
```sh
python manage.py runserver
```


<br>

## USAGE
#### 1. Endpoint List
URI Example: `http://localhost:8000/shorten-url/`


| | Available Methods | URI | Example URL |
| -: | :- | :- | -: |
| | | | |
| | **Project Endpoints** | | |
| 1. | `POST` | `shorten-url/` | `http://localhost:8000/shorten-url` |
| 2. | `GET`  | `/<short_id>` | `http://localhost:8000/<short_id>` |


<br>



###### Access and Interact with a GUI app (Postman)
To interact and start using the API, you will need a tool send HTTP requests to your api. I have develop a list of request to test and interact with the api with Postman. You will need to download the Postman Desktop app or the Web Browser plug in for Chrome. Click on the button below to guide you to download the app with the list of request I have developed to test the api fast.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/0ceacd6a31a6ad47ec4e)

<br>


## WHATS NEXT
#### 1. Thoughts on improving it.

###### Testing
- integrate functional testing into the django app
- add personalized assert messages and setup error message separated structure
###### API
- set up error handling and eliminate chunks of ugly try:
- set up rest full service (if required (del, list, ...))
- do short url should expire set up?
- refactor
###### Database
- set up a mysql db 
- set up and split stats and ShortUrl models
###### DevOps
- set up automated testing pipeline


## Information:
| Technology Stack |  |  |
| :- | :-: | :- |
| Python                    | ![back-end][python]                   | Back-End |
| Django                    | ![django][django]                     | Web Framework |
| Django Rest Extension     | ![api-extension][django-rest-extension]| API Django Extension |
| SQLite                    | ![database][sqlite]                   | Database |
| Postman                   | ![http request app][postman]          | HTTP requests app |

<br><br>






<!-- Links -->
<!-- Profiles -->
[github-profile]: https://github.com/shadowpint/


<!-- Extra -->
[postman-button-svg]:https://run.pstmn.io/button.svg



<!-- Repos -->
[github-repo]: https://github.com/shadowpint/shotput.git



<!-- images -->
[python]: readme/python.png
[django]: readme/django.png
[django-rest-extension]: readme/django-rest-extension.png
[sqlite]: readme/sqlite.jpeg
[postman]: readme/postman.png