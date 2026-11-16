"""Gerencia o cadastro e a consulta de funcionários."""
from funcionario import Funcionario


class Empresa:
    """Mantém a lista de funcionários e oferece busca e cadastro."""

    def __init__(self, nome: str = "Empresa Exemplo"):
        self.nome = nome
        self._funcionarios: list[Funcionario] = []

    def cadastrar(self, funcionario: Funcionario) -> None:
        """Adiciona um funcionário à empresa."""
        if not isinstance(funcionario, Funcionario):
            raise TypeError("O cadastro aceita somente objetos Funcionario.")
        self._funcionarios.append(funcionario)

    def listar(self) -> list[Funcionario]:
        """Devolve uma cópia dos funcionários cadastrados."""
        return self._funcionarios.copy()

    def buscar(self, termo: str) -> list[Funcionario]:
        """Busca funcionários por nome ou cargo, sem diferenciar maiúsculas."""
        termo = termo.strip().casefold()
        if not termo:
            return []
        return [f for f in self._funcionarios
                if termo in f.nome.casefold() or termo in type(f).__name__.casefold()]
