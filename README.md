# databricks-api-ingestion-pipeline
# Real-Time API Ingestion Pipeline using Databricks

## Overview
This project demonstrates a production-grade API ingestion framework using Databricks, Delta Lake, and Structured Streaming.

## Features
- REST API ingestion with retry logic
- Incremental data ingestion
- Medallion Architecture (Bronze, Silver, Gold)
- Streaming with watermarking for late data
- Deduplication and checkpointing

## Tech Stack
- Azure Databricks
- PySpark
- Delta Lake
- Structured Streaming
- REST APIs

## Architecture
API → Bronze → Silver → Gold

## How to Run
1. Configure API details
2. Run Bronze ingestion notebook
3. Start streaming Silver
4. Start streaming Gold
