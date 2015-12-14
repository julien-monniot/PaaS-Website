from django_cron import CronJobBase, Schedule
from django.utils import timezone
from .models import Historique, Notification, Flow
import subprocess


import time
from threading import Thread


class ComputeFactsAndNotifications(CronJobBase):
	RUN_EVERY_MINS = 1 # every 2 hours

	schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
	code = 'dashboard.ComputeFactsAndNotifications'    # a unique code


	def do(self):
		t = Thread(target=compute)
		t.start()


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


		fact.notified = True
		fact.save()

