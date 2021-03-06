from django import forms

from .models import Review
from .models import Interview
from .models import Club
from .models import Leader

class HorizRadioSelect(forms.RadioSelect):
   template_name = 'page/horizontal_select.html'

class StarRating(forms.RadioSelect):
	template_name = 'star_ratings/widget_base.html'

class PostForm(forms.ModelForm):

    BIN_OPTIONS = (
	    (1, 'Yes'),
	    (0, 'No'),
    )

    STARS = (
    	(1, '1'),
    	(2, '2'),
    	(3, '3'),
    	(4, '4'),
    	(5, '5'),
    )

    fun = forms.ChoiceField(widget=HorizRadioSelect, choices=BIN_OPTIONS)
    meaningful = forms.ChoiceField(widget=HorizRadioSelect, choices=BIN_OPTIONS)
    stars = forms.ChoiceField(widget=HorizRadioSelect, choices=STARS)

    CBI = forms.CharField(max_length=200)

    class Meta:
        model = Review
        fields = ('text', 'fun', 'meaningful', 'stars', 'CBI',)

class InterviewForm(forms.ModelForm):

    BIN_OPTIONS_1 = (
        (1, 'Positive'),
        (0, 'Negative'),
    )

    BIN_OPTIONS_2 = (
        (1, 'Easy'),
        (0, 'Hard'),
    )

    positive = forms.ChoiceField(widget=HorizRadioSelect, choices=BIN_OPTIONS_1)
    hard = forms.ChoiceField(widget=HorizRadioSelect, choices=BIN_OPTIONS_2)

    class Meta:
        model = Interview
        fields = ('text', 'positive', 'hard',)

class EditForm(forms.ModelForm):

    photo1 = forms.ImageField(required=False)
    photo2 = forms.ImageField(required=False)
    photo3 = forms.ImageField(required=False)

    class Meta:
        model = Club
        fields = ('name', 'desc', 'website', 'email')

class LoginForm(forms.Form):
    username = forms.CharField(label="Net ID")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)



