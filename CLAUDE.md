# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Orthodox Christian Liturgical Resource Links — a data collection and analysis project for cataloging liturgical sources.

## Environment

This project uses [pixi](https://pixi.sh) for environment and dependency management (conda + PyPI hybrid).

```bash
# Install dependencies and activate environment
pixi install

# Run a command inside the pixi environment
pixi run <command>

# Start JupyterLab
pixi run jupyter
```

The pixi environment is in `.pixi/` (gitignored). `pixi.lock` is committed for reproducibility.

## Key Dependencies

- **Web scraping**: `scrapy`, `selenium`, `aiohttp`, `bs4`, `requests`, `httpx`
- **Data processing**: `pandas`, `polars`, `pyarrow`, `duckdb`
- **NLP**: `spacy`
- **Graph analysis**: `networkx`
- **API**: `fastapi` + `uvicorn`
- **Workflow orchestration**: `prefect`
- **Testing**: `pytest`, `pytest-asyncio`
- **Linting**: `ruff`

## Commands

```bash
# Lint
pixi run ruff check .
pixi run ruff format .

# Tests
pixi run pytest
pixi run pytest path/to/test_file.py::test_name   # single test

# JupyterLab
pixi run jupyter
```

## Platform

Currently configured for `linux-64` only (`platforms` in `pixi.toml`).
