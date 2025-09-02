from ..models import User

class UserRepository:
    def create(self, data):
        """Cria um novo usuário no banco de dados."""
        return User.objects.create(**data)