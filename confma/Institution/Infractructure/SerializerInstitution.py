from rest_framework import serializers
from ..Domain.Institution import Institution


class SerializerInstitution(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = ['id', 'name', 'phone', 'address']
        extra_kwargs = {
            'name': {
                'error_messages': {
                    'required': 'Please enter a name of a institution',
                    'invalid': 'Please enter a valid name of institution'
                }
            },
            'phone': {
                'error_messages': {
                    'required': 'Please enter a phone number a institution',
                    'invalid': 'Please enter a valid phone number a institution'
                }
            },
            'address': {
                'error_messages': {
                    'required': 'Please enter a address of a institution',
                    'invalid': 'Please enter a valid address of a institution'
                }
            }
        }
