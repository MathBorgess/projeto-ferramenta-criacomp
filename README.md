# Projeto Ferramenta - Criatividade Computacional

**Direção atual: Oficina em Prancha**, experiência para construir a narrativa de uma palestra/oficina vendo imagens, formas e cores. O contexto fica guardado numa skill interna e pode alimentar diferentes saídas, como pitch deck, LinkedIn e Instagram, por prompts e skills de formato. Consulte o [escopo atualizado em 20/10](docs/escopo-oficina-narrativa.md), o [pitch de até cinco minutos](docs/pitch-oficina-em-prancha.md) e a [seleção original com três agentes Luna e um crítico](docs/experimentos/2026-10-19-sorteio-rcd/README.md). O produto ainda não foi implementado.

A primeira exploração partiu destas três ideias de ferramenta:

1. **EscapeRoom AI:** criar uma sequência jogável de enigmas.
2. **RoteiroLab:** criar roteiros curtos com ganchos alternativos e blocos cronometrados.
3. **Arena Visual:** criar rascunhos visuais em uma lousa compartilhada com um agente.

Este repositório é um fork público de [text-to-morphbox, de Filipe Calegario](https://github.com/filipecalegario/text-to-morphbox). O gerador Python original foi preservado e executado com os dados deste projeto.

## Revisar a caixa

![Caixa morfológica com 11 dimensões](output/pdf/caixa-morfologica.png)

- [Caixa morfológica em PDF](output/pdf/caixa-morfologica.pdf)
- [Três ideias no mesmo formato](docs/ideias.md)
- [PF0: processo e os três caminhos](docs/pf0-caixa-e-caminhos.md)
- [Requisitos e entregas essenciais de PF0 e PF1](docs/requisitos-e-entregas.md)
- [PF1: preparação para a escolha e o pitch](docs/pf1-preparacao.md)
- [Registro de processo e reprodução](docs/processo.md)
- [Sorteio de três caminhos e avaliação comercial com agentes](docs/experimentos/2026-10-19-sorteio-rcd/README.md)
- [Pitch da Oficina em Prancha](docs/pitch-oficina-em-prancha.md)
- [Escopo atual: narrativa visual, skill interna e múltiplas saídas](docs/escopo-oficina-narrativa.md)

**Escolha do caminho:** Matheus primeiro decidiu revisar a caixa antes de escolher. Depois solicitou três combinações aleatórias, três propostas Luna em paralelo e uma seleção por um quarto agente. Essa rodada selecionou **Oficina em Prancha como candidata à validação paga**. Implementação e retorno financeiro ainda não foram demonstrados.

**Mudança de direção em 20/10/2026:** depois da seleção, o autor ampliou a entrega de uma prancha PNG para uma base narrativa e visual reutilizável por vários formatos. Isso altera o escopo original; não representa uma nova execução do sorteio. Preço, custos e esforço anteriores precisam ser reestimados. A skill interna de cada oficina pertence ao produto; a skill genérica de exploração no skills-catalog tem outra função.

PF0 e PF1 têm prazo em **20/10/2026**, conforme os enunciados consultados em 19/10. O documento atual do pitch segue o limite de **cinco minutos**, reiterado por Matheus; a divergência com a menção de três minutos no lançamento permanece registrada nas fontes.

## Gerar novamente

Requer Python 3 e ReportLab. Uma instalação isolada:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
PYTHON=.venv/bin/python bash scripts/gerar-caixa.sh
```

O script executa `python/text_to_morph.py` a partir de `python/`, onde o programa espera encontrar `input.txt`. A saída nativa é `python/output.pdf`; a cópia para entrega fica em `output/pdf/caixa-morfologica.pdf`. Se Poppler estiver instalado, a prévia PNG também é atualizada.

O formato de entrada original continua sendo uma categoria por linha e alternativas separadas por vírgula:

```text
Categoria: Alternativa A, Alternativa B, Alternativa C
```

As escolhas de cada caminho estão em [data/caminhos.json](data/caminhos.json). Edite esse arquivo junto com `python/input.txt` ao revisar a caixa e depois rode:

```bash
PYTHON=.venv/bin/python bash scripts/gerar-caixa.sh
.venv/bin/python scripts/validar-caixa.py
```

O repositório executa a geração da caixa em PDF e o sorteio auditável de caminhos. As ferramentas de criação descritas nos documentos são conceitos para avaliação. A implementação Java e os exemplos herdados do upstream também foram preservados.

## Sortear três novos caminhos

O sorteio usa somente a biblioteca padrão do Python, lê a mesma caixa e escolhe uma posição de 1 a 4 por linha:

```bash
python3 scripts/sortear-caminhos.py --output meu-sorteio.json
```

O JSON guarda seed, opções, escolhas e tentativas. Como "Papel da IA" tem três opções, o número 4 é descartado nessa linha e a tentativa é registrada. Sequências inteiras repetidas também são registradas e sorteadas novamente; nenhuma combinação é filtrada por parecer boa ou ruim.

Para repetir as escolhas desta rodada, use um arquivo de saída novo:

```bash
python3 scripts/sortear-caminhos.py --seed 14532109174761975832 --output repeticao.json
python3 -m unittest discover -s tests -v
```

O script sorteia e registra os caminhos. Nesta rodada, os agentes foram acionados em paralelo pelo orquestrador Codex; executar o script sozinho não chama modelos nem inicia cobrança.
