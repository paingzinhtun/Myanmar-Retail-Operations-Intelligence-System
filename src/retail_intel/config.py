from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Settings:
    database_url: str | None = os.getenv("DATABASE_URL")
    raw_data_path: Path = BASE_DIR / os.getenv("RAW_DATA_PATH", "data/raw/retail_sales_raw.csv")
    processed_data_path: Path = BASE_DIR / os.getenv("PROCESSED_DATA_PATH", "data/processed/fact_sales.csv")
    product_dim_path: Path = BASE_DIR / "data/processed/dim_product.csv"
    store_dim_path: Path = BASE_DIR / "data/processed/dim_store.csv"
    days_of_history: int = int(os.getenv("DAYS_OF_HISTORY", "120"))
    random_seed: int = int(os.getenv("RANDOM_SEED", "42"))
    refresh_mode: str = os.getenv("REFRESH_MODE", "daily").strip().lower()
    refresh_interval_minutes: int = int(os.getenv("REFRESH_INTERVAL_MINUTES", "5"))
    refresh_hour: int = int(os.getenv("REFRESH_HOUR", "6"))
    refresh_minute: int = int(os.getenv("REFRESH_MINUTE", "0"))


def get_settings() -> Settings:
    settings = Settings()
    settings.raw_data_path.parent.mkdir(parents=True, exist_ok=True)
    settings.processed_data_path.parent.mkdir(parents=True, exist_ok=True)
    return settings
