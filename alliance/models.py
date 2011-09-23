from django.core.validators import MinValueValidator
from django.db import models


class Region(models.Model):
    """
    A geographical region associated with both users and opportunities.
    """
    label = models.CharField(max_length=40, unique=True)

    def __unicode__(self):
        return self.label

    class Meta:
        ordering = ('label',)


class Skill(models.Model):
    """
    A particular skill a musician has or an opportunity requires, like
    "jazz percussion" or "violin."
    """
    label = models.CharField(max_length=40, unique=True)

    def __unicode__(self):
        return self.label

    class Meta:
        ordering = ('label',)


class SkillLevel(models.Model):
    """
    Represents levels of proficiency. Users and opportunities are optionally
    associated with not only a skill (like "Piano") but a certain level of
    that skill (like "beginner" or "professional").
    """
    label = models.CharField(max_length=40, unique=True)
    order = models.SmallIntegerField(unique=True)

    def __unicode__(self):
        return self.label

    class Meta:
        ordering = ('-order', 'label')


class UserProfile(models.Model):
    """
    User profile data for this app.

    We shouldn't assume Django's AUTH_PROFILE_MODULE and User.get_profile()
    features will work for us -- a site may set those to some other app's
    model.
    """
    user = models.OneToOneField('auth.User')
    skills = models.ManyToManyField('alliance.Skill', blank=True,
        through='alliance.UserSkill')
    regions = models.ManyToManyField('alliance.Region', blank=True)

    def display_name(self):
        n = self.user.get_full_name()
        if not n:
            return self.user.username
        return n

    @models.permalink
    def get_absolute_url(self):
        return ('alliance.views.user_profile', [self.user.username])

    def __unicode__(self):
        return '%s Alliance profile' % self.user

    class Meta:
        ordering = ('user',)


class UserSkill(models.Model):
    """
    Intermediary model for the User-Skill many-to-many relationship.
    """
    user = models.ForeignKey('alliance.UserProfile')
    skill = models.ForeignKey('alliance.Skill')
    level = models.ForeignKey('alliance.SkillLevel', blank=True)


class Opportunity(models.Model):
    """
    A request for particular skills.
    """
    region = models.ForeignKey('alliance.Region')
    #reqs = models.ManyToManyField('alliance.Requirement')
    label = models.CharField(max_length=40)
    description = models.TextField()
    owner = models.ForeignKey('alliance.UserProfile')
    post_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.label

    class Meta:
        ordering = ('post_date', 'label')
        verbose_name_plural = 'opportunities'


class Requirement(models.Model):
    """
    Intermediary model for the Opportunity-Skill many-to-many relationship.
    """
    opportunity = models.ForeignKey('alliance.Opportunity')
    skill = models.ForeignKey('alliance.Skill')
    level = models.ForeignKey('alliance.SkillLevel', blank=True)
    count = models.PositiveIntegerField(blank=True, null=True,
        validators=[MinValueValidator(1)])
    takers = models.ManyToManyField('alliance.UserProfile', blank=True)
