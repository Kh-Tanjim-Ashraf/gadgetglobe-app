from django.db import models
from django.utils.text import slugify



class TimestampMixins(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class NamedSlugMixins(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs):
        # Slugify the `name` field; handle uniqueness inside the child classes `Meta` sub-class
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)