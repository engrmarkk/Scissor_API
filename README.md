# Scissor API

<!-- Back to Top Navigation Anchor -->

<a name="readme-top"></a>


<!-- https://user-images.githubusercontent.com/100721103/200149633-373db975-c47f-43a7-9288-f6cbd16e0410.mp4 -->

<br><br>
<!-- Project Shields -->
<div align="center">

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Twitter][twitter-shield]][twitter-url]

[//]: # ([![Twitter][twitter-shield2]][twitter-url2])

</div>

<br />

<div>
  <p align="center">
    <a href="https://github.com/engrmarkk/Scissor API#readme"><strong>Explore the docs »</strong></a>
    <br />
    ·
    <a href="https://github.com/engrmarkk/Scissor API/issues">Report Bug</a>
    ·
    <a href="https://github.com/engrmarkk/Scissor API/issues">Request Feature</a>
  </p>
</div>

---

<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-Scissor API">About the project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#features">Features</a></li>
      </ul>
      <li><a href="#demo">Demo</a></li>
    </li>
    <li>
      <a href="#exposure">Exposure</a>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#project-structure">Project Structure</a></li>
         <li><a href="#endpoints">Endpoints</a></li>
      </ul>
    <!-- <li><a href="#shots">Shots</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
  <p align="right"><a href="#readme-top">back to top</a></p>
</details>

---

<!-- About the api -->

## About Scissor API

The Scissor API is a project that encompasses a URL Shortener API with built-in authentication and authorization features. This project aims to provide a convenient and secure solution for URL shortening.

With the Scissor API, users can easily generate shortened URLs for long web addresses. The API allows users to submit a long URL through a simple request and receive a shortened version in return. This makes it easier to share URLs on platforms with character limitations or in situations where concise and readable links are preferred..
### Features
- URL Shortening: Generate shortened URLs from long web addresses.
- QR Code Generation: Generate QR codes corresponding to the shortened URLs.
- URL Management: View and manage the list of URLs that have been shortened.
- Authentication: Implement authentication mechanisms for secure access.
- Authorization: Set permissions and access levels for different users or roles.


<p align="right"><a href="#readme-top">back to top</a></p>



### Built With:

![Python][python]
![Flask][flask]
![Postgres][postgres]

<p align="right"><a href="#readme-top">back to top</a></p>

---

[//]: # (## Demo)

[//]: # ()
[//]: # (https://user-images.githubusercontent.com/100721103/225929529-95040462-f36d-4880-854c-c89b4bac6d33.mp4)

[//]: # ()
[//]: # (<br><p align="right"><a href="#readme-top">back to top</a></p>)

---
<!-- Lessons from the Project -->

## Exposure

Creating this project got me more exposed to:

- Debugging
- Restful API
- Thorough research
- Database Management
- Authentication
- Authorization
- Endpoint restriction
- Testing with unittest
- Swagger UI
- API Documentation
- Integration with React

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- GETTING STARTED -->

## Usage

To get a local copy up and running, follow the steps below.

### Prerequisites

Python3: [Get Python](https://www.python.org/downloads/)

### Installation

1. Clone this repo
   ```sh
   git clone https://github.com/engrmarkk/Scissor_API.git
   ```
2. Navigate into the directory
   ```sh
   cd Scissor_API
   ```
3. Create a virtual environment
   ```sh
   python -m venv your_venv_name
   ```
4. Activate the virtual environment on powershell or cmd
   ```sh
   your_venv_name\Scripts\activate.bat
   ```
   On Bash ('Scripts' for windows, 'bin' for linux)
   ```sh
   source your_venv_name/Scripts/activate.csh
   ```
5. Install project dependencies
   ```sh
   pip install -r requirements.txt
   ```
6. Set environment variables
   ```sh
   set FLASK_APP=app_config.py
   ```
   On Bash
   ```sh
   export FLASK_APP=app_config.py
   ```
   
7. Set the create_app function to run the app in development mode.
   Make sure the imported create_app function in the run.py looks like this
   ```sh
   app = create_app()
   ```
   and not like this
   ```sh
   app = create_app(configure=config_object['prodcon'])
   ```

8. Create database
   ```sh
   flask db init
   flask db migrate 'message'
   flask db upgrade
   ```
 
8. Run Flask
   ```sh
   flask run
   ```
   or
   ```sh
   python app_config.py
   ```
9. Use the link generated on the terminal to access the endpoints
    ```sh
   http://127.0.0.1:5000
   ```
   To use swagger-ui, use the link below
   ```sh
    http://127.0.0.1:5000/
   ```
   <br>
### Project structure
   ```
   .
   ├── README.md
   ├── .gitignore
   ├── LICENSE
   ├── api
   │   ├── __init__.py
   │   ├── auth
   │   │   ├── __init__.py
   │   └── config
   │   │   ├── __init__.py
   │   │   ├── your_db.sqlite3
   │   └── extensions
   │   │   ├── __init__.py
   │   └── models
   │   │   ├── __init__.py
   │   │   ├── links.py
   │   │   ├── revoke.py
   │   │   ├── users.py
   │   └── schemas
   │   │   ├── __init__.py
   │   │   ├── link.py
   │   │   ├── user.py
   │   └── test
   │   │   ├── __init__.py
   │   │   ├── test_link.py
   │   │   ├── test_user.py
   │   └── utils
   │   │   ├── __init__.py
   │   │   ├── url_validate.py
   │   └── views
   │   │   ├── __init__.py
   │   │   ├── url.py
   │   │   ├── users.py
   ├── your_venv_name
   ├── requirements.txt
   └── app_config.py
   ```  


### Endpoints
<br>
POST (Register) http://127.0.0.1:5000/register

REQUEST
```json
{
  "first_name": "string",
  "password": "string",
  "email": "string@string.com",
  "last_name": "string",
  "confirm_password": "string"
}
```
RESPONSE
```json
{
    "id": 1,
    "first_name": "string",
    "password": "string",
    "email": "string@string.com",
    "last_name": "string"
}
```
POST (Login) http://127.0.0.1:5000/login

REQUEST
```json
{
  "email": "user@example.com",
  "password": "string"
}
```
RESPONSE
```json
  {
    "access_token": "eyJhbGciOiJIUzIEyMjMtNj...................",
    "refresh_token": "eyJhbGciOiJIUzLyADmyXA...................."
  }
```

POST (Shorten) http://127.0.0.1:5000/shorten <br/>
@login_required

REQUEST
```json
{
  "url": "https://this-is-log-url-you-want-to-shorten.com/"
}
```
RESPONSE
```json
  {
    "url": "https://this-is-log-url-you-want-to-shorten.com/",
    "short_url": "https://localhost:5000/I3HVA"
  }
```


GET (Dashboard) http://127.0.0.1:5000/dashboard <br>
@login_required

RESPONSE
```json
{
  "email": "user@example.com",
  "first_name": "string",
  "id": 1,
  "last_name": "string",
  "user_links": [
    {
      "date_created": "01-01-2001",
      "id": 1,
      "short_url": "https://localhost:5000/I3HVA",
      "url": "https://this-is-log-url-you-want-to-shorten.com/",
      "user_id": 1,
      "visit": 0
    }
  ],
  "username": "string"
}
```

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Sample Screenshot -->

<!-- ## Shots -->

<!-- <br /> -->
<!-- <p>Light Mode</p> -->

<!-- [![My Blog Project Screenshot][Quiz_Api-screenshot]](https://github.com/engrmarkk/Quiz_Api/blob/main/static/images/screen-light.png) -->

<!-- <br/> -->
<!-- <p>Dark Mode</p> -->

<!-- [![My Blog Project Screenshot][Quiz_Api-screenshot2]](https://github.com/engrmarkk/Quiz_Api/blob/main/static/images/screen-dark.png) -->

[//]: # (<br/>)

[//]: # (<p align="right"><a href="#readme-top">back to top</a></p>)


<!-- Contact -->

## Contact

Adeniyi Olanrewaju - [@iamengrmark](https://twitter.com/iamengrmark) - adeniyiboladale@yahoo.com <br>

[//]: # (Gabriel Kalango - [@GabrielKalango]&#40;https://twitter.com/GabrielKalango&#41; - kallythegreat11@gmail.com)

Project Link: [Scissor Api](https://github.com/engrmarkk/Scissor_API) <br>

Live Link: [Cut Live](https://cut-ox14.onrender.com/)

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Acknowledgements -->

## Acknowledgements

This project was made possible by:

- [AltSchool Africa School of Engineering](https://altschoolafrica.com/schools/engineering)
- [Othneil Drew's README Template](https://github.com/othneildrew/Best-README-Template)
- [Ileriayo's Markdown Badges](https://github.com/Ileriayo/markdown-badges)

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Markdown Links & Images -->

[contributors-shield]: https://img.shields.io/github/contributors/engrmarkk/Academia-API.svg?style=for-the-badge
[contributors-url]: https://github.com/engrmarkk/Academia-API/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/engrmarkk/Academia-API.svg?style=for-the-badge
[forks-url]: https://github.com/engrmarkk/Academia-API/network/members
[stars-shield]: https://img.shields.io/github/stars/engrmarkk/Academia-API.svg?style=for-the-badge
[stars-url]: https://github.com/engrmarkk/Academia_API/stargazers
[issues-shield]: https://img.shields.io/github/issues/engrmarkk/Academia-API.svg?style=for-the-badge
[issues-url]: https://github.com/engrmarkk/Academia-APIissues
[license-shield]: https://img.shields.io/github/license/engrmarkk/Academia-API.svg?style=for-the-badge
[license-url]: https://github.com/engrmarkk/Academia-API/blob/main/LICENSE.txt
[twitter-shield]: https://img.shields.io/badge/-@iamengrmark-1ca0f1?style=for-the-badge&logo=twitter&logoColor=white&link=https://twitter.com/iamengrmark
[twitter-shield2]: https://img.shields.io/badge/-@GabrielKalango-1ca0f1?style=for-the-badge&logo=twitter&logoColor=white&link=https://twitter.com/GabrielKalango
[twitter-url]: https://twitter.com/iamengrmark
[postgres]: https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white
[twitter-url2]: https://twitter.com/GabrielKalango
[Quiz_Api-screenshot]: static/images/screen-light.png
[Quiz_Api-screenshot2]: static/images/screen-dark.png
[python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[jinja]: https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black
[html5]: https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white
[css3]: https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white
[sqlite]: https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white
[javascript]: https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E
[bootstrap]: https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white
