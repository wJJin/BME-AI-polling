# Generated by Django 4.1.7 on 2023-03-16 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_pollingimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollingimage',
            name='name_vote',
            field=models.CharField(choices=[('34', 'A baby who seems to want something'), ('33', 'person with a light smile in korea'), ('32', 'dancing bichon'), ('31', 'forky with headphone'), ('30', 'facial palsy patient smile'), ('29', 'angry'), ('28', 'a person who lies at home with his eyes closed'), ('27', 'depressed person at home'), ('26', 'person smiling with happiest emotion'), ('25', 'smile expression'), ('24', 'Prompt'), ('23', 'prompt'), ('22', 'photo of a tired student'), ('21', 'a face with a headache'), ('20', "a person with a \x08angry look on one's face"), ('19', 'prompt'), ('18', 'a sad dog'), ('17', "after work, person's emotion"), ('16', "Draw a picture of Korea similar to Van Gogh's work"), ('15', 'prompt'), ('14', 'happydog'), ('13', 'A blonde boy is eating nachos and guacamole with his family'), ('12', 'a person who cries out of sorrow'), ('11', 'a man flying in the clouds'), ('10', 'The girl feels happy'), ('9', '4th industry of medical devices connected with human'), ('8', "happy person's face"), ('7', 'crying baby'), ('6', 'sleepy cat'), ('5', 'welsi cogi smilyface,chair,office'), ('4', 'happy face'), ('3', "a student who can't concentrate at all while doing something else during a lecture"), ('2', 'a angry person'), ('1', 'CEO who about to retire')], max_length=256, null=True, verbose_name='작품명'),
        ),
    ]
