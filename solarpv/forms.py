from django import forms

from .models import *


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ["userID", "firstname", "middlename", "lastname", "address1", "address2", "city", "state", "zipcode",
                  "email", "officephone", "cellphone"]

        labels = {
            "userID": 'Username',
            "firstname": 'First Name',
            "middlename": 'Middle Name',
            "lastname": 'Last Name',
            "address1": 'Address',
            "address2": 'Address',
            "city": 'City',
            "state": 'State',
            "zipcode": 'Zip Code',
            "email": 'Email Address',
            "officephone": 'Office Phone',
            "cellphone": 'Cell Phone'

        }
        widgets = {
            'userID': forms.TextInput(attrs={'placeholder': 'Chosen Username - Required'}),
            'firstname': forms.TextInput(attrs={'placeholder': 'First Name - Required'}),
            'middlename': forms.TextInput(attrs={'placeholder': 'Middle Name'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Last Name - Required'}),
            'address1': forms.TextInput(attrs={'placeholder': 'Street Address - Required'}),
            'address2': forms.TextInput(attrs={'placeholder': 'Apt/Unit#'}),
            'city': forms.TextInput(attrs={'placeholder': 'City of Residence - Required'}),
            'state': forms.TextInput(attrs={'placeholder': 'State or Province - Required'}),
            'zipcode': forms.TextInput(attrs={'placeholder': 'Zip Code - Required'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email Address'}),
            'officephone': forms.TextInput(attrs={'placeholder': 'Office Phone'}),
            'cellphone': forms.TextInput(attrs={'placeholder': 'Cell Phone'})

        }


class Test_StandardForm(forms.ModelForm):
    class Meta:
        model = Test_Standard
        fields = ["standard_ID", "standard_name", 'description', 'published_date']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_ID', 'service_name', 'description', 'is_FI_required', 'FI_frequency']


class Test_SequenceForm(forms.ModelForm):
    class Meta:
        model = Test_Sequence
        fields = ['sequence_ID', 'sequence_name']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_ID', 'client_name', 'client_type']


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['location_ID', 'address1', 'address2', 'city', 'state', 'postal_code', 'country', 'phone_number', 'fax_number']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['userID', 'first_name', 'last_name', 'middle_name', 'job_title', 'email', 'office_phone', 'cell_phone', 'prefix']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['model_number', 'product_name', 'cell_technology', 'cell_manufacturer', 'number_of_cells', 'number_of_cells_in_series', 'number_of_series_strings', 'number_of_diodes', 'product_length', 'product_width', 'product_weight', 'superstate_type', 'superstate_manufacturer', 'substrate_type', 'substrate_manufacturer', 'frame_type', 'frame_adhesive', 'encapsulate_type', 'encapsulate_manufacturer', 'junction_box_type', 'junction_box_manufacturer']


class Performance_DataForm(forms.ModelForm):
    class Meta:
        model = Performance_Data
        fields = ['max_system_voltage', 'voc', 'isc', 'vmp', 'imp', 'pmp', 'ff']


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['certificate_number', 'ID', 'report_number', 'issue_date']