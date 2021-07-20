import uuid

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager,
)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.gis.db import models
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class BaseModel(models.Model):
    """Generic base model with standard metadatas"""

    timestamp_create = models.DateTimeField(auto_now_add=True, editable=False)
    timestamp_update = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        db_index=True,
        editable=False,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        db_index=True,
        editable=False,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    class Meta:
        abstract = True


class Role(BaseModel, AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """

    username_validator = UnicodeUsernameValidator()
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists.")
        },
    )
    first_name = models.CharField(_("first name"), max_length=30)
    last_name = models.CharField(_("last name"), max_length=30)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    home_phone = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_("Numéro de téléphone fixe"),
    )
    mobile_phone = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_("Numéro de téléphone portable"),
    )
    addr_appt = models.CharField(
        max_length=50, blank=True, null=True, verbose_name=_("Appartement")
    )
    addr_building = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Immeuble")
    )
    addr_street = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Rue")
    )
    addr_city = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Commune")
    )
    addr_city_code = models.CharField(
        max_length=10, blank=True, null=True, verbose_name=_("Code postal")
    )
    addr_dept = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Département")
    )
    addr_country = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Pays")
    )
    comment = models.TextField(
        blank=True, null=True, verbose_name=_("Commentaire")
    )
    id_bdsource = models.CharField(max_length=100, blank=True, null=True)
    bdsource = models.CharField(max_length=100, blank=True, null=True)
    extra_data = models.JSONField(blank=True, null=True)
    geom = models.PointField(
        srid=settings.GEODATA_SRID,
        blank=True,
        null=True,
        verbose_name=_("Localisation géographique"),
    )

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return f"{self.username} <{self.email}>"

    def save(self, *args, **kwargs):
        # self.username = generate_username(self.first_name, self.last_name)
        self.last_name = self.last_name.upper()
        super(Role, self).save(*args, **kwargs)

    def clean(self):
        super(Role, self).clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    @property
    def name_pretty(self):
        "If lastname exists, return firstname initial and lastname. Else return username."
        if self.last_name:
            first = self.first_name or " "
            return f"{first[0] + '.'} {self.last_name}".strip(" .")
        else:
            return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
