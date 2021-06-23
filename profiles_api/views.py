from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, *args, **kwargs):
        """Returns a List of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions'
            'Is similar to traditional Django View',
            'Gives you full control over you application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':"Hello!", 'an_apiview': an_apiview})
