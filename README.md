# ⚡ Enterprise Entity Resolution & Fuzzy Matching Pipeline

<p align="center">
  <a href="https://github.com/amitkumar97097/entity-resolution-pipeline/actions/workflows/test.yml">
    <img src="https://github.com/amitkumar97097/entity-resolution-pipeline/actions/workflows/test.yml/badge.svg" alt="CI Status">
  </a>
  <a href="https://amit-entity-pipeline.onrender.com/docs">
    <img src="https://img.shields.io/badge/Live%20Demo-Render-blue?style=flat&logo=render" alt="Live Demo">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.10%252B-blue.svg" alt="Python Version">
  </a>
  <a href="https://fastapi.tiangolo.com/">
    <img src="https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg?logo=fastapi&logoColor=white" alt="FastAPI">
  </a>
  <a href="https://duckdb.org/">
    <img src="https://img.shields.io/badge/DuckDB-In--Memory-yellow.svg" alt="DuckDB">
  </a>
</p>

An enterprise-grade, high-performance data engineering and microservice pipeline designed to ingest, cleanse, and resolve messy entity records against structured databases using DuckDB and advanced fuzzy string matching algorithms.

---

## 🏗️ Architecture & Core Components


[ Raw Messy Input Query ]
│
▼
[ Regex Tokenization & Normalization ]
│
▼
[ DuckDB In-Memory C-Engine (Blocking & SQL Filter) ]
│
▼
[ Jaro-Winkler Distance Scoring Engine ]
│
▼
[ Ranked JSON Matches Returned via FastAPI ]


## 🚀 Key Features

* **High-Speed Ingestion:** Leverages DuckDB's in-memory C-engine to bulk-load large datasets instantly without exhausting system memory.
* **Hybrid Matching Algorithm:** Combines exact SQL indexing with **Jaro-Winkler distance** and token-level normalization to accurately resolve typos, spelling noise, and unstructured queries.
* **RESTful Microservice:** Built with **FastAPI** for asynchronous handling, featuring auto-generated interactive Swagger UI documentation (`/docs`).
* **Production Containerization:** Fully dockerized with a clean multi-stage footprint optimized for cloud deployment.
* **Test-Driven Reliability:** Backed by a comprehensive `pytest` suite ensuring 100% test coverage for ingestion, text cleansing, and search logic.
* **Automated CI/CD:** Integrated with **GitHub Actions** to enforce zero-regression automated testing on every push.

---

## 🛠️ Tech Stack

* **Core Engine:** Python 3.10, Pandas, DuckDB (In-Memory C-Engine)
* **API Framework:** FastAPI, Uvicorn
* **Algorithms:** Jaro-Winkler Distance, Custom Regex Tokenization
* **DevOps & Cloud:** Docker, Render.com
* **Testing & CI/CD:** Pytest, GitHub Actions
* **Version Control:** Git & GitHub

---

## 🌐 Live Cloud Demo
Test the live API endpoint and interactive documentation directly in your browser:
👉 **[Open Live Swagger UI (`/docs`)](https://entity-resolution-pipeline-2.onrender.com/docs)**

---

## 🔌 API Usage Example

You can query the deployed microservice using any HTTP client:

**Request (`POST /search`):**
```json
{
  "query": "Tta Motrs!",
  "threshold": 0.5
}

```

**Response (`200 OK`):**

```json
{
  "query": "Tta Motrs!",
  "matches": [
    {
      "entity_id": "E004",
      "name": "Tata Motors Ltd.",
      "score": 0.85
    }
  ]
}

```

---

## 💻 Local Setup & Installation

### 1. Clone the Repository

```powershell
git clone [https://github.com/amitkumar97097/entity-resolution-pipeline.git](https://github.com/amitkumar97097/entity-resolution-pipeline.git)
cd entity-resolution-pipeline

```

### 2. Configure Virtual Environment

```powershell
python -m venv venv
venv\Scripts\Activate
pip install -r requirements.txt

```

### 3. Run Automated Tests

```powershell
pytest -v

```

### 4. Start Local FastAPI Server

```powershell
uvicorn app:app --reload

```

Access the local interactive documentation at: `http://127.0.0.1:8000/docs`

---

## 🐳 Docker Deployment

To build and run the container locally:

```powershell
# Build the Docker image
docker build -t entity-resolution-pipeline .

# Run the container locally on port 8000
docker run -p 8000:8000 entity-resolution-pipeline

```

---

## 👤 Author

**Amit Kumar**

* GitHub:https://github.com/amitkumar97097

```
```
