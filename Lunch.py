import argparse
from FoodCropsDataset import FoodCropsDataset
from FoodCropFactory import FoodCropFactory
from CommodityGroup import CommodityGroup
from IndicatorGroup import IndicatorGroup
from Unit import Unit

class Lunch :

    # Chargement du jeu de données 'FeedGrainsLight'
    f = FoodCropFactory()
    fcd = FoodCropsDataset(f)
    fcd.load("FeedGrainsLight.csv")

    # CommodityGroup.SORGHUM, IndicatorGroup.PRICES

    # Arguments à donner au script pour son lancement (optionnels)
    parser=argparse.ArgumentParser(description='Tri à appliquer sur les données food-crops')

    parser.add_argument("-cg","--CommodityGroup", type=str, nargs='?')
    parser.add_argument("-ig","--IndicatorGroup", type=str, nargs='?')
    parser.add_argument("-gl","--geographicalLocation", type=str, nargs='?')
    parser.add_argument("-u","--Unit", type=str, nargs='?')

    args, unknown = parser.parse_known_args() #gestion des arguments vide

    # Gestion des énumérations
    cg = None
    ig = None

    if args.CommodityGroup :
        try :
            cg = CommodityGroup[args.CommodityGroup]
        except :
            cg = "Unknown CommodityGroup"

    if args.IndicatorGroup :
        try :
            ig = IndicatorGroup[args.IndicatorGroup]
        except :
            ig = "Unknown IndicatorGroup"

    # Affichage de la liste des mesures
    liste = fcd.findMeasurements(cg,ig,args.geographicalLocation,args.Unit)
    for n in liste :
         print(n.describe())
