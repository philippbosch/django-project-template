from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.sites.models import Site


class CreatedByMixin(models.Model):
    created_by = models.ForeignKey(User, verbose_name=_('created by'), editable=False)

    class Meta:
        abstract = True


class CreationModificationDateMixin(models.Model):
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        abstract = True


class BaseModel(CreatedByMixin, CreationModificationDateMixin):
    class Meta:
        abstract = True


class SiteMixin(models.Model):
    site = models.ForeignKey(Site, verbose_name=_('site'), editable=False)

    class Meta:
        abstract = True


class AutoSlugMixin(models.Model):
    slug = models.SlugField(_('slug'), unique=True, editable=False)

    def get_slug_source(self):
        return str(self)

    def _get_unique_slug(self):
        slug = slugify(self.get_slug_source())
        unique_slug = slug
        num = 1
        while self.__class__.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        return super().save()

    class Meta:
        abstract = True
