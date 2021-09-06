# Generated by Django 3.2 on 2021-09-05 23:52

from django.db import migrations


def link_lobby_instances(apps, schema_editor):
    Lobby = apps.get_model("simpl.Lobby")
    for lobby in Lobby.objects.all():
        player = (
            lobby.player_set.filter(character__instance__isnull=False)
            .select_related("character")
            .first()
        )
        if player:
            lobby.instance_id = player.character.instance_id
            lobby.save()


def unlink_lobby_instances(apps, schema_editor):
    Lobby = apps.get_model("simpl.Lobby")
    Lobby.objects.update(instance=None)


class Migration(migrations.Migration):

    dependencies = [
        ("simpl", "0015_lobby_instance"),
    ]

    operations = [
        migrations.RunPython(link_lobby_instances, reverse_code=unlink_lobby_instances)
    ]
