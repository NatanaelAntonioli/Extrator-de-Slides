
 ## O que esse programa faz? ##
Eu simplesmente não consigo aproveitar aulas *online* (e nem a maioria das presenciais), portanto estudo com slides e livros. Porém, nem todo professor disponibiliza os slides.

Esse programa recebe um arquivo de vídeo (em formato `mp4`, até onde testei) e extrai os slides exibidos ali, produzindo um arquivo em `pdf` que contém todos os slides mostrados no vídeo, sem faltar ou repetir.

 ## Como esse programa funciona? ##
Você especifica, no cabeçalho, o total de minutos que o vídeo possui, o intervalo mínimo para procura e o nome do arquivo de vídeo.

    # ----------------------------- Variáveis ----------------------------  
    # Eu quero obter slides dos primeiros ... minutos do vídeo.  
    total_minutos = 46  
    # Se um slide é mostrado por menos de ... segundos, então ele não é importante.  
    # Slides provavelmente não serão mostrados por menos de ... segundos.  
    intervalo_segundos = 10  
    # O arquivo de vídeo possui o nome ... (formatos testados: mp4)  
    arquivo = "aula.mp4"
O programa então irá ler um frame do vídeo a cada intervalo especificado (no caso, 10 segundos) e comparar com o frame lido anteriormente. Se ambos forem bastante semelhantes, então o frame novo é descartado e uma nova leitura é feita, até que um frame diferente o suficiente seja encontrado. Quando isso acontece, ele é adicionado à uma galeria de imagens.

Ao final, as imagens são unidas para formar um arquivo em `pdf` semelhante à apresentação de slides que provavelmente foi usada no vídeo. 

Após cada uso, você precisará apagar as imagens na pasta `fotos`. Os demais arquivos não precisam ser alterados. 

 ## Quais as suas limitações? ##
 No momento, esse é um programa em Python. Ele requer que os usuários tenham algum conhecimento de Python para instalar as dependências necessárias e executá-los. Qualquer um é bem vindo para adaptá-lo em outras linguagens se assim desejar. Eu eventualmente tentarei fazer um executável com ele,  ou rodá-lo no Google Colab.
 
O programa requer que você baixe um arquivo em vídeo, e o coloque no mesmo diretório de execução. Eventualmente, pretendo fazer com que ele baixe um link do YouTube.

O programa não possui garantias de detectar todos os slides, porém ele parte da premissa que slides mostrados por menos tempo do que o configurado (no caso, 10 segundos) não são relevantes. Em meus testes, todos os slides foram exportados.

É bastante provável que o programa não funcione bem em vídeos nos quais o professor aparece com câmera, mas deve ser possível contornar esse problema mudando o limite de detecção (já que agora os slides "mudam" mais do que antes mesmo sem transição). É quase certo que o programa não vai funcionar em vídeos como os da UNIVESP, nos quais os slides aparecem uma televisão. 

Por fim, devem haver bugs. Vários bugs. Irei melhorá-lo no futuro, e você pode fazê-lo caso assim quiser. 
