from django.db import models


class CsvFile(models.Model):
    num = models.CharField(null=True)
    data = models.DateField()
    entity = models.CharField()
    entity2 = models.CharField(null=True)
    entity3 = models.CharField(null=True)
    entity4 = models.CharField(null=True)
    entity5 = models.CharField(null=True)
    entity6 = models.CharField(null=True)
    entity7 = models.CharField(null=True)

    def __str__(self):
        return f'{self.num} {self.data} {self.entity} {self.entity2} {self.entity3} {self.entity4} {self.entity5} {self.entity6} {self.entity7}'

    class Meta:
        verbose_name = 'Csv файл'
        verbose_name_plural = 'Csv файлы'


class FieldName(models.Model):
    name = models.CharField(null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Прогнозируемое поле'
        verbose_name_plural = 'Прогнозируемые поля'


class ColumnsCount(models.Model):
    count = models.CharField()

    def __str__(self):
        return f'{self.count}'

    class Meta:
        verbose_name = 'Количество столбцов'
        verbose_name_plural = 'Количество столбцов'