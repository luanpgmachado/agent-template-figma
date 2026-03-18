---
name: design-system-governanca
description: Organizar, padronizar, auditar e evoluir design systems e templates no Figma com foco em componentes, nomenclatura, foundations, estrutura de arquivos e consistencia visual. Use quando precisar revisar inconsistencias, estruturar biblioteca reutilizavel, preparar material para escala ou time, definir foundations ou padronizar templates existentes. Nao usar para criacao inicial de layouts do zero, exploracao visual ou definicao estetica aberta.
---

# Governanca de Templates e Design System

Usar esta skill para transformar arquivos e bibliotecas em sistemas claros, reutilizaveis e escalaveis. Aqui o objetivo principal e disciplina estrutural, nao exploracao visual.

## Objetivo
- Garantir consistencia entre templates e componentes.
- Reduzir duplicacao e ambiguidade.
- Aumentar escalabilidade, reutilizacao e clareza estrutural.
- Preparar o material para manutencao por time.

## Fluxo
1. Mapear a estrutura atual do arquivo e identificar duplicacoes, lacunas e incoerencias.
2. Definir ou corrigir paginas, foundations e componentes antes de refinamentos locais.
3. Consolidar variaveis visuais em tokens, estilos ou componentes reutilizaveis.
4. Renomear elementos para um padrao unico e previsivel.
5. Separar o que e foundation, componente, template e variante de tema.
6. Auditar consistencia visual e estrutural antes de encerrar.

## Estrutura recomendada no Figma
- `00 Cover`
- `01 Foundations`
- `02 Components`
- `03 Templates`
- `04 Dark Mode`

## Foundations
Definir e manter estes blocos de base:

### Cores
- Primarias
- Neutras
- Estados: positivo, alerta e critico

### Tipografia
- Escala clara para `title`, `subtitle`, `body` e `caption`

### Espacamento
- Base consistente, como `4`, `8`, `16`, `24` e `32`

### Grid
- Colunas bem definidas
- Margens consistentes

### Border radius
- Um padrao unico ou um conjunto minimo e controlado

## Componentes
Padronizar ao menos estes componentes quando fizerem parte da biblioteca:
- `Header / Institutional`
- `KPI / Default`
- `KPI / Status`
- `Card / Chart`
- `Card / Table`
- `Filter / Inline`
- `Menu / Sidebar`
- `Cover / Institutional`

## Nomenclatura
Usar um formato unico, curto e legivel:

`Categoria / Componente / Variante`

Exemplos:
- `Header / Institutional / Default`
- `KPI / Default / Positive`
- `Card / Chart / Default`
- `Menu / Sidebar / Compact`

Regras:
- Evitar nomes genericos como `Final`, `Novo`, `Teste` ou `Opcao 2`.
- Evitar misturar idioma, caixa e pluralizacao no mesmo sistema.
- Nomear por funcao e variante, nao por posicao momentanea no layout.
- Manter o mesmo padrao entre componentes, estilos e templates.

## Criterios de auditoria
- Verificar se o mesmo componente existe duplicado com pequenas variacoes desnecessarias.
- Verificar se foundations cobrem a maior parte das decisoes visuais recorrentes.
- Verificar se templates usam componentes em vez de blocos soltos.
- Verificar se dark mode reaproveita a mesma logica estrutural do modo claro.
- Verificar se qualquer pessoa do time consegue localizar rapidamente paginas, componentes e variantes.

## Regras de decisao
- Se duas solucoes forem visualmente parecidas, consolidar.
- Se uma variacao nao tiver motivo recorrente, remover.
- Se um template depender de ajustes manuais frequentes, componentizar.
- Se a organizacao do arquivo exigir explicacao longa, simplificar a estrutura.
- Se surgir conflito entre liberdade visual e consistencia, priorizar consistencia.
