# 🚌 GTT - Home Assistant Custom components

[![HACS Badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs) ![GitHub License](https://img.shields.io/github/license/aesoftsolutions/Home-Assistant-custom-components-GTT)

![GitHub Release](https://img.shields.io/github/v/release/aesoftsolutions/Home-Assistant-custom-components-GTT) [![Maintenancebadge]][maintenance] [![GitHub issuesbadge]][github_issues]

[![Forum][forumbadge]][forum]

**[Italiano](#v-it) | [English](#v-en)**

---

<a name="v-it"></a>

Questa integrazione Home Assistant fornisce informazioni sugli arrivi dei mezzi pubblici alla fermata richiesta dall'utente.

## 📑 Contenuti

- [📦 Installazione](#installation-it)
- [🔧 Configurazione](#configuration-it)
- [🆘 Contributi](#contributions-it)

---

## 📦 Installazione
<a name="installation-it"></a>

### Installazione via HACS (Raccomandata)

Installa [HACS](https://hacs.xyz/), questo ti consentirà di effettuare facilmente gli aggiornamenti.

* L'aggiunta di `GTT stop arrivals` ad HACS può essere effettuata utilizzando questo pulsante:

[![image](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=aesoftsolutions&repository=ha-gtt&category=integration)

> [!NOTE]
> Se il pulsante sopra non funziona, aggiungi `https://github.com/aesoftsolutions/Home-Assistant-custom-components-GTT` come repository personalizzato di tipo **Integrazione** in HACS.

* Clicca Installa `GTT stop arrivals`.
* Riavvia Home Assistant.

### Installazione manuale

1. Utilizzando lo strumento scelto, apri la cartella per la configurazione HA (dove trovi `configuration.yaml`).
2. Se non è presente una cartella `custom_components`, è necessario crearla.
3. Nella cartella `custom_components` crea una nuova cartella chiamata `ha_gtt`.
4. Scarica tutti i file dalla cartella `custom_components/ha_gtt/` in questo repository.
5. Inserisci i file scaricati nella nuova cartella creata nel `passaggio 3`.
6. Riavvia Home Assistant

## 🔧 Configurazione
<a name="configuration-it"></a>

### Avvia la finestra di dialogo di integrazione
La configurazione dell'integrazione avviene tramite l'interfaccia grafica utente di Home Assistant
1. Apri `Impostazioni` / `Dispositivi e servizi`
2. Fare clic sul pulsante `Aggiungi integrazione`
3. Cerca `GTT stop arrivals`
4. Clicca sull'integrazione per iniziare

## 🆘 Contributi
<a name="contributions-it"></a>

---

<a name="v-en"></a>

This Home Assistant integration provides information about public transport arrivals at the user's requested stop.

## 📑 Table of Contents

- [📦 Installation](#installation-en)
- [🔧 Configuration](#configuration-en)
- [🆘 Contributions](#contributions-en)

---

## 📦 Installation
<a name="installation-en"></a>

### Installation via HACS (Recommended)

Have [HACS](https://hacs.xyz/) installed, this will allow you to update easily.

* Adding `GTT stop arrivals` to HACS can be done using this button:

[![image](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=aesoftsolutions&repository=ha-gtt&category=integration)

> [!NOTE]
> If the button above doesn't work, add `https://github.com/aesoftsolutions/Home-Assistant-custom-components-GTT` as a custom repository of type **Integration** in HACS.

* Click Install on the `GTT stop arrivals` card.
* Restart Home Assistant.

### Manual Installation

1. Using the tool of choice open the folder for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` folder there, you need to create it.
3. In the `custom_components` folder create a new folder called `ha_gtt`.
4. Download all the files from the `custom_components/ha_gtt/` folder in this repository.
5. Place the files you downloaded in the new folder you created in `step 3`.
6. Restart Home Assistant

## 🔧 Configuration
<a name="configuration-en"></a>

### Start integration dialog
The configuration of integration is made via Home Assistant GUI
1. Open `Settings` / `Devices & services`
2. Click on `Add Integration` button
3. Search for `GTT stop arrivals`
4. Click on integration to start

## 🆘 Contributions
<a name="contributions-en"></a>

---

## Trademark Legal Notices

All product names, trademarks and registered trademarks in the images in this repository, are property of their respective owners.
All images in this repository are used by the author for identification purposes only.
The use of these names, trademarks and brands appearing in these image files, do not imply endorsement.

[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg
[github latest release]: https://img.shields.io/github/v/release/aesoftsolutions/Home-Assistant-custom-components-GTT
[github_release]: https://github.com/aesoftsolutions/Home-Assistant-custom-components-GTT/releases
[github release date]: https://img.shields.io/github/release-date/aesoftsolutions/Home-Assistant-custom-components-GTT
[github_license]: https://img.shields.io/github/release-date/aesoftsolutions/Home-Assistant-custom-components-GTT
[maintenancebadge]: https://img.shields.io/badge/Maintained%3F-Yes-brightgreen.svg
[maintenance]: https://github.com/aesoftsolutions/Home-Assistant-custom-components-GTT/graphs/commit-activity
[github issuesbadge]: https://img.shields.io/github/issues/aesoftsolutions/Home-Assistant-custom-components-GTT
[github issues]: https://github.com/aesoftsolutions/Home-Assistant-custom-components-GTT/issues
[forum]: https://forum.hassiohelp.eu/
[forumbadge]: https://img.shields.io/badge/HassioHelp-Forum-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA0ppVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8%2BIDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNS1jMDIxIDc5LjE1NTc3MiwgMjAxNC8wMS8xMy0xOTo0NDowMCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6ODcxMjY2QzY5RUIzMTFFQUEwREVGQzE4OTI4Njk5NDkiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6ODcxMjY2QzU5RUIzMTFFQUEwREVGQzE4OTI4Njk5NDkiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTQgKFdpbmRvd3MpIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9ImFkb2JlOmRvY2lkOnBob3Rvc2hvcDo0MWVhZDAwNC05ZWFmLTExZWEtOGY3ZS1mNzQ3Zjc1MjgyNGIiIHN0UmVmOmRvY3VtZW50SUQ9ImFkb2JlOmRvY2lkOnBob3Rvc2hvcDo0MWVhZDAwNC05ZWFmLTExZWEtOGY3ZS1mNzQ3Zjc1MjgyNGIiLz4gPC9yZGY6RGVzY3JpcHRpb24%2BIDwvcmRmOlJERj4gPC94OnhtcG1ldGE%2BIDw/eHBhY2tldCBlbmQ9InIiPz4xQPr3AAADq0lEQVR42rRVW2wMURj%2Bz5lL7V27KG26KIuUEJemdalu3VN3Ei/ipSWUuIV4FB4kHrwo8VLRROJBgkYElZCi4olG4rVoROOSbTa0u7pzO/6Z2Zmd3Z2uevBn/8zsf/7zff/tnKGMMRi/pjM6/j08oKiqCm1tbTA4OAhuoqkS8KKPVjceOcgJngkfnl%2B5JiWH0pQvcfUPhULQ0dEBPp8PDBZZlqGyshLGFKG0fHHr/QfNlxnbjFp7uOcl8VVVj%2BXu9XohkUgY2NRpdJMpc5qWN5971zu7ftsWkSAX2iKLYg3NZ/t6Kxbu2Oi2x4g8IxSKSDR2tLXh2JOn3nAkKv9GAzPtyigS%2BSdV1B3sejhv09lTxTBcCXjRK9buu96%2BZG/7dUYEryK59EXWewNcza7zl%2Br237kpessC4yIITIlGGk88666OtR6VMFKmZhZY9sGsdw1ATgFU1O7et%2Brki56JVUtqsl4kl0CVUjB57vo1Tad7X4Wj9U1S0vRj8HfRSQKVC5auPN7zctqiPTs1Rz2pBV6xcOuq%2BkOPusVAeZWxDg5wl%2Bhz1vW%2BpBFMDIYXt9y%2BF6lr2a6kR7IEmipDeFYsRkVewFcTyAXcBtNMhTxCTTErUxZdu96qLW8varhFsyrnQCQOYNXU8qBp//4TH/jkHZ3UCTXFoncQGKciP1SiN1JDVY2IJwgEjq3jYMVsZgC/HSBw9RnA8CgBjmS3MkdefE638sCV0WGQk9/QXYNRicH%2B7eWwYUGpOT4oq%2Bfq0Upw4SEPVOCLnwOWp5o%2BgskfWEoZe8Qg6CGwcp7XWFVxTc0UYdlMrLmQsP8zVuQcWFNiORFCTSvRQTWQs6W101SRXE7/xiDSBeC5BKywRLx/KqbuA44TYUQS4HHfsLHEcZyhulP32zjEUwL2ACuPt24%2BR0HhnONJBA8IoRlG/4P4/%2B57FTTyC9bUMAQk8OJ9Am69VsHjC2cOJbPaU0iQn4DxrjnSwVwp4eF2XwC63uBVLCchpXgQPAiUUrM8xBwlfeqs%2Bc7JwFn//KHKtAI8IkVejFgIgY8p2etEB7cPDbF32wSE8pwx926XTx6pAcPxxmFlzIo2o/qPy84sb4JTSMb7v3qiGFhJIaAzw1wbkmh8tu4IrqKm4v347V1qmvQGKvjJjEyf7v/pX3GmrGp%2BtT73UDyRHCPLMBDKwUj801dl4P7Fwc8fh0rLwiaBrp2dN2Do%2Bxfb%2Bd%2BE2GwEe%2BEPTYaW1gNQUiKaBP9T/ggwAJik5dEKYSC3AAAAAElFTkSuQmCC
