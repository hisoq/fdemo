# Generated by Django 4.1.6 on 2023-03-14 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("telefon", "0003_phones_color"),
    ]

    operations = [
        migrations.CreateModel(
            name="Electronic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=12, verbose_name="Электроника"
                    ),
                ),
            ],
            options={
                "verbose_name": "Электроника",
                "verbose_name_plural": "Электроника",
                "db_table": "electronic",
            },
        ),
        migrations.AlterField(
            model_name="phones",
            name="price",
            field=models.IntegerField(blank=True, null=True, verbose_name="Цена в $"),
        ),
        migrations.AlterField(
            model_name="phones",
            name="title",
            field=models.CharField(max_length=50, verbose_name="Модель"),
        ),
        migrations.AddField(
            model_name="phones",
            name="electronic",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="telefon.electronic",
                verbose_name="Электроника",
            ),
        ),
    ]
