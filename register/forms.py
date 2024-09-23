from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

#Iniciliazar los estilos de los inputs y checkbox
INPUT_STYLE = "bg-blanco border-2 border-verder_claro rounded-lg focus:border-verder_claro focus:ring-verder_claro"
CHECKBOX_STYLE = "bg-blanco border-2 border-verder_claro focus:border-verder_claro focus:ring-verder_claro"

#Se crea el formulario de registro usando el formulario de UserCreationForm
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": INPUT_STYLE,
                "placeholder": "Ingrese su usuario",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": INPUT_STYLE,
                "placeholder": "Ingrese su contrasena",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": INPUT_STYLE,
                "placeholder": "Confirme su contrasena",
            }
        )
    )
    checkbox = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": CHECKBOX_STYLE,
            }
        )
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "checkbox")

    #Se sobreescriben los metodos clean_username, clean_password2 y clean_checkbox para agregar validaciones personalizadas
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username.isalnum() == False:
            raise forms.ValidationError("El usuario solo puede contener letras y numeros", code="invalid_username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("El usuario ya existe", code="username_taken")
        return username
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if len(password1) < 8:
            raise forms.ValidationError("La contrasena debe tener al menos 8 caracteres", code="password_too_short")
        elif password1 != password2:
            raise forms.ValidationError("Las contrasenas no coinciden",code="password_mismatch")
        return password2
    def clean_checkbox(self):
        checkbox = self.cleaned_data.get("checkbox")
        if not checkbox:
            raise forms.ValidationError("Debe aceptar los terminos y condiciones", code="terms_not_accepted")
        return checkbox

#Se crea el formulario de inicio de sesion usando el formulario de AuthenticationForm
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": INPUT_STYLE,
                "placeholder": "Ingrese su usuario",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": INPUT_STYLE,
                "placeholder": "Ingrese su contrasena",
            }
        )
    )
    checkbox = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": CHECKBOX_STYLE,
            },
        ),
    )

    class Meta:
        model = User
        fields = ("username", "password", "checkbox")
    #Se sobreescriben los metodos clean_username y clean_password para agregar validaciones personalizadas
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("El usuario no existe", code="username_not_found")
        return username
    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise forms.ValidationError("La contrasena es incorrecta", code="invalid_password")
        return password