# exemplo-blockchain
Para entender o conceito de cadeia de confiança do blockchain e o nível de dificuldade para realizar qualquer alteração nela, 
criei um blockchain básico e claro. 

No arquivo “Block.py”, criei a classe "Block" e nela está definida a estrutura de dados do bloco e a criação do hash. 
Neste exemplo, um bloco será composto por:
1.	o número do bloco;
2.	a informação que o bloco irá armazenar (seria a transação financeira);
3.	o ponteiro para o próximo bloco;
4.	o hash do próprio bloco;
5.	conta o número de hashs calculados, até encontrar um hash válido para o bloco;
6.	o hash do bloco anterior;
7.	o registro de data e hora.

No arquivo "Blockchain.py", desenvolvi a classe “Blockchain” que é responsável por criar o bloco e também por verificar se o hash é 
valido e adicionar um novo bloco a cadeia de blocos.
