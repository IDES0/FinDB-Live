# FinDB Live: Real-Time Financial Data Retrieval

**Repository**: [FinDB Live](https://github.com/IDES0/Financial-Database-FINDB-Live)

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Usage](#usage)
5. [API Integration](#api-integration)
6. [Contributing](#contributing)
7. [License](#license)

---

## Overview
FinDB Live is a Flask-based financial data application designed for real-time retrieval and analysis of financial data. Unlike the original **FinDB Core**, which stores and organizes extensive financial datasets in a relational database, FinDB Live dynamically fetches data on-demand, allowing users to access the latest market information without relying on stored data.

## Features
- **Real-Time Stock Data Retrieval**: Access live stock data, indexes, and financial metrics through on-demand API requests.
- **Dynamic Search and Filtering**: Quickly search for stocks, indexes, and sectors using a responsive interface.
- **No Persistent Storage**: Data is fetched in real-time, so no storage of data in databases is required.
- **Data Analysis Tools**: Integrates data processing capabilities, allowing quick insights on the retrieved financial data.
- **Lightweight and Fast**: By eliminating database storage, FinDB Live offers a faster, streamlined approach for live data analysis.

## Tech Stack
- **Backend**: Flask (Python)
- **Data Retrieval APIs**: `yfinance`, `yahooquery` for financial data, `requests` for handling API requests
- **Data Processing**: Pandas for data manipulation
- **String Matching**: FuzzyWuzzy and Levenshtein for flexible search functionality
- **Production Setup**: Gunicorn and Flask-CORS for cross-origin resource sharing

## Usage

1. **Retrieve Live Data**: Perform dynamic queries for stock data, sectors, and indexes, with each request fetching the latest available information.
   
2. **Data Analysis**: Use integrated data processing tools like Pandas to explore trends and visualize real-time metrics.

3. **Search Functionality**: Leverage fuzzy matching for approximate search results based on partial or similar names, especially useful for stocks and sectors.

### Example Queries
- **On-Demand Stock Data**: Fetch current price, volume, and other details for specific stocks by ticker.
- **Real-Time Sector and Industry Insights**: View performance metrics for sectors and industries, refreshed at each request.
- **Approximate Search**: Locate stocks or indexes with similar names using fuzzy search for a more user-friendly experience.

## API Integration

FinDB Live uses **Yahoo Finance** and **YahooQuery** APIs for live financial data.

- **Real-Time Data**: Both `yfinance` and `yahooquery` are used to fetch up-to-date data on stocks, indexes, and other instruments.
- **Search and Matching**: Utilizes FuzzyWuzzy and Levenshtein libraries to improve the accuracy and flexibility of search results.
- **Data Processing**: With Pandas, FinDB Live can process data on-the-fly, providing immediate insights based on the latest retrieved data.

## Contributing
We welcome contributions to FinDB Live! If you have ideas for new features, improvements, or bug fixes, please follow these steps:

1. **Fork the Repository**
2. **Create a Feature Branch** (`git checkout -b feature/new-feature`)
3. **Commit Changes** (`git commit -m 'Add new feature'`)
4. **Push to Branch** (`git push origin feature/new-feature`)
5. **Create a Pull Request**

Please ensure all contributions adhere to the project’s coding standards and include relevant documentation.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
