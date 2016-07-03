from django.db import models

class Character(models.Model):
    id               = models.AutoField(primary_key=True)
    name             = models.CharField(max_length=200)
    level            = models.IntegerField(default=1)
    adjustment_level = models.IntegerField(default=1)
    mythic_tier      = models.IntegerField(default=0)
    description      = models.TextField()
    dm_notes         = models.TextField()

    # foreign
    player_name = models.ForeignKey(
        'players.name',
        on_delete=models.CASCADE,
    )
