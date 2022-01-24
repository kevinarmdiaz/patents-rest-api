import re
from rest_framework import serializers

def validate_equals_letter(patent):
    for letter in patent[2:4]:
        if not(patent[0]==letter):
            return False
    return True

class PatentsSerializer(serializers.Serializer):
    """Serializes a patent
        if any letter in the patent is not equal returns a ValidationError
        if the patent not match with (([A-Z]{4})[0-9]{3})$ returns a ValidationError"""
    
    id = serializers.IntegerField(required=False)
    patent = serializers.RegexField(required=False, regex=r'(([A-Z]{4})[0-9]{3})$')
    def validate(self, data):
        """
        Check that id or patent is not None.
        """
        id = data.get('id', None)
        patent = data.get('patent', None)

        if id is None and patent is None:
            raise serializers.ValidationError("Please check query params (id or patent)")
        return data

    def validate_patent(self, value):
        """
        Check that the patent is correct.
        """
        if  not validate_equals_letter(patent=value):
            raise serializers.ValidationError("This patent pattern is not allowed")
        return value

