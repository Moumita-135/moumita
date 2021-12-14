from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "User Name ..."
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Password..."
            })
    )


class SignupForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "First Name..."
            }))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Last Name..."
            }))
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "User Name..."
            }))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Email..."
            }))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Password..."
            }))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Confirm Password..."
        }))
    dept = forms.CharField(
        widget=forms.Select(
            choices=DeptChoice,
            attrs={
                'class': 'form-control'
            }))
    year = forms.CharField(
        widget=forms.Select(
            choices=YearChoice,
            attrs={
                'class': 'form-control'
            }))
    semester = forms.CharField(
        widget=forms.Select(
            choices=SemChoice,
            attrs={
                'class': 'form-control'
            }))
    enrollment = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Enrollment Number.."
            }))

    profilepic = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                # 'class': 'custom-file-input',
                'id': "customFile",
                'onchange': "readURL(this);",
                'style': "display: none;"
            }
        ))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'dept', 'year', 'semester',
                  'enrollment', 'profilepic', 'status', 'is_cdc', 'is_teacher', 'is_student')


class CategoryManagement(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Category Name..."
            }))

    class Meta:
        model = QuestionCategory
        fields = ('name', 'owner', 'status')


class QuestionManagement(forms.ModelForm):
    question = forms.Textarea()

    class Meta:
        model = Question
        fields = ('question', 'questioncategory',
                  'owner', 'status', 'postedtime')


class AnswerManagement(forms.ModelForm):
    answer = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-sm',
                'placeholder': "Provide your Answer Hear..."
            }))

    class Meta:
        model = Answer
        fields = ('answer', 'questionid',
                  'solver', 'answertime', 'status')


class ContactForm(forms.ModelForm):
    contact = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Elaborate your Concern"
            }))
    class Meta:
        model = Contact
        fields = ('name', 'email')