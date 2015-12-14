from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

class Historique(models.Model):
	ACTION_CHOICES=(
			('WUPN','WupNews'),
			('UJ','UserJoined'),
			('TS','TravelSubscribe'),
			('TU','TravelUnsubscribe'),
			('TC','TravelCreated'),
			('TCMT','TravelCommented'),
			('TCC','TravelCanceled'),

			# add new actions
		)
	OBJECT_TYPES=(
			('N','None'),
			('TR','Travel'),
		)
	action_type = models.CharField(max_length=4, choices=ACTION_CHOICES, default='WUPN')
	actor = models.ForeignKey('wu.WuProfil', null=True)
	date = models.DateTimeField(default=timezone.now)
	notified = models.BooleanField(default=False)
	object_type = models.CharField(max_length=2, choices=OBJECT_TYPES, default='N')
	object_travel = models.ForeignKey('travel.Travel', null=True)
	message = models.CharField(max_length=200, null=True)

	# add new objects (group, comment etc.. referencing the object as foreign key)

	def newTravelFact(actor, action_type, object_travel):
		historique = Historique(
		    actor=actor, 
		    action_type=action_type,
		    object_type='TR',
		    object_travel=object_travel
		    )
		historique.save()

	def news(message):
		historique = Historique(
		    message=message
		    )
		historique.save()


class Notification(models.Model):
	receiver = models.ForeignKey('wu.WuProfil')
	message = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	seen = models.BooleanField(default=False)
	fact = models.ForeignKey('Historique')

class Flow(models.Model):
	#receiver = null => concerns all members
	receiver = models.ForeignKey('wu.WuProfil', null=True)
	fact = models.ForeignKey('Historique')


