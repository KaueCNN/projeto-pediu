# Generated by Django 2.0.5 on 2018-07-02 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimentos', '0002_auto_20180702_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimentos',
            name='tipo_pgto',
            field=models.CharField(choices=[('AV', 'A Vista'), ('CH', 'Cheque'), ('PR', 'Parcelas')], max_length=100),
        ),
    ]
