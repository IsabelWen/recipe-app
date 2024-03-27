from django import forms

CHART__CHOICES = (
   ('bar_chart', 'Bar chart'),
   ('pie_chart', 'Pie chart'),
   ('line_chart', 'Line Chart'),
)

class RecipesSearchForm(forms.Form):
    recipe_name = forms.CharField(max_length=100)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)