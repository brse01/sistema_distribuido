# Sistema Distribuido

## Implementação do Algoritmo de Berkeley
Nesse algoritmo, o “servidor de tempo” é ativo e consulta periodicamente cada uma das máquinas 
sobre os valores de seus relógios. Então realiza o calculo a média das leituras realizadas e informa 
cada máquina para que se ajuste, adiantando ou atrasando seu relógio. Essa média pode ser simples
ou ajustada, desprezando-se valores extremos, o que permite contornar eventuais falhas em alguns 
relógios. Também é possível considerar o tempo de comunicação entre as máquinas. Nesse algoritmo, 
não há necessidade de que o “servidor de tempo” consulte um serviço de hora atômica.

Desenvolvedores: Bruno Sousa e @mardoniovieira
