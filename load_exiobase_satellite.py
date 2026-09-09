"""Loader for the EXIOBASE 3 satellite matrix parquet table.

Loads the F_satellite matrix (year 2022) directly from the Source Cooperative
HTTP parquet using DuckDB, and reports basic content checks.
"""

import duckdb

URL = (
    "https://data.source.coop/youssef-harby/exiobase-3/4588235/parquet/"
    "year=2022/format=ixi/matrix=F_satellite/data.parquet"
)


def load_satellite(url: str = URL) -> "duckdb.DuckDBPyRelation":
    """Load the F_satellite table and return a DuckDB relation."""
    con = duckdb.connect()
    con.execute("INSTALL httpfs")
    con.execute("LOAD httpfs")
    return con.read_parquet(url)


def main() -> None:
    df = load_satellite().df()
    print(f"rows: {len(df)}, columns: {list(df.columns)}")
    print(f"distinct stressors: {df['stressor'].nunique()}")
    print(f"distinct units: {df['unit'].nunique()}")
    co2 = df[df["stressor"].str.contains("CO2", case=False, na=False)]
    print(co2.groupby(["stressor", "unit"]).agg(
        rows=("value", "size"),
        total=("value", "sum"),
    ).reset_index().to_string())


if __name__ == "__main__":
    main()
