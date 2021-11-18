# API-for-crops-dataframe

Creation of an API to manipulate and browse data from foodcrops dataset

## ECHANDOURI Abdessamad, CREUSOT Emeline, BENJELLOUN Yasmine


## Environment and development

We used Python version 3.9 for this project and the following libraries

argparse, tkinter, argparse

## How to use the API:
### Load data :
  ```python
  # Create factory to instanciate objects
  fctr = FoodCropFactory()
  
  # create the foodCropDataset
  ds = FoodCropsDataset(fctr)
  # Load data from csv fiile
  ds.load("FeedGrains.csv")
  ```

### Usage :

To get the value of one or several measures we use findMeasurement method which the following arguments : Geographical localization, unit, commodity group and indicator group

Here is an example :

```python
from CommodityGroup import CommodityGroup
from IndicatorGroup import IndicatorGroup

# Find quantities coresponding to  COARSE_GRAINS .
fcd.findMeasurements(CommodityGroup.COARSE_GRAINS , IndicatorGroup.QUANTITIES_FED )
```
## Run script

Pour afficher toutes les données food-crops : 
```
python Run.py
```

Filter data : 
```
python Run.py --comg <str> --indg <str> --geol <str> --uni <str>
```

- --geol
geo localization
- --comg
Enum CommodityGroup
- --indg  
Enum IndicatorGroup
- --uni
Unity

#### Example
```
python Run.py --indg QUANTITIES_FED

python Run.py --comg COARSE_GRAINS -geol 'United States'
```

#### What were our difficulties and problems encountered

It was difficult to understand the subject at first and especially where to start. Moreover the object oriented approach in Python was very confusing since we were used to Java, otherwise at the level of the code the difficulties concerned mainly the foodcrop and describable classes (with the interface).
It also seems that we have a conflict when compiling the script since it doesn't work all the time because of an unidentified problem (probably a slipped syntax error that we can't identify).
We only used Git late by simple forgetfulness but the work was distributed by assigning different classes to each member of the trinomial
