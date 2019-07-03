from datetime import date
from datetime import datetime
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
#from django.http import HttpResponse

from . models import UserDetail
from . serializers import UserSerializer

class UserView(generics.RetrieveUpdateAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'user_name'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        content = data['user_name']
        print(data['dateOfBirth'][5:])
        print(date.today().strftime("%m-%d"))
        if data['dateOfBirth'][5:] == date.today().strftime("%m-%d"):
            html = ("Hello, %s! Happy birthday!" % content)
            return Response({'message': html}, status=status.HTTP_204_NO_CONTENT)
        else:
        #     bday = data['dateOfBirth']
        #     print(type(bday))
        #     # 1989 - 05 - 02
        #     bd_ar = bday.split('-')
        #     print(bd_ar[0])
        #
        #     to_ar = date.today().strftime("%Y-%m-%d")
        #
        #     d0 = date(2017, int(bd_ar[2]), int(bd_ar[1]))
        #     d1 = date(2017, int(to_ar[2]), int(to_ar[1]))
        #     delta = d1 - d0
        #     print(delta.days)
        #
        #     web = ("Hello, {} Your birthday is in {} days(s)".format(content, delta))
            dd = int(data['dateOfBirth'][8:])
            mm = int(data['dateOfBirth'][5:7])
            yy = int(data['dateOfBirth'][2:4])
            birthday = datetime(2000+yy, mm, dd)
            def calculate_dates(original_date, now):
                delta1 = datetime(now.year, original_date.month, original_date.day)
                delta2 = datetime(now.year + 1, original_date.month, original_date.day)
                days = (max(delta1, delta2) - now).days
                if days > 365:
                    days=days-365
                    return days
                else:
                    days=days
                return days
            bd = birthday
            now = datetime.now()
            c = calculate_dates(bd, now)
            html = ("Hello, %s! Your birthday is in %s days!" % (content, c))
        return Response({'message':html}, status=status.HTTP_200_OK)
