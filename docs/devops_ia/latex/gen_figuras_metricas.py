# -*- coding: utf-8 -*-
"""Figuras de métricas (números REALES de los ENTRENAMIENTO.md / labels / metricas)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = r"C:\Python\github-docs\docs\devops_ia\latex"

# Paleta Okabe-Ito (CVD-safe, validada): Precision / Recall / F1
C_P, C_R, C_F1 = "#0072B2", "#E69F00", "#009E73"
C_BAR, C_BAR2 = "#0072B2", "#56B4E9"
plt.rcParams.update({
    "font.size": 11, "axes.titlesize": 13, "axes.titleweight": "bold",
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": "#e6e6e6", "grid.linewidth": 0.8,
    "axes.axisbelow": True, "figure.facecolor": "white", "axes.facecolor": "white",
})

def barlabels(ax, rects, fmt="{:.3f}", fs=8.5):
    for r in rects:
        h = r.get_height()
        ax.text(r.get_x()+r.get_width()/2, h+0.012, fmt.format(h),
                ha="center", va="bottom", fontsize=fs, color="#333")

# ---------- FIG 1: Clasificador de TIPO (por clase) ----------
clases = ["bug", "feature", "question"]
P = [0.818, 0.831, 0.447]; R = [0.812, 0.783, 0.588]; F1 = [0.815, 0.806, 0.508]
x = np.arange(len(clases)); w = 0.26
fig, ax = plt.subplots(figsize=(8, 4.6))
b1 = ax.bar(x-w, P, w, label="Precisión", color=C_P)
b2 = ax.bar(x,   R, w, label="Recall",    color=C_R)
b3 = ax.bar(x+w, F1, w, label="F1",        color=C_F1)
for b in (b1, b2, b3): barlabels(ax, b)
ax.set_xticks(x); ax.set_xticklabels(clases); ax.set_ylim(0, 1.0)
ax.set_ylabel("Puntuación"); ax.set_title("Clasificador de tipo de issue — métricas por clase (test)")
ax.axhline(0.7097, ls="--", lw=1.2, color="#666")
ax.text(len(clases)-1+w+0.02, 0.7097+0.015, "F1-macro = 0.710", ha="right", fontsize=8.5, color="#444")
ax.legend(frameon=False, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.10))
fig.tight_layout()
fig.savefig(fr"{OUT}\fig_clasif_tipo.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.close(fig)

# ---------- FIG 2: Clasificador de SEVERIDAD (por clase) ----------
clases2 = ["crítica", "alta", "media", "baja"]
P2 = [0.506, 0.218, 0.824, 0.185]; R2 = [0.579, 0.233, 0.795, 0.203]; F12 = [0.540, 0.225, 0.810, 0.193]
x2 = np.arange(len(clases2))
fig, ax = plt.subplots(figsize=(8, 4.6))
b1 = ax.bar(x2-w, P2, w, label="Precisión", color=C_P)
b2 = ax.bar(x2,   R2, w, label="Recall",    color=C_R)
b3 = ax.bar(x2+w, F12, w, label="F1",        color=C_F1)
for b in (b1, b2, b3): barlabels(ax, b)
ax.set_xticks(x2); ax.set_xticklabels(clases2); ax.set_ylim(0, 1.0)
ax.set_ylabel("Puntuación"); ax.set_title("Clasificador de severidad — métricas por clase (test)")
ax.axhline(0.442, ls="--", lw=1.2, color="#666")
ax.text(len(clases2)-1+w+0.02, 0.442+0.015, "F1-macro = 0.442", ha="right", fontsize=8.5, color="#444")
ax.legend(frameon=False, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.10))
fig.tight_layout()
fig.savefig(fr"{OUT}\fig_clasif_severidad.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.close(fig)

# ---------- FIG 3: Distribución de clases (soporte del test) ----------
fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
# tipo
ct = ["bug", "feature", "question"]; st = [13366, 13821, 2813]
axes[0].barh(ct[::-1], st[::-1], color=C_BAR)
for i, v in enumerate(st[::-1]):
    axes[0].text(v+200, i, f"{v:,}", va="center", fontsize=9, color="#333")
axes[0].set_title("Tipo de issue"); axes[0].set_xlim(0, 16000); axes[0].set_xlabel("Nº de ejemplos (test)")
# severidad
cs = ["crítica", "alta", "media", "baja"]; ss = [1968, 2002, 16054, 1388]
order = np.argsort(ss)  # asc
axes[1].barh([cs[i] for i in order], [ss[i] for i in order], color=C_BAR2)
for i, idx in enumerate(order):
    axes[1].text(ss[idx]+250, i, f"{ss[idx]:,}", va="center", fontsize=9, color="#333")
axes[1].set_title("Severidad"); axes[1].set_xlim(0, 18500); axes[1].set_xlabel("Nº de ejemplos (test)")
fig.suptitle("Distribución de clases en el conjunto de prueba (evidencia del desbalance)", fontweight="bold")
fig.tight_layout()
fig.savefig(fr"{OUT}\fig_distribucion_clases.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.close(fig)

# ---------- FIG 4: Evolución del resumidor (BLEU-4 y ROUGE-L) ----------
fig, axes = plt.subplots(1, 2, figsize=(9, 4.4))
fases = ["seq2seq\nbase", "pointer-\ngenerator"]
bleu = [6.68, 11.62]; rouge = [0.2092, 0.2927]
r = axes[0].bar(fases, bleu, color=[C_BAR2, C_F1], width=0.55)
barlabels(axes[0], r, fmt="{:.2f}", fs=10)
axes[0].set_title("BLEU-4 (test, corpus Java)"); axes[0].set_ylim(0, 14); axes[0].set_ylabel("BLEU-4")
axes[0].text(0.5, 13.0, "+74 %", ha="center", fontsize=10, color="#009E73", fontweight="bold")
r = axes[1].bar(fases, rouge, color=[C_BAR2, C_F1], width=0.55)
barlabels(axes[1], r, fmt="{:.3f}", fs=10)
axes[1].set_title("ROUGE-L (test, corpus Java)"); axes[1].set_ylim(0, 0.36); axes[1].set_ylabel("ROUGE-L (F)")
axes[1].text(0.5, 0.335, "+40 %", ha="center", fontsize=10, color="#009E73", fontweight="bold")
fig.suptitle("Efecto del mecanismo de copia (pointer-generator) sobre el seq2seq base", fontweight="bold")
fig.tight_layout()
fig.savefig(fr"{OUT}\fig_resumidor_evolucion.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.close(fig)

# ---------- FIG 5: BLEU-4 por lenguaje (modelo multilenguaje v3) ----------
langs = ["C#", "JavaScript", "Python", "C++", "Java"]
vals = [12.72, 12.19, 11.83, 11.82, 9.52]
fig, ax = plt.subplots(figsize=(8, 4.4))
cols = [C_BAR]*len(langs); cols[-1] = C_R  # Java resaltado (trade-off)
rr = ax.bar(langs, vals, color=cols, width=0.62)
barlabels(ax, rr, fmt="{:.2f}", fs=9.5)
ax.axhline(11.79, ls="--", lw=1.3, color="#666")
ax.text(len(langs)-0.5, 11.79+0.15, "Global = 11.79", ha="right", fontsize=9, color="#444")
ax.set_ylim(0, 14.5); ax.set_ylabel("BLEU-4")
ax.set_title("Resumidor multilenguaje (v3) — BLEU-4 por lenguaje (test)")
ax.text(4, 9.52-1.15, "trade-off Java\n(-2.1 vs solo-Java)", ha="center", fontsize=8, color="#B36B00")
fig.tight_layout()
fig.savefig(fr"{OUT}\fig_resumidor_lenguaje.png", dpi=150, bbox_inches="tight", facecolor="white")
plt.close(fig)

print("OK: 5 figuras de metricas generadas")
