
from rest_framework.response import Response
from rest_framework import status
from patents_api import serializers
from rest_framework.views import APIView

def get_letter_patent(id):
    id = id - 1
    letter_position = id//1000
    if letter_position <=0:
         letter_position = 0
    return chr(65 + (letter_position))

def get_number_patent(id):
    id = id - 1
    return id - 1000*(id//1000)



class PatentsGeneratorView(APIView):
    """Get patent by id or get id by patent
    """
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        qp_serializer = serializers.PatentsSerializer(data=request.query_params)
        qp_serializer.is_valid(raise_exception=True)
        id = qp_serializer.data.get('id', None)
        patent = qp_serializer.data.get('patent', None)
        if id is not None:
            patent = f"{get_letter_patent(id)*4}{get_number_patent(id):03d}"
            validate_patent = serializers.PatentsSerializer(data={'patent':patent})
            validate_patent.is_valid(raise_exception=True)
            return Response({f"Patent of Id {id} is": patent})
        if patent:
            patent = patent.upper()
            id  = (ord(patent[0])-65)*1000 + int(patent[4:])
            return Response({f"Id of Patent {patent} is": id + 1})


