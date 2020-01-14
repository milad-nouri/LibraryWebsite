
import datetime

from django import forms # 1st
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class RenewBookForm(forms.Form): # 1st
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).") # 1st

    def clean_renewal_date(self):
# The first is that we get our data using self.cleaned_data['renewal_date'] and that we return 
# this data whether or not we change it at the end of the function. This step gets us the data
# "cleaned" and sanitized of potentially unsafe input using the default validators, and converted 
# into the correct standard type for the data (in this case a Python datetime.datetime object).

        data = self.cleaned_data['renewal_date']
        
        # Check if a date is not in the past. 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data