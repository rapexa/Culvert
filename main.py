from readCsv import readFileCsvFileDimensionsOfThreeGrain, readFileDimensionsOfSingleGrain, readFileDimensionsOfWingWalls
from helper import Draw_wing_walls, find_row, Draw_single_grain_culvert, Draw_Two_grain_culvert, Draw_Three_grain_culvert, find_rwo_wing_walls

listTitlesSingleGrain, listValuesSingleGrain = readFileDimensionsOfSingleGrain()
listTitlesThreeGrain, listValuesThreeGrain = readFileCsvFileDimensionsOfThreeGrain()
listTitlesWingWalls, listValuesWingWalls = readFileDimensionsOfWingWalls()

if __name__ == '__main__':

    ProjectName = input("[-] Enter the project name : ")
    Number = int(input("[-] Enter the number (Number) : "))
    D = float(input("[-] Enter the number (D) : "))
    H = float(input("[-] Enter the number (H) : "))
    HS = float(input("[-] Enter the number (HS) : "))
    HLittle = float(input("[-] Enter the number (h) : "))

    if Number == 3 or Number == 2 :
        
        threeGrain = find_row(D,H,HS,listValuesThreeGrain)
        print(f"[+] Done calculating {Number} grain culvert parameters!")
        WingWalls = find_rwo_wing_walls(HLittle,listValuesWingWalls)
        print(f"[+] Done calculating {Number} grain Wing Walls parameters!")

        if Number == 2:
            if Draw_Two_grain_culvert(threeGrain,HS,ProjectName) and Draw_wing_walls(WingWalls,ProjectName) :
                print(f"[+] Done drawing {Number} grain culvert!")

        if Number == 3:
            if Draw_Three_grain_culvert(threeGrain,HS,ProjectName) and Draw_wing_walls(WingWalls,ProjectName) :
                print(f"[+] Done drawing {Number} grain culvert!")

    elif Number == 1 :
        
        singleGrain = find_row(D,H,HS,listValuesSingleGrain)
        print("[+] Done calculating single grain culvert  parameters!")
        WingWalls = find_rwo_wing_walls(HLittle,listValuesWingWalls)
        print("[+] Done calculating single grain Wing Walls parameters!")
        
        if Draw_single_grain_culvert(singleGrain,HS,ProjectName) and Draw_wing_walls(WingWalls,ProjectName) :
            print("[+] Done drawing single grain culvert!")