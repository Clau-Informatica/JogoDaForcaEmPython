#importando biblioteca que gera valores pseudoaleatórios
import random
#definindo o 'boneco' da forca
boneco = ['', 'O', 'O-', 'O-|', 'O-|-', 'O-|-<']

#criando a classe do jogo
class Forca:
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_certas = []

    # Método para adivinhar a letra
    def adivinha(self, letra):
        if letra in self.palavra and letra not in self.letras_certas:
            self.letras_certas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def forca_acabou(self):
        if self.forca_venceu() or (len(self.letras_erradas) >= 5):
            return True
        return False

    # Método para verificar se o jogo se o jogador venceu
    def forca_venceu(self):
        if '_' not in self.palavra_escondida():
            return True
        return False

    # Método para não mostrar a letra escolhida
    def palavra_escondida(self):
        status = ''
        for letra in self.palavra:
            if letra not in self.letras_certas:
                status += '_'
            else:
                status += letra
        return status

    # Método para ver o status do jogo
    def show_status(self):
        print('\n ---------- JOGO DA FORCA ----------')
        print(boneco[len(self.letras_erradas)])
        print(f'Palavra: {self.palavra_escondida()}')
        print('\n Letras Erradas: ')
        for letra in self.letras_erradas:
            print(letra,)
        print('\n Letras Corretas:')
        for letra in self.letras_certas:
            print(letra,)
    
# Função para escolher uma palavra aleatória dentro de 'palavras.txt'
def palavra_aleatoria():
    with open('palavras.txt', 'rt') as arquivo:
        palavras = arquivo.readlines()
    return palavras[random.randint(0, len(palavras))].strip()
    

def main():
    # Objeto do jogo
    jogo = Forca(palavra_aleatoria())

    # Enquanto não terminar, solicitar letras
    while not jogo.forca_acabou():
        jogo.show_status()
        letra_escolhida = input('\nDigite uma letra: ')
        jogo.adivinha(letra_escolhida)

    # Verifica o Status do jogo
    jogo.show_status()

    # De acordo com o resultado, mostra mensagens
    if jogo.forca_venceu():
        print('\nPARABÉNS! Você ganhou o jogo.')
    else:
        print('\nFim de jogo, talvez em outra lua você acerte!')
        print(f'A palavra era {jogo.palavra}')

# Executa o programa
if __name__ == '__main__':
    main()