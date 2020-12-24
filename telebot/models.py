from django.db import models


class Message(models.Model):
    id_message = models.IntegerField(null=True)

    def __str__(self):
        return "%s - %s" % (self.id, self.id_message)


class Activities(models.Model):
    status = models.CharField(max_length=16, null=True, blank=True, unique=True )

    def __str__(self):
        return "%s" % self.status


class Admins(models.Model):
    name = models.CharField(max_length=22, null=True, blank=True, default="Admin")
    number_admin = models.CharField(max_length=22, null=True, blank=True)
    activity = models.ForeignKey(Activities, to_field='status',
                                 default='Активен',
                                 on_delete=models.CASCADE,
                                 null=True, blank=True)

    def __str__(self):
        return "%s - %s - %s" % (self.name, self.number_admin, self.activity)


class ClientAdmin(models.Model):
    clientId = models.CharField(max_length=22, null=True, blank=True)
    adminId = models.CharField(max_length=22, null=True, blank=True)

