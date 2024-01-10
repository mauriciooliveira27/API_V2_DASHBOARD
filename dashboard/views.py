from rest_framework import generics
from .models import DashBoard
from .serializers import DashBoardSerializer, GroupSerializer, UserSerializer
from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta


class DashBoardsAPIView(generics.ListCreateAPIView):

    queryset            =       DashBoard.objects.all()
    serializer_class    =       DashBoardSerializer



class DashBoardAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = DashBoard.objects.all()
    serializer_class = DashBoardSerializer




class TimeZoneHourAPIView(APIView):
    def get(self, request, hour):
        try:
            # Certifique-se de que 'hour' é um número inteiro
            hour = int(hour)
        except ValueError:
            return Response({

                                'error': 'The value of "hour" must be an integer.'

                            }, status=status.HTTP_400_BAD_REQUEST)

        # Obtendo dados da última hora
        last_hour               =       timezone.now() - timedelta(hours=hour)
        data_last_hour          =       DashBoard.objects.filter(data__gte=last_hour)
        serializer_last_hour    =       DashBoardSerializer(data_last_hour, many=True)

        # Você pode adicionar lógica semelhante para a última semana e o último mês
        return Response({

                            'ultima_hora': serializer_last_hour.data,
                            # Adicione outros dados aqui, se necessário
                        }, status=status.HTTP_202_ACCEPTED)
    



class TimeZoneDayAPIView(APIView):
    def get(self, request, day):
        try:
            day = int(day)
        except ValueError:
            return Response({

                                    'error':'The value of "hour" must be an integer.'
                                    
                            }, status=status.HTTP_400_BAD_REQUEST)
        
        last_day            =       timezone.now() - timedelta(days=day)
        data_last_day       =       DashBoard.objects.filter(data__gte = last_day)
        serializer_last_day =       DashBoardSerializer(data_last_day, many = True)

        return Response({

                            'ultimos_dias' : serializer_last_day.data,

                        }, status=status.HTTP_202_ACCEPTED)




class TimeZoneWeekAPIView(APIView):
    def get(self,request, week):
        try:

            weeks  = int(week)
            
        except ValueError:
            return Response({

                                'error':'The value of "hour" must be an integer.'
                                
                            }, status=status.HTTP_400_BAD_REQUEST)

        last_weeks              =           timezone.now() - timedelta(weeks=week)
        data_last_weeks         =           DashBoard.objects.filter(data__gte = last_weeks)
        serializer_last_weeks   =           DashBoardSerializer(data_last_weeks , many = True)

        return Response({

                            'ultima_semana':serializer_last_weeks.data,

                        },  status=status.HTTP_202_ACCEPTED)
    






#KW / Ton
    

    #pena = KW 
    #pena = peso_acum+