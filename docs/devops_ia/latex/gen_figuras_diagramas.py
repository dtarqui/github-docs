# -*- coding: utf-8 -*-
"""Diagramas (arquitectura / pipeline / despliegue / flujo) — cajas anchas, centradas, flechas uniformes."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = r"C:\Python\github-docs\docs\devops_ia\latex"
AZUL, VERDE, NAR, GRIS, MOR = "#1f3b57", "#2e7d5b", "#b36b00", "#555", "#6a3d8f"
FILL_B, FILL_G, FILL_AI, FILL_D, FILL_K = "#dceaf5", "#dcefe4", "#fdeecf", "#eeeeee", "#f2e9f7"

def box(ax, cx, cy, w, h, text, fc="#ffffff", ec=AZUL, fs=10, tc=None):
    """Caja centrada en (cx, cy)."""
    ax.add_patch(FancyBboxPatch((cx-w/2, cy-h/2), w, h, boxstyle="round,pad=0.02,rounding_size=0.06",
                                linewidth=1.6, edgecolor=ec, facecolor=fc, zorder=2))
    ax.text(cx, cy, text, ha="center", va="center", fontsize=fs, fontweight="bold",
            color=tc or ec, zorder=3)

def arrow(ax, p0, p1, color=GRIS, lw=1.8):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=13, lw=lw,
                                 color=color, zorder=1, shrinkA=0, shrinkB=0))

def centers(xL, xR, n, w):
    """Centros x de n cajas de ancho w, distribuidas uniformemente en [xL, xR]."""
    if n == 1: return [(xL+xR)/2]
    gap = (xR-xL - n*w)/(n-1)
    return [xL + w/2 + i*(w+gap) for i in range(n)]

def canvas(xmax, ymin, ymax):
    """Lienzo con alto proporcional al contenido (1:1) para evitar espacio en blanco."""
    fig, ax = plt.subplots(figsize=(xmax, ymax-ymin))
    ax.set_xlim(0, xmax); ax.set_ylim(ymin, ymax); ax.axis("off"); return fig, ax

# ==================== D1: Arquitectura ====================
fig, ax = canvas(12, 2.2, 7.35)
ax.text(0.3, 7.05, "Arquitectura de la plataforma Mini-GitHub (vista de contenedores)",
        fontsize=13, fontweight="bold", color=AZUL)
box(ax, 6.0, 6.35, 3.0, 0.7, "Usuario (navegador)", ec=GRIS, tc=GRIS)
box(ax, 6.0, 5.25, 4.6, 0.8, "Frontend  ·  Next.js / React  (:3000)", fc="#eef4fb", fs=10.5)
arrow(ax, (6.0, 6.0), (6.0, 5.65))
cx = centers(0.4, 11.6, 3, 3.6)   # Keycloak / negocio / IA
yrow, hrow = 3.55, 1.2
box(ax, cx[0], yrow, 3.6, hrow, "Keycloak\n(OIDC / JWT)", fc=FILL_K, ec=MOR, tc=MOR, fs=10.5)
box(ax, cx[1], yrow, 3.6, hrow,
    "Microservicios de negocio\n(Java · Spring)\nusers · issues · repository\nfiles · pull-request · organizations",
    fc=FILL_B, fs=8.8)
box(ax, cx[2], yrow, 3.6, hrow,
    "Servicios de IA (Python · FastAPI)\nissue-classifier  (:8095)\ncommit-summarizer  (:8096)",
    fc=FILL_AI, ec=NAR, tc=NAR, fs=9.2)
for c in cx: arrow(ax, (6.0, 4.85), (c, yrow+hrow/2))
ax.text(cx[2], yrow+hrow/2+0.14, "REST + JWT", ha="center", fontsize=8, color=NAR, style="italic")
ax.text(6.0, 2.55, "Persistencia:  PostgreSQL  ·  MongoDB  ·  git-server",
        ha="center", fontsize=9.5, color=GRIS, style="italic")
arrow(ax, (cx[1], yrow-hrow/2), (6.0, 2.75), color=GRIS)
fig.savefig(fr"{OUT}\fig_arquitectura.png", dpi=150, bbox_inches="tight", facecolor="white"); plt.close(fig)

# ==================== D2: Pipeline MLOps ====================
fig, ax = canvas(13, 0.9, 4.4)
ax.text(0.3, 4.2, "Pipeline MLOps por modelo (Apache Airflow) — mismo grafo para los 3 modelos",
        fontsize=12.5, fontweight="bold", color=AZUL)
yb = 2.55
cxs = centers(0.4, 6.6, 3, 1.9)
for c, t in zip(cxs, ["preprocess", "train", "evaluate"]):
    box(ax, c, yb, 1.9, 0.9, t, fc="#eef4fb", fs=10.5)
for i in range(len(cxs)-1):
    arrow(ax, (cxs[i]+0.95, yb), (cxs[i+1]-0.95, yb))
box(ax, 8.1, yb, 2.2, 1.15, "quality gate\nF1 / BLEU ≥ umbral", fc=FILL_AI, ec=NAR, tc=NAR, fs=9.5)
arrow(ax, (cxs[2]+0.95, yb), (8.1-1.1, yb))
box(ax, 11.1, yb+0.75, 3.4, 0.85, "register model\n→ deploy (/reload)", fc=FILL_G, ec=VERDE, tc=VERDE, fs=9.5)
box(ax, 11.1, yb-0.75, 3.4, 0.85, "model_rejected", fc="#f7dede", ec="#a33", tc="#a33", fs=10)
arrow(ax, (8.1+1.1, yb+0.25), (11.1-1.7, yb+0.75), color=VERDE)
arrow(ax, (8.1+1.1, yb-0.25), (11.1-1.7, yb-0.75), color="#a33")
ax.text(9.55, yb+0.62, "sí", fontsize=9, color=VERDE, fontweight="bold")
ax.text(9.55, yb-0.42, "no", fontsize=9, color="#a33", fontweight="bold")
ax.text(0.4, 1.15, "Model registry versionado (vNNN)  ·  hot-swap sin reiniciar  ·  umbral configurable por corrida",
        fontsize=8.8, color=GRIS, style="italic")
fig.savefig(fr"{OUT}\fig_pipeline_mlops.png", dpi=150, bbox_inches="tight", facecolor="white"); plt.close(fig)

# ==================== D3: Flujo del resumidor híbrido ====================
fig, ax = canvas(11, 0.15, 7.0)
ax.text(0.3, 6.7, "Modelo 2 — resumen de commit: sistema híbrido en cascada",
        fontsize=12.5, fontweight="bold", color=AZUL)
XC = 4.6
box(ax, XC, 6.05, 3.2, 0.66, "diff  (git diff)", ec=GRIS, tc=GRIS)
box(ax, XC, 5.05, 5.6, 0.7, "Normalización a formato NNGen  +  poda", fc="#eef4fb", fs=10)
arrow(ax, (XC, 5.72), (XC, 5.40))
niveles = [
    ("1. Heurística SE (ChangeScribe)", FILL_G, VERDE),
    ("2. Recuperación NNGen  (cos ≥ 0.5  ∧  BLEU ≥ 0.5)", FILL_G, VERDE),
    ("3. Generativo pointer-generator (beam search)", FILL_AI, NAR),
    ("4. Respaldo por nombres de archivo", FILL_D, GRIS),
]
wlev, hlev = 6.6, 0.62
ys = [3.95, 3.05, 2.15, 1.25]
arrow(ax, (XC, 4.70), (XC, ys[0]+hlev/2))
for i, (t, fc, ec) in enumerate(niveles):
    box(ax, XC, ys[i], wlev, hlev, t, fc=fc, ec=ec, tc=ec, fs=9.2)
    if i < len(niveles)-1:
        arrow(ax, (XC, ys[i]-hlev/2), (XC, ys[i+1]+hlev/2))
    arrow(ax, (XC+wlev/2, ys[i]), (XC+wlev/2+0.9, ys[i]), color=ec)
box(ax, 9.5, 2.6, 2.4, 2.9, "mensaje\nde commit\n(≤ 25 tokens)", ec=AZUL, fs=10)
ax.text(0.3, 0.45, "El resultado no siempre proviene de la red neuronal: responde el primer nivel cuya condición se cumple.",
        fontsize=8.4, color=GRIS, style="italic")
fig.savefig(fr"{OUT}\fig_flujo_resumidor.png", dpi=150, bbox_inches="tight", facecolor="white"); plt.close(fig)

# ==================== D4: Despliegue ECS/Fargate ====================
fig, ax = canvas(12, 0.0, 6.55)
ax.text(0.3, 6.4, "Despliegue en AWS — ECS Fargate (CDK)", fontsize=13, fontweight="bold", color=AZUL)
box(ax, 6.0, 5.55, 11.0, 0.7, "Internet  →  Balanceadores ALB  (frontend · keycloak · repository · shared-api)",
    fc="#eef4fb", fs=10)
ax.add_patch(FancyBboxPatch((0.5, 1.05), 11.0, 3.95, boxstyle="round,pad=0.02,rounding_size=0.08",
                            linewidth=1.4, edgecolor=GRIS, facecolor="#fafafa", zorder=0))
ax.text(0.75, 4.72, "VPC  ·  ECS cluster “github-ecs” (Fargate)  ·  Service Discovery (Cloud Map github.local)",
        fontsize=9.3, color=GRIS, fontweight="bold")
arrow(ax, (6.0, 5.2), (6.0, 5.0))
servs = [("frontend", FILL_B, AZUL), ("keycloak", FILL_K, MOR), ("users", FILL_B, AZUL), ("issues", FILL_B, AZUL),
         ("repository", FILL_B, AZUL), ("pull-request", FILL_B, AZUL), ("organizations", FILL_B, AZUL), ("git-server", FILL_D, GRIS),
         ("issue-classifier", FILL_AI, NAR), ("commit-summarizer", FILL_AI, NAR), ("mongodb", FILL_D, GRIS)]
colcx = centers(0.9, 11.1, 4, 2.45)
row_y = [3.95, 3.15, 2.35]
for i, (name, fc, ec) in enumerate(servs):
    c = colcx[i % 4]; y = row_y[i // 4]
    box(ax, c, y, 2.45, 0.6, name, fc=fc, ec=ec, tc=ec, fs=8.8)
box(ax, colcx[3], 1.55, 2.45, 0.55, "RDS PostgreSQL", fc=FILL_D, ec=GRIS, tc=GRIS, fs=8.8)
box(ax, colcx[0], 0.5, 3.2, 0.75, "ECR: imágenes de\nlos 2 servicios de IA", fc=FILL_AI, ec=NAR, tc=NAR, fs=8.6)
arrow(ax, (colcx[0], 0.875), (colcx[0], 2.35-0.30), color=NAR)
ax.text(6.6, 0.5, "resto de imágenes: Docker Hub / build local  ·  despliegue manual (cdk deploy)",
        fontsize=8.3, color=GRIS, style="italic")
fig.savefig(fr"{OUT}\fig_despliegue_ecs.png", dpi=150, bbox_inches="tight", facecolor="white"); plt.close(fig)

print("OK: 4 diagramas regenerados")
