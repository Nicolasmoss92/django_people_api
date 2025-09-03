# api_people/views.py
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError

from .services.user_service import UserService
from .serializers import UserSerializer


# Instanciamos o serviço para uso na view.
user_service = UserService()

class CreateUserView(APIView):
    """
    View para a criação de um novo usuário.
    Utiliza a classe APIView para uma estrutura mais organizada.
    """
    
    def post(self, request, *args, **kwargs):
        """
        Método POST para lidar com a criação do usuário.
        """
        serializer = UserSerializer(data=request.data)
        
        # O is_valid() já lida com as validações definidas no Serializer e no Model
        # e também com as validações customizadas, como a do `clean_cpf`.
        if serializer.is_valid():

            user_service.create_user(serializer.validated_data)
            
            # Retorna uma resposta de sucesso com os dados do usuário criado
            return Response(status=status.HTTP_204_NO_CONTENT)

        # Se os dados não forem válidos, o DRF já formata os erros automaticamente.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)