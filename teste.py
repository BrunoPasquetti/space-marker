from extensoes import*
pygame.init()
tamanho = (800,500)
tela = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()
fundo = pygame.image.load("bg.jpg")
branco =(255,255,255)
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer_music.play(-1)

estrelas = {}

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring ("Space","Nome da Estrela:")
            print(item)
            if item == None:
                item + "desconhecidos"+str(pos)
            estrelas[item] = pos
            pygame.draw.circle(tela, branco, pos, 10)
