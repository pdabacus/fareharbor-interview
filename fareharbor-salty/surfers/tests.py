from django.test import TestCase
from surfers.models import Surfer, Shaper, Surfboard
from django.core.exceptions import ObjectDoesNotExist

from datetime import date


class SurferTestCase(TestCase):
    def setUp(self):
        Surfer.objects.create(name="alpha", skill=1, bio="newby")

    @staticmethod
    def save_reset_surfer(surfer: Surfer):
        surfer_id = surfer.pk
        surfer.save()
        return Surfer.objects.get(pk=surfer_id)

    def test_change_name_skill(self):
        alpha = Surfer.objects.get(name="alpha")
        self.assertEqual(alpha.name, "alpha")
        alpha.name = "alpha2"
        alpha = self.save_reset_surfer(alpha)
        self.assertEqual(alpha.name, "alpha2")
        alpha.name = 2
        alpha = self.save_reset_surfer(alpha)
        self.assertEqual(alpha.name, "2")

    def test_add_remove_surfers(self):
        alpha = Surfer.objects.get(name="alpha")
        self.assertEquals(Surfer.objects.count(), 1)
        self.assertEquals(Surfboard.objects.count(), 0)
        Surfer.objects.create(name="beta", skill=2, bio="asdf")
        self.assertEquals(Surfer.objects.count(), 2)

        Surfer.objects.filter(pk=alpha.pk).delete()
        self.assertEquals(Surfer.objects.count(), 1)
        with self.assertRaises(ObjectDoesNotExist) as context:
            alpha = Surfer.objects.get(name="alpha")
        self.assertTrue("does not exist" in str(context.exception))


class ShaperTestCase(TestCase):
    def setUp(self):
        Shaper.objects.create(name="alice", shaping_since="2001-01-01")

    @staticmethod
    def save_reset_shaper(shaper: Shaper):
        shaper_id = shaper.pk
        shaper.save()
        return Shaper.objects.get(pk=shaper_id)

    def test_change_name_year(self):
        alice = Shaper.objects.get(name="alice")
        self.assertEqual(alice.name, "alice")
        alice.name = "alice2"
        alice = self.save_reset_shaper(alice)
        self.assertEqual(alice.name, "alice2")
        alice.name = 1
        alice = self.save_reset_shaper(alice)
        self.assertEqual(alice.name, "1")
        alice.shaping_since = "2002-01-01"
        alice = self.save_reset_shaper(alice)
        self.assertEqual(alice.shaping_since, date(2002, 1, 1))

    def test_add_remove_shapers(self):
        alice = Shaper.objects.get(name="alice")
        self.assertEquals(Shaper.objects.count(), 1)
        self.assertEquals(Surfboard.objects.count(), 0)
        Shaper.objects.create(name="bob", shaping_since="2002-01-01")
        self.assertEquals(Shaper.objects.count(), 2)

        Shaper.objects.filter(pk=alice.pk).delete()
        self.assertEquals(Shaper.objects.count(), 1)
        with self.assertRaises(ObjectDoesNotExist) as context:
            alice = Shaper.objects.get(name="alice")
        self.assertTrue("does not exist" in str(context.exception))


class SurfboardTestCase(TestCase):
    def setUp(self):
        alpha = Surfer.objects.create(name="alpha", skill=1, bio="newby")
        alice = Shaper.objects.create(name="alice", shaping_since="2001-01-01")
        uno = Surfboard.objects.create(
            model_name="uno",
            length=100,
            width=20,
            surfer=alpha
        )
        uno.shapers.add(alice)
        
    @staticmethod
    def save_reset_surfboard(surfboard: Surfboard):
        surfboard_id = surfboard.pk
        surfboard.save()
        return Surfboard.objects.get(pk=surfboard_id)

    def test_change_name_owner(self):
        alpha = Surfer.objects.get(name="alpha")
        alice = Shaper.objects.get(name="alice")
        uno = Surfboard.objects.get(model_name="uno")
        self.assertEqual(uno.surfer, alpha)
        self.assertEqual(uno.shapers.count(), 1)
        self.assertEqual(uno.shapers.first(), alice)
        uno.model_name = "uno2"
        uno = self.save_reset_surfboard(uno)
        self.assertEqual(uno.model_name, "uno2")

        beta = Surfer.objects.create(name="beta", skill=2)
        bob = Shaper.objects.create(name="bob", shaping_since="2002-01-01")
        uno.surfer = beta
        uno.shapers.remove(alice)
        uno.shapers.add(bob)
        uno = self.save_reset_surfboard(uno)
        self.assertEqual(uno.surfer, beta)
        self.assertEqual(uno.shapers.count(), 1)
        self.assertEqual(uno.shapers.first(), bob)

        uno.shapers.set([alice])
        uno = self.save_reset_surfboard(uno)
        self.assertEqual(uno.surfer, beta)
        self.assertEqual(uno.shapers.count(), 1)
        self.assertEqual(uno.shapers.first(), alice)

    def test_add_remove_surfboards(self):
        self.assertEquals(Surfer.objects.count(), 1)
        self.assertEquals(Surfboard.objects.count(), 1)
        Surfer.objects.create(name="beta", skill=2, bio="asdf")
        self.assertEquals(Surfer.objects.count(), 2)
