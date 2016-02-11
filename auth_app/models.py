from django.db import models
from django.contrib.auth.models import User


PROFILE_CATEGORY = (
        (1, 'A'),
        (2, 'B'),
        (3, 'C'),
        (4, 'D'),
    )



class Person(models.Model):
    user = models.OneToOneField(User,related_name="persons")
    profile_category=models.IntegerField(choices = PROFILE_CATEGORY, null=True, blank=True) #category A=6% , B=9%, C=12%, D=12.5%
    #image=models.ImageField(upload_to='images/', null=True, blank=True)
    salary=models.FloatField(null=True, blank=True) #credit rating deciding factor
    profession=models.CharField(max_length=200, null=True, blank=True)
    phone=models.CharField(max_length=15)
    city=models.CharField(max_length=100, null=True, blank=True)
    state=models.CharField(max_length=100,null=True, blank=True)
    credits_available=models.IntegerField(default=0)
    credits_spent=models.IntegerField(default=0)
    total_posts=models.IntegerField(default=0)
    total_successful_posts=models.IntegerField(default=0)
    money_invested=models.ManyToManyField('self',through="MmInvestment", symmetrical=False, null=True, blank=True)
    def __unicode__(self):
        return self.user.username
    def credit_rating(self):
        if self.salary> 100000:
            try:
                return 5+ (self.total_successful_posts/self.total_posts)*5
            except:
                return 0
        else:
            try:
                return (self.salary/100000)*5+(self.total_successful_posts/self.total_posts)*5
            except:
                return 0

class MmInvestment(models.Model):
    investor=models.ForeignKey(Person,related_name="investor")
    seeker=models.ForeignKey(Person, related_name="seeker")
    amount=models.FloatField(default=0.0)
    credit_rating=models.IntegerField(default=0)
    

class Post(models.Model):
      amount_requested=models.CharField(max_length=10)
      amount_received=models.CharField(max_length=10)
      #slug=models.SlugField(unique=True)
    
      #def save(self,*args,**kwargs):
       #   self.slug=slugify(self.amount_requested)
	#  super(Post,self).save(*args,**kwargs)
      def __unicode__(self):
	  return unicode(self.amount_requested)
      def __unicode__(self):
	  return unicode(self.amount_received)
      
