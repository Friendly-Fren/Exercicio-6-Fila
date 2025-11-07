from collections import deque
import random
import time

class Alma:
    def __init__(self, nome):
        self.nome = nome
        self.estado = "esperando"

    def __str__(self):
        return f"Alma: {self.nome} | Estado: {self.estado}"

class Purgatorio:
    def __init__(self):
        self.fila = deque()

    def chegada_da_alma(self, nome):
        alma = Alma(nome)
        self.fila.append(alma)
        print(f"\n⚰️  {alma.nome} chegou ao purgatório.")

    def atender_alma(self):
        if self.fila:
            alma = self.fila.popleft()
            alma.estado = "julgada"
            print(f"\n👼 {alma.nome} está sendo julgada...")
            time.sleep(1)
            destino = random.choice(["céu", "inferno", "reencarnação"])
            print(f"⚖️  Destino de {alma.nome}: {destino.upper()}")
        else:
            print("\n✨ Não há almas na fila.")

    def mostrar_fila(self):
        print("\n📜 Fila atual de almas:")
        if not self.fila:
            print("Nenhuma alma esperando.")
        else:
            for alma in self.fila:
                print(f" - {alma}")

def menu():
    purgatorio = Purgatorio()
    while True:
        print("\n=== Menu do Purgatório ===")
        print("1. Nova alma chega")
        print("2. Atender próxima alma")
        print("3. Mostrar fila")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome da alma: ")
            purgatorio.chegada_da_alma(nome)
        elif escolha == "2":
            purgatorio.atender_alma()
        elif escolha == "3":
            purgatorio.mostrar_fila()
        elif escolha == "4":
            print("\n🌫️ O purgatório fecha suas portas por hoje...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()