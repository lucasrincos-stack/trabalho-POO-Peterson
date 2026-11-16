"""Cargos disponíveis na empresa."""
from funcionario import Funcionario


class Gerente(Funcionario):
    """Funcionário gerente, responsável por uma equipe."""

    def __init__(self, nome: str, idade: int, salario: float, tamanho_equipe: int):
        super().__init__(nome, idade, salario)
        if tamanho_equipe < 0:
            raise ValueError("O tamanho da equipe não pode ser negativo.")
        self.tamanho_equipe = tamanho_equipe

    def calcular_bonus(self) -> float:
        """Gerentes recebem bônus equivalente a 20% do salário."""
        return self.salario * 0.20

    def __str__(self) -> str:
        """Inclui o tamanho da equipe na apresentação."""
        return f"{super().__str__()} | Equipe: {self.tamanho_equipe} pessoa(s)"


class Desenvolvedor(Funcionario):
    """Funcionário de desenvolvimento com linguagem principal."""

    def __init__(self, nome: str, idade: int, salario: float, linguagem: str):
        super().__init__(nome, idade, salario)
        linguagem = linguagem.strip()
        if not linguagem:
            raise ValueError("A linguagem principal não pode ficar vazia.")
        self.linguagem = linguagem

    def calcular_bonus(self) -> float:
        """Desenvolvedores recebem bônus equivalente a 10% do salário."""
        return self.salario * 0.10

    def __str__(self) -> str:
        """Inclui a linguagem principal na apresentação."""
        return f"{super().__str__()} | Linguagem: {self.linguagem}"


class Estagiario(Funcionario):
    """Funcionário estagiário com instituição de ensino."""

    def __init__(self, nome: str, idade: int, salario: float, instituicao: str):
        super().__init__(nome, idade, salario)
        instituicao = instituicao.strip()
        if not instituicao:
            raise ValueError("A instituição de ensino não pode ficar vazia.")
        self.instituicao = instituicao

    def calcular_bonus(self) -> float:
        """Estagiários recebem bônus equivalente a 5% do salário."""
        return self.salario * 0.05

    def __str__(self) -> str:
        """Inclui a instituição na apresentação."""
        return f"{super().__str__()} | Instituição: {self.instituicao}"
