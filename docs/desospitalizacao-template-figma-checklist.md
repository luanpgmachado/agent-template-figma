# Checklist Operacional - Template Figma de Desospitalizacao

## Objetivo

Executar a montagem do template `Dashboard / Desospitalizacao / Default` em blocos curtos, com pontos claros de parada, validacao e retomada.

Referencias:

- `docs/desospitalizacao-template-figma-blueprint.md`
- `docs/desospitalizacao-template-figma.md`

## Legenda

- `[x]` concluido no repositorio ou validado nesta sessao
- `[~]` em andamento ou pronto para execucao imediata
- `[ ]` depende de execucao manual no Figma

## Modo de execucao intermitente

Trabalhar por ciclos curtos, nesta ordem:

1. concluir uma fase inteira
2. validar o criterio de aceite da fase
3. parar em um ponto seguro
4. retomar da proxima fase sem reestruturar o que ja foi montado

Pontos de parada recomendados:

- apos foundations
- apos shell + header
- apos linha de KPIs
- apos paineis principais
- apos tabela
- apos validacao do frame `Clean`

## Fase 0 - Preparacao documental

- [x] Alinhar o blueprint com `Shell / App` e `Sidebar / Institutional`
- [x] Alinhar o documento-base com grid, auto layout e regras de conteudo estrutural
- [x] Consolidar a hierarquia do frame principal
- [x] Consolidar a lista de componentes necessarios
- [x] Consolidar regras do que pode e do que nao pode ser preenchido

Criterio de aceite:

- blueprint e documento-base descrevem a mesma estrutura
- nao restam larguras absolutas herdadas do layout antigo
- `Main / Content` esta explicitamente documentado

## Fase 1 - Preparacao do arquivo Figma

- [ ] Criar as paginas `00 Cover`, `01 Foundations`, `02 Components`, `03 Templates`
- [ ] Criar o frame `Dashboard / Desospitalizacao / Default` em `1280 x 720`
- [ ] Duplicar o frame-base somente ao final da montagem, para gerar `Dashboard / Desospitalizacao / Clean`

Criterio de aceite:

- as 4 paginas existem com a nomenclatura definida
- o frame principal foi criado no local correto
- ainda nao ha conteudo ficticio inserido

## Fase 2 - Foundations

- [ ] Registrar `Colors`
- [ ] Registrar `Typography`
- [ ] Registrar `Spacing`
- [ ] Registrar `Radii`
- [ ] Registrar `Strokes`
- [ ] Registrar `Effects`

Criterio de aceite:

- todos os tokens minimos do blueprint existem
- as cores e estilos usados nos componentes partem dessas foundations

Ponto de parada:

- foundations publicadas e prontas para reutilizacao

## Fase 3 - Shell institucional

- [ ] Criar `Shell / App`
- [ ] Criar `Sidebar / Institutional`
- [ ] Configurar sidebar fixa com `232` px
- [ ] Configurar `Main / Content` com auto layout vertical, padding `16` e gap `10`
- [ ] Aplicar o grid de `12` colunas no content area

Criterio de aceite:

- a sidebar nao expande horizontalmente
- o content area ocupa o restante do frame
- o grid esta aplicado no content area, nao no frame inteiro
- a sidebar esta neutra, sem labels inventados, sem contadores e sem menu detalhado

Ponto de parada:

- shell validado sem nenhum bloco analitico ainda

## Fase 4 - Header

- [ ] Criar `Header / Institutional / Badge`
- [ ] Aplicar hierarquia titulo/subtitulo
- [ ] Aplicar badge estrutural no canto direito

Criterio de aceite:

- o header respeita a altura alvo
- a leitura institucional esta clara
- o badge nao contem data real nem texto operacional especifico

Ponto de parada:

- shell e header prontos para receber os blocos de conteudo

## Fase 5 - KPIs

- [ ] Criar `KPI / Card / Default`
- [ ] Publicar variants `Positive`, `Warning` e `Critical`
- [ ] Montar `KPI / Row / 4-up`
- [ ] Inserir as 4 instancias no frame principal

Criterio de aceite:

- os 4 cards escalam com `Fill container`
- nao existem numeros, series ou variacoes preenchidas
- labels de KPI permanecem vazias ou neutras no template final, salvo decisao editorial explicita posterior

Ponto de parada:

- linha de KPIs pronta e totalmente estrutural

## Fase 6 - Paineis principais

- [ ] Criar `Panel / Journey / Default`
- [ ] Criar `Chart / BarRow / Default`
- [ ] Criar `Metric / SupportCard / Default`
- [ ] Criar `Panel / Trend / Default`
- [ ] Criar `Chart / Line / MultiSeries`
- [ ] Criar `Metric / RiskNote / Default`
- [ ] Montar `Panels / Row / Main` com distribuicao `7/5`

Criterio de aceite:

- o painel esquerdo ocupa 7 colunas e o direito 5 colunas
- nao ha dados desenhados, apenas estrutura vazia ou neutra
- side metrics e risk notes funcionam como componentes reutilizaveis

Ponto de parada:

- paineis principais prontos sem tabela

## Fase 7 - Tabela estrutural

- [ ] Criar `Panel / Table / Default`
- [ ] Criar `Table / Header / Default`
- [ ] Criar `Table / Row / PatientPriority`
- [ ] Criar `Badge / Risk` como component set
- [ ] Criar `Divider / Soft`
- [ ] Inserir o painel de tabela no frame principal

Criterio de aceite:

- colunas respeitam a proporcao definida no blueprint
- linhas permanecem vazias ou neutras
- badges nao representam casos reais

Ponto de parada:

- frame `Default` completo

## Fase 8 - Clean

- [ ] Duplicar `Dashboard / Desospitalizacao / Default`
- [ ] Renomear a copia para `Dashboard / Desospitalizacao / Clean`
- [ ] Remover notas auxiliares
- [ ] Remover indicacoes temporarias de montagem
- [ ] Confirmar que apenas a estrutura reutilizavel permaneceu

Criterio de aceite:

- o frame `Clean` nao possui notas, instrucoes, marcadores ou guias textuais de montagem
- o frame `Clean` mantem apenas estrutura, estilos e componentes reutilizaveis

## Fase 9 - Validacao final

- [ ] Verificar se nao ha nomes de pacientes
- [ ] Verificar se nao ha unidades especificas
- [ ] Verificar se nao ha datas reais
- [ ] Verificar se nao ha KPIs numericos preenchidos
- [ ] Verificar se nao ha series mensais desenhadas
- [ ] Verificar se a sidebar continua neutra
- [ ] Verificar se a hierarquia bate com o blueprint
- [ ] Verificar se todos os blocos principais usam auto layout

Criterio de aceite:

- o template pode ser duplicado sem limpeza adicional
- a leitura continua institucional, sobria e hospitalar
- nenhum bloco depende de conteudo ficticio para funcionar visualmente

## Status desta sessao

- [x] Documentacao-base alinhada
- [x] Blueprint ajustado para shell com sidebar
- [x] Checklist operacional criado
- [~] Execucao pronta para comecar no Figma a partir da `Fase 1`
