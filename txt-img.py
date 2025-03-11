from PIL import Image
import numpy as np

caminho_txt = 'data/resultado.txt'

matriz = np.loadtxt(caminho_txt, dtype=np.uint8)

imagem = Image.fromarray(matriz, mode='L')

caminho_imagem = caminho_txt.replace('.txt', '_convertido.png')

imagem.save(caminho_imagem)
print(f"Imagem salva como: {caminho_imagem}")
imagem.show()