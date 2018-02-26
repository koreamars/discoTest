from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class AirCraft(models.Model):
    name = models.CharField(max_length=200)
    thumnail = models.CharField(max_length=300, default='')
    vote = models.IntegerField(default=0)
    model = models.CharField(max_length=200, default='')
    boarding = models.IntegerField(default=0)
    producer = models.CharField(max_length=200, default='')
    combatRadius = models.IntegerField(default=0)
    takeoffWeight = models.IntegerField(default=0)
    maxSpeed = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ammoSlot1 = models.IntegerField(default=0)
    ammoSlot2 = models.IntegerField(default=0)
    ammoSlot3 = models.IntegerField(default=0)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class AmmoDataModel(models.Model):
    name = models.CharField(max_length=200)
    thumnail = models.CharField(max_length=300)
    model = models.CharField(max_length=200)
    producer = models.CharField(max_length=200)
    homingType = models.CharField(max_length=200)
    ammoType = models.CharField(max_length=200)
    operationalRange = models.IntegerField(default=0)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class VoteDataModel(models.Model):
    type = models.CharField(max_length=200)
    modelId = models.IntegerField(default=0)
    vote = models.IntegerField(default=0)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


