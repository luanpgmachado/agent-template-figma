---
name: figma-caneca-generator
description: |
  Cria templates profissionais e editáveis no Figma para artes de canecas personalizadas em sublimação (tamanho padrão 20,5x9,6cm). 
  
  Use esta skill quando precisar:
  - Criar templates de canecas com molduras, fotos e textos editáveis
  - Gerar artes comemorativas, infantis, para casais ou corporativas
  - Aplicar margens de segurança automáticas para sublimação
  - Validar e integrar fotos do repositório do projeto
  - Organizar camadas profissionalmente no Figma para fácil edição
  
  A skill funciona como designer especialista em canecas, garantindo qualidade profissional e pronto para impressão.
compatibility: |
  - Figma MCP server com skill `figma-use`
  - Acesso a arquivo Figma para edição
  - Acesso ao repositório de imagens em: `C:\Users\luanp\OneDrive\Rep-2026\projetos-pessoais\4 - Planejamento\7 - AGENT-TEMPLATE-FIGMA\docs\img\foto-arte-caneca`
---

# Figma Caneca Generator

Skill especializada em criar templates editáveis e profissionais no Figma para artes de canecas em sublimação.

## Como funciona

Você descreve o tipo de arte de caneca que quer criar. A skill:

1. **Cria o template** com dimensões corretas (20,5x9,6cm em 300 DPI para sublimação)
2. **Organiza as camadas** logicamente no Figma (fundo, molduras, fotos, textos, decorações, margens)
3. **Valida fotos** se fornecidas (verifica arquivo, resolução, proporção, qualidade)
4. **Aplica margens de segurança** (2mm nas bordas para compensar corte)
5. **Deixa pronto para edição** com textos editáveis, placeholders de foto, e elementos decorativos

## Exemplos de uso

### Moldura com foto
"Crie um template de caneca com moldura de coração, espaço para foto no centro e área de texto personalizado no topo. Use a foto: familia-feliz"

A skill vai:
- Procurar `familia-feliz.*` em `docs\img\foto-arte-caneca`
- Validar resolução (recomendado 1200x1200px+)
- Verificar se a foto cabe bem na moldura
- Alertar se houver risco de corte ou qualidade baixa
- Integrar a foto no template

### Moldura Grade Vertical
"Crie um template de caneca com moldura grade vertical (retângulo vertical) com 2 fotos: 'casal-1' e 'casal-2' lado a lado na vertical, com nomes editáveis embaixo de cada foto"

A skill vai:
- Usar estilo grade vertical (padrão para múltiplas fotos)
- Validar ambas as fotos
- Organizar 2 retângulos verticais lado a lado
- Adicionar campos de texto editáveis para nomes
- Aplicar margens de segurança para não cortar faces

### Moldura Grade Horizontal
"Crie um template de caneca com moldura grade horizontal (retângulo horizontal), fundo branco e espaço para uma paisagem. Use a foto: viagem-praia. Adicionar texto 'Lembranças de férias' no topo"

A skill vai:
- Usar estilo grade horizontal (melhor para paisagens)
- Integrar a foto em proporção horizontal
- Adicionar decoração nas laterais
- Incluir texto editável principal

### Arte comemorativa
"Crie um template de caneca para Natal com fundo vermelho, flocos de neve animados, texto 'Feliz Natal' e espaço para nome personalizado"

A skill vai criar elementos decorativos, definir fontes editáveis e organizar tudo para fácil customização.

### Arte infantil
"Template de caneca com tema de unicórnio, cores pastéis, arco-íris, nuvens e espaço para nome da criança em 3 tamanhos diferentes"

## Estrutura padrão do template

Cada template contém:

```
📦 Canvas (20,5cm × 9,6cm @ 300 DPI)
├── Fundo (imagem ou gradiente)
├── Moldura (se aplicável)
├── [Foto] (se applicable - com validação)
├── Elementos decorativos (shapes, ícones)
├── Textos editáveis (com nomes descritivos)
├── Margens de segurança (2mm invisíveis nas bordas)
└── Informações de impressão (nota no Figma)
```

## Especificações técnicas

### Dimensões
- **Tamanho físico**: 20,5cm × 9,6cm (caneca padrão)
- **Resolução**: 300 DPI para sublimação
- **Orientação**: Sempre horizontal
- **Sangra**: 2mm em todas as bordas

### Camadas
Nomeadas descritivamente para fácil navegação:
- `BG` ou `Fundo`
- `Moldura` (se houver)
- `Foto` (se houver)
- `Decoração_1`, `Decoração_2` (se houver)
- `Texto_Principal`, `Texto_Secundario`
- `SafeZone` (invisível, apenas referência)

### Textos editáveis
- Fonte legível (mínimo 14pt)
- Com anotações de limite de caracteres (ex: "máx 30 caracteres")
- Nomes claramente identificáveis no Figma

## Validação de fotos

Quando você fornecer um nome de foto, a skill:

1. **Verifica existência**: Procura em `foto-arte-caneca` (aceita .jpg, .png, .webp)
2. **Valida resolução**: Recomenda 1200×1200px ou superior para qualidade de impressão
3. **Analisa proporção**: Verifica se cabe bem no espaço da moldura
4. **Avalia qualidade**: Alerta se comprimida, muito pequena ou incompatível
5. **Previne corte**: Verifica se elementos importantes estão longe das margens

Se algo não estiver OK, a skill avisa e sugere ajustes antes de integrar.

## Tipos de arte suportados

- **Molduras com foto**: Coração, quadrado, círculo, moldura decorativa
- **Moldura Estilo Grade - Vertical**: Foto dentro de retângulo vertical. Ideal para 1-2 fotos. O retângulo fica orientado na vertical, permitindo melhor proporção para rostos e pessoas
- **Moldura Estilo Grade - Horizontal**: Arte dentro de retângulo horizontal. Ideal para paisagens, grupos maiores ou composições horizontais. O retângulo ocupa a largura principal da caneca
- **⚠️ Regra de múltiplas fotos**: Se forem 2 ou mais fotos, prefira usar o **estilo grade vertical** para melhor aproveitamento de espaço
- **Artes comemorativas**: Natal, Ano Novo, Dia das Mães, Aniversário
- **Artes infantis**: Tema unicórnio, astronauta, dinossauro, princesa
- **Artes para casais**: Casal + nome, data especial, frase personalizada
- **Frases e textos**: Motivacional, corporativo, customizado
- **Templates corporativos**: Logo + texto, tema de marca

## Antes de começar

1. **Crie um arquivo no Figma** (ou compartilhe URL se já tiver)
2. **Tenha fotos prontas** em `docs\img\foto-arte-caneca` (nomear claramente)
3. **Descreva o estilo** que quer (cores, tema, tipo de moldura)
4. **Informe o propósito** (presente, comercial, corporativo)

Exemplo de prompt:
> "Crie um template de caneca com moldura redonda, fundo branco com padrão de estrelas, foto em https://[figma-url] e espaço para nome + data. Usar foto 'noivos-sorrindo' do repositório"

## Saída esperada

✅ Template completamente pronto no Figma
✅ Camadas organizadas e nomeadas
✅ Elementos editáveis claramente marcados
✅ Margens de segurança aplicadas
✅ Anotações de guia de edição
✅ Pronto para exportação em alta resolução

## Melhorias futuras

- Suporte a variantes (claro/escuro)
- Templates pré-salvos reutilizáveis
- Integração com variables do Figma para cores corporativas
- Geração de guia de edição em PDF

---

**Repositório de imagens**: `C:\Users\luanp\OneDrive\Rep-2026\projetos-pessoais\4 - Planejamento\7 - AGENT-TEMPLATE-FIGMA\docs\img\foto-arte-caneca`

**Codepage**: AGENT-TEMPLATE-FIGMA (seu projeto)
