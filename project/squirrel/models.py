from django.db import models
from django.utils.translation import gettext as _

class Sighting(models.Model):
    latitude = models.FloatField(
            max_length = 50,
            help_text=_('Latitude value'),
             )

    longitude = models.FloatField(
             max_length = 50,
             help_text=_('Longitude value'),
             )
    
    unique_squirrel_ID = models.CharField(
            max_length = 50,
            help_text=_('Squirrel_ID'),
             )
    PM = 'PM'
    AM = 'AM'
    OTHER = 'Other'
    SHIFT_CHOICES=(
            (PM,'PM'),
            (AM,'AM'),
            (OTHER,'Other'),
            )
    shift = models.CharField(
            max_length=15,
            choices= SHIFT_CHOICES,
            default = OTHER,
            )
    date = models.DateField(
            help_text=_('The date you saw the squirrel'),
            )
    
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    OTHER = 'Other'
    AGE_CHOICES=[
            (ADULT,'adult'),
            (JUVENILE, 'juvenile'),
            (OTHER, 'Other'),
            ]
    age = models.CharField(
            max_length=15,
            choices= AGE_CHOICES,
            default = OTHER,
            )
   

    BLACK='Black'
    CINNAMON= 'Cinnamon'
    GRAY = 'Gray'
    OTHER = 'Other'
    PRIMARY_FUR_COLOR_CHOICE=[
            (BLACK,'Black'),
            (CINNAMON,'Cinnamon'),
            (GRAY,'Gray'),
            (OTHER,'Other'),
            ]
    primary_fur_color=models.CharField(
        max_length = 50,
        choices = PRIMARY_FUR_COLOR_CHOICE,
        default = OTHER,
        )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND= 'Above Ground'
    OTHER = 'Other'
    LOCATION_CHOICE = [
            (GROUND_PLANE, 'Ground Plane'),
            (ABOVE_GROUND, 'Above Ground'),
            (OTHER, 'Blank or other'),
            ]
    location=models.CharField(
            max_length = 100,
            choices = LOCATION_CHOICE,
            default = OTHER,
            )

    
    specific_location = models.CharField(
        max_length = 500,
	help_text=_('Specific Location'),
        blank = True,
	)
    
    running = models.BooleanField(
            default = False,
            help_text = _('Running?'),
            )
    chasing = models.BooleanField(
            default = False,
            help_text = _('Chasing?'),
            )
    climbing = models.BooleanField(
            default = False,
            help_text = _('Climbing?'),
            )
    eating = models.BooleanField(
            default = False,
            help_text = _('Eating?'),
            )
    foraging = models.BooleanField(
            default = False,
            help_text = _('Foraging?'),
            )

    other_activities = models.CharField(
        max_length = 500,
        help_text=_('Specific Location'),
        blank = True,
        )

    kuks = models.BooleanField(
            default = False,
            help_text = _('Kuks?'),
            )
    quaas = models.BooleanField( 
            default = False,
            help_text = _('Quaas?'),
            )
    moans = models.BooleanField(
            default = False,
            help_text = _('Moans?'),
            )
    tail_flags = models.BooleanField(
            default = False,
            help_text = _('Tail Flags?'),
            )
    tail_twitches = models.BooleanField(
            default = False,
            help_text = _('Tail twitches?'),
            )
    approaches = models.BooleanField(
            default = False,
            help_text = _('Approaches?'),
            )
    indifferent = models.BooleanField(
            default = False,
            help_text = _('Indifferent?'),
            )
    runs_from = models.BooleanField(
            default = False,
            help_text = _('Runs from?'),
            )
    other_interactions = models.CharField(
        max_length = 500,
        help_text=_('Other Interactions?'),
        blank = True,
        )

