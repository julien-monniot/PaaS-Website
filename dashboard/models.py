from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator

class Historique(models.Model):
	ACTION_CHOICES=(
			('WUPN','WupNews'),
			('UJ','UserJoined'),
			('TS','TravelSubscribe'),
			('TU','TravelUnsubscribe'),
			('TCT','TravelCreated'),
			('TC','TravelCommented'),
			('TCC','TravelCanceled'),

			# add new actions
		)
	OBJECT_TYPES=(
			('N','None'),
			('TR','Travel'),
		)
	action_type = models.CharField(max_length=4, choices=ACTION_CHOICES, default='WUPN')
	actor = models.ForeignKey('wu.WuProfil')
	date = models.DateTimeField(default=timezone.now)
	notified = models.BooleanField(default=False)
	object_type = models.CharField(max_length=2, choices=OBJECT_TYPES, default='N')
	object_travel = models.ForeignKey('travel.Travel', null=True)

	# add new objects (group, comment etc.. referencing the object as foreign key)

	def newTravelFact(actor, action_type, object_travel):
		historique = Historique(
		    actor=actor, 
		    action_type=action_type,
		    object_type='TR',
		    object_travel=object_travel
		    )
		historique.save()

class Notification:
	receiver = models.ForeignKey('wu.WuProfil')
	message = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	seen = models.BooleanField(default=False)

class Flow:
	receiver = models.ForeignKey('wu.WuProfil')
	fact = models.ForeignKey('Historique')


