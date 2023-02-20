from django.db import models


class Employee(models.Model):
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    profession = models.ForeignKey('Professions', on_delete=models.PROTECT, verbose_name='Профессия')
    qualification = models.CharField(max_length=50, verbose_name='Квалификация')
    experience = models.CharField(max_length=20, verbose_name='Опыт')
    image = models.ImageField(upload_to='images/', verbose_name='Фотография')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудника'
        ordering = ['surname']


class Service(models.Model):
    service = models.CharField(max_length=50, verbose_name='Услуга')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.service

    class Meta:
        verbose_name_plural = 'Услуги'
        verbose_name = 'Услуга'
        ordering = ['service']


class Professions(models.Model):
    profession = models.CharField(max_length=50, verbose_name='Профессия')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.profession

    class Meta:
        verbose_name_plural = 'Профессии'
        verbose_name = 'Профессия'
        ordering = ['profession']


class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    telephone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(max_length=100, verbose_name='Email')
    service = models.ForeignKey('Service', on_delete=models.PROTECT, verbose_name='Услуга')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'
        ordering = ['service']


class Advantages(models.Model):
    advantage = models.TextField(verbose_name='Преимущество')

    def __str__(self):
        return self.advantage

    class Meta:
        verbose_name_plural = 'Преимущества'
        verbose_name = 'Преимущество'
        ordering = ['id']


class Contacts(models.Model):
    telephone = models.CharField(max_length=20, verbose_name='Телефон')

    def __str__(self):
        return self.telephone

    class Meta:
        verbose_name_plural = 'Контакты'
        verbose_name = 'Контакт'
        ordering = ['id']


class Information(models.Model):
    address = models.CharField(max_length=255, verbose_name='Адрес')
    working_hours = models.CharField(max_length=50, verbose_name='Время работы')

    def __str__(self):
        return self.address, self.working_hours

    class Meta:
        verbose_name_plural = 'Информация'
        verbose_name = 'Информацию'
        ordering = ['id']
