
from rest_framework.response import Response
from rest_framework import status
from patents_api import serializers
from rest_framework.views import APIView
from math import log10
def get_number_by_letter(range_id):
    return (log10(range_id) - 1)

def get_letter_patent(id):
    letter_position = id//999
    if letter_position <=0:
         letter_position = 0
    return chr(65 + (letter_position))

def get_number_patent(id):
    return id - 999*(id//999)



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
            return Response({f"Patent of Id {id} is": patent})
        if patent:
            patent = patent.upper()
            id  = (ord(patent[0])-65)*999 + int(patent[4:])
            return Response({f"Id of Patent {patent} is": id})


