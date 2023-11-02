from django import forms
from .models import UserProfile,Appointment


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['child_name', 'parent_name', 'email','password']  # Add other fields as needed
        widgets = {
            'password': forms.PasswordInput(),
        }
        
class appointment(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['child_name', 'age_group','doctor','last_certificate','appointment_date','appointment_time', 'email', 'password']
        # widgets = {
        #     'password':forms.PasswordInput(),
        # }


def apointment_data():
    data = []
    collection_ref = db.collection('your_collection_name')
    documents = collection_ref.stream()

    for doc in documents:
        data.append(doc.to_dict())

    return data

def childVacc():
    data = []
    collection_ref = db.collection('your_collection_name')
    documents = collection_ref.stream()

    for doc in documents:
        data.append(doc.to_dict())

    return data

def history():
    data = []
    collection_ref = db.collection('your_collection_name')
    documents = collection_ref.stream()

    for doc in documents:
        data.append(doc.to_dict())

    return data


        