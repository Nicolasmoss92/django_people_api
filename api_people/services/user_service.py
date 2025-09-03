from django.core.exceptions import ValidationError

from api_people.models import User
from ..repositories.user_repository import UserRepository


class UserService:
    def __init__(self, repository=None):
        # Injeção de dependência manual
        self.repository = repository or UserRepository()

    def create_user(self, data):
        """
        Lógica de negócio para criar um novo usuário.
        Valida e delega a criação para o repositório.
        """
        required_fields = ["first_name", "last_name", "email", "cpf"]
        if not all(field in data for field in required_fields):
            raise ValidationError("Campos obrigatórios ausentes.")

        if User.objects.filter(cpf=data["cpf"]).exists():
            raise ValidationError("CPF já cadastrado.")

        return self.repository.create(data)
