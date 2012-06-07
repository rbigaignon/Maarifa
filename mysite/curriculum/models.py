from django.db import models


class Curriculum(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class CurriculumUnit(models.Model):
    curriculum = models.ForeignKey(Curriculum)
    level = models.IntegerField()
    body = models.TextField()

    def __unicode__(self):
        return unicode(self.curriculum) + ' (level %d)' % self.level

    class Meta:
        unique_together = ('curriculum', 'level')