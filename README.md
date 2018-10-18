# visao3-3
## Elisa Malzoni

### Executando o programa
Para criar o vocabulário, rode `create_vocab.py`, que guarda a contagem e o vocabulário em arquivos. Não será necessário, já que os arquivos então neste repositório.

Para rodar o programa:

`python3 similar_images.py {imagem a ser buscada} {tipo de similaridade(bovw|poi)} [show` 

`show` - opcional, mostra as imagens encontradas

Exemplo de uso:

`python3 similar_images.py ./101_ObjectCategories/platypus/image_0030.jpg bovw show`

### Desempenho
#### Points of Interest
Busca de 4 imagens de categoria exixtente no banco:

  - Busca 1 - carro
![imagem poi](./imgs/poi_01.png)


  - Busca 2 - pessoa
![imagem poi](./imgs/poi_02.png)


  - Busca 3 - moto lateral
![imagem poi](./imgs/poi_03.png)


  - Busca 4 - bicicleta
![imagem poi](./imgs/poi_04.png)

Busca de imagem de categoria diferente das do banco:

  - ornintorrinco
![imagem poi](./imgs/poi_05.png)


#### Bag of Visual Words
Busca de 3 imagens de categoria exixtente no banco:

  - Busca 1 - ornintorrinco
![imagem bovw](./imgs/bovw_01.png)


  - Busca 2 - pessoa
![imagem bovw](./imgs/bovw_02.png)


  - Busca 3 - elefante
![imagem bovw](./imgs/bovw_03.png)


Busca de imagem de categoria diferente das do banco:

  - acordeão
![imagem bovw](./imgs/bovw_04.png)
