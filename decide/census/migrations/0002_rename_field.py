# Generated migration to rename voting_id to voting_id_2

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='census',
            old_name='voting_id',
            new_name='voting_id_2',
        ),
        migrations.AlterUniqueTogether(
            name='census',
            unique_together={('voting_id_2', 'voter_id')},
        ),
    ]
