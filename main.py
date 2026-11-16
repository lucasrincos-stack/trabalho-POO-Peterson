"""Aplicação de terminal para gestão básica de funcionários."""
from funcionarios import Gerente, Desenvolvedor, Estagiario
from empresa import Empresa


def ler_inteiro(mensagem: str, minimo: int = 0) -> int:
    """Lê um inteiro no mínimo indicado, repetindo em caso de erro."""
    while True:
        try:
            valor = int(input(mensagem))
            if valor < minimo:
                raise ValueError
            return valor
        except ValueError:
            print(f"Informe um número inteiro igual ou maior que {minimo}.")


def ler_salario() -> float:
    """Lê um salário positivo, aceitando vírgula decimal."""
    while True:
        try:
            valor = float(input("Salário mensal (R$): ").replace(",", "."))
            if valor <= 0:
                raise ValueError
            return valor
        except ValueError:
            print("Informe um salário numérico maior que zero.")


def cadastrar_funcionario(empresa: Empresa) -> None:
    """Solicita dados e cadastra o cargo selecionado."""
    print("\nCargo: 1) Gerente  2) Desenvolvedor  3) Estagiário")
    cargo = input("Escolha: ").strip()
    nome = input("Nome: ")
    idade = ler_inteiro("Idade: ", 16)
    salario = ler_salario()
    try:
        if cargo == "1":
            funcionario = Gerente(nome, idade, salario, ler_inteiro("Tamanho da equipe: "))
        elif cargo == "2":
            funcionario = Desenvolvedor(nome, idade, salario, input("Linguagem principal: "))
        elif cargo == "3":
            funcionario = Estagiario(nome, idade, salario, input("Instituição de ensino: "))
        else:
            print("Cargo inválido.")
            return
        empresa.cadastrar(funcionario)
        print(f"Funcionário(a) {funcionario.nome} cadastrado(a) com sucesso!")
    except ValueError as erro:
        print(f"Não foi possível cadastrar: {erro}")


def exibir_funcionarios(funcionarios: list) -> None:
    if not funcionarios:
        print("Nenhum funcionário encontrado.")
        return
    for numero, funcionario in enumerate(funcionarios, start=1):
        print(f"{numero}. {funcionario}")


def main() -> None:
    empresa = Empresa()
    while True:
        print(f"\n=== RH | {empresa.nome} ===")
        print("1. Cadastrar funcionário\n2. Listar funcionários\n3. Buscar por nome/cargo")
        print("4. Calcular bônus (polimorfismo)\n0. Sair")
        opcao = input("Opção: ").strip()
        if opcao == "1":
            cadastrar_funcionario(empresa)
        elif opcao == "2":
            exibir_funcionarios(empresa.listar())
        elif opcao == "3":
            exibir_funcionarios(empresa.buscar(input("Nome ou cargo: ")))
        elif opcao == "4":
            if not empresa.listar():
                print("Cadastre um funcionário primeiro.")
            else:
                for funcionario in empresa.listar():
                    print(f"{funcionario.nome}: bônus de R$ {funcionario.calcular_bonus():.2f}")
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    main()
