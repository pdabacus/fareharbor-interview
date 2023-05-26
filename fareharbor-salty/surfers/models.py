from django.db import models


class Surfer(models.Model):
    name = models.CharField(max_length=200)
    skill = models.PositiveIntegerField()

    bio = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return "%s (%d)" % (self.name, self.pk)

    def fav_models_shapers(self):
        models = dict()
        shapers = dict()
        for board in self.surfboard_set.all():
            model = board.surfboard_model
            if model.id in models:
                models[model.id] += 1
            else:
                models[model.id] = 1
            for shaper in board.shapers.all():
                if shaper.id in shapers:
                    shapers[shaper.id] += 1
                else:
                    shapers[shaper.id] = 1
        fav_models, _ = zip(*sorted(models.items(), key=lambda x: x[1]))
        fav_shapers, _ = zip(*sorted(shapers.items(), key=lambda x: x[1]))
        return fav_models, fav_shapers

    @property
    def recommendations(self):
        NUM_RECS = 3
        rankings = dict()
        fav_models, fav_shapers = self.fav_models_shapers()
        rankings["fav_models"] = fav_models
        rankings["fav_shapers"] = fav_shapers
        rankings["fav_surfers"] = list()
        recs = list()
        my_boards = set(self.surfboard_set.all())
        boards = list(board for board in Surfboard.objects.all() if board not in my_boards)
        for i in range(NUM_RECS):
            best_board_id = 0
            for board_id in range(1, len(boards)):
                comp = board_compare(rankings, boards[best_board_id], boards[board_id])
                if comp > 0:
                    best_board_id = board_id
            board = boards.pop(best_board_id)
            recs.append(board)
        return recs


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


def board_compare(rankings, first:Surfboard, second:Surfboard):
    fav_models = rankings["fav_models"]
    fav_shapers = rankings["fav_shapers"]
    fav_surfers = rankings["fav_surfers"]
    if first.pk == second.pk:
        return 0

    if first.pk > second.pk:
        return -1
    else:
        return 1

