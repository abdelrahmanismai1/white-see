from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator


# Create your models here.
class Customer(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    first_name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2, "Title must be greater than 2 characters")], 
    )
    last_name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "Title must be greater than 2 characters")],  
    )
    
    phone = models.CharField( max_length=11,
        validators=[
            RegexValidator(
            regex=r"^01\d\d\d\d\d\d\d\d\d$",
            message='Invalid Phone number',
            code='invalid'
            ),
        ],
    )

    profession_in_passport = models.CharField(max_length=200,null=True, blank=True,)
    #personal_information 
    #address
    #education_degree 
    #computer_skills
    #languages
    #experience
    
    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
    
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'