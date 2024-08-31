from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password
from django.views.decorators.http import require_POST
from json import JSONEncoder,loads
from web.models import User, Token
from .readCsv import readFileCsvFileDimensionsOfThreeGrain, readFileDimensionsOfSingleGrain, readFileDimensionsOfWingWalls
from .helper import Draw_wing_walls, find_row, Draw_single_grain_culvert, Draw_Two_grain_culvert, Draw_Three_grain_culvert, find_rwo_wing_walls

listTitlesSingleGrain, listValuesSingleGrain = readFileDimensionsOfSingleGrain()
listTitlesThreeGrain, listValuesThreeGrain = readFileCsvFileDimensionsOfThreeGrain()
listTitlesWingWalls, listValuesWingWalls = readFileDimensionsOfWingWalls()

@csrf_exempt
def register(request):
    "register a new user"

    if request.method == 'POST':

        encoded = request.body
        json = loads(encoded.decode('utf-8'))
        
        username = json['user']
        password = json['pass']

        try:

            User.objects.create_user(username=username,
                                    email=username,
                                    password=password)
            
            this_user = get_object_or_404(User, username=username)            

            refresh_token = RefreshToken.for_user(this_user)

            # token = sha256(f"{this_user}-Culvert".encode("utf-8")).hexdigest()
            
            Token.objects.create(user=this_user,token=str(refresh_token.access_token))
                
            return JsonResponse({
                'data': "user created successfully",
                'code' : 200,
            }, encoder=JSONEncoder)

        except Exception as e:

            return JsonResponse({
                'data': 'error creating user',
                'code' : 404,
            }, encoder=JSONEncoder)

    else:

        return JsonResponse({
            'data': 'request not valid!',
            'code': 401,
        }, encoder=JSONEncoder)

@csrf_exempt
def login(request):
    "login a user"

    if request.method == 'POST':

        encoded = request.body
        json = loads(encoded.decode('utf-8'))

        username = json['user']
        password = json['pass']

        this_user = get_object_or_404(User, username=username)

        if (check_password(password, this_user.password)):  # authentication

            this_token = get_object_or_404(Token, user=this_user)
            token = this_token.token
            
            context = {}
            context['code'] = 200
            context['token'] = token
            return JsonResponse(context, encoder=JSONEncoder)

        else:
            
            context = {}
            context['code'] = 404
            context['data'] = 'error password incorrect'
            return JsonResponse(context, encoder=JSONEncoder)
        
    context = {}
    context['code'] = 401
    context['data'] = "request not valid!"
    return JsonResponse(context, encoder=JSONEncoder)

@csrf_exempt
@require_POST
def whoami(request):
    "whoami from request"

    if request.method == 'POST':

        encoded = request.body
        json = loads(encoded.decode('utf-8'))

        this_token = json['token']
        
        try:
            this_user = get_object_or_404(User, token__token=this_token)

            return JsonResponse({
                'data': this_user.username,
                'code' : 200,
            }, encoder=JSONEncoder)

        except Exception as e:

            return JsonResponse({
                'data': "token invalid!",
                'code' : 404,
            }, encoder=JSONEncoder)

    else:

        return JsonResponse({
            'data': 'request not valid!',
            'code': 401,
        }, encoder=JSONEncoder)

@csrf_exempt
def Calculate(request):
    "calculate datas for user a user"
    #TODO: make this function for users to allow using culvert core

    if request.method == 'POST':

        encoded = request.body
        json = loads(encoded.decode('utf-8'))

        this_token = json['token']
        ProjectName = json['ProjectName']
        Number = int(json['Number'])
        D = float(json['D'])
        H = float(json['H'])
        HS = float(json['HS'])
        HLittle = float(json['h'])
        
        #TODO: handle if didnt found find_row and find_rwo_wing_walls (the return none)
        try:
            this_user = get_object_or_404(User, token__token=this_token)

            if Number == 3 or Number == 2 :
                
                # calculating 3-2 grain culvert parameters
                threeGrain = find_row(D,H,HS,listValuesThreeGrain)
                
                # calculating 3-2 grain Wing Walls parameters
                WingWalls = find_rwo_wing_walls(HLittle,listValuesWingWalls)

                if Number == 2:

                    # drawing 2 grain culvert and Draw wing walls
                    if Draw_Two_grain_culvert(threeGrain,HS,ProjectName) and Draw_wing_walls(WingWalls,ProjectName) :

                        return JsonResponse({
                            'data': this_user.username,
                            'code' : 200,
                        }, encoder=JSONEncoder)

                if Number == 3:

                    # drawing 3 grain culvert and Draw wing walls
                    if Draw_Three_grain_culvert(threeGrain,HS,ProjectName) and Draw_wing_walls(WingWalls,ProjectName) :
                        
                        return JsonResponse({
                            'data': this_user.username,
                            'code' : 200,
                        }, encoder=JSONEncoder)

            elif Number == 1 :
                
                # calculating 1 grain Wing Walls parameters
                singleGrain = find_row(D,H,HS,listValuesSingleGrain)

                # calculating 1 grain Wing Walls parameters
                WingWalls = find_rwo_wing_walls(HLittle,listValuesWingWalls)

                # drawing 3 grain culvert and Draw wing walls
                if Draw_single_grain_culvert(singleGrain,HS,ProjectName) and Draw_wing_walls(WingWalls,ProjectName) :
                    
                    return JsonResponse({
                        'data': this_user.username,
                        'code' : 200,
                    }, encoder=JSONEncoder)

        except Exception as e:

            return JsonResponse({
                'data': "token invalid!",
                'code' : 404,
            }, encoder=JSONEncoder)

    else:

        return JsonResponse({
            'data': 'request not valid!',
            'code': 401,
        }, encoder=JSONEncoder, status_code=401)

def index(request):
    return HttpResponse("Ok!")