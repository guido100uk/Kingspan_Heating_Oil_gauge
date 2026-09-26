from pathlib import Path

import yaml

from conftest import ROOT

PACKAGE_PATH = ROOT / "packages" / "heating_oil.yaml"
OIL_DASH_PATH = ROOT / "dashboards" / "oil_tank.yaml"
DEFAULT_URL = "https://homefuelsdirect.co.uk/home/heating-oil-prices/london"


def load_package() -> dict:
    return yaml.safe_load(PACKAGE_PATH.read_text(encoding="utf-8"))


def test_heating_oil_package_exists_and_parses():
    assert PACKAGE_PATH.is_file()
    package = load_package()
    assert isinstance(package, dict)


def test_price_url_helper_defaults_to_london_hfd():
    url = load_package()["input_text"]["heating_oil_price_url"]
    assert url["initial"] == DEFAULT_URL
    assert url["max"] == 255
    assert url["name"] == "Oil price page URL"


def test_price_selector_defaults_to_current_live_price():
    sel = load_package()["input_text"]["heating_oil_price_selector"]
    assert sel["initial"] == "#currentLivePrice"
    assert sel["name"] == "Oil price CSS selector"


def test_price_is_pence_defaults_on():
    flag = load_package()["input_boolean"]["heating_oil_price_is_pence"]
    assert flag["initial"] is True


def test_rest_sensor_uses_url_helper_and_unique_id():
    rest = load_package()["rest"]
    assert isinstance(rest, list)
    block = rest[0]
    blob = yaml.safe_dump(block, sort_keys=False)
    assert "resource_template" in block
    assert "input_text.heating_oil_price_url" in blob
    assert "heating_oil_price_per_litre" in blob
    assert "GBP/L" in blob
    assert "86400" in blob
    assert "#currentLivePrice" in blob or "heating_oil_price_selector" in blob
    assert "pence" in blob


def test_refresh_automation_watches_menu_helpers():
    autos = load_package()["automation"]
    refresh = next(a for a in autos if a["id"] == "heating_oil_price_refresh")
    blob = yaml.safe_dump(refresh, sort_keys=False)
    assert "input_text.heating_oil_price_url" in blob
    assert "input_text.heating_oil_price_selector" in blob
    assert "input_boolean.heating_oil_price_is_pence" in blob
    assert "sensor.heating_oil_price_per_litre" in blob
    assert "from_state is not none" in blob


def test_run_out_date_sensor_uses_forecast_empty_days():
    package = load_package()
    fmt = package["input_select"]["heating_oil_date_format"]
    assert "initial" not in fmt
    assert fmt["options"][0] == "DD/MM/YYYY"
    assert "System default" in fmt["options"]
    blob = yaml.safe_dump(package["template"], sort_keys=False)
    assert "heating_oil_run_out_date" in blob
    assert "_forecast_empty" in blob
    assert "_last_reading_date" in blob
    assert "as_datetime" in blob
    assert "timedelta" in blob
    assert "heating_oil_date_format" in blob
    assert "now() + timedelta" not in blob
    assert "ns.days is number and ns.base is not none" in blob


def test_order_litres_helper_and_cost_sensor():
    package = load_package()
    litres = package["input_number"]["heating_oil_order_litres"]
    assert litres["min"] == 1
    assert litres["max"] == 5000
    assert litres["initial"] == 500
    assert litres["unit_of_measurement"] == "L"
    blob = yaml.safe_dump(package["template"], sort_keys=False)
    assert "heating_oil_order_cost" in blob
    assert "sensor.heating_oil_price_per_litre" in blob
    assert "input_number.heating_oil_order_litres" in blob
    assert "round(2)" in blob


def test_oil_tank_dashboard_shows_price_and_url_menu():
    text = OIL_DASH_PATH.read_text(encoding="utf-8")
    assert text.index("sensor.my_tank_oil_level") < text.index(
        "sensor.heating_oil_run_out_date"
    )
    assert text.index("sensor.heating_oil_run_out_date") < text.index(
        "sensor.my_tank_forecast_empty"
    )
    assert "Run out date" in text
    assert "sensor.heating_oil_price_per_litre" in text
    assert "input_number.heating_oil_order_litres" in text
    assert "sensor.heating_oil_order_cost" in text
    assert "Order cost (approximate cost)" in text
    assert "input_select.heating_oil_date_format" in text
    assert "Date format" in text
    assert "input_text.heating_oil_price_url" in text
    assert "input_text.heating_oil_price_selector" in text
    assert "input_boolean.heating_oil_price_is_pence" in text


def test_readme_covers_oil_price_scrape():
    text = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    assert "current oil price" in text
    assert "homefuelsdirect.co.uk" in text
    assert "oil price page url" in text
    assert "css selector" in text
    assert "heating_oil_price_per_litre" in text
    assert "oil order litres" in text
    assert "order cost" in text
    assert "approximate cost" in text
    assert "run out date" in text
    assert "date format" in text
    assert "docs/heating-oil.png" in text
    assert (ROOT / "docs" / "heating-oil.png").is_file()
