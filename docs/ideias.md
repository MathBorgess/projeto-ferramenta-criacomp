# Três ideias de ferramenta

Data: 19/10/2026. EscapeRoom AI e a proposta de roteiros foram fornecidas por Matheus. O nome **RoteiroLab** é uma sugestão de trabalho. **Arena Visual** completa a terceira ideia a partir da Arena de Matheus e do pedido de uma lousa de rascunho generativo. As descrições são propostas, sem alegação de implementação ou validação com usuários.

## 1. EscapeRoom AI - Criador de salas de enigmas

**Proposta:** uma ferramenta para professores, estudantes e entusiastas de jogos criarem salas de enigmas interativas. A IA sugere desafios, pistas e soluções de acordo com o tema, o público e a dificuldade desejados.

**Como funciona:** o usuário escolhe um tema, como investigação policial ou mistério em uma escola, e define para quem é a experiência. A IA propõe enigmas que podem ser editados e organizados em uma sequência jogável.

**Controle:** o usuário seleciona os enigmas, modifica enunciados e pistas, define a dificuldade, corrige soluções e estabelece a ordem dos desafios.

**Revisão e comparação:** a ferramenta aponta possíveis ambiguidades, dependências entre pistas e diferenças de dificuldade. O usuário compara dois percursos e testa se outra pessoa consegue resolver a sala. A análise da IA é uma indicação a conferir; a clareza das soluções precisa de teste humano.

**Tipo:** híbrida.

**Diferencial proposto:** reunir criação, revisão e teste de uma sequência de enigmas em um fluxo acessível a quem não desenvolve jogos gráficos. A utilidade desse fluxo ainda precisa ser comparada às ferramentas existentes.

**O que outra pessoa cria:** uma pequena sala temática com início, sequência de desafios, pistas e encerramento.

**Recorte mínimo sugerido:** uma sala textual de três enigmas, editor da sequência e modo de jogar. Gráficos elaborados e partidas simultâneas ficam para depois da validação desse ciclo.

## 2. RoteiroLab - Roteiros curtos e campanhas

**Proposta:** uma ferramenta para criadores de conteúdo e profissionais de marketing criarem roteiros de vídeos curtos e peças de lançamento. A IA sugere abordagens de narrativa, ganchos e organização dos blocos conforme o público, o tom e a plataforma.

**Como funciona:** o usuário insere uma ideia solta, um resumo ou uma dor do público, define tom de voz, plataforma e duração desejada. A IA oferece ganchos alternativos e estrutura o roteiro em blocos com tempo estimado de fala.

**Controle:** o usuário reescreve frases, fixa ganchos e blocos favoritos, altera a ordem da narrativa, ajusta o ritmo de leitura e aceita ou rejeita cada sugestão.

**Revisão e comparação:** o usuário abre ramificações do mesmo roteiro, compara ganchos lado a lado e ensaia a leitura com um cronômetro. A estimativa inicial de duração deve poder ser ajustada ao ritmo real da pessoa.

**Tipo:** híbrida.

**Diferencial proposto:** trabalhar a estrutura temporal do roteiro junto com a comparação de ganchos, mantendo o controle editorial de quem vai gravar.

**O que outra pessoa cria:** um roteiro de vídeo curto pronto para ensaio, com alternativas de abertura e blocos organizados por tempo.

**Recorte mínimo sugerido:** roteiro de até 60 segundos, três ganchos, editor de blocos, travas e estimativa de leitura. Analisar tendências reais de engajamento exige definir fontes e acesso a dados. Enquanto isso não existir, sugestões sobre retenção são hipóteses editoriais; não garantem desempenho.

## 3. Arena Visual - Lousa de rascunho generativo

**Proposta:** uma interface de rascunho generativo para estudantes, designers iniciantes e pessoas que pensam desenhando. A pessoa conversa com seu agente no ChatGPT ou Claude e usa uma lousa para desenhar, anotar e apontar o que quer explorar. O agente desenha de volta, propõe cores, renderizações e caminhos visuais.

**Como funciona:** o usuário abre uma lousa, faz um rabisco e explica sua intenção pela conversa. O agente interpreta o desenho e propõe uma continuação, uma composição ou uma renderização como alternativa. A pessoa edita por cima, seleciona uma região, pede uma nova variação e continua o rascunho. A integração com cada cliente depende dos recursos que ele oferecer e precisa ser verificada em um protótipo.

**Controle:** o usuário mantém seus traços, desfaz alterações, trava regiões, define o que a IA pode transformar e escolhe quais propostas entram na composição. Pode editar desenho e instruções diretamente; suas mudanças passam a integrar o contexto da próxima proposta.

**Revisão e comparação:** a ferramenta preserva o original e permite ramificar a mesma intenção em alternativas lado a lado. O usuário compara composição, cores e fidelidade à intenção, mistura partes escolhidas e pode voltar a uma versão anterior. As observações do agente ajudam a revisão; a decisão visual continua com a pessoa.

**Tipo:** híbrida.

**Diferencial proposto:** levar a lógica da Arena de Matheus - rascunho editável, contexto persistente, propostas e comparação de versões - para o desenho. A lousa funciona como parte da conversa com o agente, e cada intervenção humana orienta a próxima rodada.

**O que outra pessoa cria:** uma prancha visual que evolui de rabiscos e anotações para uma composição escolhida, com alternativas preservadas.

**Recorte mínimo sugerido:** uma lousa 2D, texto de intenção, uma operação de geração a partir do desenho, duas alternativas preservadas e exportação PNG. Uma primeira integração com um único cliente reduz o escopo; múltiplos clientes e renderização contínua exigem validação posterior.

### Relação com a Arena existente

A [Arena pública de Matheus](https://github.com/MathBorgess/arena) documenta um fluxo editorial com texto, propostas, versões, fontes e ramificações. Seu README delimita a v1 a texto revisado e exportado. Desenho, pintura e renderização são a extensão proposta neste projeto; esta descrição não afirma que esses recursos já existam no MCP.
