from django import forms

class StudentForm(forms.Form):
    student_id = forms.CharField(
        max_length=10,
        label="Student ID",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Student ID"
        })
    )

    name = forms.CharField(
        max_length=100,
        label="Student Name",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Student Name"
        })
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Email"
        })
    )

    python_marks = forms.IntegerField(
        min_value=0,
        max_value=100,
        label="Python Marks",
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    java_marks = forms.IntegerField(
        min_value=0,
        max_value=100,
        label="Java Marks",
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    dbms_marks = forms.IntegerField(
        min_value=0,
        max_value=100,
        label="DBMS Marks",
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )