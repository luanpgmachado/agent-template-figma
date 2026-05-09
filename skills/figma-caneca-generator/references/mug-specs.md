# Especificações de Canecas para Sublimação

## Dimensões Padrão

### Caneca Cilíndrica Padrão 11oz
- **Altura**: ~9,5cm
- **Circunferência**: 20,5cm (diâmetro ~6,5cm)
- **Área imprimível**: 20,5cm × 9,6cm (horizontal)
- **Resolução**: 300 DPI (mínimo 72 DPI, recomendado 300 DPI)

### Conversão para Pixels
A 300 DPI:
- **Largura**: 20,5cm = 2456 pixels
- **Altura**: 9,6cm = 1148 pixels
- **Proporção**: 2.137:1 (horizontal)

## Sangra e Margens de Segurança

### Zona de Segurança (SafeZone)
- **Margem superior**: 2mm (não será impresso - topo da caneca)
- **Margem inferior**: 2mm (não será impresso - base da caneca)
- **Margens laterais**: 2mm em cada lado

**Área segura prática**:
- Largura segura: 20,5cm - 4mm = 20,1cm (2408 px)
- Altura segura: 9,6cm - 4mm = 9,2cm (1100 px)

### Elementos Importantes
Elementos críticos (rostos, logos) devem estar a **pelo menos 5mm** das bordas para evitar corte.

## Preparação de Imagens

### Resolução Recomendada
- **Mínimo**: 1200 × 1200px (para fotos isoladas)
- **Ideal**: 1500 × 1500px ou superior
- **Profissional**: 2456 × 1148px (tamanho exato da caneca)

### Formatos Suportados
- ✅ **JPEG** (.jpg, .jpeg) - Ideal para fotos
- ✅ **PNG** (.png) - Ideal para elementos com transparência
- ✅ **WebP** (.webp) - Compressão moderna

### Proporções Comuns
| Tipo | Proporção | Nota |
|------|-----------|------|
| Retrato/Rosto | 1:1 (quadrado) | Ideal para moldura vertical |
| Paisagem | 3:2 ou 16:10 | Ideal para moldura horizontal |
| Quadrado | 1:1 | Versátil |
| Ultra-wide | 2:1 ou mais | Requer cuidado com cortes |

## Cores e Processo

### Sublimação
- **Processo**: Transferência térmica de tinta para material
- **Temperatura**: ~200-210°C
- **Pressão**: ~3.5-4kg/cm²
- **Tempo**: ~30-60 segundos (depende da caneca)

### Espaço de Cor
- **Recomendado**: RGB (para telas) ou CMYK (para impressoras)
- **Perfil**: sRGB (padrão web)
- **Modo**: 8 bits por canal

### Considerações de Cor
| Cor | Nota |
|-----|------|
| Branco | Função em canecas brancas = cor da caneca |
| Cores Vibrantes | Saem melhor em canecas brancas |
| Tons Escuros | Requerem canecas mais claras para visibilidade |
| Preto | Use #000000 ou CMYK 0,0,0,100 |

## Camadas Ideais

### Estrutura Recomendada
```
Canvas (20,5cm × 9,6cm @ 300 DPI)
├── 01_BG (Background/Fundo)
├── 02_Moldura
├── 03_Foto
├── 04_Decorações
├── 05_Textos
├── 06_SafeZone (guia invisível)
└── 07_Notas (informações de impressão)
```

### Convenção de Nomenclatura
- Usar números para ordem de profundidade
- Use underscores para separar palavras
- Exemplo: `01_BG`, `02_Moldura_Coracaico`, `03_Foto_Casal`

## Boas Práticas

### O Que Fazer ✅
- Sempre exportar em 300 DPI
- Manter proporção 20,5cm × 9,6cm
- Deixar margens de segurança
- Validar cores antes de imprimir
- Usar fontes sem serifa para textos pequenos
- Fazer prova/teste antes de produção em massa
- Documentar camadas e instruções de edição

### O Que Evitar ❌
- Colocar elementos críticos nas bordas
- Usar imagens com muito zoom (pixeladas)
- Fontes muito finas ou ornamentadas
- Gradientes muito sutis (podem pixelar)
- Sombras muito complexas
- Muitos elementos (visualmente poluído)
- Deixar branco "vazio" sem propósito

## Processo de Impressão Típico

1. **Preparação**: Limpar caneca, aplicar primer (se necessário)
2. **Transferência**: Aquecer a caneca até ~70-80°C
3. **Prensagem**: Aplicar filme com design por 30-60s a 200-210°C
4. **Resfriamento**: Deixar esfriar naturalmente
5. **Finalização**: Verificar qualidade, aplicar camada de proteção (opcional)

## Variações de Tamanho

| Tamanho | Volume | Circunferência | Altura |
|---------|--------|-----------------|--------|
| 6oz | 177mL | 17cm | 7,5cm |
| **11oz** | **325mL** | **20,5cm** | **9,6cm** |
| 15oz | 443mL | 23cm | 10,5cm |
| 20oz | 590mL | 26cm | 12cm |

*Padrão desta skill: 11oz (20,5cm × 9,6cm)*

## Recursos Adicionais

- [Figma Plugin: Sublimation Guide](https://www.figma.com/plugins)
- [DPI Calculator](https://www.nist.gov/pml/pixel-image-resolution-and-unit-conversion-calculator)
- [Color Spaces for Print](https://www.color-management-guide.com)

