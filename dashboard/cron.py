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
		pass



