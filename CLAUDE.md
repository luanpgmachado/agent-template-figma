# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Idioma

Responder em pt-BR por padrao. Preservar codigo, comandos, caminhos e literais no idioma original.

## Repositorio

Repositorio de templates Figma e governanca de design system para qualquer segmento. Nao ha codigo executavel — o conteudo e documentacao, skills e configuracoes de agentes Codex.

## Estrutura

```
.codex/
  config.toml              # max_threads=1, max_depth=1
  agents/                  # subagentes TOML (gpt-5.3-Codex)
    template-creator.toml  # cria templates visuais
    design-governor.toml   # padroniza foundations e componentes
    repo-integrator.toml   # mantém .codex e AGENTS.md
    reviewer.toml          # revisa conflitos e riscos (read-only)
  skills/
    figma-templates-saude/SKILL.md     # criacao de dashboards institucionais
    design-system-governanca/SKILL.md  # auditoria e organizacao de bibliotecas
skills/
  figma-caneca-generator/SKILL.md     # templates de canecas para sublimacao
docs/                      # blueprints, roteiros, checklists e imagens de referencia
AGENTS.md                  # diretrizes do repositorio (leia antes de qualquer tarefa)
```

## Skills — quando usar cada uma

| Skill | Usar quando |
|-------|-------------|
| `figma-templates-saude` | Criar dashboards executivos/operacionais, capas institucionais, telas de leitos, CC, DRE |
| `design-system-governanca` | Auditar, renomear, consolidar componentes ou foundations existentes |
| `figma-caneca-generator` | Criar artes de caneca para sublimacao (20,5×9,6cm, 300 DPI) |

Nao misturar: criacao de layout e governanca sao fluxos separados.

## Convencoes de nomenclatura (Figma)

Formato: `Categoria / Componente / Variante`

Exemplos: `Header / Institutional / Default`, `KPI / Default / Positive`, `Card / Chart / Default`

Proibido: nomes como `Final`, `Novo`, `Teste`, `Opcao 2`, mistura de idiomas ou caixas.

## Estrutura padrao de arquivo Figma

```
00 Cover
01 Foundations   (Colors, Typography, Spacing, Radii, Strokes, Effects)
02 Components
03 Templates
04 Dark Mode     (quando aplicavel)
```

## Paleta e visual

- Base clara: branco e off-white
- Texto: grafite ou preto
- Destaque: verde institucional
- Dark mode: base preta/grafite + mesmo verde
- Visual sobrio, corporativo; sem estetica de startup

## Regras de decisao criticas

- Grid e hierarquia antes de detalhe visual.
- Se dois componentes forem parecidos, consolidar.
- Se um template exige ajuste manual frequente, componentizar.
- Se a organizacao exige explicacao longa, simplificar a estrutura.
- Consistencia > liberdade visual.

## Imagens de referencia

Fotos para canecas: `docs/img/foto-arte-caneca/` (aceita .jpg, .png, .webp)  
Capturas de progresso Figma: `docs/img/img-dash/`
