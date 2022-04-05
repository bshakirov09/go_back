from django.db import models


class SingeltonModel(models.Model):

    class Meta:
        abstract=True

    def save(self,*args,**kwargs):
        self.pk = 1
        super(SingeltonModel, self).save(*args,**kwargs)

    def delete(self,*args,**kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.object.get_or_create(pk=1)
        return obj