# Blueprint Figma - Dashboard Operacional de Desospitalizacao

## Escopo

Blueprint de construcao para o template `Dashboard / Desospitalizacao / Default`, derivado do mockup HTML e do roteiro `desospitalizacao-template-figma.md`.
Este documento orienta apenas o layout estrutural, sem preenchimento de dados ficticios.

Direcao adotada:

- template operacional, nao promocional
- leitura em poucos segundos
- composicao institucional de saude
- blocos 100% reutilizaveis em outros temas assistenciais

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

- `Header`
- `KPI`
- `Panel`
- `Chart`
- `Metric`
- `Table`
- `Badge`

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
- layout grid: `12 columns`
- margins: `16`
- gutter: `10`

### Estrutura raiz

Usar esta hierarquia:

```text
Dashboard / Desospitalizacao / Default
  Content / Root
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

- direcao: vertical
- padding: `16 16 16 16`
- gap: `10`
- width: `Fill container`
- height: fixed `720`

## Hierarquia detalhada do frame principal

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
- width util: `1248`
- cada card: `Fill container`
- altura minima: `92`

Largura de referencia por card:

- `304.5` px em distribuicao igual

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

Largura de referencia:

- `723.8` px

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
- `Journey / SideMetrics` com largura fixa entre `164` e `180`

#### Painel direito

Componente:

- `Panel / Trend / Default`

Largura de referencia:

- `514.2` px

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

Conteudo estrutural nos dois paineis:

- areas vazias para barras, grafico, pontos e notas operacionais

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

## Componentes necessarios

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

Recomendacao:

- transformar os tres badges em variants dentro de um mesmo component set `Badge / Risk`

## Orientacoes de auto layout

### Regra geral

- todos os blocos de primeiro nivel devem usar auto layout
- evitar agrupamentos soltos
- usar `Fill container` para areas que precisam escalar sem quebrar o grid

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

- nomes de pacientes
- unidades assistenciais especificas
- datas de atualizacao
- numeros dos KPIs
- series mensais
- textos de observacao operacional
- badges de risco vinculados a casos reais

Estrutural apenas:

- barras da jornada
- linhas da tendencia
- microcards de apoio
- espacos vazios para conteudo

## O que pode ser fixo

Pode permanecer fixo no template:

- titulo principal `Dashboard de Desospitalizacao`
- labels dos 4 KPIs
- titulo e descricao curta das secoes
- labels das colunas da tabela
- estrutura e estilos dos badges
- estrutura do header institucional
- grid, paddings, radii e strokes

## Regras para duplicacao

- duplicar a pagina `03 Templates`
- preservar a arquitetura de componentes em `02 Components`
- trocar apenas conteudos estruturais, se necessario
- nao editar diretamente instancias para mudar estrutura
- se surgir nova severidade, expandir `Badge / Risk`, nao criar badge avulso

## Mapeamento do mockup HTML

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
2. Aplicar grid de 12 colunas com margem `16` e gutter `10`.
3. Montar o `Header / Institutional / Badge` e publicar como componente.
4. Montar `KPI / Card` com variants e instanciar a linha de 4 cards.
5. Montar `Panel / Journey / Default` com `Chart / BarRow` e `Metric / SupportCard`.
6. Montar `Panel / Trend / Default` com `Chart / Line / MultiSeries` e `Metric / RiskNote`.
7. Montar `Panel / Table / Default`, `Table / Header / Default` e `Table / Row / PatientPriority`.
8. Consolidar `Badge / Risk` como component set.
9. Duplicar o frame final para `Dashboard / Desospitalizacao / Clean`.
