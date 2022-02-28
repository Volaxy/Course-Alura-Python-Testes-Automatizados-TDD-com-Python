Vamos analisar a classe `Leilao`:

```
class Auction:
    def __init__(self, description):
        self.description = description
        self.__casts = []

        self.lowest_bidder = sys.float_info.max
        self.highest_bidder = sys.float_info.min

       # restante do código
```
Nesta classe, existe uma lista de lances. Ou seja, uma composição com uma lista. O que esperamos que ocorra com ela?

Esperamos que sejam adicionados os lances pertencentes ao leilão. Algo como `leilao.lances.append(lance)` é uma má prática, já que estamos muito acoplados com a implementação da classe `Leilao`.

Além de ferir o princípio do **Diga, não pergunte** (o *Tell don't ask*), estamos ferindo outro princípio chamado **Lei de Demeter**, ou o **Princípio do menor conhecimento** (*Principle of least knowledge*).

Esse princípio diz que devemos ter o menor conhecimento sobre a implementação da classe. Dessa forma, evitamos o acoplamento entre as classes do sistema.

Claro, o acoplamento sempre existirá. Quando estamos utilizando uma lista, string, dicionário, estamos acoplados com essa classe. Porém, isso é chamado de "acoplamento bom". A chance de uma dessas classes mudar e afetar o código é muito pequena.

<span style="background-color: #f0f0f0; color: black; padding: 10px;">Acoplar com classes estáveis é muito melhor do que com classes instáveis</span>

Então só devemos nos acoplar com classes do sistema?

Não! No código que escrevemos existem classes mais estáveis do que outras. São essas que devemos optar por acoplar.

Seguindo esses princípios como a Lei de Demeter e o Diga, não pergunte, escrevemos um código mais simples de ser alterado e escalado.

Quem quiser ver um pouco mais sobre a Lei de Demeter, deixo [esse texto](https://en.wikipedia.org/wiki/Law_of_Demeter), em inglês, da Wikipédia.