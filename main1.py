from extensoes import*

pygame.init()
pygame.display.set_caption("Space Do Bruno")
tamanho = (800, 500)
tela = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
try:
    fundo = pygame.image.load("bg.jpg")
except pygame.error:
    fundo = pygame.Surface(tamanho)
    fundo.fill((0,0,0))

branco = (255, 255, 255)
try:
    pygame.mixer.music.load("Space_Machine_Power.mp3")
    pygame.mixer.music.play(-1)
except pygame.error:
    print("Erro ao carregar o arquivo de áudio")
try:
    icone = pygame.image.load("space.png")
    pygame.display.set_icon(icone)
except pygame.error:
    print("Erro ao carregar o icone")
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
    soma_x = 0
    soma_y = 0

    for pos, item in estrelas:
        pygame.draw.circle(tela, branco, pos, 3)
        texto_superficie = fonte.render(item + " - " + str(pos), True, branco)
        texto_rect = texto_superficie.get_rect()
        texto_rect.center = (pos[0], pos[1] - 20)
        tela.blit(texto_superficie, texto_rect)
        soma_x += pos[0]
        soma_y += pos[1]

    soma_total = soma_x + soma_y
    texto_soma = "Soma Total: " + str(soma_total)
    posicao_texto_soma = (1, 45)
    renderizar_texto(texto_soma, branco, posicao_texto_soma)

    if len(estrelas) >= 2:
        for i in range(len(estrelas) - 1):
            ponto_atual = estrelas[i][0]
            proximo_ponto = estrelas[i + 1][0]
            pygame.draw.line(tela, branco, ponto_atual, proximo_ponto)

            distancia_x = abs(proximo_ponto[0] - ponto_atual[0])
            distancia_y = abs(proximo_ponto[1] - ponto_atual[1])
            soma_distancias = distancia_x + distancia_y

            posicao_texto_distancias = (
                (ponto_atual[0] + proximo_ponto[0]) // 2,
                (ponto_atual[1] + proximo_ponto[1]) // 2 - 20,
            )
            texto_distancias = "Distância: " + str(soma_distancias)
            renderizar_texto(texto_distancias, branco, posicao_texto_distancias)

    

    pygame.display.update()
    clock.tick(60)

pygame.quit()
