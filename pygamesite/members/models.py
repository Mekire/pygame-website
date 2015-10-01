from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
	BANNED = -1
	MEMBER = 0
	MOD = 1
	ADMIN = 2
	RANKS = ((BANNED, 'Banned'),
			 (MEMBER, 'Member'),
			 (MOD, 'Moderator'),
			 (ADMIN, 'Admin'))

	user = models.OneToOneField(User)
	avatar = models.ImageField(upload_to='avatars/%Y/%m/%d', null=True, default=None)
	rank = models.SmallIntegerField(choices=RANKS, default=MEMBER)
	joined = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return(self.user.username)

