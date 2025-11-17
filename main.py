#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ricerca di una stringa all'interno di uno o più PDF.
- Permette di analizzare un singolo file o un'intera cartella
- Usa PyPDF2 per l'estrazione del testo
- Mostra una barra di progresso (tqdm)
- Genera due file di log:
      • File con la stringa.txt
      • File senza stringa.txt
"""

import os
from tqdm import tqdm
from PyPDF2 import PdfReader


# ---------------- Lettura PDF ----------------
def extract_text_from_pdf(pdf_path):
    """Estrae il testo da un PDF. Ritorna stringa vuota in caso di errore."""
    try:
        reader = PdfReader(pdf_path)
        text = []
        for page in reader.pages:
            try:
                text.append(page.extract_text() or "")
            except Exception:
                continue
        return "\n".join(text)
    except Exception:
        return ""


# ---------------- Ricerca in un singolo PDF ----------------
def search_in_pdf(pdf_path, needle):
    """Ritorna True se la stringa è presente nel PDF."""
    text = extract_text_from_pdf(pdf_path).lower()
    return needle.lower() in text


# ---------------- Flusso guidato ----------------
def guided_flow():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("— Ricerca stringa nei PDF —\n")

    # 1) Stringa da cercare
    needle = input("1) Inserisci la stringa da cercare: ").strip()
    if not needle:
        print("❌ Nessuna stringa inserita. Interrompo.")
        return

    # 2) Percorso input (file o cartella)
    while True:
        path = input("\n2) Inserisci percorso PDF o cartella: ").strip()
        if os.path.isfile(path) and path.lower().endswith(".pdf"):
            pdf_files = [path]
            break
        elif os.path.isdir(path):
            pdf_files = [
                os.path.join(path, f)
                for f in os.listdir(path)
                if f.lower().endswith(".pdf")
            ]
            if not pdf_files:
                print("❌ Nessun PDF nella cartella. Riprova.")
                continue
            break
        else:
            print("❌ Percorso non valido. Riprova.")

    print(f"\n📄 PDF trovati: {len(pdf_files)}\n")

    # 3) File di output
    out_yes = "File con la stringa.txt"
    out_no = "File senza stringa.txt"

    found = []
    not_found = []

    # 4) Analisi con barra di progresso
    for pdf in tqdm(pdf_files, desc="Analisi PDF", unit="file"):
        if search_in_pdf(pdf, needle):
            found.append(pdf)
        else:
            not_found.append(pdf)

    # 5) Scrittura risultati
    with open(out_yes, "w", encoding="utf-8") as f:
        for p in found:
            f.write(p + "\n")

    with open(out_no, "w", encoding="utf-8") as f:
        for p in not_found:
            f.write(p + "\n")

    # 6) Report
    print("\n— RISULTATO —")
    print(f"✔ File con la stringa: {len(found)} → {out_yes}")
    print(f"✘ File senza stringa: {len(not_found)} → {out_no}")
    print("\nFatto! Puoi aprire i report generati.")


# ---------------- Entrypoint ----------------
if __name__ == "__main__":
    guided_flow()
