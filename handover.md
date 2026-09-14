# Handover

## Changelog

### 2026-09-14 16:17 — Order cost labelled approximate
- Heating oil row is now **Order cost (approximate cost)**.

### 2026-09-14 16:05 — Run out date format
- **Date format** helper on the Heating oil page: **System default** (locale `%x`) or DD/MM/YYYY, MM/DD/YYYY, YYYY-MM-DD, D Month YYYY.
- Run out date is no longer forced to ISO `YYYY-MM-DD`.
- Live: **Date format** is on the Heating oil card; System default currently shows `02/18/28`. Pick **DD/MM/YYYY** or **D Month YYYY** if you prefer.

### 2026-09-14 15:45 — Run out date on Heating oil
- Entities card order is Level, **Run out date**, Days until empty.
- Template sensor `sensor.heating_oil_run_out_date` is today plus the SENSiT `*_forecast_empty` days (YYYY-MM-DD).
- Live Heating oil page: Level, Run out date, Days until empty. At 522 days remaining the date is 2028-02-18.

### 2026-09-13 18:55 — Generic My Tank examples, no house IP
- README and dashboard snippet now use **My Tank** (`sensor.my_tank_*`) as the example device.
- Docs use `your ip address running HA` instead of a house-specific IP. Did not change the running Home Assistant instance.

### 2026-09-13 15:10 — Split out of home_assistant
- This repo is Heating oil only: SENSiT gauge snippet, price scrape, litres × cost.
- Presence simulator is now [presence_simulator](https://github.com/guido100uk/presence_simulator). Combined history stays in [home_assistant](https://github.com/guido100uk/home_assistant).
- Live house is unchanged: still copy `packages/heating_oil.yaml` through the HA Terminal.

### 2026-09-13 14:40 — Oil order litres times current price
- Heating oil page: type **Oil order litres** (1–5000 L, default 500) and see **Order cost** in GBP.
- Live check: at 1.1046 GBP/L, 500 L = £552.30 and 1000 L = £1104.60.

### 2026-09-13 14:30 — Scrapable £/L price
- URL and CSS-selector helpers (default Home Fuels Direct London / `#currentLivePrice`), pence toggle, REST sensor `sensor.heating_oil_price_per_litre`.

### 2026-09-13 14:20 — SENSiT gauge
- Kingspan Watchman SENSiT via HACS. Tank device My Tank. Sidebar **Heating oil** needle gauge plus litres / days / last reading.
