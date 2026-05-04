from django.conf import settings
from django.db import models
from django.urls import reverse


class WineProject(models.Model):
    WINE_STYLE_CHOICES = [
        ("ევროპული", "ევროპული"),
        ("ქვევრი", "ქვევრი"),
        ("ქარვისფერი", "ქარვისფერი"),
        ("წითელი", "წითელი"),
        ("თეთრი", "თეთრი"),
        ("ვარდისფერი", "ვარდისფერი"),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="wine_projects",
        null=True,
        blank=True,
    )
    name = models.CharField("პროექტის სახელი", max_length=255)
    grape_type = models.CharField("ყურძნის ჯიში", max_length=120, blank=True)
    harvest_date = models.DateField("მოსავლის თარიღი", null=True, blank=True)
    wine_style = models.CharField("ღვინის სტილი", max_length=50, choices=WINE_STYLE_CHOICES, default="ქვევრი")
    initial_brix = models.DecimalField("საწყისი Brix", max_digits=5, decimal_places=2, null=True, blank=True)
    initial_sugar = models.DecimalField("საწყისი შაქარი", max_digits=6, decimal_places=2, null=True, blank=True)
    initial_ph = models.DecimalField("საწყისი pH", max_digits=4, decimal_places=2, null=True, blank=True)
    initial_acidity = models.DecimalField("საწყისი მჟავიანობა", max_digits=5, decimal_places=2, null=True, blank=True)
    vessel = models.CharField("ჭურჭელი", max_length=120, blank=True)
    volume_liters = models.DecimalField("მოცულობა ლიტრებში", max_digits=8, decimal_places=2, null=True, blank=True)
    notes = models.TextField("შენიშვნა", blank=True)
    is_active = models.BooleanField("აქტიური", default=True)
    created_at = models.DateTimeField("შექმნის თარიღი", auto_now_add=True)
    updated_at = models.DateTimeField("განახლების თარიღი", auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "ღვინის პროექტი"
        verbose_name_plural = "ღვინის პროექტები"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})

    @property
    def latest_entry(self):
        return self.entries.order_by("-measured_at").first()


class FermentationEntry(models.Model):
    project = models.ForeignKey(WineProject, on_delete=models.CASCADE, related_name="entries", verbose_name="პროექტი")
    measured_at = models.DateTimeField("თარიღი და დრო")
    temperature = models.DecimalField("ტემპერატურა °C", max_digits=5, decimal_places=2, null=True, blank=True)
    brix = models.DecimalField("Brix", max_digits=5, decimal_places=2, null=True, blank=True)
    sugar = models.DecimalField("შაქარი", max_digits=6, decimal_places=2, null=True, blank=True)
    ph = models.DecimalField("pH", max_digits=4, decimal_places=2, null=True, blank=True)
    acidity = models.DecimalField("მჟავიანობა გ/ლ", max_digits=5, decimal_places=2, null=True, blank=True)
    action = models.CharField("ქმედება", max_length=255, blank=True)
    comment = models.TextField("კომენტარი", blank=True)
    created_at = models.DateTimeField("ჩანაწერის შექმნა", auto_now_add=True)

    class Meta:
        ordering = ["-measured_at"]
        verbose_name = "ფერმენტაციის ჩანაწერი"
        verbose_name_plural = "ფერმენტაციის ჩანაწერები"

    def __str__(self):
        return f"{self.project} - {self.measured_at:%Y-%m-%d %H:%M}"
