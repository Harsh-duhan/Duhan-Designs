<div align="center">

# 🎨 Duhan Designs
### Realm of Creativity

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

<br />

**Elevate your visual identity with our premium curated collections.**

[Explore Collections](#-curated-collections) • [Join Us](#-join-us) • [Contact](#-contact)

</div>

---

## 📖 Overview

**Duhan Designs** is a robust, data-driven web application built using the Django framework. The project integrates a refined front-end experience with a powerful Python-based backend and a MySQL relational database. It is designed to demonstrate scalable architecture, secure data handling, and modern web standards.

## ✨ Core Features

*   **Dynamic Content Management**: Fully integrated Django Admin interface for seamless data control.
*   **Relational Data Modeling**: Complex MySQL database schema managed through the Django ORM.
*   **Secure Authentication**: Robust implementation of user sessions and permissions.
*   **Responsive Frontend**: High-fidelity UI components optimized for performance and accessibility.
*   **RESTful Architecture**: Structured URL routing and efficient view logic.

## 📦 Curated Collections

Discover designs that speak to your audience:
*   ☕ **Cafe Aesthetics**: Warm, inviting designs for coffee shops and bistros.
*   🧱 **Urban Walls**: Edgy, street-style poster designs for modern spaces.
*   🎓 **Academic Excellence**: Professional templates for educational institutions.
*   🎉 **Festival Vibes**: Vibrant, energetic designs for events and celebrations.

## 🛠️ Technical Specifications

### Backend Architecture
*   **Framework**: Django (Python)
*   **Database**: MySQL
*   **Environment**: Virtualenv / Pipenv
*   **Security**: CSRF Protection, SQL Injection Prevention, Secure Environment Variables

### Frontend Environment
*   **Markup**: HTML5 Semantic Elements
*   **Styling**: CSS3 (Flexbox and Grid)
*   **Scripting**: JavaScript (ES6+)

## 🚀 Getting Started

Follow these steps to set up the project locally.

### Prerequisites
*   Python 3.8 or higher
*   MySQL Server 8.0+
*   Git

### Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Harsh-duhan/Duhan-Designs.git
    cd Duhan-Designs
    ```

2.  **Initialize Virtual Environment**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Database Setup**
    Create a MySQL database and update `core/settings.py` with your credentials.
    ```sql
    CREATE DATABASE duhan_designs_db CHARACTER SET utf8mb4;
    ```
    Then run migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Run the Server**
    ```bash
    python manage.py runserver
    ```

## 📂 Project Structure

```plaintext
Duhan-Designs/
├── core/                   # Project configuration and settings
│   ├── settings.py         # Main Django settings (MySQL config)
│   └── urls.py             # Root URL routing
├── apps/                   # Application-specific logic
│   ├── models.py           # MySQL database schema definitions
│   ├── views.py            # Business logic and request handling
│   └── templates/          # HTML templates
├── static/                 # CSS, JavaScript, and Images
├── manage.py               # Django command-line utility
└── requirements.txt        # Python dependencies
```

## 📞 Contact

**Harsh Duhan**
*   GitHub: [Harsh-duhan](https://github.com/Harsh-duhan)

---
<div align="center">
  <sub>&copy; 2024 Duhan Designs. All rights reserved.</sub>
</div>