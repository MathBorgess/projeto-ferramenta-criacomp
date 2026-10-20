# Registro do processo

Data: 19/10/2026. Responsável pela direção e pelas ideias de partida: Matheus. Organização e execução: agente Codex com revisão humana pendente.

## O que foi pedido

Criar um fork público de text-to-morphbox para o Projeto Ferramenta; levantar PF0 e PF1 no e-mail institucional; organizar requisitos e entregas; estruturar EscapeRoom AI, a ferramenta de roteiros e uma terceira ideia baseada na Arena de Matheus; gerar a caixa morfológica.

Direção da terceira ideia, fornecida por Matheus:

> Interface de rascunho generativo. Você abre o ChatGPT, Claude, possui uma lousa e pode desenhar para seu agente. Ele desenha de volta, pinta, renderiza, sugere

Durante a execução, Matheus esclareceu que a referência era sua Arena como produto. A proposta visual foi estruturada a partir dessa direção e do README público da Arena. Matheus também decidiu escolher o caminho somente depois de revisar a caixa.

## O que foi usado

- [text-to-morphbox](https://github.com/filipecalegario/text-to-morphbox), commit de origem `64e1081f6d5ae4376eb1a1d00b96fa3e89a00165`.
- `python/text_to_morph.py` original, sem mudança de lógica.
- ReportLab 4.4.9, dependência fixada em `requirements.txt`.
- Python 3.12.14 e Poppler para gerar o PDF e sua prévia.
- Enunciados de PF0 e PF1, lembretes de 19/10 e lançamento do projeto; conteúdo privado preservado fora do repositório público.
- README público da Arena e páginas oficiais de similares, com links em [PF1](pf1-preparacao.md).

## O que foi preparado

Três descrições comparáveis; uma caixa com 11 dimensões; três combinações explícitas; requisitos, marcos e pendências de PF0/PF1; entrada editável e instruções de reprodução.

O validador verifica o mínimo de categorias, a existência de três caminhos distintos e completos, a correspondência das escolhas às alternativas e a largura das legendas para o gerador original. São verificações estruturais. Não medem qualidade criativa, utilidade ou aceitação acadêmica.

O script de geração executou o programa original com sucesso. A conferência de conteúdo encontrou as 54 legendas esperadas (11 categorias e 43 alternativas) em uma página A4 horizontal. A saída nativa e o PDF de entrega são idênticos. A prévia PNG foi inspecionada: textos legíveis e dentro das células.

```text
Validação: 11 categorias; 3 caminhos completos e distintos; textos cabem nas células.
SHA256 do gerador original: 8e9db550109b4bb0bab12cb8c357a3b82963a0c53108e47b1f8eab400c1a9b2d
SHA256 da entrada: 0f16e52804a38a6c38bdd38e20bb272bc576aa35401c523359912bc28361dbbf
SHA256 do PDF desta execução: a5bd45b4aac7521099080f4428dc0de69e9ee9e287ce16302b998e7babaed02c
```

O ReportLab inclui data de criação no PDF; uma nova execução pode produzir outro hash mesmo com a mesma entrada. Os hashes acima identificam esta execução.

## O que permanece aberto

- Avaliação da caixa e escolha humana de uma ideia.
- Relação e divergência das propostas em relação ao Autoral.
- Uso real de similares, suas tasks e a diferença que vale desenvolver.
- Prototipação da ferramenta escolhida e observação de outra pessoa criando com ela.
- Apresentação, link na planilha de grupos e entrega no Classroom.

As três ferramentas não foram implementadas nesta etapa. A hipótese de benefício de cada uma permanece sem resultado observado.

## Rodada posterior de sorteio e seleção

Matheus solicitou três combinações aleatórias da caixa, três agentes Luna em paralelo e um quarto agente como advogado do diabo, aplicando Revenue-Centric Design. A [rodada completa](experimentos/2026-10-19-sorteio-rcd/README.md) preserva seed, escolhas, tentativas, prompts integrais, propostas e parecer.

O crítico selecionou Oficina em Prancha para validação paga; nenhuma proposta justificou investimento com a evidência disponível. Em seguida, por novo pedido de Matheus, foi preparado o [documento do pitch](pitch-oficina-em-prancha.md), com limite de cinco minutos, tecnologias propostas e cronograma. As tasks do There's An AI For That aguardam rótulos e links do usuário, porque o navegador bloqueou o acesso ao domínio por sua política de segurança. Essa lacuna não foi preenchida por suposição.

**Complemento em 19/10/2026:** Matheus enviou as descrições de Miro AI e Canva AI e dez links classificados como **Supported features**. Os [rótulos recebidos](referencias/2026-10-19-taaft-miro-canva.md) foram incorporados ao pitch, sem convertê-los em tasks. A comparação foi ajustada após consultar as páginas oficiais: Miro já documenta planos editáveis de oficina e Canva já oferece criação, edição e exportação visual. O diferencial passou a explicitar a hipótese de utilidade do fluxo, a verificar por tempo, retrabalho, preservação dos blocos e disposição a pagar. Não houve teste dos produtos, validação comercial ou nova geração das propostas dos agentes.
