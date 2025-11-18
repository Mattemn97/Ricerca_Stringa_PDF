# Ricerca_Stringa_PDF
Questo script permette di cercare una stringa o una REGEX all’interno di uno o più file PDF, con possibilità di analizzare intere cartelle in modo ricorsivo.
Alla fine genera automaticamente due file di report:
- File con la stringa.txt
- File senza stringa.txt

L’obiettivo è offrire un tool semplice, immediato e utilizzabile da terminale senza configurazioni complicate.

## ✨ Funzionalità principali
- ✔️ Estrazione testo dai PDF tramite PyPDF2
- ✔️ Ricerca case-insensitive
- ✔️ Modalità REGEX opzionale
- ✔️ Supporto a:
- singolo PDF
- cartella
- ricerca ricorsiva nelle sottocartelle
- ✔️ Barra di progresso con tqdm
- ✔️ Gestione robusta degli errori
- ✔️ Generazione automatica dei file:
- File con la stringa.txt
- File senza stringa.txt

## 📦 Requisiti
Installazione dei pacchetti necessari:
``` bash
pip install PyPDF2 tqdm
```

## ▶️ Utilizzo

Esegui lo script normalmente:
``` bash
python3 cerca_pdf.py
```

Ti guiderà passo passo:
1. Ti chiederà se vuoi usare una REGEX
2. Inserirai la stringa o il pattern
3. Indicherai un PDF singolo o una cartella
4. Lo script eseguirà la scansione e genererà i due file di output

## 📁 Output generati
Alla fine dell’analisi troverai nella cartella di lavoro:
- File con la stringa.txt

  Contiene tutti i PDF in cui la stringa/regex è stata trovata.

- File senza stringa.txt

  Contiene tutti i PDF in cui non è stata trovata.

## 📄 Esempio di esecuzione
``` bash
— Ricerca stringa/REGEX nei PDF (ricorsiva) —

Vuoi usare una REGEX? [s/N]: s
1) Inserisci la REGEX da cercare: fattura\s+\d+
2) Inserisci percorso PDF o cartella: ./documenti/

📄 PDF trovati: 128

Analisi PDF (REGEX): 100%|█████████████████████| 128/128 [00:08]

— RISULTATO —
✔ File con la stringa/regex: 47 → File con la stringa.txt
✘ File senza: 81 → File senza stringa.txt

Fatto! Report generati.
```

## 🧩 Struttura del codice
Lo script è organizzato in moduli funzionali:
- Estrazione testo PDF
- Ricerca semplice
- Ricerca REGEX
- Scansione ricorsiva delle cartelle
- Flusso guidato via terminale
- Entrypoint if __name__ == "__main__":
