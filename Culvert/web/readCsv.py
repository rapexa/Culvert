from .config import *

def readFileCsvFileDimensionsOfThreeGrain():
    
    list_titles = []
    list_values = []

    with open(DIMENSIONS_OF_THREE_GRAIN_FILE, "r") as csv_file_Dimensions_of_three_grain:
        lines = csv_file_Dimensions_of_three_grain.readlines()
        lines_count = 0
        for line in lines:
            if lines_count == 0:
                list_titles = line.strip().split(',')
                lines_count += 1
            else:
                list_values.append(line.strip().split(","))

    return list_titles, list_values

def readFileDimensionsOfSingleGrain():
    
    list_titles = []
    list_values = []

    with open(DIMENSIONS_OF_SINGLE_GRAIN_FILE, "r") as csv_file_Dimensions_of_single_grain:
        lines = csv_file_Dimensions_of_single_grain.readlines()
        lines_count = 0
        for line in lines:
            if lines_count == 0:
                list_titles = line.strip().split(',')
                lines_count += 1
            else:
                list_values.append(line.strip().split(","))

    return list_titles, list_values

def readFileDimensionsOfWingWalls():
    
    list_titles = []
    list_values = []

    with open(DIMENSIONS_OF_WING_WALLS_FILE, "r") as csv_file_Dimensions_of_wing_walls:
        lines = csv_file_Dimensions_of_wing_walls.readlines()
        lines_count = 0
        for line in lines:
            if lines_count == 0:
                list_titles = line.strip().split(',')
                lines_count += 1
            else:
                list_values.append(line.strip().split(","))

    return list_titles, list_values