from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class ProductSpec:
    product: str
    category: str
    supplier: str
    base_price: int
    daily_demand: int
    stock_floor: int


PRODUCTS = [
    ProductSpec("Shan Instant Noodle", "Food", "Shwe Taung Supply", 950, 18, 40),
    ProductSpec("ABC Soft Drink 330ml", "Beverage", "Ayeyar Distribution", 700, 22, 55),
    ProductSpec("Myanmar Premium Rice 1kg", "Staples", "Golden Grain Co", 3200, 12, 35),
    ProductSpec("Thanaka Face Pack", "Personal Care", "Mandalay Beauty Mart", 4200, 6, 20),
    ProductSpec("Paracetamol 10 Pack", "Health", "CarePlus Pharma", 1800, 8, 18),
    ProductSpec("Palm Cooking Oil 1L", "Household", "Union Essentials", 5400, 10, 24),
    ProductSpec("3 in 1 Coffee Mix", "Beverage", "Shwe Moe Trading", 3800, 14, 30),
    ProductSpec("Laundry Powder 500g", "Household", "Union Essentials", 2600, 9, 22),
]

STORES = [
    {"store_name": "Yangon Downtown", "city": "Yangon", "township": "Lanmadaw"},
    {"store_name": "Mandalay Central", "city": "Mandalay", "township": "Chanayethazan"},
    {"store_name": "Naypyidaw Junction", "city": "Naypyidaw", "township": "Zabuthiri"},
]

PAYMENT_TYPES = ["Cash", "KBZPay", "WavePay", "Card"]


def generate_sales_data(days: int, seed: int) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    end_date = date.today()
    start_date = end_date - timedelta(days=days - 1)

    rows: list[dict] = []
    sale_id = 1
    opening_stock: dict[tuple[str, str], int] = {}

    for store in STORES:
        for spec in PRODUCTS:
            opening_stock[(store["store_name"], spec.product)] = spec.stock_floor + int(rng.integers(30, 90))

    for current_date in pd.date_range(start_date, end_date, freq="D"):
        day_multiplier = 1.25 if current_date.weekday() in (4, 5) else 1.0

        for store in STORES:
            for spec in PRODUCTS:
                key = (store["store_name"], spec.product)
                current_stock = opening_stock[key]

                if current_stock <= spec.stock_floor:
                    replenish_qty = int(rng.integers(25, 80))
                    current_stock += replenish_qty

                quantity = max(
                    0,
                    int(
                        rng.normal(
                            loc=spec.daily_demand * day_multiplier,
                            scale=max(1.0, spec.daily_demand * 0.25),
                        )
                    ),
                )
                quantity = min(quantity, current_stock)

                if quantity == 0:
                    opening_stock[key] = current_stock
                    continue

                unit_price = int(spec.base_price + rng.integers(-150, 350))
                revenue = quantity * unit_price
                current_stock -= quantity
                opening_stock[key] = current_stock

                rows.append(
                    {
                        "sale_id": sale_id,
                        "date": current_date.date(),
                        "product": spec.product,
                        "quantity": quantity,
                        "price": unit_price,
                        "category": spec.category,
                        "store_location": store["store_name"],
                        "city": store["city"],
                        "township": store["township"],
                        "stock_on_hand": current_stock,
                        "supplier": spec.supplier,
                        "payment_type": rng.choice(PAYMENT_TYPES, p=[0.52, 0.22, 0.18, 0.08]),
                    }
                )
                sale_id += 1

    return pd.DataFrame(rows)
