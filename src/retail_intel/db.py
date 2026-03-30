from __future__ import annotations

from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine


def get_engine(database_url: str | None) -> Engine | None:
    if not database_url:
        return None
    return create_engine(database_url, future=True)


def execute_sql_file(engine: Engine, path: Path) -> None:
    sql_text = path.read_text(encoding="utf-8")
    with engine.begin() as connection:
        for statement in [segment.strip() for segment in sql_text.split(";") if segment.strip()]:
            connection.execute(text(statement))


def append_table(engine: Engine, table_name: str, frame: pd.DataFrame) -> None:
    frame.to_sql(table_name, engine, if_exists="append", index=False)


def read_sql(engine: Engine, query: str) -> pd.DataFrame:
    with engine.begin() as connection:
        return pd.read_sql(text(query), connection)
