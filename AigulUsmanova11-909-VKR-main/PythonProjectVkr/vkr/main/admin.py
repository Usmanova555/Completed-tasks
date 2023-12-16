from django.contrib import admin
from .models import CsvFile, FieldName, ColumnsCount


admin.site.register(CsvFile)
admin.site.register(FieldName)
admin.site.register(ColumnsCount)