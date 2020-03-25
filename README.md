# 3city-transport

A simple web application that given a starting point in 3city shows
a heat map of 3city indicating travel time using public transportation


## Goal

Create a POC tool with possible social impact and industrialize perspective.


## Possible extensions
- frequency of communication
- different means of transport
- time-of-the-day-dependent map
- ...


# Run

```
export TRICITY=~/3city-transport/
export TRICITY_DATA=~/3city-transport/data/
export TRICITY_STATE=~/3city-transport/src/state/
```

# Components

```
├── data                    <--- auxiliary data; expected metadata etc.
│   ├── ztm_Gdansk.csv
│   └── ztm_gdansk.json
├── notebooks               <--- Jupyter notebooks for development of the module & ad hoc analysis
│   ├── ...
├── src                     <--- library
│   ├── state               <--- state of data
│   │   └── stops_3city_checked.csv
│   ├── README.md
│   └── distance_matrix_api.py
├── Makefile
├── README.md
└── requirements.txt        <--- package information
```

# Install

Written in Python 3.7

Create virtual environment:
```
python3.7 -m venv ~/virtualenvs/3city
```

Activate virtual env:
```
source ~/virtualenvs/3city/bin/activate
```

Change folder to `3city-transport` and install package:
```
make dev_install
```

# Notebooks

Notebooks are used for ad-hoc data analysis and prototyping of functionalities.

The naming convention is based on
[Data Science Cookiecutter](https://drivendata.github.io/cookiecutter-data-science/)
and is a version number - author's name - description, like `0.1-pawel.tiutiurski-distance_matrix_api.ipynb`.


### Loose remarks:

1.  **authentication method**
* account on google cloud platform
* it is necessary to link a billing account
* Distance Matrix API - Access travel distance and time for a matrix of origins and destinations with the Distance Matrix API. The information returned is based on the recommended route between start and end points and consists of rows containing duration and distance values for each pair.

2.  **requests quotas**
* 200$ in monthly free quota
* 1000 requests cost 5$ 

3.  **input and output formats**
* output format: json


output format: json
