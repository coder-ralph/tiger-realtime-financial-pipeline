# Tiger Real-Time Financial Pipeline 🐅💹

A real-time financial data pipeline built for **Global Hack Week: Hacktoberfest**, designed to stream live cryptocurrency trade data via WebSockets (Twelve Data) and ingest it directly into a high-performance **Tiger Cloud (TimescaleDB)** hypertable.

---

## 🚀 Features

* **Real-Time WebSockets**: Connects persistently to Twelve Data to stream live second-by-second trade data for assets like `BTC/USD` and `ETH/USD`.
* **Optimized Time-Series Storage**: Leverages **TimescaleDB hypertables** with columnar `segmentby` compression and optimization for efficient time-series ingestion and analytical querying.
* **Python Automation**: Uses a custom Python data pipeline script (`financial_pipeline.py`) to parse websocket payloads and insert records into PostgreSQL via `psycopg2`.

---

## 🛠️ Tech Stack

* **Database**: Tiger Cloud / TimescaleDB (PostgreSQL-compatible time-series database)
* **Data Source**: Twelve Data API & WebSockets
* **Language & Libraries**: Python 3, `twelvedata`, `websocket-client`, `psycopg2-binary`
* **Environment**: GitHub Codespaces

---

## ⚙️ Quick Start Guide

### 1. Clone the Repository & Set Up Virtual Environment
```bash
git clone [https://github.com/coder-ralph/tiger-realtime-financial-pipeline.git](https://github.com/coder-ralph/tiger-realtime-financial-pipeline.git)
cd tiger-realtime-financial-pipeline

# Create and activate virtual environment
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install twelvedata websocket-client psycopg2-binary

```

### 2. Set Up Your Tiger Cloud Database Schema

Run the following SQL script inside your Tiger Cloud SQL Editor to create your asset table and real-time hypertable:

```sql
-- Create asset metadata table
CREATE TABLE IF NOT EXISTS crypto_assets (
    symbol TEXT PRIMARY KEY,
    name TEXT,
    type TEXT
);

-- Create real-time ticks hypertable
CREATE TABLE IF NOT EXISTS crypto_ticks (
    "time" TIMESTAMPTZ,
    symbol TEXT,
    price DOUBLE PRECISION,
    day_volume NUMERIC
) WITH (
    tsdb.hypertable,
    tsdb.segmentby='symbol',
    tsdb.orderby='time DESC'
);

```

### 3. Configure Credentials

Update your `financial_pipeline.py` script with your Tiger Cloud database connection credentials and your Twelve Data API key:

```python
DB_HOST = "your-cluster-host.tsdb.cloud.timescale.com"
DB_NAME = "tsdb"
DB_USER = "tsdbadmin"
DB_PASSWORD = "your-database-password"
DB_PORT = "35305"

td = TDClient(apikey="your-twelve-data-api-key")

```

### 4. Run the Pipeline

```bash
python financial_pipeline.py

```

---

## 📄 License

This project is open-source and built for Global Hack Week.
