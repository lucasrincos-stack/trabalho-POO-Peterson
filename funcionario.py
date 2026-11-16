"""Modelo base para funcionários da empresa."""


class Funcionario:
    """Representa dados comuns a todos os funcionários."""

    def __init__(self, nome: str, idade: int, salario: float):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    @property
    def nome(self) -> str:
        """Retorna o nome do funcionário."""
        return self.__nome

    @nome.setter
    def nome(self, valor: str) -> None:
        """Valida e define o nome."""
        valor = valor.strip()
        if not valor:
            raise ValueError("O nome não pode ficar vazio.")
        self.__nome = valor

    @property
    def idade(self) -> int:
        """Retorna a idade do funcionário."""
        return self.__idade

    @idade.setter
    def idade(self, valor: int) -> None:
        """Aceita idade inteira a partir de 16 anos."""
        if isinstance(valor, bool) or not isinstance(valor, int) or valor < 16:
            raise ValueError("A idade deve ser um número inteiro igual ou maior que 16.")
        self.__idade = valor

    @property
    def salario(self) -> float:
        """Retorna o salário mensal."""
        return self.__salario

    @salario.setter
    def salario(self, valor: float) -> None:
        """Valida e define um salário positivo."""
        try:
            valor = float(valor)
        except (TypeError, ValueError) as erro:
            raise ValueError("Informe um salário numérico.") from erro
        if valor <= 0:
            raise ValueError("O salário deve ser maior que zero.")
        self.__salario = valor

    def calcular_bonus(self) -> float:
        """Calcula o bônus da função (sobrescrito nas subclasses)."""
        raise NotImplementedError("Cada cargo deve implementar seu bônus.")

    def __str__(self) -> str:
        """Formata os dados comuns do funcionário."""
        return (f"{type(self).__name__}: {self.nome} | {self.idade} anos | "
                f"Salário: R$ {self.salario:.2f} | Bônus: R$ {self.calcular_bonus():.2f}")
