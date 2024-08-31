#!bin/bash/python3

from dxf2img import DXF2IMG
from config import *

def generate_output_file(filenamePath,ProjectName):

    return str(filenamePath) + '-' + ProjectName + ".dxf"

def find_rwo_wing_walls(h,rows):
     
    for row in rows:
         
         if h == float(row[0]):
              return row
         
         else:
              continue

def find_row(D,H,HS,rows):

    for row in rows:

        string_hs = row[3]

        first_value_hs = float(string_hs.split(" ")[0])
        second_value_hs = float(string_hs.split(" ")[-1])
        h_value = float(row[2])
        d_value = float(row[1])

        first_char_hs = string_hs.split(" ")[1]
        second_char_hs = string_hs.split(" ")[-2]

        if first_char_hs == "<=" and second_char_hs == "<=":
            if first_value_hs <= HS <= second_value_hs and H == h_value and D == d_value:
                return row

        if first_char_hs == "<" and second_char_hs == "<=":
            if first_value_hs < HS <= second_value_hs and H == h_value and D == d_value:
                return row

        if first_char_hs == "<=" and second_char_hs == "<":
            if first_value_hs <= HS < second_value_hs and H == h_value and D == d_value:
                return row
            

        if first_char_hs == "<" and second_char_hs == "<":
            if first_value_hs < HS < second_value_hs and H == h_value and D == d_value:
                return row

def Draw_wing_walls(WingWalls,ProjectName):
        
        h = WingWalls[0]
        x = WingWalls[1]
        b = WingWalls[2]
        f = WingWalls[3]
        m = WingWalls[4]
        x2 = WingWalls[5]
        c3 = WingWalls[6]

        key = "MMMMM"
        Values = {"h" : h, "x" : x, "b" : b, "f" : f, "m" : m, "X2" : x2, "c3" : c3}

        with open(WING_WALLS_DXF, "r") as f:
            
            content = f.read()

        for index, value in Values.items():
            
            content = content.replace(key+index, value)

        OUTPUT_WING_WALLS_DXF_FILE_NAME = generate_output_file(OUTPUT_WING_WALLS_DXF, ProjectName)

        with open(OUTPUT_WING_WALLS_DXF_FILE_NAME, "w") as f:
            f.write(content)

        Convertor =  DXF2IMG()
        Convertor.convert_dxf2img([OUTPUT_WING_WALLS_DXF_FILE_NAME],img_format='.png')

        return True

def Draw_single_grain_culvert(singleGrain,HS,ProjectName):

        D = singleGrain[1]
        H = singleGrain[2]
        HS = str(HS)
        a1 = singleGrain[4]
        a2 = singleGrain[5]
        b1 = singleGrain[6]
        b2 = singleGrain[7]
        c1 = singleGrain[8]
        c2 = singleGrain[9]
        f = singleGrain[10]
        m = singleGrain[11]
        t = singleGrain[12]
        j = singleGrain[14]
        
        key = "MMMMM"
        Values = {"D" : D, "H" : H, "SH" : HS, "a1" : a1, "a2" : a2, "b1" : b1, "b2" : b2, "c1" : c1, "c2" : c2, "f" : f, "m" : m, "t" : t, "j": j}

        with open(ONE_SPAN_CULVERT_DXF, "r") as f:
            
            content = f.read()

        for index, value in Values.items():
            
            content = content.replace(key+index, value)

        OUTPUT_ONE_SPAN_CULVERT_DXF_FILE_NAME = generate_output_file(OUTPUT_ONE_SPAN_CULVERT_DXF, ProjectName)

        with open(OUTPUT_ONE_SPAN_CULVERT_DXF_FILE_NAME, "w") as f:
            f.write(content)

        Convertor =  DXF2IMG()
        Convertor.convert_dxf2img([OUTPUT_ONE_SPAN_CULVERT_DXF_FILE_NAME],img_format='.png')

        return True

def Draw_Two_grain_culvert(threeGrain,HS,ProjectName):

        D = threeGrain[1]
        H = threeGrain[2]
        HS = str(HS)
        a1 = threeGrain[4]
        a2 = threeGrain[5]
        b1 = threeGrain[6]
        b2 = threeGrain[7]
        c1 = threeGrain[8]
        c2 = threeGrain[9]
        f = threeGrain[10]
        m = threeGrain[11]
        p1 = threeGrain[12]
        p2 = threeGrain[13]
        e = threeGrain[14]
        n = threeGrain[15]
        k = threeGrain[16]
        t = threeGrain[17]
        j = threeGrain[19]
        
        key = "MMMMM"
        Values = {"D" : D, "H" : H, "SH" : HS, "K" : k, "n" : n, "e" : e, "P1" : p1, "P2" : p2, "a1" : a1, "a2" : a2, "b1" : b1, "b2" : b2, "c1" : c1, "c2" : c2, "f" : f, "m" : m, "t" : t, "j": j}

        with open(TWO_SPAN_CULVERT_DXF, "r") as f:
            
            content = f.read()

        for index, value in Values.items():
            
            content = content.replace(key+index, value)

        OUTPUT_TWO_SPAN_CULVERT_DXF_FILE_NAME = generate_output_file(OUTPUT_TWO_SPAN_CULVERT_DXF, ProjectName)

        with open(OUTPUT_TWO_SPAN_CULVERT_DXF_FILE_NAME, "w") as f:
            f.write(content)

        Convertor =  DXF2IMG()
        Convertor.convert_dxf2img([OUTPUT_TWO_SPAN_CULVERT_DXF_FILE_NAME],img_format='.png')

        return True

def Draw_Three_grain_culvert(threeGrain,HS,ProjectName):
        
        D = threeGrain[1]
        H = threeGrain[2]
        HS = str(HS)
        a1 = threeGrain[4]
        a2 = threeGrain[5]
        b1 = threeGrain[6]
        b2 = threeGrain[7]
        c1 = threeGrain[8]
        c2 = threeGrain[9]
        f = threeGrain[10]
        m = threeGrain[11]
        p1 = threeGrain[12]
        p2 = threeGrain[13]
        e = threeGrain[14]
        n = threeGrain[15]
        k = threeGrain[16]
        t = threeGrain[17]
        j = threeGrain[19]
        
        key = "MMMMM"
        Values = {"D" : D, "H" : H, "SH" : HS, "K" : k, "n" : n, "e" : e, "P1" : p1, "P2" : p2, "a1" : a1, "a2" : a2, "b1" : b1, "b2" : b2, "c1" : c1, "c2" : c2, "f" : f, "m" : m, "t" : t, "j": j}

        with open(THREE_SPAN_CULVERT_DXF, "r") as f:
            
            content = f.read()

        for index, value in Values.items():
            
            content = content.replace(key+index, value)

        OUTPUT_THREE_SPAN_CULVERT_DXF_FILE_NAME = generate_output_file(OUTPUT_THREE_SPAN_CULVERT_DXF, ProjectName)

        with open(OUTPUT_THREE_SPAN_CULVERT_DXF_FILE_NAME, "w") as f:
            f.write(content)

        Convertor =  DXF2IMG()
        Convertor.convert_dxf2img([OUTPUT_THREE_SPAN_CULVERT_DXF_FILE_NAME],img_format='.png')

        return True
