from rest_framework import serializers

from .models import Date_details


class DateSerializers(serializers.ModelSerializer):

    Age = serializers.SerializerMethodField('AgeCalculator')
    class Meta:
       model = Date_details
       fields = ('Day','Month','Year','Age',)
    

    def AgeCalculator(self,obj):
        import datetime
        
        x= datetime.datetime.now().year
    
        if obj.Day== 29 and obj.Month== 2 :
            age=((x-obj.Year)//4)
        else:
            age=(x-obj.Year)
        return age
