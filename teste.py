import pygame
import tkinter
from tkinter import simpledialog
import pickle

pygame.init()
pygame.display.set_caption("Space Do Bruno")
tamanho = (800, 500)
tela = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
fundo = pygame.image.load("bg.jpg")
branco = (255, 255, 255)
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
icone = pygame.image.load("space.png")
pygame.display.set_icon(icone)

estrelas = []

fonte = pygame.font.Font(None, 20)
tamanho_letra = 20
fonte = pygame.font.Font(None, tamanho_letra)
texto_1 = "Pressione F10 para Salvar os Pontos"
posicao_texto_1 = (1, 1)
texto_2 = "Pressione F11 para Carregar os Pontos"
posicao_texto_2 = (1, 15)
texto_3 = "Pressione F12 para Deletar os Pontos"
posicao_texto_3 = (1, 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_F10:
                with open("pontos.pkl", "wb") as arquivo:
                    pickle.dump(estrelas, arquivo)
                print("Pontos salvos!")
            elif event.key == pygame.K_F11:
                try:
                    with open("pontos.pkl", "rb") as arquivo:
                        estrelas = pickle.load(arquivo)
                    print("Pontos carregados!")
                except FileNotFoundError:
                    print("Arquivo de pontos não encontrado.")
            elif event.key == pygame.K_F12:
                estrelas = []
                print("Pontos deletados!")
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela:")
            print(item)
            if item is None:
                item = "desconhecidos"
            estrelas.append((pos, item))

    def renderizar_texto(texto, cor, posicao):
        texto_renderizado = fonte.render(texto, True, cor)
        tela.blit(texto_renderizado, posicao)

    tela.blit(fundo, (0, 0))
    renderizar_texto(texto_1, branco, posicao_texto_1)
    renderizar_texto(texto_2, branco, posicao_texto_2)
    renderizar_texto(texto_3, branco, posicao_texto_3)

    for pos, item in estrelas:
        pygame.draw.circle(tela, branco, pos, 3)
        texto_superficie = fonte.render(item + " - " + str(pos), True, branco)
        texto_rect = texto_superficie.get_rect()
        texto_rect.center = (pos[0], pos[1] - 20)
        tela.blit(texto_superficie, texto_rect)
    if len(estrelas) >= 2:
        for i in range(len(estrelas) - 1):
            ponto_atual = estrelas[i][0]
            proximo_ponto = estrelas[i + 1][0]
            pygame.draw.line(tela, branco, ponto_atual, proximo_ponto)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
