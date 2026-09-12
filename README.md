# 📚 Campus Library & Student Borrowing Engine

A lightweight, terminal-based CLI application built in Python and powered by SQLite. This system manages university student searches, automates student access tier classification based on age, tracks checked-out books, and calculates overall fee revenues.

---

## 🚀 Features

* **Student Directory & Auto Email Generator:** Keyword search engine using pattern matching (`LIKE`) that dynamically generates official student email handles (`firstname.lastname@library.com`) using SQL string concatenation.
* **Access Tier Classifier:** Evaluates student ages and dynamically classifies members into privilege brackets (Senior Scholar, Graduate & Research, Undergraduate, Junior Pass) using `CASE WHEN` conditional statements.
* **Borrowing & Fee Revenue Analytics:** Relational multi-table `LEFT JOIN` reporting total accumulated fees per student using SQL aggregations (`SUM` and `GROUP BY`).
* **Session Search History Log:** In-memory tracking system that displays up to the 3 most recent search terms in reverse chronological order using custom index iteration.
* **Zero-Setup Database:** Automatically creates database tables (`students`, `borrowings`) and inserts initial seed data on first execution.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Database:** SQLite3
* **SQL Features:** `LEFT JOIN`, `CASE WHEN`, `SUM()`, `GROUP BY`, String Concatenation (`||`), Pattern Matching (`LIKE`)

---

## 📂 Project Structure

```text
├── main2.py               # Application entry point, embedded database engine & CLI menu
└── library_engine.db     # SQLite database file (automatically generated on first run)
