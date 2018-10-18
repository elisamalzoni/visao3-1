# visao3-3
## Elisa Malzoni

### Executando o programa
Para criar o vocabulário, rode `create_vocab.py`, que guarda a contagem e o vocabulário em arquivos. Não será necessario, já que os arquivos então neste repositório.

Para rodar o programa:

`python3 similar_images.py {imagem a ser buscada} {tipo de similaridade(bovw|poi)} [show` 

`show` - opcional, mostra as imagens encontradas

Exemplo de uso:

`python3 similar_images.py ./101_ObjectCategories/platypus/image_0030.jpg bovw show`

### Desempenho
#### Points of Interest


|Imagem Buscada                  |./101_ObjectCategories/platypus/image_0030.jpg        |
|--------------------------------|------------------------------------------------------|
|Imagem com maior similaridade   |./VOC2005_1/PNGImages/TUGraz_bike/bike_313.png        |
|Imagem com 2a maior similaridade|./VOC2005_1/PNGImages/Caltech_motorbikes_side/0090.png|
|Imagem com 3a maior similaridade|./VOC2005_1/PNGImages/TUGraz_person/person_186.png    |

#### Bag of Visual Words
