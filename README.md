# DRF_implementation


# Project Title

The project was inteded to implement DRF to create api endpoints

## Description

The DRF app provides api endpoints for car app using which mobile apps or third party apps can be integrated.
The app offers two endpoints to access list of brands and respective models. HTTP GET POST requests were successfuly tested 
on Postman.


## Installation


1. Clone the repository: git clone https://github.com/your-username/your-repo.git
2. Install dependencies: pip install -r requirements.txt
3. Run database migrations: python manage.py migrate
4. Start the development server: python manage.py runserver


## Usage

```
Example:

    "brands": "http://127.0.0.1:8000/api/brands/",
    "cars": "http://127.0.0.1:8000/api/cars/"
[
    {
        "name": "Kia",
        "launch": "March 2019",
        "style": "Hatchback"
    },
    {
        "name": "Suzuki",
        "launch": "April 2009",
        "style": "Sedan"
    }

]



[
    {
        "name": "Seltos",
        "price": 12.3,
        "fuel": "Petrol",
        "seat": 5
    },
    {
        "name": "Dzire",
        "price": 5.0,
        "fuel": "Petrol",
        "seat": 4
    }
]




