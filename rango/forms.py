import re

from django import forms

from rango.models import Category, Page


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        model = Category
        fields = ("name",)


class PageForm(forms.ModelForm):
    error_css_class = "form_error_message"
    required_css_class = "form_required_field"

    title = forms.CharField(
        max_length=128, help_text="Please enter the title of the page."
    )
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get("url")

        if url:
            # Strip away any leading http or https
            url = re.sub(r"https?:/{2}", "", url)
        # If url is not empty and doesn't start with 'https://',
        # then prepend 'https://' as we want to make sure
        # we are accessing a secure site
        if url:
            url = f"https://{url}"
            cleaned_data["url"] = url

        return cleaned_data

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page
        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values; we may not want to include them.
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ("category",)
        # or specify the fields to include (don't include the category field).
        # fields = ('title', 'url', 'views')
