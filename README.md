
 [![Tests](https://github.com/tamireinhorn/Extrator-de-Slides/actions/workflows/tests.yaml/badge.svg?branch=dev)](https://github.com/tamireinhorn/Extrator-de-Slides/actions/workflows/tests.yaml)


 Esse programa é um fork do [original](https://github.com/NatanaelAntonioli/Extrator-de-Slides), mas com uma série de bug fixes e melhorias. A ideia é que esta seja a versão definitiva, pois é a que está sendo mantida. Como o funcionamento do programa está diferente, esse README também será.

 ## O que esse programa faz? ##

O programa busca extrair, a partir de um arquivo de vídeo de uma video aula, os slides desta em formato `.pdf` para que o usuário possa tê-los mesmo que o professor não os mande.

 ## Como esse programa funciona? ##
O usuário deve apenas rodar o arquivo `src/SlideExtractor.py` em sua máquina. Ao fazer isso, o programa vai abrir janela para que seja escolhido o vídeo de uma aula. Em seguida, o usuário deve especificar quanto tempo um slide deve durar para ser considerado relevante.
O programa irá criar uma pasta com o nome de `slides de {nome do arquivo}`, e salvar todos os slides lá, bem como o PDF.
O programa então irá ler um frame do vídeo a cada intervalo especificado e comparar com o frame lido anteriormente. Se ambos forem bastante semelhantes, então o frame novo é descartado e uma nova leitura é feita, até que um frame diferente o suficiente seja encontrado. Quando isso acontece, ele é adicionado à pasta.
Ao final, as imagens são unidas para formar um arquivo em `pdf` semelhante à apresentação de slides que provavelmente foi usada no vídeo. 

 ## Quais as suas limitações? ##
 No momento, esse é um programa em Python. Ele requer que os usuários tenham algum conhecimento de Python para instalar as dependências necessárias e executá-los. 
 
O programa requer que você baixe um arquivo em vídeo, e o coloque no mesmo diretório de execução. Eventualmente, pretendo fazer com que ele baixe um link do YouTube.

O programa não possui garantias de detectar todos os slides, porém ele parte da premissa que slides mostrados por menos tempo do que o configurado não são relevantes. Em meus testes, todos os slides foram exportados.

É bastante provável que o programa não funcione bem em vídeos nos quais o professor aparece com câmera, mas deve ser possível contornar esse problema mudando o limite de detecção (já que agora os slides "mudam" mais do que antes mesmo sem transição). É quase certo que o programa não vai funcionar em vídeos como os da UNIVESP, nos quais os slides aparecem uma televisão. 
