"""sub_todo Models."""

from django.db import models


class MainItem(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'MainItem(name={!r})'.format(self.name)


class SubItem(models.Model):
    main_parent = models.ForeignKey(MainItem)
    name = models.TextField()


    def __str__(self):
        return self.name

    def __repr__(self):
        return 'SubItem(name={!r})'.format(self.name)
