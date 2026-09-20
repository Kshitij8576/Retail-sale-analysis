# Retail Sales Analysis

A simple beginner-level data analysis project built using Python, Pandas and Streamlit.

## Project Objective

The goal of this project is to analyze retail sales data and understand:

- Total sales
- Total orders
- Total quantity sold
- Average order value
- Sales by category
- Monthly sales
- Sales by city
- Top-selling products

## Tools Used

- Python
- Pandas
- Streamlit
- CSV

## Project Structure

```text
retail-sales-analysis/
│
├── app.py
├── sales.csv
├── requirements.txt
└── README.md
```

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

The project will open in a browser.

## Dataset

The dataset contains sample retail sales records with:

- Order ID
- Date
- Product
- Category
- City
- Quantity
- Unit Price

Sales are calculated using:

```text
Sales = Quantity × Unit Price
```

## Analysis

The dashboard shows basic sales analysis using charts and summary metrics.

This project is intentionally simple and was created as a beginner-level data analysis project.
