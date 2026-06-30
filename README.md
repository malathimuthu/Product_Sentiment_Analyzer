# Product Sentiment Analyzer

## Overview

Product Sentiment Analyzer is a web application that collects product reviews, analyzes customer sentiment using Natural Language Processing (NLP), stores the data in MongoDB, and exports reviews to CSV format.

---

## Features

- Add Product Reviews
- Sentiment Analysis (Positive, Neutral, Negative)
- Search Reviews
- Update Reviews
- Delete Reviews
- Dashboard with Statistics
- CSV Export
- MongoDB Database
- REST API using Flask
- React Frontend

---

## Technologies Used

### Frontend
- React.js
- HTML
- CSS
- JavaScript

### Backend
- Flask
- Python

### Database
- MongoDB

### Libraries
- Pandas
- TextBlob / VADER
- Flask-CORS
- PyMongo

---

## Project Structure

```
Product_Sentiment_Analyzer/

├── backend/
│   ├── app.py
│   ├── routes.py
│   ├── database.py
│   ├── sentiment.py
│   ├── utils.py
│   ├── config.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
└── README.md
```

---

## Installation

### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend

```bash
cd frontend
npm install
npm start
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /reviews | Get all reviews |
| POST | /reviews | Add review |
| PUT | /reviews/{id} | Update review |
| DELETE | /reviews/{id} | Delete review |
| GET | /statistics | Get statistics |
| GET | /export | Export CSV |

---

## Output

- Review Management
- Sentiment Analysis
- Interactive Dashboard
- CSV Export
- MongoDB Storage

---

## Author

**Malathi M**

Artificial Intelligence & Machine Learning

---

## License

This project is developed for educational purposes.