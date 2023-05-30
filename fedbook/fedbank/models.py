from django.db import models


class Person(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_OTHER = 2
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female'), (GENDER_OTHER, 'Other')]
    gender = models.IntegerField(choices=GENDER_CHOICES)
    district = models.ForeignKey('Country', on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    FIXED = 0
    SAVING = 1
    CURRENT = 2
    RECURRING = 3
    account = models.IntegerField(choices=[
                                      (FIXED, 'Fixed Deposit'),
                                      (RECURRING, 'Recurring Deposit'),
                                      (SAVING, 'Saving Account'),
                                      (CURRENT, 'Current Account')
                                  ])
    material = models

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=15)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name