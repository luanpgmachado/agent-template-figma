# 🎨 Figma Caneca Generator - Skill

Skill especializada em criar templates profissionais e editáveis no Figma para artes de canecas personalizadas em sublimação (tamanho padrão 20,5x9,6cm).

## 📁 Estrutura do Projeto

```
figma-caneca-generator/
├── SKILL.md                          # Documentação principal da skill
├── README.md                         # Este arquivo
├── evals/
│   └── evals.json                   # 5 test cases para validação
├── scripts/
│   └── validate_photo.py            # Script para validar fotos
├── references/
│   └── mug-specs.md                 # Especificações técnicas de canecas
└── assets/                          # (vazio - para futuros recursos)
```

## 🚀 Como Usar

### 1. Uso Básico
Simplesmente descreva o tipo de caneca que quer criar:

```
"Crie um template de caneca com moldura de coração, espaço para foto no centro 
e área de texto personalizado no topo. Use a foto: familia-feliz"
```

### 2. Com Múltiplas Fotos
Para 2 ou mais fotos, use o estilo **grade vertical**:

```
"Crie um template de caneca com moldura grade vertical com 2 fotos lado a lado: 
'casal-1' e 'casal-2', com nomes editáveis embaixo"
```

### 3. Paisagem/Horizontal
Use o estilo **grade horizontal** para paisagens:

```
"Template de caneca com moldura grade horizontal para paisagem. 
Use foto 'viagem-praia' com decoração nas laterais"
```

## 📋 Tipos de Arte Suportados

- **Molduras**: Coração, quadrado, círculo, decorativa
- **Grade Vertical**: Ideal para 1-2 fotos (retratos, rostos)
- **Grade Horizontal**: Ideal para paisagens e grupos
- **Comemorativas**: Natal, Aniversário, Dia das Mães
- **Infantis**: Unicórnio, astronauta, dinossauro, princesa
- **Para casais**: Com nomes, datas, frases
- **Corporativas**: Logo + texto, temas de marca

## ⚙️ Especificações Técnicas

| Propriedade | Valor |
|-------------|-------|
| **Tamanho** | 20,5cm × 9,6cm |
| **Resolução** | 300 DPI |
| **Pixels** | 2456 × 1148px |
| **Margem segura** | 2mm em todas as bordas |
| **Processo** | Sublimação térmica |

## 📸 Validação de Fotos

A skill automaticamente:
- ✅ Procura a foto no repositório
- ✅ Valida resolução (mín. 1200×1200px)
- ✅ Verifica compatibilidade com moldura
- ✅ Alerta sobre riscos de corte
- ✅ Integra após validação

**Repositório de imagens**:
```
C:\Users\luanp\OneDrive\Rep-2026\projetos-pessoais\4 - Planejamento\7 - AGENT-TEMPLATE-FIGMA\docs\img\foto-arte-caneca
```

## 🧪 Test Cases

A skill foi validada com 5 casos de teste:

1. **Moldura com Foto** - Coração + validação de imagem
2. **Arte Comemorativa** - Natal com elementos decorativos
3. **Arte Infantil** - Unicórnio com cores pastéis
4. **Grade Vertical** - 2 fotos lado a lado
5. **Grade Horizontal** - Paisagem com decoração

Ver: `evals/evals.json`

## 📚 Referências

- **Especificações de canecas**: `references/mug-specs.md`
- **Script de validação**: `scripts/validate_photo.py`
- **Documentação completa**: `SKILL.md`

## 🎯 Saída Esperada

Cada template gerado inclui:

✅ Canvas 20,5 × 9,6cm @ 300 DPI
✅ Camadas organizadas e nomeadas
✅ Elementos editáveis claramente marcados
✅ Margens de segurança aplicadas
✅ Pronto para edição e exportação
✅ Qualidade profissional para sublimação

## 🔄 Fluxo de Trabalho Típico

```mermaid
graph LR
    A["Descreva o design"] → B["Skill cria template"]
    B → C["Valida fotos"]
    C → D["Organiza camadas"]
    D → E["Aplica margens"]
    E → F["Figma pronto"]
    F → G["Você edita/exporta"]
```

## ⚡ Próximos Passos

- [ ] Executar 5 test cases
- [ ] Revisar resultados
- [ ] Iteração se necessário
- [ ] Otimização de descrição
- [ ] Packagear como `.skill`

## 📝 Notas

- Sempre mantenha as dimensões 20,5 × 9,6cm
- Use 300 DPI para qualidade profissional
- Respeite as margens de segurança
- Nomeie camadas descritivamente
- Deixe campos de texto editáveis claros

## 🤝 Contribuições

Para melhorias, atualize:
- `SKILL.md` - Instruções da skill
- `evals/evals.json` - Test cases
- `references/mug-specs.md` - Especificações técnicas

---

**Versão**: 1.0.0  
**Status**: Em desenvolvimento/Testes  
**Último update**: 2026-05-09
