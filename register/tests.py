from django.test import TestCase
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm

class SignUpFormTest(TestCase):

    def test_valid_form(self):
        form_data = {
            'username': 'user123',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
            'checkbox': True,
        }
        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_username(self):
        form_data = {
            'username': 'user@123',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
            'checkbox': True,
        }
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertEqual(form.errors['username'][0], "El usuario solo puede contener letras y numeros")

    def test_password_mismatch(self):
        form_data = {
            'username': 'user123',
            'password1': 'strongpassword123',
            'password2': 'differentpassword',
            'checkbox': True,
        }
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)
        self.assertEqual(form.errors['password2'][0], "Las contrasenas no coinciden")

    def test_terms_not_accepted(self):
        form_data = {
            'username': 'user123',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
            'checkbox': False,
        }
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('checkbox', form.errors)
        self.assertEqual(form.errors['checkbox'][0], "Debe aceptar los terminos y condiciones")

    def test_password_too_short(self):
        form_data = {
            'username': 'user123',
            'password1': 'short',
            'password2': 'short',
            'checkbox': True,
        }
        form = SignUpForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)
        self.assertEqual(form.errors['password2'][0], "La contrasena debe tener al menos 8 caracteres")

class LoginFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='user123', password='correctpassword')

    def test_username_not_found(self):
        form_data = {
            'username': 'usernotfound123',
            'password': 'strongpassword123'
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertEqual(form.errors['username'][0], "El usuario no existe")

    def test_invalid_password(self):
        form_data = {
            'username': 'user123',
            'password': 'invalidpassword123'
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)
        self.assertEqual(form.errors['password'][0], "La contrasena es incorrecta")