# Template Figma - Dashboard de Desospitalizacao

## Objetivo

Transformar o mockup HTML `desospitalizacao-mockup.html` em um template reutilizavel no Figma, com linguagem institucional de saude, grid rigido, leitura executiva rapida e componentes reaproveitaveis.

## Tipo de template

- Dashboard operacional
- Contexto: desospitalizacao
- Estilo: institucional, sobrio, analitico
- Formato base: `1280 x 720`

## Estrutura da pagina no Figma

Criar as paginas nesta ordem:

1. `00 Cover`
2. `01 Foundations`
3. `02 Components`
4. `03 Templates`

Criar o frame principal em `03 Templates` com o nome:

`Dashboard / Desospitalizacao / Default`

## Grid e espacamento

### Frame principal
- Largura: `1280`
- Altura: `720`
- Fill: `#FFFFFF`
- Stroke: `rgba(44, 90, 38, 0.15)`

### Grid recomendado
- `12` colunas
- Margens laterais: `16`
- Gutter: `10`
- Base de espacamento: `4, 8, 10, 12, 16, 24`

### Estrutura vertical
- Header: `73`
- Linha de KPIs: altura minima `92`
- Linha de paineis: altura minima `270`
- Tabela inferior: bloco flexivel ocupando o restante

## Paleta

Registrar em `01 Foundations / Colors`:

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

## Tipografia

Registrar em `01 Foundations / Typography`:

- `Title / Page` -> `22 / 110% / Semibold`
- `Title / Section` -> `13 / 120% / Bold`
- `Body / Small` -> `12 / 140% / Regular`
- `Body / XS` -> `11 / 140% / Regular`
- `Caption / Tiny` -> `10 / 140% / Regular`
- `Metric / KPI` -> `34 / 100% / Bold`
- `Metric / Support` -> `24 / 100% / Bold`
- `Metric / Note` -> `20 / 110% / Bold`

Fonte recomendada: `Segoe UI` ou equivalente sans-serif de alta legibilidade.

## Composicao do layout

### 1. Header institucional
Usar um bloco horizontal com:

- Titulo: `Dashboard de Desospitalizacao`
- Subtitulo operacional abaixo do titulo
- Badge de atualizacao no canto direito

Especificacao:
- Padding: `18 24 16 24`
- Background: gradiente `#298148 -> #518C57`
- Texto branco
- Badge com borda clara, fundo translúcido e radius total

Nome do componente:

`Header / Institutional / Badge`

### 2. Linha de KPIs
Criar uma linha com `4` cards de mesma largura:

- `Pacientes Elegiveis Alta`
- `Alta Prevista 24h`
- `Risco Readmissao 30d`
- `Retorno UTI 48h`

Estrutura interna de cada card:
- label no topo
- valor principal grande
- coluna lateral com meta + observacao curta

Especificacao:
- Altura minima: `92`
- Padding: `12`
- Border: `2px`
- Gap entre cards: `10`

Nome do componente:

`KPI / Card / Default`

Variantes sugeridas:
- `Default`
- `Positive`
- `Warning`
- `Critical`

### 3. Linha principal de conteudo
Montar dois paineis lado a lado.

#### Painel esquerdo - Jornada
Estrutura:
- titulo e descricao
- lista horizontal de barras
- area lateral com metricas de apoio

Subestrutura:
- coluna esquerda: ranking de indicadores com label, subtitle, barra e valor
- coluna direita: cards de apoio com metrica resumida

Componentes:
- `Panel / Journey / Default`
- `Chart / BarRow / Default`
- `Metric / SupportCard / Default`

#### Painel direito - Tendencia / Risco
Estrutura:
- titulo e descricao
- grafico de serie temporal
- linha inferior com `3` notas de risco

Componentes:
- `Panel / Trend / Default`
- `Chart / Line / MultiSeries`
- `Metric / RiskNote / Default`

### 4. Tabela de priorizacao
Criar um painel full width na parte inferior.

Estrutura:
- titulo e descricao
- header da tabela
- linhas de pacientes
- badges de risco por severidade

Colunas:
1. `Paciente`
2. `Unidade`
3. `Status Alta`
4. `Risco`
5. `Tempo Internacao`

Componentes:
- `Panel / Table / Default`
- `Table / Header / Default`
- `Table / Row / PatientPriority`
- `Badge / Risk / High`
- `Badge / Risk / Medium`
- `Badge / Risk / Low`

## Auto layout recomendado

### Frame principal
- Auto layout vertical
- Gap entre blocos: `10`
- Padding inferior: `16`

### Cards KPI
- Container horizontal com `Fill container`
- Cada card com `Fill container`

### Linha de paineis
- Container horizontal
- Gap `10`
- Cada painel com `Fill container`

### Tabela
- Header e linhas em auto layout vertical
- Cada linha com colunas fixas ou proporcionais consistentes

## Ordem de construcao no Figma

1. Criar o frame `1280 x 720`
2. Aplicar grid de `12` colunas
3. Montar o `Header / Institutional / Badge`
4. Montar e componentizar `KPI / Card / Default`
5. Montar `Panel / Journey / Default`
6. Montar `Panel / Trend / Default`
7. Montar `Table / Row / PatientPriority`
8. Consolidar badges e metric cards como componentes
9. Duplicar o frame como template base limpo

## Conteudos que devem virar placeholder

Substituir dados reais por placeholders no template final:

- nome de pacientes
- medico responsavel
- numero de atendimento
- numero de prescricao
- unidades especificas
- datas de atualizacao
- metricas numericas do mes

Manter como texto editavel:

- titulos de secao
- labels dos KPIs
- labels da tabela
- rotulos de risco

## Regras de reutilizacao

- Nao desenhar cards soltos fora de componentes
- Nao usar nomes genericos como `Card 1`, `Tabela Nova` ou `Versao Final`
- Separar componentes de conteudo real
- Manter todas as variacoes de risco como variante de um mesmo badge
- Reaproveitar a mesma estrutura para outros dashboards assistenciais

## Mapeamento do mockup HTML para Figma

- `.topbar` -> `Header / Institutional / Badge`
- `.card` -> `KPI / Card / Default`
- `.journey` -> `Panel / Journey / Default`
- `.journey-item` -> `Chart / BarRow / Default`
- `.support-card` -> `Metric / SupportCard / Default`
- `.trend` -> `Panel / Trend / Default`
- `.risk-note` -> `Metric / RiskNote / Default`
- `.table-panel` -> `Panel / Table / Default`
- `.badge` -> `Badge / Risk / Variant`

## Resultado esperado

Ao final, o arquivo de Figma deve permitir:

- duplicar rapidamente o dashboard para outro tema assistencial
- trocar dados sem quebrar a composicao
- reaproveitar header, KPIs, paineis e tabela em outros mockups
- manter visual institucional e leitura operacional em poucos segundos
