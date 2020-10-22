Squirrel Tracker in Central Park
====================================

<div align="center">
<img src="https://images.unsplash.com/photo-1470130623320-9583a8d06241?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80"><br>
</div>

## What is it?

**Squirrel** is an app that allows you to track NYC squirrel sightings in Central Park of New York.
Users of this app can view squirrels' data(either in list or map), and can also add, update the data themselves.
## Main Features

Here are the main features that **Squirrel** does:

### 1. Management Commands

- A command to import data from .csv file. The file path should be specified at the command line after the name of the management command. 
```
$ python manage.py import_squirrel_data /path/to/file.csv
```
- A command to export data into .csv file. The file path should be specified at the command line after the name of the management command. 
```
$ python manage.py export_squirrel_data /path/to/file.csv
```

### 2. Views

On the index page, the users can choose to view the following options: map of sightings, list of sightings, general stats of sightings, or they can also add a new sighting.

Specific functions of the views are described below:

* Map

A view that shows a map that displays location of the first 100 squirrels' sightings

Located at: /map

* Sighting List

A view that lists all squirrel sightings with links to view each sighting

Located at: /sightings

* Update

A view to update a particular sighting

Located at : /sightings/unique-squirrel-id

* Details

A view to list the specific details of a unique squirrel ID

Located at: /sightings/unique-squirrel-id/IDdetails

* Add

A view to create a new sighting. (If format of data doesn't comply, users will be asked to update the specific data.)

Located at: /sightings/add

* Stats

A view with general stats about the sightings (total number of data, total number of squirrels above ground, total number of adult squirrels, total number of squirrels with cinnamon fur color, total number of squirrels eating).

Located at: /sightings/stats

## Group Information

* Project Group yuxinxinyu, Section 1
* Group Members: Susan Shang, Xinyu Mei

## List of UNIs

UNIs: [ys3386, xm2256]

## Dependencies

- [Django](https://www.djangoproject.com/)

## Source
- [CSV data source](https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv)
