No código, devolvemos uma cópia da lista de lances quando utilizamos a property:

```
class Auction:
    # código omitido

    @property
    def casts(self):
        return self.__casts[:]
```
Foi dito que isso é uma cópia rasa, mas o que isso significa?

Quando utilizamos uma cópia rasa, apenas a referência da lista, neste caso, é diferente. Todos os outros objetos dentro dessa lista compartilham a mesma referência. Ou seja, apesar da lista de lances ser uma cópia, os lances dentro da lista copiada são os mesmos lances do leilão.

Para que os lances sejam diferentes, precisamos copiar a lista profundamente. Por isso os termos cópia rasa e cópia profunda.

Poderia dar exemplos e falar sobre o funcionamento das cópias, porém, o Yan, um dos escritores do blog da Alura já escreveu um excelente post sobre cópias de lista no Python. Recomendo muito a leitura desse post. Para quem estiver interessado, pode encontrar a leitura neste link: http://blog.alura.com.br/como-fazer-copia-de-lista-python/