from django.contrib.auth.models import AbstractUser
from django.db import models


# каждый новый класс - это таблица


class Food(models.Model):
    title = models.TextField(verbose_name="Название блюда")
    sostav = models.TextField(verbose_name="Состав")
    ves = models.IntegerField(verbose_name="Вес")
    price = models.IntegerField(verbose_name="Цена")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Названия блюд и напитков'


class Work(models.Model):
    title = models.CharField(max_length=200, verbose_name="Ваше ФИО")
    name_of_work = models.CharField(max_length=200, verbose_name="Выбранное поле деятельности")
    text = models.TextField(verbose_name="Ваше резюме")
    age = models.IntegerField(verbose_name="Сколько Вам лет")
    created = models.DateField(auto_now_add=True, verbose_name="Время отправки формы на сайт")

    class Meta:
        verbose_name_plural = 'Форма с резюме на работу'
        ordering = ['created', 'title']


class Booking(models.Model):
    title = models.CharField(max_length=200, verbose_name="ФИО")
    time_from = models.CharField(max_length=200, verbose_name="Время от начала бронирования")  #
    time_to = models.CharField(max_length=200, verbose_name="время до конца бронирования")  #
    phone_number = models.IntegerField(verbose_name="Номер телефона")
    number_of_table = models.IntegerField(verbose_name="Номер столика")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Время на момент бронирования")

    class Meta:
        verbose_name_plural = 'Забронировать столик'
        ordering = ['created', 'title']


class Menu(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    name = models.CharField(max_length=100, verbose_name="Название ресторана (одно и то же)")

    class Meta:
        verbose_name_plural = 'Главная страница - тайтлы в меню'


class Actions(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    text = models.TextField(verbose_name="текст")

    class Meta:
        verbose_name_plural = 'Акции и предложения'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории блюд'


# волшебная функция
def __str__(self):
    return self.title


class Profile(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    lastname = models.CharField(max_length=50, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество")
    email = models.EmailField(verbose_name="Email")
    foods = models.ManyToManyField(Food)

    class Meta:
        verbose_name_plural = 'Профили пользователей'


class Forum(models.Model):
    title_fio = models.CharField(max_length=100, verbose_name="ФИО")
    message = models.TextField(verbose_name="Текст отзыва")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания отзыва")
    image = models.FileField(null=True,  upload_to='uploads/% Y/% m/% d/', verbose_name='Добавьте аватар')

    class Meta:
        verbose_name_plural = 'Отзывы посетителей'
        ordering = ['created', 'title_fio']


class New(models.Model):
    title = models.CharField(max_length=100, verbose_name="ФИО")
    phone_number = models.IntegerField(verbose_name="Номер телефона")
    name = models.CharField(max_length=100, verbose_name="Название блюда")

    class Meta:
        verbose_name_plural = 'Сделать заказ'


class About(models.Model):
    phone_number = models.IntegerField(verbose_name="Номер телефона")
    text = models.TextField(verbose_name="текст")

    class Meta:
        verbose_name_plural = 'Информация о нас'
