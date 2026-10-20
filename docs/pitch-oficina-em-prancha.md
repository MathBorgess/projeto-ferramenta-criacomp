# Pitch Oficina em Prancha

**Projeto Ferramenta | PF1 | duração máxima de cinco minutos.** Ideia selecionada na [rodada morfológica com três agentes Luna e um crítico](experimentos/2026-10-19-sorteio-rcd/README.md). O produto é uma proposta; o MVP e a validação comercial ainda serão realizados.

Apresentar somente o roteiro falado. Os quadros de apoio ficam para perguntas e preparação. Os tempos são metas para ensaio; reservar os últimos vinte segundos para pausas. O limite de cinco minutos segue a orientação mais recente de Matheus nesta conversa.

O roteiro tem **527 palavras**. A 120 palavras por minuto, a estimativa textual é de cerca de **4min24s**, antes das pausas. A duração real depende do ensaio com cronômetro.

## Roteiro falado

### 0:00 a 0:40 O que queremos criar e para quem

<!-- fala:inicio -->
Quem vende oficinas precisa preparar uma experiência que faça sentido para cada público. Nossa proposta é a Oficina em Prancha: uma ferramenta com IA para facilitadores independentes criarem um roteiro curto e transformá-lo em uma prancha visual. O foco inicial é quem já tem uma oficina contratada e precisa preparar seu material. Queremos ajudar essa pessoa a experimentar aberturas, organizar instruções e escolher uma apresentação visual, mantendo sua voz. O resultado será um material criado pelo próprio facilitador, pronto para apoiar a condução da atividade.
<!-- fala:fim -->

### 0:40 a 1:30 Como a pessoa vai interagir

<!-- fala:inicio -->
Imagine uma oficina de ideação para pequenos empreendedores. O facilitador informa a ideia e o público e escreve seus blocos de abertura, atividade e fechamento. A IA sugere formas e cores para organizar esse conteúdo. A pessoa seleciona uma região, conversa sobre o que quer mudar e compara dois ganchos lado a lado. Pode misturar alternativas e editar o texto sem perder os blocos anteriores. Antes de exportar, recebe alertas de contraste e legibilidade. Ao final, baixa uma prancha PNG. A IA propõe; o facilitador decide o que entra na oficina.
<!-- fala:fim -->

### 1:30 a 2:10 Qual benefício pode sustentar a cobrança

<!-- fala:inicio -->
Nossa hipótese comercial é cobrar cento e quarenta e nove reais por uma prancha para uma oficina. O comprador seria o facilitador que já recebe pela atividade e reconhece valor no preparo do material. Esse preço ainda precisa ser testado. Um cenário hipotético de estresse, incluindo trabalho e aquisição do cliente, deixa apenas treze reais por venda antes de impostos. Por isso, não estamos apresentando um negócio validado. Precisamos observar se alguém paga, consegue criar sem ajuda e recebe um benefício que justifique o preço.
<!-- fala:fim -->

### 2:10 a 2:55 O que já existe e onde queremos diferenciar

<!-- fala:inicio -->
Miro já combina criação com IA e quadros colaborativos, inclusive para preparar oficinas. Canva permite gerar materiais visuais e refiná-los com controle humano. Nossa hipótese é que um fluxo dedicado à oficina ajude a preservar blocos, comparar ganchos e combinar escolhas visuais antes da exportação. Vamos compará-lo com Miro ou Canva usando o mesmo conteúdo e medir tempo, retrabalho e preservação. A revisão de acessibilidade será uma triagem; um PNG não garante acesso por leitores de tela nem conformidade completa.
<!-- fala:fim -->

### 2:55 a 3:45 Quais tecnologias planejamos usar

<!-- fala:inicio -->
Planejamos uma interface web em React e TypeScript, com Vite. Uma API Python com FastAPI vai organizar os pedidos e validar as respostas do modelo. A IA entra durante o uso, propondo formas, cores e variações a partir do conteúdo selecionado. Começaremos com um modelo de texto acessado por API, sem treinar modelo próprio. A composição visual usará elementos simples, e o navegador fará a exportação PNG. SQLite poderá guardar rascunhos e versões. No primeiro protótipo, queremos um único fluxo que funcione de ponta a ponta.
<!-- fala:fim -->

### 3:45 a 4:40 Por que cabe no projeto e como vamos verificar

<!-- fala:inicio -->
Até vinte e sete de outubro, queremos fechar o protótipo de baixa fidelidade e a arquitetura. Até dez de novembro, completar criação, comparação e exportação. Em doze de novembro, outra pessoa deverá usar a ferramenta sem explicação por cima do ombro. O congelamento será em dezessete de novembro. Escolhemos essa ideia porque seu escopo estático parece mais viável que uma sala jogável, enquanto o público está ligado a uma atividade remunerada. O teste comercial proposto é obter três pagamentos entre dez ofertas qualificadas e medir todos os custos. Se o valor não aparecer, teremos motivo concreto para rever a proposta.
<!-- fala:fim -->

## Apoio para responder às seis perguntas

| Pergunta de PF1 | Resposta no projeto |
| --- | --- |
| O que é, para que serve e como funciona? | Ferramenta híbrida para criar roteiro curto e prancha visual de uma oficina, com sugestões de IA e decisões do facilitador. |
| Quem usa e como se beneficia? | Facilitadores independentes com oficinas contratadas; hipótese de reduzir montagem e retrabalho. Benefício será medido, sem presumir receita adicional. |
| Como interage? | Ideia e público → blocos → selecionar e conversar → comparar ganchos → misturar alternativas → revisar → exportar PNG. |
| Quais similares e tasks? | Miro AI e Canva, com fontes oficiais e links de Supported features do There's An AI For That fornecidos por Matheus. O material recebido não identifica uma task específica; ver a distinção abaixo. |
| Quais ferramentas e tecnologias? | React, TypeScript, Vite, FastAPI/Pydantic, SQLite, API de modelo textual e exportação PNG no navegador; escolhas de planejamento, sem instalação nesta etapa. |
| Viabilidade e cronograma? | Uma pessoa cria uma prancha por vez; composição por formas e texto; sem treino de modelo, editor genérico ou colaboração simultânea no MVP. Marcos de 27/10 a 26/11 abaixo. |

## Similares e referências do catálogo

Fontes oficiais consultadas em 19/10/2026 e rótulos do catálogo fornecidos por Matheus na mesma data. A comparação descreve capacidades documentadas; nenhum teste de uso dos produtos foi realizado nesta rodada.

| Produto | Capacidade documentada semelhante | Diferença a testar na Oficina em Prancha | Supported features recebidas do There's An AI For That |
| --- | --- | --- | --- |
| [Miro AI](https://help.miro.com/hc/en-us/articles/36650745968914-Miro-AI-board-layout-with-Sidekicks-and-Flows) | Gera quadros estruturados e editáveis por instruções; a documentação inclui planos de oficina | Preservação dos blocos, comparação de ganchos e composição em um fluxo dedicado; utilidade adicional ainda não demonstrada | [Team Collaboration](https://theresanaiforthat.com/feature/team-collaboration/), [Visual Creation](https://theresanaiforthat.com/feature/visual-creation/) e [Image Generation](https://theresanaiforthat.com/feature/imagegen/); demais rótulos no registro abaixo |
| Canva AI no texto recebido; [Magic Design](https://www.canva.com/magic-design/) como destino informado | A página oficial do Magic Design descreve geração por instruções, personalização no editor e exportação PNG | Comparar aberturas e preservar blocos durante o preparo da oficina; criação visual e controle humano já são capacidades das alternativas | [Integrations](https://theresanaiforthat.com/feature/integrations/), [SynthID](https://theresanaiforthat.com/feature/synthid/), [Outpainting](https://theresanaiforthat.com/feature/outpainting/) e [Inpainting](https://theresanaiforthat.com/feature/inpainting/), associados a Canva AI no trecho recebido |

O [registro das referências recebidas](referencias/2026-10-19-taaft-miro-canva.md) preserva os dez rótulos e seus links. O material usa **Supported features**, sem indicar uma task específica ou a URL da ficha de cada produto no catálogo. O acesso direto ao domínio foi bloqueado pelo navegador; os links de features têm como fonte a mensagem de Matheus. Essa distinção mantém visível o limite em relação ao pedido de tasks de PF1. As afirmações antigas sobre beta ou gratuidade do Miro não foram usadas como informação atual.

A diferenciação será comparada com o mesmo conteúdo em Miro ou Canva, usando também um modelo de linguagem quando fizer parte do fluxo habitual da pessoa. Medir tempo até uma prancha útil, retrabalho e preservação dos blocos; depois verificar se a vantagem percebida justifica o preço. Nenhuma dessas vantagens foi observada nesta rodada.

## Tecnologias e fronteiras do MVP

| Parte | Plano | Verificação necessária |
| --- | --- | --- |
| Interface | React e TypeScript com [Vite](https://vite.dev/guide/); formulário, blocos e comparação | Uma pessoa completar o fluxo sem explicação externa |
| API | [FastAPI](https://fastapi.tiangolo.com/) e validação com Pydantic | Rejeitar resposta inválida e preservar o rascunho |
| IA no produto | Um modelo textual por API; [OpenRouter](https://openrouter.ai/docs/quickstart) é o adaptador candidato | Escolher modelo, medir custo/latência e explicar o acesso à chave na própria interface; sem contratação nesta etapa |
| Composição | Formas, texto e paletas em SVG/Canvas; sugestões da IA viram parâmetros editáveis | Mistura de alternativas sem apagar texto ou blocos preservados |
| Saída | PNG pelo [Canvas do navegador](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toBlob) | Imagem exportada corresponder à versão escolhida |
| Estado | SQLite para rascunhos e versões; chaves fora dos dados versionados | Recuperar rascunho e não sobrescrever trabalho manual |
| Revisão | Regras de contraste/legibilidade e avisos textuais | Triagem visual, sem certificação ou garantia de acessibilidade integral; [referência W3C](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) |

Esses componentes ainda não foram implementados. O repositório contém atualmente o gerador de caixa, o sorteio e os documentos de exploração.

## Conta comercial e critério de validação

Uma unidade proposta é um roteiro curto com prancha PNG para uma oficina. Todas as cifras são hipóteses de planejamento; nenhuma venda, custo operacional ou economia do cliente foi observado.

| Item por venda | Cenário de estresse do crítico |
| --- | ---: |
| Preço hipotético | R$149 |
| IA, infraestrutura e pagamento | R$11 |
| Operação e suporte: 45 min a R$60/h | R$45 |
| Aquisição: 4 h a R$60/h para 3 compradores | R$80 |
| Contribuição antes de impostos e demais custos omitidos | **R$13** |

Desenvolvimento imputado: R$2.400; recuperação nesse cenário: **185 vendas**, sem despesas adicionais. Mais quinze minutos de trabalho por venda tornam a contribuição negativa. Portanto, há uma oferta cobrável definida e uma conta auditável, mas retorno financeiro ainda precisa ser demonstrado.

Benefício econômico do cliente = gasto efetivamente evitado + horas reaproveitáveis × valor/hora − preço − custo da revisão, sem contar duas vezes a mesma economia. O tempo poupado só vira entrada de caixa se houver capacidade efetivamente vendida ou despesa evitada.

Teste futuro proposto: um canal de facilitadores com acesso confirmado, dez ofertas qualificadas, até quatro horas comerciais, três pagamentos integrais, exportação autônoma e contribuição **medida de pelo menos R$15 por venda após todos os custos**. Sem pagamento ou com contribuição não positiva, interromper a oferta. Um ou dois pagamentos serão inconclusivos. O teste não foi iniciado.

## Cronograma de desenvolvimento

| Marco | Entrega proposta | Critério de conclusão |
| --- | --- | --- |
| 20/10 | Pitch e recorte do projeto | Explicar produto, público, fluxo, similares, tecnologias e plano |
| 27/10 | Baixa fidelidade e arquitetura | Caminho do usuário representado e dependência do modelo escolhida para ensaio |
| 28/10 a 09/11 | Implementação do ciclo mínimo | Entrada, sugestão da IA, edição, comparação, revisão e PNG integrados |
| 10/11 | Ponta a ponta | Uma criação completa exportada com modelo em ação |
| 12/11 | Uso por outro grupo | Pessoa concluir sem explicação por cima do ombro; dificuldades registradas |
| 13 a 16/11 | Correções do ciclo central | Impedimentos de uso corrigidos e custos medidos |
| 17/11 | Congelamento | Versão reproduzível, instruções na interface e acesso ao modelo explicado |
| 26/11 | Avaliação cruzada e post-mortem | Versão acessível e relato do processo, resultados e limites |

As quarenta horas estimadas pelo proponente são uma hipótese para o escopo mínimo. Disponibilidade e divisão de trabalho do grupo ainda precisam ser definidas. A primeira revisão de viabilidade deve verificar preservação dos blocos, custo das sugestões e qualidade do PNG.

## Ensaio e fechamento da entrega

- [ ] Ensaiar apenas o roteiro falado com cronômetro e ficar abaixo de cinco minutos.
- [x] Registrar os dez rótulos e links de Supported features fornecidos por Matheus, mantendo explícita a diferença em relação a tasks.
- [ ] Identificar a task específica associada a cada similar; os trechos recebidos trazem features, sem esse campo.
- [ ] Confirmar responsabilidades e o recorte que o grupo pretende desenvolver.
- [ ] Se houver demonstração em baixa fidelidade, identificá-la como simulação.
- [ ] Colocar o link da apresentação na planilha de Definição de Grupos.

Seleção e raciocínio comercial: [parecer do advogado do diabo](experimentos/2026-10-19-sorteio-rcd/selecao-advogado-do-diabo.md). Método: [Revenue-Centric Design, de Richard (@richardrx), curadoria heliocosta-dev](https://github.com/heliocosta-dev/revenue-centric-design/tree/1942760c2242f609bf63ce2c97204f5a1791bd68); [termos de uso do material RCD e suas adaptações nesta rodada](experimentos/2026-10-19-sorteio-rcd/RCD-LICENSE.txt).
