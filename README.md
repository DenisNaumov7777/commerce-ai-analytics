# Commerce AI Analytics

**Author:** Denis Naumov  
**Location:** Cologne, Germany  
**Status:** Active  
**Stack:** Python 3.10+, FastAPI, AsyncIO, Watson NLP, Pydantic V2

---

## 📖 Overview

**Commerce AI Analytics** is a high-performance, asynchronous microservice designed for e-commerce platforms. It solves the critical business challenge of understanding customer sentiment at scale.

Unlike simple sentiment analysis (Positive/Negative), this application leverages **IBM Watson NLP libraries** to detect granular emotions—**Joy, Anger, Fear, Sadness, and Disgust**—within customer feedback text. This enables data-driven decisions for product improvement and customer support automation.

## 🚀 Key Features

* **Asynchronous Architecture:** Built on **FastAPI** and `httpx` for non-blocking I/O, allowing high throughput.
* **Strict Data Validation:** Utilizes **Pydantic V2** models to ensure robust request/response schemas.
* **Resilient "Mock Mode":** Automatically switches to a simulation mode if the external AI service is unreachable (e.g., local development), ensuring 100% uptime.
* **Modular Design:** Clean separation of concerns (Routers, Services, Models) ready for microservices deployment.
* **Code Quality:** Adheres to strict PEP 8 standards with a **10/10 Pylint score**.

---

## 📂 Project Structure

```text
commerce-ai-analytics/
├── app/
│   ├── main.py              # Application entry point
│   ├── config.py            # Environment configuration
│   ├── models.py            # Data schemas (Request/Response)
│   ├── services.py          # Business logic & External API integration
│   └── routers/             # API Endpoints
├── tests/
│   └── test_api.py          # Automated test suite
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation

```

---

## 🛠️ Installation & Setup

Follow these steps to set up the project locally.

### 1. Clone the Repository

```bash
git clone [https://github.com/DenisNaumov7777/commerce-ai-analytics.git](https://github.com/DenisNaumov7777/commerce-ai-analytics.git)
cd commerce-ai-analytics

```

### 2. Create a Virtual Environment

It is recommended to use a virtual environment to isolate dependencies.

```bash
# MacOS/Linux
python3 -m venv env
source env/bin/activate

# Windows
python -m venv env
.\env\Scripts\activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

---

## 🏃‍♂️ Running the Application

Start the local development server using **Uvicorn**:

```bash
uvicorn app.main:app --reload

```

* **Server URL:** `http://127.0.0.1:8000`
* **Interactive API Docs (Swagger UI):** `http://127.0.0.1:8000/docs`
* **Alternative Docs (ReDoc):** `http://127.0.0.1:8000/redoc`

You can test the API directly in the browser via Swagger UI by navigating to the `/docs` endpoint and using the **"Try it out"** button on the `POST /api/v1/emotion` route.

---

## ✅ Quality Assurance

This project maintains high engineering standards through automated testing and static code analysis.

### 1. Automated Tests (Pytest)

Run the test suite to verify API endpoints and the mock fallback logic:

```bash
pytest -v

```

*Expected Result: All tests PASSED.*

### 2. Static Code Analysis (Pylint)

Check code quality and PEP 8 compliance. The project currently maintains a **perfect 10.00/10 score**.

```bash
PYTHONPATH=. python -m pylint app

```

*Expected Output:*

> `Your code has been rated at 10.00/10`

---

## 📜 License

This project is licensed under the **Apache License 2.0**.

---

## 👤 Author

**Denis Naumov**

* 📍 Cologne, Germany

```

