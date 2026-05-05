# Generated manually for the restored wine fermentation Django app.

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="WineProject",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255, verbose_name="პროექტის სახელი")),
                ("grape_type", models.CharField(blank=True, max_length=120, verbose_name="ყურძნის ჯიში")),
                ("harvest_date", models.DateField(blank=True, null=True, verbose_name="მოსავლის თარიღი")),
                ("wine_style", models.CharField(choices=[("ევროპული", "ევროპული"), ("ქვევრი", "ქვევრი"), ("ქარვისფერი", "ქარვისფერი"), ("წითელი", "წითელი"), ("თეთრი", "თეთრი"), ("ვარდისფერი", "ვარდისფერი")], default="ქვევრი", max_length=50, verbose_name="ღვინის სტილი")),
                ("initial_brix", models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name="საწყისი Brix")),
                ("initial_sugar", models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name="საწყისი შაქარი")),
                ("initial_ph", models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name="საწყისი pH")),
                ("initial_acidity", models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name="საწყისი მჟავიანობა")),
                ("vessel", models.CharField(blank=True, max_length=120, verbose_name="ჭურჭელი")),
                ("volume_liters", models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name="მოცულობა ლიტრებში")),
                ("notes", models.TextField(blank=True, verbose_name="შენიშვნა")),
                ("is_active", models.BooleanField(default=True, verbose_name="აქტიური")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="შექმნის თარიღი")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="განახლების თარიღი")),
                ("owner", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="wine_projects", to=settings.AUTH_USER_MODEL)),
            ],
            options={"verbose_name": "ღვინის პროექტი", "verbose_name_plural": "ღვინის პროექტები", "ordering": ["-created_at"]},
        ),
        migrations.CreateModel(
            name="FermentationEntry",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("measured_at", models.DateTimeField(verbose_name="თარიღი და დრო")),
                ("temperature", models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name="ტემპერატურა °C")),
                ("brix", models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name="Brix")),
                ("sugar", models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name="შაქარი")),
                ("ph", models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name="pH")),
                ("acidity", models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name="მჟავიანობა გ/ლ")),
                ("action", models.CharField(blank=True, max_length=255, verbose_name="ქმედება")),
                ("comment", models.TextField(blank=True, verbose_name="კომენტარი")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="ჩანაწერის შექმნა")),
                ("project", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="entries", to="wine_app.wineproject", verbose_name="პროექტი")),
            ],
            options={"verbose_name": "ფერმენტაციის ჩანაწერი", "verbose_name_plural": "ფერმენტაციის ჩანაწერები", "ordering": ["-measured_at"]},
        ),
    ]
