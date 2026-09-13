# Handover

## Changelog

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
