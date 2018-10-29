from django.db import models


class Poll(models.Model):
	text = models.CharField(max_length=255)
	pub_date = models.DateField()

	def __str__(self):
		return self.text

class Choice(models.Model):
	question = models.ForeignKey(Poll, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=255)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return f"{self.question.text[:25]} - {self.choice_text[:25]}"


	
class Newspaper(models.Model):
	article = models.TextField(max_length=650)
	reporter = models.CharField(max_length=100)
	name = models.CharField(max_length=200)

	def __str__(self):
		return f'{self.name} - {self.article[:20]} '

class Partisanlean(models.Model):
	publication_name = models.ForeignKey(Newspaper, on_delete=models.CASCADE)
	partisan = models.BooleanField() 

	def __str__(self):
		return f'{self.publication_name}'