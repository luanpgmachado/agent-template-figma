# Blueprint Figma - Dashboard Operacional de Desospitalizacao com Sidebar

## Escopo

Blueprint de construcao para o template `Dashboard / Desospitalizacao / Default`, derivado do mockup HTML e do roteiro `desospitalizacao-template-figma.md`.
Este documento orienta apenas o layout estrutural, sem preenchimento de dados ficticios, sem placeholders textuais e sem copia do visual de referencia.

Direcao adotada:

- template operacional, nao promocional
- leitura em poucos segundos
- composicao institucional de saude
- blocos 100% reutilizaveis em outros temas assistenciais
- shell com sidebar institucional fixa e area principal em grid rigido

## Estrutura de paginas

Criar as paginas do arquivo nesta ordem:

1. `00 Cover`
2. `01 Foundations`
3. `02 Components`
4. `03 Templates`

### 00 Cover

Objetivo: capa de navegacao do arquivo.

Blocos:

- `Cover / Title`
- `Cover / Metadata`
- `Cover / Preview`

Conteudo fixo:

- nome do sistema de templates
- subtitulo `Dashboard Operacional`
- observacao curta sobre reutilizacao assistencial

Conteudo estrutural:

- miniatura vazia ou frame de referencia
- autor, data e versao como metadados opcionais

### 01 Foundations

Secoes minimas:

- `Colors`
- `Typography`
- `Spacing`
- `Radii`
- `Strokes`
- `Effects`

### 02 Components

Agrupar os componentes por families:

- `Shell`
- `Sidebar`
- `Header`
- `KPI`
- `Panel`
- `Chart`
- `Metric`
- `Table`
- `Badge`
- `Divider`

### 03 Templates

Frames recomendados:

- `Dashboard / Desospitalizacao / Default`
- `Dashboard / Desospitalizacao / Clean`

`Default` contem apenas a estrutura visual principal.

`Clean` e a copia pronta para uso sem notas auxiliares nem conteudos simulados.

## Foundations minimas

### Colors

Registrar como styles:

- `Green / 900` -> `#2F6F3C`
- `Green / 800` -> `#377F46`
- `Green / 700` -> `#4F8F57`
- `Green / 300` -> `#B7CFB4`
- `Green / 200` -> `#DBE7D8`
- `Ink / Default` -> `#243222`
- `Text / Muted` -> `#637161`
- `Surface / Base` -> `#FFFFFF`
- `Surface / Soft` -> `#F8FBF7`
- `Surface / Positive` -> `#F5FAF3`
- `Surface / Warning` -> `#FFF9EA`
- `Surface / Critical` -> `#FFF3EC`

### Typography

Registrar como text styles:

- `Title / Page` -> `22 / 110% / Semibold`
- `Title / Section` -> `13 / 120% / Bold`
- `Body / Small` -> `12 / 140% / Regular`
- `Body / XS` -> `11 / 140% / Regular`
- `Caption / Tiny` -> `10 / 140% / Regular`
- `Metric / KPI` -> `34 / 100% / Bold`
- `Metric / Support` -> `24 / 100% / Bold`
- `Metric / Note` -> `20 / 110% / Bold`

Fonte recomendada:

- `Segoe UI`
- fallback: `Arial` ou outra sans-serif de alta legibilidade

### Spacing

Tokens minimos:

- `Space / 4`
- `Space / 8`
- `Space / 10`
- `Space / 12`
- `Space / 16`
- `Space / 24`

### Radii

Tokens minimos:

- `Radius / 8`
- `Radius / 12`
- `Radius / Pill`

### Strokes

Tokens minimos:

- `Stroke / Subtle` -> `1px rgba(47, 111, 60, 0.12)`
- `Stroke / Strong` -> `2px #DBE7D8`

### Effects

Somente um efeito leve:

- `Shadow / Card / Soft` -> sombra curta e difusa, baixa opacidade

## Frame principal

### Configuracao base

- nome: `Dashboard / Desospitalizacao / Default`
- tamanho: `1280 x 720`
- fill: `Surface / Base`
- stroke: `rgba(44, 90, 38, 0.15)`
- layout grid: `12 columns` no content area
- margins: `16`
- gutter: `10`
- sidebar fixa: `232` px
- content area: `Fill container`

### Estrutura raiz

Usar esta hierarquia:

```text
Dashboard / Desospitalizacao / Default
  Shell / App
    Sidebar / Institutional
      Brand Area
      Navigation Slots
      Utility Footer
    Main / Content
      Header / Institutional / Badge
      KPI / Row / 4-up
        KPI / Card / Default
        KPI / Card / Positive
        KPI / Card / Warning
        KPI / Card / Critical
      Panels / Row / Main
        Panel / Journey / Default
        Panel / Trend / Default
      Panel / Table / Default
```

### Auto layout da raiz

- direcao: horizontal
- `Shell / App` com sidebar fixa e main expansivel
- padding externo: `0`
- gap: `0`
- width: `Fill container`
- height: fixed `720`

### Auto layout do conteudo principal

- `Main / Content`: vertical
- padding interno: `16`
- gap: `10`
- width: `Fill container`
- height: `Fill container`

## Hierarquia detalhada do frame principal

### 0. Shell e sidebar institucional

Componentes:

- `Shell / App`
- `Sidebar / Institutional`

Estrutura:

```text
Shell / App
  Sidebar / Institutional
    Brand Area
    Navigation Slots
    Utility Footer
  Main / Content
```

Config da sidebar:

- largura fixa: `232`
- auto layout vertical
- padding interno: `16`
- gap: `12`
- fill: `Surface / Soft`
- separacao visual discreta com stroke sutil

Fixo:

- zona de marca no topo
- slots de navegacao sem nomes operacionais ficticios
- rodape utilitario discreto

Conteudo estrutural:

- areas vazias ou neutras para brand, navegacao e utilitarios
- sem menu detalhado, sem contadores e sem labels inventados

### 1. Header institucional

Componente:

- `Header / Institutional / Badge`

Estrutura:

```text
Header / Institutional / Badge
  Header / Content
    Header / Copy
      Title
      Subtitle
    Badge / Update / Soft
```

Config:

- altura alvo: `73`
- auto layout horizontal
- align: `Space between`
- padding: `18 24 16 24`
- radius: `12`
- fill: gradiente `#298148 -> #518C57`
- texto branco

Fixo:

- estrutura do header
- estilo do badge
- hierarquia titulo/subtitulo

Conteudo variavel apenas se houver referencia editorial, sem simular dados clinicos ou operacionais.

### 2. Linha de KPIs

Container:

- `KPI / Row / 4-up`

Config do container:

- auto layout horizontal
- gap: `10`
- cada card: `Fill container`
- altura minima: `92`

Distribuicao:

- 4 cards em larguras iguais dentro do content area
- preferir proporcao por colunas ou `Fill container` sem largura absoluta

Componentes:

- `KPI / Card / Default`
- `KPI / Card / Positive`
- `KPI / Card / Warning`
- `KPI / Card / Critical`

Estrutura interna:

```text
KPI / Card / Variant
  KPI / Card / Header
    Label
  KPI / Card / Body
    Value
    KPI / SideMeta
      Meta
      Note
```

Config:

- padding: `12`
- radius: `12`
- stroke: `Stroke / Strong`
- auto layout horizontal
- align: `Space between`
- gap: `12`

Fixo:

- composicao label + bloco principal + coluna lateral
- comportamento das variantes

Conteudo estrutural:

- areas vazias para valor principal, meta e observacao curta
- sem numeros, sem simbolos de tendencia e sem preenchimento editorial

### 3. Linha principal de paineis

Container:

- `Panels / Row / Main`

Config do container:

- auto layout horizontal
- gap: `10`
- height minima: `270`

Distribuicao recomendada no grid:

- painel esquerdo: `7 colunas`
- painel direito: `5 colunas`

#### Painel esquerdo

Componente:

- `Panel / Journey / Default`

Estrutura:

```text
Panel / Journey / Default
  Panel / Heading
    Title
    Description
  Journey / Grid
    Journey / List
      Chart / BarRow / Default
      Chart / BarRow / Default
      Chart / BarRow / Default
      Chart / BarRow / Default
    Journey / SideMetrics
      Metric / SupportCard / Default
      Metric / SupportCard / Default
```

Config:

- auto layout vertical
- padding: `16`
- gap: `12`
- fill: `Surface / Soft`
- radius: `12`

Subgrid interna:

- `Journey / Grid` em horizontal
- gap: `12`
- `Journey / List` com `Fill container`
- `Journey / SideMetrics` com largura proporcional ao container ou faixa visual equivalente a 2-3 colunas

#### Painel direito

Componente:

- `Panel / Trend / Default`

Estrutura:

```text
Panel / Trend / Default
  Panel / Heading
    Title
    Description
  Chart / Line / MultiSeries
  Risk / Notes / Row
    Metric / RiskNote / Default
    Metric / RiskNote / Default
    Metric / RiskNote / Default
```

Config:

- auto layout vertical
- padding: `16`
- gap: `12`
- fill: `Surface / Soft`
- radius: `12`

Fixo nos dois paineis:

- heading com titulo e descricao
- estrutura do container
- estilos de fundo e borda

Distribuicao:

- painel esquerdo: 7 colunas
- painel direito: 5 colunas
- evitar medidas absolutas; usar a malha do content area

Conteudo estrutural nos dois paineis:

- areas vazias para barras, grafico, pontos e notas operacionais
- sem series desenhadas, sem marcadores de dado e sem texto de insight

### 4. Tabela de priorizacao

Componente pai:

- `Panel / Table / Default`

Estrutura:

```text
Panel / Table / Default
  Panel / Heading
    Title
    Description
  Table / Header / Default
  Table / Body
    Table / Row / PatientPriority
    Table / Row / PatientPriority
    Table / Row / PatientPriority
    Table / Row / PatientPriority
```

Config:

- auto layout vertical
- padding: `16`
- gap: `10`
- fill: `Surface / Base`
- radius: `12`
- stroke: `Stroke / Subtle`
- altura: `Fill container` dentro do frame raiz

Colunas:

1. `Paciente`
2. `Unidade`
3. `Status Alta`
4. `Risco`
5. `Tempo Internacao`

Distribuicao recomendada:

- `Paciente` -> 32%
- `Unidade` -> 18%
- `Status Alta` -> 20%
- `Risco` -> 14%
- `Tempo Internacao` -> 16%

Fixo:

- labels do cabecalho
- largura relativa das colunas
- estilo da linha

Conteudo estrutural:

- linhas vazias ou blocos neutros para paciente, unidade, status, risco e tempo
- sem nomes, sem unidades reais e sem dados simulados

## Componentes necessarios

### Shell

- `Shell / App`

### Sidebar

- `Sidebar / Institutional`

### Header

- `Header / Institutional / Badge`

### KPI

- `KPI / Row / 4-up`
- `KPI / Card / Default`
- `KPI / Card / Positive`
- `KPI / Card / Warning`
- `KPI / Card / Critical`

### Panels e charts

- `Panel / Journey / Default`
- `Panel / Trend / Default`
- `Chart / BarRow / Default`
- `Chart / Line / MultiSeries`
- `Metric / SupportCard / Default`
- `Metric / RiskNote / Default`

### Table

- `Panel / Table / Default`
- `Table / Header / Default`
- `Table / Row / PatientPriority`

### Badge

- `Badge / Risk / Low`
- `Badge / Risk / Medium`
- `Badge / Risk / High`

### Divider

- `Divider / Soft`

Recomendacao:

- transformar os tres badges em variants dentro de um mesmo component set `Badge / Risk`

## Orientacoes de auto layout

### Regra geral

- todos os blocos de primeiro nivel devem usar auto layout
- evitar agrupamentos soltos
- usar `Fill container` para areas que precisam escalar sem quebrar o grid
- manter `Shell / App` em horizontal e `Main / Content` em vertical
- sidebar sempre com largura fixa

### Shell

- horizontal
- sidebar fixa
- content area expansivel

### Sidebar

- vertical
- altura completa
- gaps regulares e areas neutras

### Header

- horizontal
- `Space between`
- altura fixa

### KPI row

- horizontal
- 4 itens com `Fill container`

### Panel row

- horizontal
- esquerda maior que direita
- ambos com altura uniforme visual, nao necessariamente numerica

### Table

- vertical para painel e corpo
- horizontal para cada linha
- colunas consistentes via larguras fixas ou percentuais replicadas

## O que nao deve ser preenchido

Nao inserir dados ficticios, amostras numericas ou casos reais no template final.

Nao preencher:

- labels detalhadas da sidebar
- nomes de pacientes
- unidades assistenciais especificas
- datas de atualizacao
- numeros dos KPIs
- series mensais
- textos de observacao operacional
- badges de risco vinculados a casos reais

Estrutural apenas:

- shell, sidebar e divisorias
- barras da jornada
- linhas da tendencia
- microcards de apoio
- espacos vazios para conteudo

## O que pode ser fixo

Pode permanecer fixo no template:

- titulo principal `Dashboard de Desospitalizacao`
- titulo e descricao curta das secoes
- labels das colunas da tabela
- estrutura e estilos dos badges
- estrutura do header institucional
- grid, paddings, radii e strokes
- largura da sidebar
- estrutura geral do shell

## Regras para duplicacao

- duplicar a pagina `03 Templates`
- preservar a arquitetura de componentes em `02 Components`
- trocar apenas conteudos estruturais, se necessario
- nao editar diretamente instancias para mudar estrutura
- se surgir nova severidade, expandir `Badge / Risk`, nao criar badge avulso

## Mapeamento do mockup HTML

- `shell/sidebar` -> `Sidebar / Institutional`
- `.topbar` -> `Header / Institutional / Badge`
- `.cards` -> `KPI / Row / 4-up`
- `.card` -> `KPI / Card / Variant`
- `.journey` -> `Panel / Journey / Default`
- `.journey-item` -> `Chart / BarRow / Default`
- `.support-card` -> `Metric / SupportCard / Default`
- `.trend` -> `Panel / Trend / Default`
- `.risk-note` -> `Metric / RiskNote / Default`
- `.table-panel` -> `Panel / Table / Default`
- `.badge` -> `Badge / Risk / Variant`

## Checklist de montagem

1. Criar `03 Templates / Dashboard / Desospitalizacao / Default` em `1280 x 720`.
2. Montar `Shell / App` com sidebar fixa de `232` px.
3. Aplicar grid de 12 colunas no content area com margem `16` e gutter `10`.
4. Montar o `Header / Institutional / Badge` e publicar como componente.
5. Montar `KPI / Card` com variants e instanciar a linha de 4 cards.
6. Montar `Panel / Journey / Default` com `Chart / BarRow` e `Metric / SupportCard`.
7. Montar `Panel / Trend / Default` com `Chart / Line / MultiSeries` e `Metric / RiskNote`.
8. Montar `Panel / Table / Default`, `Table / Header / Default` e `Table / Row / PatientPriority`.
9. Consolidar `Badge / Risk` e `Divider / Soft` como component sets.
10. Duplicar o frame final para `Dashboard / Desospitalizacao / Clean`.
