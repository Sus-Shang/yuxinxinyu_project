Squirrel Tracker in Central Park
====================================

<div align="center">
<img src="https://images.unsplash.com/photo-1470130623320-9583a8d06241?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80"><br>
</div>

## What is it?

**Squirrel** is an app that allows you to track NYC squirrel sightings in Central Park of New York.

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
* Map
- A view that shows a map that displays location of squirrel sightings: /map
* Sighting List
- A view that lists all squirrel sightings with links to view each sighting: /sightings
* Update
- A view to update a particular sighting: /sightings/<unique-squirrel-id>
* Add
- A view to create a new sighting: /sightings/add
* Stats
- A view with general stats about the sightings: /sightings/stats

## Group Information

* Project Group yuxinxinyu, Section 1
* Group Members: Susan Shang, Xinyu Mei

## List of UNIS

UNIs: [ys3386,xm2256]

## Dependencies

- [Django](https://www.djangoproject.com/)

## Source
-[CSV data source](https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv)
