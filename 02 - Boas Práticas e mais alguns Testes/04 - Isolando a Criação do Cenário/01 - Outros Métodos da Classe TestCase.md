Vimos na aula o método `setUp` que é executado antes de cada método de testes. Este não é o único método que herdamos da classe `TestCase`, além deste, temos outros métodos como o `tearDown`, `setUpClass` e o `tearDownClass`.

Vamos imaginar que estamos realizando um teste que faz a conexão com um serviço externo, envia um e-mail ou então faz uma modificação no banco de dados.

Nesses casos, precisamos abrir uma conexão, executar os testes e fechar a conexão em seguida. Fechar a conexão é algo em comum com esses tipos de testes.

Podemos então declarar o método `tearDown` que é executado logo após a execução do teste. Ou seja, caso abrimos uma conexão, podemos utilizar o método tearDown para fechá-la após os testes.

Analogamente ao método `setUp` e `tearDown`, temos o `setUpClass` e o `tearDownClass`. Ambos funcionam de uma forma parecida com o `setUp` e `tearDown`, porém, ao invés de serem executados antes de cada método, são executados apenas uma vez - o `setUpClass` no momento que a classe é criada e o `tearDownClass` após o último teste da classe ser rodado.

Os métodos `tearDown` e `tearDownClass` são muito utilizados em testes que integram duas partes do sistema - banco de dados, sistemas externos, ou então desejamos fechar uma conexão que foi aberta.

Esses tipos de testes, que verificam como duas partes do sistema se integram, são chamados de **testes de integração**.