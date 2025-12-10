# GTT - Home Assistant Custom components

<p align="center">
  <img src="https://github.com/aesoftsolutions/Home-Assistant-custom-components-GTT/blob/main/assets/brand/logo@2x.png" width="300px">
</p>

[![HACS Badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs) ![GitHub License](https://img.shields.io/github/license/aesoftsolutions/Home-Assistant-custom-components-GTT)

![GitHub Release](https://img.shields.io/github/v/release/aesoftsolutions/Home-Assistant-custom-components-GTT) [![Maintenancebadge]][maintenance]

[![Websitebadge]][website] [![Forum][forumbadge]][forum]

---

This Home Assistant integration provides information about public transport arrivals at the user's requested stop.

* Real-time data retrieval (update every 60 seconds).
* Configuration via User Interface (UI).
* Exposes the next steps as sensor attributes.

---

## 📦 Installation

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

### Start integration dialog

The configuration of integration is made via Home Assistant GUI
1. Open `Settings` / `Devices & services`
2. Click on `Add Integration` button
3. Search for `GTT stop arrivals`
4. Click on integration to start
5. Enter required stop information:
  * **GTT Stop ID:** Enter the number of your stop (e.g., `466`).
  * **Name:** A descriptive name for the sensor (e.g., `GTT fermata 466`).
6. Enter optional area information:
  * **Device name:** A descriptive name for the device (e.g., `GTT fermata 466`).
  * **Area:** An area to assign the newly created sensor to.

## 📊 Sensor exposed data

The integration creates a `sensor.assigned_name` entity (e.g. `sensor.gtt_fermata_466`).

| Property | Description |
| :--- | :--- |
| **State** | The real-time arrival time of the first vehicle (es. `10:09`). |
| `stop_id` | The ID of the configured stop. |
| `stop_name` | The name of the configured stop. |
| `stop_desc` | The description of the configured stop (road intersection). |
| `stop_city` | The city where the configured stop is located. |
| `line_arrivals` | A comprehensive dictionary list with real-time next arrivals, grouped by line, ideal for advanced Lovelace cards. |
| `incoming_line` | The line of the first arriving vehicle.. |
| `direction_next` | The direction of the first arriving vehicle. |

`line_arrivals` is structured with a list of the following attributes:

| Property | Description |
| :--- | :--- |
| `line` | The ID of the line. |
| `direction` | The destination of the line. |
| `next_rt` | The list of next arrivals at the stop for the line. |
| `first_arrival` | The time of the next arrival at the stop for the line. |

### Attributes structure representation (example with stop 466)

```yaml
stop_id: 466
stop_name: STATUTO
stop_desc: "P. STATUTO PER V. CIBRARIO"
stop_city: "TORINO"
line_arrivals:
  - line: '13'
    direction: PARELLA, PIAZZA CAMPANELLA
    next_rt: 
      - '10:22' 
      - '10:28' 
      - '10:45' 
      - '10:53' 
      - '11:02'
    first_arrival: '10:22'
  - line: 56
    direction: GRUGLIASCO, CORSO TIRRENO
    next_rt: 
      - '10:25' 
      - '10:37' 
      - '10:46' 
      - '11:00'
    first_arrival: '10:25'
  - line: 65
    direction: PARELLA, VIA SERVAIS
    next_rt: 
      - '10:34' 
      - '10:54' 
      - '11:14'
    first_arrival: '10:34'
incoming_line: 13
direction_next: PARELLA, PIAZZA CAMPANELLA
```

## 🎭 Here are some advanced examples of using the attributes provided by the integration

### Lovelace markdown card example sensor

For this example, we're using `config-template-card` to also include a title in the card. If you haven't already downloaded it, you can get it through HACS.

```yaml
type: custom:config-template-card
title: GTT — Fermata {{ state_attr('sensor.gtt_fermata_466', 'stop_id') }}
primary: Prossimi passaggi per linea
entities:
  - sensor.gtt_fermata_466
card:
  type: markdown
  content: >
    **🚏 Fermata {{ state_attr('sensor.gtt_fermata_466', 'stop_id') }}** ({{
    state_attr('sensor.gtt_fermata_466', 'stop_name') }})

    {% set linee = state_attr('sensor.gtt_fermata_466', 'line_arrivals') %}

    {% if not linee %}
      Nessun dato disponibile.
    {% else %}

      {% for l in linee %}
        {% set rt = l.next_rt|default([]) %}
        {% set next3 = rt[0:3] %}
        {% if not next3 %}
        {% else %}
      🚍 **{{ l.line }}** - {{ l.direction }}
      🕙 {{ next3 | join(", ") }}
        {% endif %}
      {% endfor %}
    {% endif %}
```
### Custom GTT Timeline card

To use this custom card you need to follow these steps
1. Download `gtt-timeline-card.js` from [this link](https://raw.githubusercontent.com/aesoftsolutions/Home-Assistant-custom-components-GTT/refs/heads/main/assets/gtt-timeline-card.js)
2. Copy to `config\www` of your Home Assistant installation (using a file editor)
3. Add resource:
   - Settings → Dashboards → ⋮ → Resources
   - **+ ADD RESOURCE**
   - URL: `/local/gtt-timeline-card.js`
   - Type: **JavaScript Module**
4. Hard refresh browser (Ctrl+Shift+R)

5. Edit dashboard → Add card
6. Search **Manual**
7. In the editor, insert the following lines of code.
```yaml
type: custom:gtt-timeline-card
entity: sensor.gtt_fermata_466
```

---

## 🔍 Troubleshooting

### Card doesn't appear
- Check browser console (F12) for errors
- Verify resource (`gtt-timeline-card.js`) is loaded in Dashboard → Resources
- Hard refresh the dashboard: Ctrl+Shift+R
- Manually clean browser cache in History settings

### Sensors not found
- Verify sensor names in Developer Tools → States

### Stop data not loading
- The current version of the GTT integration only uses real-time arrival data provided by the API. If no real-time information is available for the line, the integration displays N/A.

---

## 📝 Changelog

### v0.3.0 (2025-12-05)
- 🌐 Fix some localization

### v0.2.0 (2025-12-05)
- 🎉 Beta public release (already available in HACS)
- ✨ Custom card
- 🎨 Add more stop information

### v0.1.0 (2025-11-28)
- 🎉 Initial test release (internal only)
- ✨ Markdown code for dashboard

---

## Trademark Legal Notices

All product names, trademarks and registered trademarks in the images in this repository, are property of their respective owners.
All images in this repository are used by the author for identification purposes only.
The use of these names, trademarks and brands appearing in these image files, do not imply endorsement.

[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg
[github_release]: https://github.com/aesoftsolutions/Home-Assistant-custom-components-GTT/releases
[github_license]: https://img.shields.io/github/release-date/aesoftsolutions/Home-Assistant-custom-components-GTT
[maintenancebadge]: https://img.shields.io/badge/Maintained%3F-Yes-brightgreen.svg
[maintenance]: https://github.com/aesoftsolutions/Home-Assistant-custom-components-GTT/graphs/commit-activity
[website]: https://hassiohelp.eu/
[websitebadge]: https://img.shields.io/website?down_message=Offline&label=HssioHelp&logoColor=blue&up_message=Online&url=https%3A%2F%2Fhassiohelp.eu
[forum]: https://forum.hassiohelp.eu/
[forumbadge]: https://img.shields.io/badge/HassioHelp-Forum-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA0ppVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8%2BIDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNS1jMDIxIDc5LjE1NTc3MiwgMjAxNC8wMS8xMy0xOTo0NDowMCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6ODcxMjY2QzY5RUIzMTFFQUEwREVGQzE4OTI4Njk5NDkiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6ODcxMjY2QzU5RUIzMTFFQUEwREVGQzE4OTI4Njk5NDkiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTQgKFdpbmRvd3MpIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9ImFkb2JlOmRvY2lkOnBob3Rvc2hvcDo0MWVhZDAwNC05ZWFmLTExZWEtOGY3ZS1mNzQ3Zjc1MjgyNGIiIHN0UmVmOmRvY3VtZW50SUQ9ImFkb2JlOmRvY2lkOnBob3Rvc2hvcDo0MWVhZDAwNC05ZWFmLTExZWEtOGY3ZS1mNzQ3Zjc1MjgyNGIiLz4gPC9yZGY6RGVzY3JpcHRpb24%2BIDwvcmRmOlJERj4gPC94OnhtcG1ldGE%2BIDw/eHBhY2tldCBlbmQ9InIiPz4xQPr3AAADq0lEQVR42rRVW2wMURj%2Bz5lL7V27KG26KIuUEJemdalu3VN3Ei/ipSWUuIV4FB4kHrwo8VLRROJBgkYElZCi4olG4rVoROOSbTa0u7pzO/6Z2Zmd3Z2uevBn/8zsf/7zff/tnKGMMRi/pjM6/j08oKiqCm1tbTA4OAhuoqkS8KKPVjceOcgJngkfnl%2B5JiWH0pQvcfUPhULQ0dEBPp8PDBZZlqGyshLGFKG0fHHr/QfNlxnbjFp7uOcl8VVVj%2BXu9XohkUgY2NRpdJMpc5qWN5971zu7ftsWkSAX2iKLYg3NZ/t6Kxbu2Oi2x4g8IxSKSDR2tLXh2JOn3nAkKv9GAzPtyigS%2BSdV1B3sejhv09lTxTBcCXjRK9buu96%2BZG/7dUYEryK59EXWewNcza7zl%2Br237kpessC4yIITIlGGk88666OtR6VMFKmZhZY9sGsdw1ATgFU1O7et%2Brki56JVUtqsl4kl0CVUjB57vo1Tad7X4Wj9U1S0vRj8HfRSQKVC5auPN7zctqiPTs1Rz2pBV6xcOuq%2BkOPusVAeZWxDg5wl%2Bhz1vW%2BpBFMDIYXt9y%2BF6lr2a6kR7IEmipDeFYsRkVewFcTyAXcBtNMhTxCTTErUxZdu96qLW8varhFsyrnQCQOYNXU8qBp//4TH/jkHZ3UCTXFoncQGKciP1SiN1JDVY2IJwgEjq3jYMVsZgC/HSBw9RnA8CgBjmS3MkdefE638sCV0WGQk9/QXYNRicH%2B7eWwYUGpOT4oq%2Bfq0Upw4SEPVOCLnwOWp5o%2BgskfWEoZe8Qg6CGwcp7XWFVxTc0UYdlMrLmQsP8zVuQcWFNiORFCTSvRQTWQs6W101SRXE7/xiDSBeC5BKywRLx/KqbuA44TYUQS4HHfsLHEcZyhulP32zjEUwL2ACuPt24%2BR0HhnONJBA8IoRlG/4P4/%2B57FTTyC9bUMAQk8OJ9Am69VsHjC2cOJbPaU0iQn4DxrjnSwVwp4eF2XwC63uBVLCchpXgQPAiUUrM8xBwlfeqs%2Bc7JwFn//KHKtAI8IkVejFgIgY8p2etEB7cPDbF32wSE8pwx926XTx6pAcPxxmFlzIo2o/qPy84sb4JTSMb7v3qiGFhJIaAzw1wbkmh8tu4IrqKm4v347V1qmvQGKvjJjEyf7v/pX3GmrGp%2BtT73UDyRHCPLMBDKwUj801dl4P7Fwc8fh0rLwiaBrp2dN2Do%2Bxfb%2Bd%2BE2GwEe%2BEPTYaW1gNQUiKaBP9T/ggwAJik5dEKYSC3AAAAAElFTkSuQmCC
