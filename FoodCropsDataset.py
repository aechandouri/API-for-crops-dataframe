import pandas as pd
from CommodityGroup import CommodityGroup
from IndicatorGroup import IndicatorGroup
from FoodCropFactory import FoodCropFactory
from Unit import Unit

class FoodCropsDataset:
    def __init__(self, factory: FoodCropFactory):
        self.factory = factory


        self.__locationMeasurementIndex = {}
        self.__commodityMeasurementIndex = {}
        self.__indicatorGroupMeasurementIndex = {}
        self.__unitMeasurementIndex = {}

        self.__measurements = []


        units = {
            1: self.factory.createCount(1, "Million bushels", "Million bushels"),
            2: self.factory.createSurface(2, "Million acres"),
            3: self.factory.createVolume(3, "Bushels"),
            4: self.factory.createUnitRatio(4, self.factory.createPrice(100, "Dollars"), self.factory.createVolume(101, "bushel"), "Dollars per bushels"),
            5: self.factory.createUnitRatio(5, self.factory.createPrice(100, "Dollars"), self.factory.createWeight(102, 1, "cwt"), "Dollars per cwt"),
            6: self.factory.createUnitRatio(6, self.factory.createWeight(3, 1, "Bushels"), self.factory.createSurface(103, "acre"), "Bushels per acre"),
            7: self.factory.createWeight(7, 1, "1,000 metric tons"),
            8: self.factory.createWeight(8, 1, "Million metric tons"),
            9: self.factory.createWeight(9, 1, "1,000 tons"),
            10: self.factory.createSurface(10, "1,000 acres"),
            11: self.factory.createUnitRatio(11, self.factory.createWeight(104, 1, "Tons"), self.factory.createSurface(103, "acre"), "Tons per acre"),
            12: self.factory.createUnitRatio(11, self.factory.createPrice(100, "Dollars"), self.factory.createWeight(105, 1, "ton"), "Dollars per ton"),
            13: self.factory.createRatio(13, "Ratio"),
            14: self.factory.createUnitRatio(14, self.factory.createPrice(106, "Cents"), self.factory.createWeight(107, 1, "pound"), "Cents per pound"),
            15: self.factory.createRatio(15, "Index"),
            16: self.factory.createVolume(16, "Carloads originated"),
            17: self.factory.createVolume(17, "1,000 liters"),
            18: self.factory.createVolume(18, "Gallons"),
            31: self.factory.createUnitRatio(31, self.factory.createPrice(100, "Dollars"), self.factory.createWeight(108, 1, "short ton"), "Dollars per short ton"),
            41: self.factory.createWeight(41, 1, "Ton"),
            44: self.factory.createSurface(44, "1,000 hectare"),
            45: self.factory.createUnitRatio(45, self.factory.createWeight(3, 1, "Metric tons"), self.factory.createSurface(1010, "hectare"), "Metric tons per hectare"),
            46: self.factory.createCount(46, "Million animal units", "Million animal units"),
        }
    def load(self, datasetPath: str):
        FCdataset = pd.read_csv(datasetPath)
        FCdataset = FCdataset.dropna()
        FCdataset.reset_index(drop=True)
        for i, j in FCdataset.iterrows():
            # on récupère le grpe de l'indicateur
            indicatorGroup = IndicatorGroup(j["SC_Group_ID"])
            # On cree / récupère  l'unité de l'ind
            id = j["SC_Unit_ID"]
            unit = units[id]

            # On cree / récupère l'ind
            ind = self.factory.createIndicator(j["SC_Attribute_ID"], j["SC_Frequency_ID"], j["SC_Frequency_Desc"], j["SC_GeographyIndented_Desc"], indicatorGroup, unit, j["SC_Attribute_Desc"])

            # on récupère le grpe des cultures vivrières
            commodityGroup = CommodityGroup(j["SC_GroupCommod_ID"])
            
            com = self.factory.createCommodity(commodityGroup, j["SC_Commodity_ID"], j["SC_Commodity_Desc"])

            # On créée ensuite la mesure
            measure = self.factory.createMeasurement(i, j["Year_ID"], j["Amount"], j["Timeperiod_ID"], j["Timeperiod_Desc"], commodity, indicator)
            self.__measurements.append(measurement)
            
            if j["SC_GeographyIndented_Desc"] in self.__locationMeasurementIndex:
                self.__locationMeasurementIndex[j["SC_GeographyIndented_Desc"]].append(measurement)
            else:
                self.__locationMeasurementIndex[j["SC_GeographyIndented_Desc"]] = [measurement]

            if unit in self.__unitMeasurementIndex:
                self.__unitMeasurementIndex[unit].append(measurement)
            else:
                self.__unitMeasurementIndex[unit] = [measurement]
                
            if indicatorGroup in self.__indicatorGroupMeasurementIndex:
                self.__indicatorGroupMeasurementIndex[indicatorGroup].append(measurement)
            else:
                self.__indicatorGroupMeasurementIndex[indicatorGroup] = [measurement]
                
            if commodityGroup in self.__commodityMeasurementIndex:
                self.__commodityMeasurementIndex[commodityGroup].append(measurement)
            else:
                self.__commodityMeasurementIndex[commodityGroup] = [measurement]

            

    def findMeasurements(self, geographicalLocation: str = None, commodityGroup: CommodityGroup = None, indicatorGroup: IndicatorGroup = None, unit: Unit = None) -> list:
        list_measure = self.__measurements[:]
        

        if geographicalLocation is not None:
            liste = []
            temp = self.__locationMeasurementIndex.get(geographicalLocation, [])
            for val in list_measure:
                if val in temp:
                    liste.append(val)
            list_measure = liste
            
        if commodityGroup is not None:
            liste = []
            temp = self.__commodityMeasurementIndex.get(commodityGroup, [])
            for measure in list_measure:
                if val in temp:
                    list.append(val)
            list_measure = liste

        if indicatorGroup is not None:
            liste = []
            temp = self.__indicatorGroupMeasurementIndex.get(indicatorGroup, [])
            for val in list_measure:
                if val in temp:
                    list.append(val)
            list_measure = liste
        if unit is not None:
            liste = []
            temp = self.__unitMeasurementIndex.get(unit, [])
            for val in measurementList:
                if val in temp:
                    list.append(val)
            list_measure = listew

        return list_measure
