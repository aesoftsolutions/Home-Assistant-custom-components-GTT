# 🚌 gtt_torino - Home Assistant Custom Component

[![HACS Badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)

Integrazione personalizzata per Home Assistant che fornisce gli orari di arrivo in tempo reale di bus e tram GTT (Gruppo Torinese Trasporti) per una specifica fermata.

## 🌟 Caratteristiche

* Recupero dati in tempo reale (aggiornamento ogni 60 secondi).
* Configurazione tramite Interfaccia Utente (UI) con `config_flow`.
* Espone i prossimi passaggi come attributi del sensore.

## 💾 Installazione

Questa integrazione è progettata per essere installata tramite **HACS (Home Assistant Community Store)**.

### Prerequisiti

1.  Avere HACS installato e configurato.

### Passaggi di Installazione HACS

1.  Apri Home Assistant e vai su **HACS**.
2.  Vai su **Integrazioni**.
3.  Clicca sui tre puntini in alto a destra e seleziona **"Custom repositories"**.
4.  Incolla l'URL di questo repository GitHub: `https://github.com/IlTuoUsername/gtt_torino`
5.  Seleziona la categoria **"Integration"**.
6.  Cerca **"GTT Torino Real-Time Bus/Tram"** nella lista delle integrazioni di HACS e clicca su **"Download"**.
7.  **Riavvia** Home Assistant per assicurarti che il componente venga caricato.

## ⚙️ Configurazione

Dopo il riavvio, segui questi passaggi per configurare una fermata:

1.  Vai su **Impostazioni** -> **Dispositivi e Servizi**.
2.  Clicca su **"Aggiungi integrazione"** e cerca **"GTT Torino Real-Time Bus/Tram"**.
3.  Inserisci i dettagli richiesti:
    * **ID Fermata GTT:** Inserisci il numero di 4 cifre della tua fermata (es. `1762`).
    * **Nome:** Un nome descrittivo per il sensore (es. `Arrivi Fermi`).
4.  Completa il processo.

## 📊 Dati Esposti dal Sensore

L'integrazione crea un'entità `sensor.nome_assegnato` (es. `sensor.arrivi_fermi`).

| Proprietà | Descrizione |
| :--- | :--- |
| **Stato (State)** | L'orario di arrivo in tempo reale del primo mezzo (es. `10:09` o `5 min`). |
| `fermata_id` (Attributo) | L'ID della fermata configurata. |
| `arrivi_per_linea` (Attributo) | Una lista completa di dizionari con i prossimi passaggi in tempo reale, raggruppati per linea, ideale per card Lovelace avanzate. |
| `linea_in_arrivo` (Attributo) | La linea del primo mezzo in arrivo. |
| `direzione_prossimo` (Attributo) | La direzione del primo mezzo in arrivo. |

---

**NOTA BENE:** Assicurati di sostituire tutte le occorrenze di `@IlTuoUsername` e l'URL del repository con i tuoi dati reali prima di caricare su GitHub.
