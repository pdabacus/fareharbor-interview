from django.db import models


class Surfer(models.Model):
    name = models.CharField(max_length=200)
    skill = models.PositiveIntegerField()

    bio = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return "%s (%d)" % (self.name, self.pk)


class Shaper(models.Model):
    name = models.CharField(max_length=200)
    shaping_since = models.DateField()
    label = models.CharField(max_length=200)
    bio = models.TextField(blank=True)

    website_url = models.URLField(blank=True)

    def __unicode__(self):
        return u'%s (since %s)' % (self.name, self.shaping_since.year)

    def __str__(self):
        return "%s (%d)" % (self.name, self.pk)


class SurfboardModel(models.Model):
    model_name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return "%s (%d)" % (self.model_name, self.pk)


class Surfboard(models.Model):
    # DeprecationWarning("removing field 'model_name' after db column 'surfboard_model' created")
    model_name = models.CharField(max_length=200)

    surfboard_model = models.ForeignKey(SurfboardModel, on_delete=models.CASCADE)

    length = models.FloatField()
    width = models.FloatField()

    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    created_at = models.DateField(auto_now_add=True)

    # DeprecationWarning("removing field 'shaper' after db column 'shapers' created")
    #shaper = models.ForeignKey(Shaper)

    shapers = models.ManyToManyField(Shaper)

    surfer = models.ForeignKey(Surfer)

    @property
    def display_length(self):
        return '''%s' - %s"''' % (int(self.length / 12), self.length % 12)

    @property
    def display_dimensions(self):
        return u'%s x %s"' % (
            self.display_length,
            self.width,
        )

    def __unicode__(self):
        return u'%s by %s (%s)' % (
            self.model_name,
            self.shapers.first().name,
            self.display_dimensions,
        )

    def __str__(self):
        return "%s (%d)" % (self.model_name, self.pk)
