# Sistema Bancário DIO - Atualizações

## Versão 01

### Operação de depósito

Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de saque

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de extrato
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
Os valores devem ser exibidos utilizando o formato R\$ xxx.xx, exemplo: 1500.45 = R$ 1500.45

## Versão 02

Separar as funções existentes de saque, depósito e extrato em funções. Criar três novas funções: cadastrar usuário (cliente), cadastrar conta bancária (vincular com usuário) e listar contas.

## Versão ??

Com os novos conhecimentos adquiridos sobre data e hora, você foi encarregado de implementar as seguintes funcionalidades no sistema:

- Estabelecer um limite de 10 transações diárias para uma conta.
- Se o usuário tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas para aquele dia.
- Mostre no extrato, a data e hora de todas as transações.
