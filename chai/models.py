from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User


class chaiVarity(models.Model):
    CHAI_TYPE=[
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('PL','PLAIN'),
        ('KL','KIWI'),
    
    ]
  

    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chais/')
    type = models.CharField(max_length=2, choices=CHAI_TYPE,default='PL')
    date_added=models.DateTimeField(default=timezone.now)
    description=models.TextField(default='')
    price=models.DecimalField(default=0 , 
        max_digits=1000,decimal_places=2,
        validators=[MinValueValidator(149),MaxValueValidator(1000)],
    )
     
    def __str__(self):
        return self.name
       
    
# Create your models here.
class ChaiReview(models.Model):
    chai=models.ForeignKey(chaiVarity,on_delete=models.CASCADE,related_name='review')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
class Store(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    chai_varities=models.ManyToManyField(chaiVarity,related_name='stores')  

    def __str__(self):
        return self.name
    
class ChaiCertificate(models.Model):
    chai=models.OneToOneField(chaiVarity,on_delete=models.CASCADE,related_name='certificate')
    certificate_number=models.CharField(max_length=100)
    issued_date=models.DateTimeField(default=timezone.now) 
    valid_untill=models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.name.chai}' 
