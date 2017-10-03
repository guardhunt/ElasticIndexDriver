from crontab import CronTab

class RegesterCron:

	def __init__(self):
		self.path_to_cron = ""
		self.interval = 0

	def start_cron(user_to_set, path, interval):
		new_cron = CronTab(user = user_to_set)
		job = new_cron.new(command='python' + path)
		job.minute.every(interval)
		test_cron.write()

