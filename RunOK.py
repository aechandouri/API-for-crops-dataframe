
from FoodCropFactory import FoodCropFactory
import argparse
from CommodityGroup import CommodityGroup
from FoodCropsDataset import FoodCropsDataset
from IndicatorGroup import IndicatorGroup
from Unit import Unit

class Run :

    # loading dataset
    ff = FoodCropFactory()
    fd = FoodCropsDataset(ff)
    fd.load("FeedGrains.csv")

    # arg for script launching
    p_parser=argparse.ArgumentParser(description = 'Sorting for data')
    
    
    p_parser.add_argument("--indg","___IndicatorGroup", type=str, nargs= '?')
    p_parser.add_argument("--geol","___geographicalLocation", type=str, nargs= '?')
    p_parser.add_argument("--comg","___CommodityGroup", type=str, nargs= '?')
    p_parser.add_argument("--uni","___Unit", type=str, nargs= '?')
    
    p_arg, p_unknown = p_parser.parse_known_args() #empty arg
    # Enum management
    indg = None
    comg = None
    
    
    if p_arg.IndicatorGroup :
        
        try :
            indg = IndicatorGroup[p_arg.IndicatorGroup]
        except :
            indg = "IndicatorGroup not known"

    if p_arg.CommodityGroup :
        try :
            comg = CommodityGroup[p_arg.CommodityGroup]
        except :
            comg = " CommodityGroup not known"

    
    # display measure list
    list_measure = fd.findMeasurements(p_arg.geographicalLocation,comg,indg,p_arg.Unit)
    for i in list_measure :
         print(i.describe())
