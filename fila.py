from collections import deque
class FilaAtendimento:
    def __init__(self):
        self.fila = deque()

    def adicionar_pessoa(self, nome):
        self.fila.append(nome)
        print(f"\n{nome} foi adicionado(a) à fila.")

    def atender_pessoa(self):
        if len(self.fila) > 0:
            pessoa_atendida = self.fila.popleft()
            print(f"\n{pessoa_atendida} foi atendido(a)!")
        else:
            print("\nA fila está vazia. Não há ninguém para atender.")

    def mostrar_fila(self):
        if len(self.fila) > 0:
            print("\nPessoas na fila:")
            for i, pessoa in enumerate(self.fila, 1):
                print(f"{i}. {pessoa}")
        else:
            print("\nA fila está vazia.")

def main():
    fila = FilaAtendimento()
    
    while True:
        print("\n=== Sistema de Fila de Atendimento ===")
        print("1 - Adicionar pessoa à fila")
        print("2 - Atender pessoa")
        print("3 - Mostrar fila")
        print("4 - Sair")
        
        try:
            opcao = int(input("\nEscolha uma opção: "))
            
            if opcao == 1:
                nome = input("Digite o nome da pessoa: ")
                fila.adicionar_pessoa(nome)
            elif opcao == 2:
                fila.atender_pessoa()
            elif opcao == 3:
                fila.mostrar_fila()
            elif opcao == 4:
                print("\nPrograma encerrado. Até mais!")
                break
            else:
                print("\nOpção inválida! Por favor, escolha uma opção válida.")
        except ValueError:
            print("\nEntrada inválida! Por favor, digite um número.")

if __name__ == "__main__":
    main()