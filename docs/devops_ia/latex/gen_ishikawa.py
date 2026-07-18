# -*- coding: utf-8 -*-
"""Genera el diagrama de Ishikawa (causas del problema) para el perfil DevOps e IA."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(17.5, 9))
ax.set_xlim(0, 18.5)
ax.set_ylim(0, 9)
ax.axis("off")

spine_y = 4.5
spine_x0, spine_x1 = 1.2, 13.3

# --- Columna vertebral (flecha hacia el problema) ---
ax.annotate("", xy=(spine_x1 + 0.05, spine_y), xytext=(spine_x0, spine_y),
            arrowprops=dict(arrowstyle="-|>", lw=3, color="#1f3b57"))

# --- Cabeza: problema central ---
head = FancyBboxPatch((13.6, 2.5), 4.7, 4.0,
                      boxstyle="round,pad=0.1,rounding_size=0.15",
                      linewidth=2, edgecolor="#7a1f1f", facecolor="#f4d9d9")
ax.add_patch(head)
ax.text(15.95, 4.5,
        "Dependencia de procesos\nmanuales, sin asistencia de IA,\npara clasificar los issues\n(tipo y severidad) y resumir\nlos cambios de los commits,\nlo que deriva en inconsistencias\ne historial de cambios\nde baja trazabilidad",
        ha="center", va="center", fontsize=9.0, fontweight="bold", color="#7a1f1f")

# (titulo, color_borde, color_relleno, lado(+1 arriba/-1 abajo), x_union, [causas])
categories = [
    ("Métodos / Procesos", "#2e6f8e", "#d6ecf5", +1, 3.4,
        ["Triage de issues manual", "Commits sin guía de redacción", "Sin flujo asistido por IA"]),
    ("Personas", "#2e6f8e", "#d6ecf5", +1, 6.4,
        ["Clasificación por criterio individual", "Variabilidad entre usuarios", "Commits omitidos o genéricos"]),
    ("Datos", "#2e6f8e", "#d6ecf5", +1, 9.4,
        ["Issues sin clasificar (tipo/severidad)", "Mensajes 'fix' / 'update'", "Historial poco trazable"]),
    ("Herramientas", "#3a7d44", "#dcefd9", -1, 4.4,
        ["Plataforma sin modelos de IA", "Sin servicio de clasificación", "Sin servicio de resumen"]),
    ("Medición", "#3a7d44", "#dcefd9", -1, 7.4,
        ["Tipo y severidad no asignados", "Sin métricas de evaluación", "Calidad de commit no evaluada"]),
    ("Entorno", "#3a7d44", "#dcefd9", -1, 10.4,
        ["Volumen creciente de datos", "Equipos distribuidos", "Datasets públicos en inglés"]),
]

for title, ec, fc, side, jx, causes in categories:
    end_x = jx - 2.2
    end_y = spine_y + side * 3.1
    # hueso diagonal
    ax.plot([jx, end_x], [spine_y, end_y], color=ec, lw=2.2, zorder=1)
    # caja de categoria
    box = FancyBboxPatch((end_x - 1.15, end_y - 0.45), 2.3, 0.9,
                         boxstyle="round,pad=0.05,rounding_size=0.1",
                         linewidth=1.6, edgecolor=ec, facecolor=fc, zorder=3)
    ax.add_patch(box)
    ax.text(end_x, end_y, title, ha="center", va="center",
            fontsize=11, fontweight="bold", color=ec, zorder=4)
    # causas a lo largo del hueso
    for i, c in enumerate(causes):
        t = 0.34 + i * 0.20
        cx = jx + (end_x - jx) * t
        cy = spine_y + (end_y - spine_y) * t
        ax.text(cx + 0.15, cy, "- " + c, ha="left", va="center",
                fontsize=8.2, color="#333333", zorder=2)

ax.text(0.4, 8.7, "Diagrama de Ishikawa - Causas del problema",
        ha="left", va="center", fontsize=14, fontweight="bold", color="#1f3b57")

# Extiende los límites (invisible) para que el recorte "tight" no corte las cajas
ax.plot([-0.4, 18.4], [spine_y, spine_y], alpha=0.0)

fig.savefig(r"C:\Python\github-docs\docs\devops_ia\latex\ishikawa_issues_commits.png",
            dpi=150, bbox_inches="tight", facecolor="white")
print("OK: ishikawa_issues_commits.png generado")
