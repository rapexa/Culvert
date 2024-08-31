#/bin/bash/python3

# Domain specific

DOMAIN = ''

# INPUT FILES:

DIMENSIONS_OF_THREE_GRAIN_FILE = "../assets/Dimensions-of-three-grain.csv"
DIMENSIONS_OF_SINGLE_GRAIN_FILE = "../assets/Dimensions-of-single-grain.csv"
DIMENSIONS_OF_WING_WALLS_FILE = "../assets/Dimensions-of-wing-walls.csv"
DETAILS_OF_SLAB_AND_CORNICE = "../assets/Details-of-slab-and-cornice.csv"
ONE_SPAN_CULVERT_DXF = "../assets/One-Span-Culvert.dxf"
TWO_SPAN_CULVERT_DXF = "../assets/Two-Span-Culvert.dxf"
THREE_SPAN_CULVERT_DXF = "../assets/Three-Span-Culvert.dxf"
WING_WALLS_DXF = "../assets/Wing-Walls.dxf"

# OUTPUT FILES:

OUTPUT_ONE_SPAN_CULVERT_DXF = "../outputs/One-Span-Culvert"
OUTPUT_TWO_SPAN_CULVERT_DXF = "../outputs/Two-Span-Culvert"
OUTPUT_THREE_SPAN_CULVERT_DXF = "../outputs/Three-Span-Culvert"
OUTPUT_WING_WALLS_DXF = "../outputs/Wing-Walls"
OUTPUT_SLAB_AND_CORNICE = "../outputs/Details-of-slab-and-cornice"

# OUTPUT FILES WEB:

BASE_URL_OUTPUT = "http://127.0.0.1:8000/outputs?fileName="
WEB_OUTPUT_ONE_SPAN_CULVERT_DXF = BASE_URL_OUTPUT + "One-Span-Culvert"
WEB_OUTPUT_TWO_SPAN_CULVERT_DXF = BASE_URL_OUTPUT + "Two-Span-Culvert"
WEB_UTPUT_THREE_SPAN_CULVERT_DXF = BASE_URL_OUTPUT + "Three-Span-Culvert"
WEB_OUTPUT_WING_WALLS_DXF = BASE_URL_OUTPUT + "Wing-Walls"
WEB_OUTPUT_SLAB_AND_CORNICE = BASE_URL_OUTPUT + "Details-of-slab-and-cornice"