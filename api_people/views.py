# api_people/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ValidationError

from .services.user_service import UserService
from .serializers import UserSerializer


# Instanciamos o serviço para uso na view.
user_service = UserService()

@api_view(['POST'])
def create_user_view(request):
    """
    Controller para a criação de um novo usuário.
    Recebe a requisição POST e delega a lógica ao serviço.
    """
    if request.method == 'POST':
        try:
            # Chama a lógica de negócio do serviço
            new_user = user_service.create_user(request.data)
            
            # Serializa o objeto criado e retorna uma resposta de sucesso
            serializer = UserSerializer(new_user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except ValidationError as e:
            # Lida com erros de validação
            return Response({"error": e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            # Lida com outros erros inesperados
            return Response({"error": "Ocorreu um erro interno."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)