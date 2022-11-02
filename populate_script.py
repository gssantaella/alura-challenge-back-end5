import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

import random
from string import hexdigits, ascii_uppercase
from aluraflixbe.models import Categoria, Video

URL_BASE = 'tst.com.br'


def cria_categorias(quantidade):
    for _ in range(quantidade):
        titulo = ''.join(random.choices(ascii_uppercase, k=15))
        cor = '#' + ''.join(random.choices(hexdigits, k=6))
        c = Categoria(titulo=titulo, cor=cor)
        c.save()


def cria_videos(quantidade):
    for _ in range(quantidade):
        titulo = ''.join(random.choices(ascii_uppercase, k=15))
        descricao = ''.join(random.choices(ascii_uppercase, k=40))
        url = URL_BASE + '/' + ''.join(random.choices(ascii_uppercase, k=8))
        categoria = random.choice(Categoria.objects.all())
        v = Video(titulo=titulo, descricao=descricao, url=url, categoria=categoria)
        v.save()


#cria_categorias(10)
#cria_videos(50)
print('Dados incluidos com sucesso')