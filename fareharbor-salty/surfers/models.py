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

    def fav_surfers(self, fav_models=None, fav_shapers=None):
        if fav_models is None or fav_shapers is None:
            fav_models, fav_shapers = self.fav_models_shapers()
        surfer_rankings = list()
        for surfer in Surfer.objects.exclude(id=self.id):
            surfer_fav_models, surfer_fav_shapers = surfer.fav_models_shapers()
            model_hits = sum(1 for x in surfer_fav_models if x in fav_models)
            shaper_hits = sum(1 for x in surfer_fav_shapers if x in fav_shapers)
            model_h = 0
            for m in surfer_fav_models:
                if m in fav_models:
                    model_h += 1
            likeability_metric = 2*model_hits + shaper_hits
            surfer_rankings.append((surfer.id, likeability_metric))
        fav_surfers, _ = zip(*sorted(surfer_rankings, reverse=True, key=lambda x: x[1]))
        return fav_surfers

    @property
    def recommendations(self):
        NUM_RECS = 3
        rankings = dict()
        fav_models, fav_shapers = self.fav_models_shapers()
        rankings["fav_models"] = fav_models
        rankings["fav_shapers"] = fav_shapers
        rankings["fav_surfers"] = self.fav_surfers(fav_models, fav_shapers)
        shaper_rankings = [(shaper.id, shaper.surfboard_set.count()) for shaper in Shaper.objects.all()]
        rankings["pop_shapers"], _ = zip(*sorted(shaper_rankings, reverse=True, key=lambda x: x[1]))

        #print(rankings)
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
    pop_shapers = rankings["pop_shapers"]
    if first.pk == second.pk:
        return 0
    
    def negative_one_index(arr, key):
        try:
            return arr.index(key)
        except ValueError:
            return -1

    # check if first or second belong to a favorite model for surfer
    first_model = first.surfboard_model.id
    second_model = second.surfboard_model.id
    first_model_index = negative_one_index(fav_models, first_model)
    second_model_index = negative_one_index(fav_models, second_model)
    if first_model_index == -1 and second_model_index >= 0:
        return 1
    if second_model_index == -1 and first_model_index >= 0:
        return -1
    if first_model_index < second_model_index:
        return -1
    if second_model_index < first_model_index:
        return 1

    # check if first or second were made by a favorite shaper for surfer
    first_shapers = set(shaper.id for shaper in first.shapers.all())
    second_shapers = set(shaper.id for shaper in second.shapers.all())
    for fav_shaper in fav_shapers:
        first_has_fav_shaper = (fav_shaper in first_shapers)
        second_has_fav_shaper = (fav_shaper in second_shapers)
        if second_has_fav_shaper and not first_has_fav_shaper:
            return 1
        if first_has_fav_shaper and not second_has_fav_shaper:
            return -1

    # check if first or second belong to a favorite other surfer
    first_surfer = first.surfer.id
    second_surfer = second.surfer.id
    first_surfer_index = negative_one_index(fav_surfers, first_surfer)
    second_surfer_index = negative_one_index(fav_surfers, second_surfer)
    if first_surfer_index == -1 and second_surfer_index >= 0:
        return 1
    if second_surfer_index == -1 and first_surfer_index >= 0:
        return -1
    if first_surfer_index < second_surfer_index:
        return -1
    if second_surfer_index < first_surfer_index:
        return 1
    
    # check if first or second belong to a popular shaper
    first_shapers = set(shaper.id for shaper in first.shapers.all())
    second_shapers = set(shaper.id for shaper in second.shapers.all())
    for pop_shaper in pop_shapers:
        first_has_pop_shaper = (pop_shaper in first_shapers)
        second_has_pop_shaper = (pop_shaper in second_shapers)
        if second_has_pop_shaper and not first_has_pop_shaper:
            return 1
        if first_has_pop_shaper and not second_has_pop_shaper:
            return -1
    
    return 0

