from django.db import models

from mptt.models import MPTTModel, TreeForeignKey
from members.models import Member

class Forum(models.Model):
	name = models.CharField(max_length=256, blank=False)
	description = models.TextField(blank=False)

	def __unicode__(self):
		return(self.name)

class Thread(models.Model):
	forum = models.ForeignKey(Forum)
	headline = models.CharField(max_length=256, blank=False)
	text = models.TextField(blank=False)
	published = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return('Forum: {0}'.format(self.forum))

class Comment(models.Model):
	poster = models.ForeignKey(Member)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
	thread = models.ForeignKey(Thread)
	published = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return('Comment by {0} posted {1}'.format(self.poster, self.published))

