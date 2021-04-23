from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User
from django.conf import settings

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, password=None, is_active=True): #pragma: no cover
        if not email:
            raise ValueError("Users must have a username")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            username = username
        )
        user_obj.set_password(password) # change user password
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj

class ClientInformation(models.Model):
    class States(models.TextChoices):
        ALABAMA='AL'
        ALASKA='AK'
        ARIZONA='AZ'
        ARKANSAS='AR'
        CALIFORNIA='CA'
        COLORADO='CO'
        CONNECTICUT='CT'
        DELAWARE='DE'
        FLORIDA='FL'
        GEORGIA='GA'
        HAWAII='HI'
        IDAHO='ID'
        ILLINOIS='IL'
        INDIANA='IN'
        IOWA='IA'
        KANSAS='KS'
        KENTUCKY='KY'
        LOUISIANA='LA'
        MAINE='ME'
        MARYLAND='MD'
        MASSACHUSETTS='MA'
        MICHIGAN='MI'
        MINNESOTA='MN'
        MISSISSIPPI='MS'
        MISSOURI='MO'
        MONTANA='MT'
        NEBRASKA='NE'
        NEVADA='NV'
        NEW_HAMPSHIRE='NH'
        NEW_JERSEY='NJ'
        NEW_MEXICO='NM'
        NEW_YORK='NY'
        NORTH_CAROLINA='NC'
        NORTH_DAKOTA='ND'
        OHIO='OH'
        OKLAHOMA='OK'
        OREGON='OR'
        PENNSYLVANIA='PA'
        RHODE_ISLAND='RI'
        SOUTH_CAROLINA='SC'
        SOUTH_DAKOTA='SD'
        TENNESSEE='TN'
        TEXAS='TX'
        UTAH='UT'
        VERMONT='VT'
        VIRGINIA='VA'
        WASHINGTON='WA'
        WEST_VIRGINIA='WV'
        WISCONSIN='WI'
        WYOMING='WY'

    auth_user_id = models.OneToOneField(User, to_field='id', on_delete = models.CASCADE)
    fullname = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, null = True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=States.choices)
    zipcode = models.CharField(max_length=9)

    def str(self): #pragma: no cover
        return self.fullname

class FuelQuote(models.Model):
    client_id = models.ForeignKey(ClientInformation, on_delete=models.CASCADE)
    gallons = models.IntegerField()
    deliver_address = models.CharField(max_length=100)
    delivery_date = models.DateField()
    suggested_price_per_gallons = models.DecimalField(max_digits=3, decimal_places=2)
    total_amount_due = models.DecimalField(max_digits=9, decimal_places=2)

    def str(self): #pragma: no cover
        return str(self.id)