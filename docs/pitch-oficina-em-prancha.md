# Pitch Oficina em Prancha

**Projeto Ferramenta | PF1 | máximo de cinco minutos.** Atualizado em 20/10/2026 para a direção de narrativa visual, skill interna e múltiplas saídas. O produto permanece uma proposta, sem MVP ou validação comercial realizados.

A [mudança de escopo](escopo-oficina-narrativa.md) foi informada pelo autor depois da seleção morfológica. O [pitch anterior](https://github.com/MathBorgess/projeto-ferramenta-criacomp/blob/f7d3ef162595d01fd8ec685422e6d264cc658282/docs/pitch-oficina-em-prancha.md) e as [propostas originais](experimentos/2026-10-19-sorteio-rcd/README.md) permanecem como histórico. A nova direção não foi submetida a outra rodada de seleção.

Apresentar somente os blocos marcados como fala. A duração abaixo é uma estimativa textual, sem ensaio humano.

**Duração estimada:** 490 palavras; 4min05s a 120 palavras/minuto. Com 30 segundos de pausas: 4min35s. Sem ensaio humano.

## Roteiro falado

### O que é e para quem

<!-- fala:inicio -->
Quem prepara uma palestra ou oficina precisa construir uma narrativa e depois adaptá-la para diferentes materiais. Nossa proposta é a Oficina em Prancha: uma ferramenta com IA em que a pessoa desenvolve essa narrativa enquanto vê e escolhe imagens, formas e cores. O foco inicial continua sendo facilitadores e palestrantes que usam esse conteúdo no trabalho. Queremos que o contexto criado permaneça disponível e possa alimentar outras entregas, sem começar cada material com um novo briefing.
<!-- fala:fim -->

### Como a pessoa cria

<!-- fala:inicio -->
Imagine uma oficina de ideação para pequenos empreendedores. A pessoa informa público, objetivo e duração, organiza a abertura, os exemplos, a atividade e o fechamento. Ao lado do texto, vê um painel visual. A IA sugere alternativas de narrativa e composição; o usuário escolhe referências, troca cores e formas e edita os blocos. As escolhas aprovadas são guardadas numa skill interna da oficina, junto com seu contexto e os arquivos visuais. A pessoa pode fechar e retomar o projeto. Ela não precisa escrever ou instalar uma skill: interage com sua narrativa e seus materiais.
<!-- fala:fim -->

### O que acontece no final

<!-- fala:inicio -->
Com essa base pronta, o usuário escolhe uma saída: por exemplo, um pitch deck, um post de LinkedIn ou um carrossel para Instagram. Cada formato tem um prompt e uma skill próprios, que trabalham com o mesmo contexto aprovado. O conteúdo é gerado dentro da ferramenta, onde o usuário pode revisar e editar o resultado. O objetivo é adaptar a mensagem ao formato, preservando fatos, voz e escolhas visuais. Uma nova geração deve criar outra versão, mantendo o trabalho anterior disponível.
<!-- fala:fim -->

### Benefício, similares e diferença a testar

<!-- fala:inicio -->
Nossa hipótese de valor é reduzir rebriefing, correções e inconsistências entre materiais da mesma oficina. Miro e Canva fazem parte do levantamento anterior de similares. Agora precisamos comparar o fluxo completo: construir, retomar e adaptar a narrativa para várias saídas. Não demonstramos uma vantagem competitiva. Também precisamos testar disposição a pagar e medir geração, armazenamento, revisões e suporte. O preço pensado para uma prancha PNG pertence ao escopo anterior e será recalculado para essa nova entrega.
<!-- fala:fim -->

### Tecnologias e recorte

<!-- fala:inicio -->
O produto será um aplicativo desktop em Electron, baixável para uso interno. Propomos React e TypeScript na interface, acesso a um modelo de linguagem e persistência do contexto e das imagens. A construção terá um repositório privado. Para o primeiro protótipo, propomos blocos editáveis e templates limitados. Imagens fornecidas pelo usuário permitem testar a experiência antes de integrar geração de imagens. Sistemas operacionais, fornecedor de IA e formatos de exportação ainda precisam ser definidos. O aplicativo ainda não foi implementado.
<!-- fala:fim -->

### Viabilidade e verificação

<!-- fala:inicio -->
O primeiro teste técnico será salvar uma oficina visual, reabri-la e gerar duas saídas sem repetir o briefing. A meta proposta é chegar aos três formatos. Os marcos registrados são arquitetura e baixa fidelidade em vinte e sete de outubro, ciclo ponta a ponta em dez de novembro, teste externo em doze e congelamento em dezessete. Outra pessoa deverá concluir o fluxo sem nossa explicação. Vamos observar preservação do conteúdo, tempo, correções e custo. A estimativa de esforço será refeita para este escopo.
<!-- fala:fim -->

## Apoio para responder às perguntas de PF1

| Pergunta | Resposta no projeto |
| --- | --- |
| O que é e como funciona? | Criação de narrativa com painel visual; contexto guardado numa skill interna e reutilizado por adaptadores de saída. |
| Público e benefício? | Foco inicial proposto em facilitadores e palestrantes profissionais; reduzir repetição de briefing e retrabalho é hipótese ainda não medida. |
| Interação? | Briefing → narrativa e escolhas visuais → base salva → seleção de formato → geração → revisão e nova versão. |
| Similares, tasks e diferença? | [Levantamento de 19/10](referencias/2026-10-19-taaft-miro-canva.md) com Miro AI e Canva AI/Magic Design. Os trechos fornecidos contêm Supported features, sem tasks específicas verificadas. Comparação do novo escopo ainda pendente. |
| Tecnologias? | Electron confirmado; React/TypeScript, acesso a modelo textual, persistência e templates propostos. Fornecedor de IA, sistemas-alvo e exportadores a definir. |
| Viabilidade e cronograma? | Um usuário por projeto, templates limitados e teste cedo de persistência/reutilização. Marcos registrados abaixo; esforço anterior não se transfere automaticamente. |

## Entregas e limites propostos

| Marco registrado | Entrega a planejar no novo escopo |
| --- | --- |
| 27/10 | Baixa fidelidade, estrutura do contexto interno e resultado mínimo de cada saída definidos |
| 10/11 | Narrativa visual, salvamento/reabertura e geração pelos adaptadores num ciclo completo |
| 12/11 | Outra pessoa completa o fluxo; registrar dificuldades e fidelidade entre saídas |
| 17/11 | Congelamento do recorte que passou pelos testes |
| 26/11 | Avaliação cruzada e post-mortem com resultados e limitações |

Datas registradas nos enunciados consultados em 19/10; não foram consultadas novamente nesta atualização. O novo planejamento exige confirmar capacidade e responsabilidades do grupo e formatos técnicos de exportação. O autor confirmou em 20/10 que o conteúdo será gerado dentro da ferramenta.

A direção confirmada pede aplicativo Electron para download/uso interno, imagens, formas e cores visíveis durante a criação, contexto interno e geração das saídas no próprio app. O uso de templates, o público inicial mantido e a forma de armazenamento são propostas de implementação. Não há autorização de publicação automática nas redes ou lançamento comercial nesta preparação.

## Similares e referências do catálogo

A comparação de Miro e Canva foi feita para a prancha visual anterior, com fontes e datas no [registro preservado](referencias/2026-10-19-taaft-miro-canva.md). A hipótese atual é preservar decisões narrativas e visuais entre formatos com menos rebriefing e correções. Ela deve ser comparada ao fluxo habitual do público com o mesmo conteúdo e entregas equivalentes. Não alegar exclusividade por usar uma skill internamente.

## Hipótese comercial a reestimar

Os R$149 de preço, R$13 de contribuição no cenário de estresse e quarenta horas de esforço estavam associados ao produto anterior. Não são estimativas desta nova versão. Recalcular custos e definir quantidade de formatos/revisões antes de propor uma oferta. Nenhum pagamento, economia, receita adicional ou benefício do cliente foi observado.

## Preparação da apresentação

- [ ] Ensaiar os blocos de fala e permanecer abaixo de cinco minutos.
- [ ] Confirmar resultado mínimo e extensão de arquivo de cada formato.
- [x] Registrar a decisão do autor: conteúdo gerado dentro da ferramenta, usando internamente o contexto da oficina e o prompt + skill do formato.
- [ ] Completar as tasks específicas do catálogo com evidência, sem confundir features com tasks.
- [ ] Confirmar responsabilidades do grupo e registrar o link na planilha da disciplina.

Método comercial: [Revenue-Centric Design, Richard (@richardrx)](https://github.com/heliocosta-dev/revenue-centric-design/tree/1942760c2242f609bf63ce2c97204f5a1791bd68); [termos completos aplicáveis](experimentos/2026-10-19-sorteio-rcd/RCD-LICENSE.txt).
