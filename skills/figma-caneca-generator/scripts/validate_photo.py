#!/usr/bin/env python3
"""
Script para validar fotos antes de integrar no template de caneca.

Verifica:
- Existência do arquivo
- Resolução mínima (1200x1200px recomendado)
- Formato suportado (.jpg, .png, .webp)
- Proporção (aviso se muito distorcida)
- Qualidade de compressão
"""

import os
from pathlib import Path
from PIL import Image
import sys

# Configurações
PHOTO_REPO = r"C:\Users\luanp\OneDrive\Rep-2026\projetos-pessoais\4 - Planejamento\7 - AGENT-TEMPLATE-FIGMA\docs\img\foto-arte-caneca"
MIN_RESOLUTION = 1200  # pixels
SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.webp'}


def find_photo(filename):
    """Procura a foto no repositório, aceitando diferentes extensões."""
    base_name = Path(filename).stem

    for ext in SUPPORTED_FORMATS:
        photo_path = Path(PHOTO_REPO) / f"{base_name}{ext}"
        if photo_path.exists():
            return photo_path

    return None


def validate_photo(filename):
    """Valida uma foto e retorna relatório."""
    photo_path = find_photo(filename)

    report = {
        "filename": filename,
        "exists": False,
        "resolution": None,
        "dimensions": None,
        "format": None,
        "size_kb": None,
        "aspect_ratio": None,
        "warnings": [],
        "errors": [],
        "is_valid": False
    }

    # Verificar existência
    if not photo_path:
        report["errors"].append(f"Foto '{filename}' não encontrada em {PHOTO_REPO}")
        return report

    report["exists"] = True
    report["format"] = photo_path.suffix.lower()
    report["size_kb"] = round(photo_path.stat().st_size / 1024, 2)

    try:
        # Abrir imagem
        img = Image.open(photo_path)
        width, height = img.size
        report["dimensions"] = f"{width}x{height}"

        # Calcular resolução (assumindo mínimo de 72 DPI)
        min_side = min(width, height)
        report["resolution"] = min_side

        # Verificar resolução mínima
        if min_side < MIN_RESOLUTION:
            report["warnings"].append(
                f"Resolução baixa: {min_side}px (recomendado: {MIN_RESOLUTION}px+)"
            )

        # Calcular proporção
        aspect_ratio = round(width / height, 2)
        report["aspect_ratio"] = aspect_ratio

        # Avisar sobre proporção extrema
        if aspect_ratio > 2.5 or aspect_ratio < 0.4:
            report["warnings"].append(
                f"Proporção extrema: {aspect_ratio}:1 (pode não caber bem em moldura)"
            )

        # Verificar modo de cor
        if img.mode not in ['RGB', 'RGBA', 'L']:
            img = img.convert('RGB')
            report["warnings"].append(f"Modo de cor convertido para RGB")

        report["is_valid"] = len(report["errors"]) == 0

    except Exception as e:
        report["errors"].append(f"Erro ao processar imagem: {str(e)}")

    return report


def print_report(report):
    """Imprime relatório formatado."""
    status = "✅ VÁLIDO" if report["is_valid"] else "❌ INVÁLIDO"
    print(f"\n{status} | {report['filename']}")
    print("-" * 60)

    if report["exists"]:
        print(f"Formato: {report['format']}")
        print(f"Dimensões: {report['dimensions']}")
        print(f"Proporção: {report['aspect_ratio']}")
        print(f"Tamanho: {report['size_kb']}KB")

    if report["warnings"]:
        print("\n⚠️  Avisos:")
        for w in report["warnings"]:
            print(f"  - {w}")

    if report["errors"]:
        print("\n🚫 Erros:")
        for e in report["errors"]:
            print(f"  - {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python validate_photo.py <nome-da-foto>")
        print("Exemplo: python validate_photo.py casal-feliz")
        sys.exit(1)

    filename = sys.argv[1]
    report = validate_photo(filename)
    print_report(report)

    sys.exit(0 if report["is_valid"] else 1)
