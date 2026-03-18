# agent-template-figma

Repositorio para templates e governanca de agentes do Codex aplicados a fluxos de Figma.

## Estrutura

- `AGENTS.md`: diretrizes do repositorio
- `.codex/config.toml`: configuracao central de agentes
- `.codex/agents/`: definicoes TOML dos subagentes
- `.codex/skills/`: skills locais do projeto

## Subagentes

- `template_creator`: cria templates visuais
- `design_governor`: padroniza foundations e componentes
- `repo_integrator`: integra convencoes do repositorio
- `reviewer`: revisa riscos e inconsistencias

## Uso

O repositorio esta preparado para uso local com Codex e subagentes baseados em arquivos TOML.
