# -*- coding: utf-8 -*-
"""
Convierte los Apendice_*.md a PDF (carpeta PDFs/) para \\includepdf del template.
md -> HTML (con estilo academico) -> PDF via Chrome headless (--print-to-pdf).
Las imagenes se resuelven desde Figuras/ (el HTML temporal se escribe en esta carpeta).
"""
import os, re, subprocess, sys, pathlib

BASE = pathlib.Path(r"C:\Python\github-docs\docs\devops_ia\latex")
OUT  = BASE / "PDFs"
OUT.mkdir(exist_ok=True)

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(CHROME):
    CHROME = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

import markdown

CSS = """
@page { size: letter; margin: 2.2cm 2.2cm 2.0cm 2.2cm; }
* { box-sizing: border-box; }
body { font-family: Arial, "Helvetica Neue", sans-serif; font-size: 10.8pt;
       line-height: 1.42; color: #111; text-align: justify; }
h1 { font-size: 15pt; text-align: left; border-bottom: 2px solid #333;
     padding-bottom: 6px; margin: 0 0 14px 0; }
h2 { font-size: 12.5pt; margin: 16px 0 6px 0; color: #16324f; }
h3 { font-size: 11pt; margin: 12px 0 4px 0; color: #333; }
p  { margin: 6px 0; }
ul, ol { margin: 6px 0 6px 0; padding-left: 22px; }
li { margin: 2px 0; }
strong { color: #000; }
hr { border: none; border-top: 1px solid #ccc; margin: 14px 0; }
a { color: #16324f; text-decoration: none; word-break: break-all; }
table { border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 9.6pt;
        page-break-inside: avoid; }
th, td { border: 1px solid #999; padding: 4px 7px; text-align: left;
         vertical-align: top; word-wrap: break-word; }
th { background: #eef2f6; font-weight: bold; }
tr:nth-child(even) td { background: #f8f9fa; }
pre { background: #f5f5f5; border: 1px solid #ddd; border-radius: 3px;
      padding: 8px 10px; font-size: 8.9pt; line-height: 1.3;
      white-space: pre-wrap; word-wrap: break-word; overflow-wrap: anywhere;
      page-break-inside: avoid; }
code { font-family: Consolas, "Courier New", monospace; font-size: 9.2pt; }
p code { background: #f0f0f0; padding: 0 3px; border-radius: 2px; }
img { display: block; margin: 10px auto 2px auto; max-width: 78%;
      border: 1px solid #ccc; }
/* Figuras con el formato del template (rotulo+titulo arriba, Nota/Fuente abajo) */
figure.fig { margin: 16px 0; text-align: center; page-break-inside: avoid; }
figcaption.figlabel { font-size: 10.4pt; margin-bottom: 6px; line-height: 1.3; }
figure.fig img { display: block; margin: 4px auto; max-width: 82%;
                 border: 1px solid #ccc; }
.fuente { font-size: 9.4pt; margin-top: 5px; }
/* Tablas con el formato del template (rotulo+titulo arriba, Nota/Fuente abajo) */
.tabla { margin: 16px 0; text-align: center; page-break-inside: avoid; }
.tablabel { font-size: 10.4pt; margin-bottom: 5px; line-height: 1.3; }
.tabla table { width: auto; margin: 4px auto; text-align: left; }
.tabla .fuente { text-align: center; }
"""

def _style_tables(html, letter):
    n = [0]
    def repl(m):
        n[0] += 1
        desc, body = m.group(1).strip(), m.group(2)
        return (f'<div class="tabla">\n'
                f'<div class="tablabel"><strong>Tabla {letter}.{n[0]}.</strong> {desc}</div>\n'
                f'<table>{body}</table>\n'
                f'<div class="fuente"><em>Nota.</em> Fuente: Elaboración propia, 2026.</div>\n'
                f'</div>')
    return re.sub(r'<p>Tabla:\s*(.+?)</p>\s*<table>(.*?)</table>',
                  repl, html, flags=re.DOTALL)

FIG_RE = re.compile(
    r'!\[([^\]]*)\]\(([^)]+)\)\s*\n\s*\n\s*\*\s*(Figura[^\n]*?)\s*\*',
    re.MULTILINE)

def _fig_block(m):
    alt, path, cap = m.group(1), m.group(2), m.group(3)
    mm = re.match(r'(Figura\s+[A-Z]\.\d+)\.\s*(.*?)\s*Fuente:\s*(.*)', cap)
    if mm:
        label, title = mm.group(1), mm.group(2).strip()
        fuente = mm.group(3).strip().rstrip('.')
        fuente = (fuente[:1].upper() + fuente[1:]) if fuente else "Elaboración propia, 2026"
    else:
        label, title, fuente = "Figura", cap, "Elaboración propia, 2026"
    return (f'\n<figure class="fig">\n'
            f'<figcaption class="figlabel"><strong>{label}.</strong><br>{title}</figcaption>\n'
            f'<img src="{path}" alt="{alt}">\n'
            f'<div class="fuente"><em>Nota.</em> Fuente: {fuente}.</div>\n'
            f'</figure>\n')

def to_html(md_text, letter="X"):
    # Quita el H1 (el titulo va en la portadilla del apendice, no dentro del PDF)
    md_text = re.sub(r'^#\s+[^\n]*\n', '', md_text, count=1)
    # Reestructura cada figura al formato del template (rotulo+titulo arriba, imagen, Nota/Fuente)
    md_text = FIG_RE.sub(_fig_block, md_text)
    html = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list"],
        output_format="html5",
    )
    html = _style_tables(html, letter)
    return f"<!DOCTYPE html><html lang='es'><head><meta charset='utf-8'>" \
           f"<style>{CSS}</style></head><body>{html}</body></html>"

def render(md_path):
    name = md_path.stem  # Apendice_A_Metodologia
    letter = name.split("_")[1] if len(name.split("_")) > 1 else "X"
    html = to_html(md_path.read_text(encoding="utf-8"), letter)
    tmp = BASE / f"_tmp_{name}.html"
    tmp.write_text(html, encoding="utf-8")
    pdf = OUT / f"{name}.pdf"
    url = "file:///" + str(tmp).replace("\\", "/")
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
           "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
           "--virtual-time-budget=12000",
           f"--print-to-pdf={pdf}", url]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    tmp.unlink(missing_ok=True)
    ok = pdf.exists() and pdf.stat().st_size > 1000
    print(f"[{'OK' if ok else 'FAIL'}] {pdf.name}"
          + ("" if ok else f"  err: {r.stderr[-300:]}"))
    return ok

def main():
    mds = sorted(BASE.glob("Apendice_*.md"))
    if not mds:
        print("No hay Apendice_*.md"); sys.exit(1)
    print(f"Chrome: {CHROME}\nSalida: {OUT}\n")
    allok = all(render(m) for m in mds)
    print("\nTerminado." if allok else "\nHubo fallos.")
    sys.exit(0 if allok else 2)

if __name__ == "__main__":
    main()
