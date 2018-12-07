class LeavingTime:
	
	def __init__(self, hour = 5, minute = 0, second = 0):
		if(hour <= 9):
			hour = hour + 12
		self.hour = hour
		self.minute = minute
		self.second = second
		
		
	def getHoursLeft(self, now):
		time = self.timeRemaining(now)
		return int(time/3600)
		
	
	def getMinutesLeft(self, now):
		time = self.timeRemaining(now)
		time = time - int(time/3600)*3600
		return int(time/60)
		
		
	def getSecondsLeft(self, now):
		time = self.timeRemaining(now)
		time = time - int(time/3600)*3600
		time = time - int(time/60)*60
		return int(time)
		
		
	def timeRemaining(self, now):
		return self.hour*3600 + self.minute*60 + self.second - now.hour*3600 - now.minute*60 - now.second
		
	def getPercentComplete(self, now):
		totalTime = self.hour*3600 + self.minute*60 + self.second - 32400
		amountComplete = now.hour*3600 + now.minute*60 + now.second - 32400
		return int((amountComplete/totalTime)*100)