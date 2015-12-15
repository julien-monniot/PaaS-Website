# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator


#This fonctions is normally called by a daemon
# but for demonstration it will be run for each creation of facts
def compute():
	facts = Historique.objects.filter(notified=False)
	for fact in facts:
		if fact.action_type == 'TC':
			newFlow = Flow(fact=fact)
			newFlow.save()
		if fact.action_type == 'TS':
			newFlow = Flow(fact=fact)
			newFlow.save()
			newNotification = Notification(fact=fact, receiver=fact.object_travel.author, message="Un membre a rejoin votre voyage")
			newNotification.save()
		if fact.action_type == 'TU':
			newFlow = Flow(fact=fact)
			newFlow.save()
			newNotification = Notification(fact=fact, receiver=fact.object_travel.author, message="Un membre a quitté votre voyage")
			newNotification.save()

		if fact.action_type == 'UJ':
			newFlow = Flow(fact=fact)
			newFlow.save()
			newNotification = Notification(fact=fact, message="Un nouveau membre a rejoin la famille. Accueillons le comme il faut!")
			newNotification.save()


		fact.notified = True
		fact.save()




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
			('U','User'),  # object is actor
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
		compute()

	def newUserFact(actor, action_type, object_user):
		historique = Historique(
		    actor=actor,
		    action_type=action_type,
		    object_type='U'
		    )
		historique.save()
		compute()

	def news(message):
		historique = Historique(
		    message=message
		    )
		historique.save()

		compute()


class Notification(models.Model):
	receiver = models.ForeignKey('wu.WuProfil', null=True)
	message = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	seen = models.BooleanField(default=False)
	fact = models.ForeignKey('Historique')

class Flow(models.Model):
	#receiver = null => concerns all members
	receiver = models.ForeignKey('wu.WuProfil', null=True)
	fact = models.ForeignKey('Historique')




