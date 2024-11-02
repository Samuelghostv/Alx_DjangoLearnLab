# LibraryProject

## Steps of creating Virtual Environment 
Note as the first thing you should before creating your django project

create directory called

## mkdir introduction_to_Django

Navigate to the introduction_to_django

## cd path/to/your/introduction_to_django

Create the Virtual Environment: is the environment is going to contain your or hold store your django project

## python -m venv venv
Note the virtual name is venv but which you can also changed it to your like
eg
## python -m venv mykeke
note: that mykeke is the virtual name here

Activate the Virtual Environment in other for it to run or to be in up state

## venv\Scripts\activate  
## mykeke\Script\activate
Note: this command for windows

Installation of Django in the virtual environment

## pip install django
Note: this command will install the django inside your virtual environment

Create your First django project 

## django-admin startproject LibraryProject
Note: this command will create your django project name as " LibraryProject"

Navigate to LibraryProject directory which is your django project name

## cd LibraryProject

Note: at your windows you can open it straight using 
## code .

Run django server 

## python manage.py runserver
Note: in oder to see your django application is runnig successful, have to run the server
which it will give you localhost address in this form http://127.0.0.1:8000/

## Overview
This project, **LibraryProject**, is a Django-based application designed as part of an introductory exercise for setting up a Django development environment. The setup and basic structure follow Django’s conventions to provide a foundation for developing Django applications.

## Main Objectives
- Set up a Django development environment.
- Create a Django project.
- Run the Django development server.
- Familiarize with Django project structure.

## Prerequisites
- **Python**: Ensure Python is installed on your system. Check by running `python --version`.
- **pip**: Make sure `pip` is installed to manage Python packages.

## Project Setup

### 1. Install Django
Install Django via `pip`:
```bash
pip install django
