from django.contrib import admin
from django.contrib.gis.geos import Point
from datetime import datetime
from leaflet.admin import LeafletGeoAdmin
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

from waterwatch.settings import BASE_DIR

from waterwatchapp.models import WaterConsumption

import traceback
import os


try:

    # Register your models here.
    class WaterConsumptionAdmin(LeafletGeoAdmin):
        pass

    admin.site.register(WaterConsumption, WaterConsumptionAdmin)

    df_excelReader = pd.read_excel( os.path.join(BASE_DIR, 'tabledata_source/waterwatch_clean2.xlsx') )

    for index, row in df_excelReader.iterrows():
        Id = index
        Suburb = row['Suburb']
        NoOfSingleResProp = row['Number of single-residential properties_number']
        AvgMonthlyKL = row['Oct 2017\nkl/month']
        AvgMonthlyKLPredicted = 0
        PredictionAccuracy = 0
        Month = row ['Month']
        Year = row['Year']
        DateTime = datetime.now()
        Longitude = row['Longitude']
        Latitude = row['Latitude']

        # this is to avoid django access the model when it is not created yet
        # https://stackoverflow.com/a/78504146/7658051

        # from django.db import connection
        # all_tables = connection.introspection.table_names()
        # table_name =  'waterwatchapp' + '_' + 'WaterConsumption'.lower()
        # if table_name in all_tables:


        WaterConsumption(Id=Id,
                        Suburb=Suburb,
                        NoOfSingleResProp=NoOfSingleResProp,
                        AvgMonthlyKL=AvgMonthlyKL,
                        AvgMonthlyKLPredicted=AvgMonthlyKLPredicted,
                        PredictionAccuracy=PredictionAccuracy,
                        Month=Month,
                        Year=Year,
                        DateTime=DateTime,
                        geom=Point(Longitude, Latitude)
                        ).save()
        
except Exception:
    print(traceback.format_exc())
    print("Cannot access table WaterConsumption.")