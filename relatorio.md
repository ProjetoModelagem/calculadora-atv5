# Relatório dos Testes

## Resultado da Execução

Todos os testes foram executados com sucesso:

Ran 16 tests in ~0.004s

OK


**Resumo:**
-  **Total de testes:** 16
-  **Falhas:** 0
-  **Erros:** 0

Os testes cobrem:
- **Unidade**: validação de entrada/saída, tipagem, consistência de histórico, inicialização, modificação de dados, limites inferior/superior, valores fora do intervalo, fluxos de controle e mensagens de erro.
- **Integração**: operações sequenciais e integração entre métodos (uso do último resultado e histórico).

---

## Cobertura de Código

De acordo com o `coverage report` e o relatório HTML:

| Arquivo                       | Cobertura |
|---------------------------------|----------|
| `src\calculadora.py`           | **100%** |
| `tests\test_integracao.py`     | **96%**  |
| `tests\test_unidade.py`        | **99%**  |
| **Total do projeto**           | **99%**  |

> *Relatório gerado com* [coverage.py v7.10.6](https://coverage.readthedocs.io) em **19/09/2025**.

---

## Problemas Encontrados e Correções

- **Repetição de verificação de tipos:** cada método validava os argumentos separadamente.  
  **Correção:** criado o método auxiliar `_verifica_tipo` na classe `Calculadora` para centralizar a checagem e evitar duplicação.

- **Estado após erro:** confirmou-se via testes que, em caso de divisão por zero, o atributo `resultado` e o `historico` permanecem inalterados. Nenhuma correção foi necessária, apenas verificação.

Nenhum outro bug foi identificado no código da calculadora.

---

## O que foi aprendido/feito?

- **Testes de Unidade** garantem que cada método da calculadora funciona isoladamente, incluindo casos de borda (zero, números muito grandes/pequenos) e mensagens de erro claras.
- **Testes de Integração** validam a interação entre métodos, como o encadeamento de operações e a manutenção correta do histórico.
- **Cobertura de Código** próxima de 100% reforça que a maioria dos caminhos de execução foi verificada, aumentando a confiabilidade.
- Criação de um relatório em Markdown e de um relatório HTML de cobertura para facilitar o entendimento.

---

*Projeto concluído com sucesso, atendendo a todos os requisitos de testes de unidade e integração descritos na atividade.* 
