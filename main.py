# Dependências - parte delas precisam ser importadas com o pip
from skimage.metrics import structural_similarity as compare_ssim
import traceback
import cv2
import datetime
import time
from PIL import Image
from os.path import exists



# ----------------------------- Sobre ----------------------------
# Por enquanto o programa só funciona com vídeos que mostrem apenas slides.
# Vídeos com a câmera do professor ou com o professor mostrando os slides em uma televisão
# farão com que um slide seja exportado a cada 10 segundos (na configuração original).
# No pior dos casos, o programa fará um slide a cada 10 segundos.
# Aos poucos quero ir deixando ele melhor e fazer com que mais casos sejam cobertos.

# ----------------------------- Variáveis ----------------------------
# Eu quero obter slides dos primeiros ... minutos do vídeo.
total_minutos = int(input("Qual a duração do vídeo desejado? ")) #TODO: Idealmente, isso viria do arquivo em si.
# Se um slide é mostrado por menos de ... segundos, então ele não é importante.
# Slides provavelmente não serão mostrados por menos de ... segundos.
intervalo_segundos = int(input("Quantos segundos um slide tem que durar para ser relevante? "))
# O arquivo de vídeo possui o nome ... (formatos testados: mp4)
arquivo = 'aula.mp4' #input("Qual o nome do arquivo .mp4 da aula? ")  #TODO: Permitir que usuário selecione isso do diretório.

# ----------------------------- Execução ----------------------------
# Primeiro, ler a captura e abrir os diretórios/vetores
cap = cv2.VideoCapture(arquivo)
prints_directory = "fotos"
diferencas = []
iteracoes = int(total_minutos * 60 / intervalo_segundos)

skip_next = False   
last_i = -8

start = time.time()
print("Iniciando a extração...")
# Para cada iteração, ou seja, a cada pedaço de tantos segundos
for i in range(iteracoes):

    # Carrega o frame. Usa uma técnica meio go-horse.

    pos = i * 1000 * intervalo_segundos  # define o segundo a ser verificado
    cap.set(0, pos)
    ret, frame = cap.read()
    # if ret: # For debug
    #     cv2.imshow('frame', frame)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
    #     print(2)
    try:
        cv2.imwrite("atual.png", frame) # Salva o frame atual como atual.png
    except:
        i = iteracoes + 5000

    # Faz a comparacão do frame atual com o último.
    # Se a diferença for muito grande, então temos slides diferentes e um novo precisa ser salvo.

    write = True

    imageA = cv2.imread("atual.png")
    imageB = cv2.imread("last.png") # Se não tem last, isso aqui dá merda. Tem que dar resize também.

    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY) # Transforma imagens em grayscale
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    score = compare_ssim(grayA, grayB) # Compara imagens. 

    diferencas.append(score) # Adiciona numa lista o score de diferença. Próximo de 1 -> imagens sao iguais.
    tam = len(diferencas) # Mantém track do tamanho da lista
    try:
        comp = diferencas[tam - 1] - diferencas[tam - 2] # Eu tento pegar os dois scores de comparação mais recentes.
        if abs(comp) < 0.05 and i != 0: # Aí se a diferença deles for bem pouca, eu não escrevo. Ou seja:
            # Se os scores de comparação entre 2 frames seguidos forem muito próximos, eu não salvo o frame atual. 
            write = False
    except Exception:
        traceback.print_exc()

    # Escreve o quadro na pasta.

    if write and not skip_next: # Se for pra escrever e NÃO FOR pra pular pra próxima.
        cv2.imwrite("fotos/" + str(i) + ".png", frame) # Escreve a imagem pra pasta. 
        cv2.imwrite("last.png", frame) # Salva o frame válido como last. 
        print("Slide encontrado aos " + str(datetime.timedelta(seconds=i * intervalo_segundos)) + ".")

        # Isso aqui é necessário para evitar que todos os slides sejam escritos duas vezes.
        skip_next = True # Garante que vai pular pra próxima. 
        last_i = i 
    if write and skip_next and not last_i == i:
        skip_next = False # Aí na próxima iteração, ele reseta. Pra que skip next então?

# Por fim, produzir o PDF.
lista_imagens = []

# Isso aqui faz com que a pesquisa ocorra em ordem numérica e não alfabética.
# Se não, o programa faz algo como 1, 10, 11,...19, 100, 101, ... 199, 2, 20,21,...29,200,201,...299
for i in range(iteracoes + 5):
    try:
        im = Image.open("fotos/" + str(i) + ".png")
        lista_imagens.append(im)
    except:
        pass

pdf1_filename = "slides.pdf"
capa = Image.open("capa.png")

capa.save(pdf1_filename, "PDF", resolution=100.0, save_all=True, append_images=lista_imagens)

end = time.time()
tempo = end - start
print("Extração concluída em " + str(datetime.timedelta(seconds=tempo)) + "!")
