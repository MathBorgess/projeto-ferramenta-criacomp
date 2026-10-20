# Rodada aleatória - três propostas e seleção comercial

Direção de Matheus em 19/10/2026: sortear três sequências da caixa, executar três subagentes Luna em paralelo, registrar todas as propostas e então usar um quarto agente como advogado do diabo para selecionar uma. Esta autorização amplia a exploração anterior; a seleção desta rodada é uma avaliação dos agentes, sem compromisso de investimento ou evidência de venda.

## Sorteio preservado

Uma execução, seed `14532109174761975832`, entrada original com 11 dimensões. [Registro integral](sorteio.json), com números, itens, tentativas, hash da entrada e snapshot das opções. Não houve filtro comercial no sorteio.

| Proposta | Sequência de posições, na ordem das linhas da caixa |
| --- | --- |
| 01 | 4 - 1 - 3 - 4 - 3 - 1 - 1 - 2 - 3 - 3 - 1 |
| 02 | 4 - 3 - 1 - 2 - 4 - 4 - 1 - 4 - 3 - 2 - 3 |
| 03 | 3 - 1 - 3 - 1 - 4 - 3 - 2 - 4 - 1 - 2 - 2 |

O sorteio usa `randint(1, 4)` em cada linha. Se a posição não existe, repete somente aquela linha; se a sequência inteira já foi aceita, registra e descarta a duplicata. Isso preserva chances iguais entre opções válidas. A caixa não foi alterada para acomodar o sorteio.

## Aplicação de Revenue-Centric Design

Skill de [Richard (@richardrx)](https://x.com/richardrx), curada em [heliocosta-dev/revenue-centric-design](https://github.com/heliocosta-dev/revenue-centric-design/tree/1942760c2242f609bf63ce2c97204f5a1791bd68). A [licença específica do material RCD e suas adaptações](RCD-LICENSE.txt) acompanha esta rodada.

As propostas devem explicitar comprador, tarefa atual, primeiro valor entregue, preço hipotético, custo de servir, canal inicial e teste futuro de compra. Referências pertinentes: ICP e primeiros clientes; piso de custo/teto de valor; qualidade do sinal. As fontes originais estão nos prompts e devem ser citadas nas propostas.

Retorno financeiro será analisado em três contas distintas: receita cobrada pelo produto, contribuição depois dos custos e benefício econômico para o cliente. Nenhuma delas é resultado observado desta rodada.

## Critérios definidos antes das propostas

O advogado do diabo deve conferir primeiro fidelidade às 11 escolhas e IA no produto. Não pode salvar uma ideia trocando sua sequência. Em seguida, compara os cinco critérios abaixo; notas de 0 a 5 são julgamentos, não medições de mercado.

| Critério | Peso |
| --- | --- |
| Clareza do pagador, dor e motivo de compra | 30% |
| Conta econômica conservadora, incluindo trabalho e aquisição | 25% |
| Viabilidade do MVP e do uso autônomo no calendário | 20% |
| Canal inicial plausível e teste de pagamento executável | 15% |
| Diferenciação perante alternativa manual e LLM genérico | 10% |

Selecionar uma das três comparativamente, explicar as duas descartadas e apresentar a objeção mais forte à vencedora. Se nenhuma estiver pronta para investimento, preservar essa conclusão e escolher apenas a candidata menos frágil para validação. O crítico também deve testar a sensibilidade dos preços e custos; a pontuação sozinha não decide.

## Registro dos agentes

Os três agentes proponentes são solicitados como `gpt-6-luna`, sem histórico das ideias anteriores e com um arquivo de saída exclusivo. A concorrência é realizada pelo orquestrador nesta conversa, depois do sorteio. O quarto agente só será acionado quando as três propostas estiverem registradas.

- [Brief comum integral](prompts/brief-comum.md)
- [Prompt da proposta 01](prompts/proposta-01.md)
- [Prompt da proposta 02](prompts/proposta-02.md)
- [Prompt da proposta 03](prompts/proposta-03.md)

## Propostas registradas

| Proposta | Conceito | Comprador hipotético | Preço proposto, ainda não validado | Fragilidade principal |
| --- | --- | --- | --- | --- |
| [01 - Sala de Enredos](proposta-01.md) | Rascunho visual de narrativa com sala jogável | Mediador independente ou pequeno estúdio de oficinas | R$149 por sala/oficina | Esforço de construir e servir o fluxo jogável; disposição a pagar desconhecida |
| [02 - Oficina em Prancha](proposta-02.md) | Roteiro curto de oficina exportado em prancha PNG | Facilitador independente de oficinas recorrentes | R$149 por prancha/oficina | Substituição por ferramentas existentes e limite de acessibilidade do PNG |
| [03 - Traço](proposta-03.md) | Rascunho visual com registro da intenção | Designer iniciante | R$29 por prancha PNG | Alternativas gratuitas fortes e aquisição cara para o ticket |

Os arquivos das propostas preservam as saídas dos respectivos agentes. O [registro de execução](execucao.json) identifica modelos solicitados, prompts, saídas e hashes. Nenhuma dessas propostas constitui uma venda observada.

## Seleção concluída

**Vencedora desta rodada: proposta 02, Oficina em Prancha, para validação paga.** O [parecer integral do advogado do diabo](selecao-advogado-do-diabo.md) confere as 33 escolhas, refaz as contas e compara as três propostas. Nenhuma justificou investimento comercial com a evidência disponível.

O menor escopo e o desenvolvimento estimado em 40 horas favoreceram a 02. No cenário original, ela previa R$83 de contribuição por venda. O crítico substituiu o CAC hipotético por R$80 (quatro horas comerciais a R$60/h para três compradores) e acrescentou 15 minutos de operação. O resultado é **R$149 - R$11 de caixa - R$45 de trabalho - R$80 de aquisição = R$13 por venda**, antes de impostos e outros custos não cobertos. Para recuperar R$2.400 de desenvolvimento imputado seriam 185 vendas nesse cenário.

Essa conta expõe a fragilidade: com mais 15 minutos de trabalho, a contribuição se torna negativa. O teste futuro proposto exige três pagamentos integrais entre dez ofertas qualificadas, exportação autônoma e contribuição medida de pelo menos R$15 depois de todos os custos. Não foi executado.

O principal argumento contra a escolha é a substituição por Canva, Miro e um LLM genérico. A decisão é qual hipótese testar primeiro, não uma demonstração de retorno financeiro. O [documento do pitch](../../pitch-oficina-em-prancha.md) desenvolve a candidata selecionada.
