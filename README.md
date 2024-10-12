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
FinDB Live is a Flask-based financial data application designed for real-time retrieval, analysis, and personalized financial insights. Unlike **FinDB Core**, which focuses on storing and organizing historical and current financial data, FinDB Live dynamically fetches information on-demand, allowing users to access the latest market data and tools without relying on stored datasets.

## Features
- **Real-Time Stock Data Retrieval**: Access up-to-the-minute stock data, indexes, and financial metrics via on-demand API requests.
- **Dynamic Search and Filtering**: Instantly search for stocks, indexes, and sectors with responsive, real-time filtering.
- **User Accounts and Authentication**: Secure user login and account management to enable personalized financial tracking.
- **Paper Trading and Portfolio Management**: Simulate trades and manage virtual portfolios using live market data, allowing users to test strategies without financial risk.
- **Customizable Indices and Models**: Create and manage custom financial indices and analytical models based on live data, tailored to user-defined criteria and metrics.
- **Data Analysis Tools**: Integrates data processing capabilities for quick insights on retrieved financial data.
- **Cross-Origin Resource Sharing (CORS)**: Configured with `flask-cors` to handle API requests across different origins.
- **Lightweight and Fast**: Designed without persistent database storage, making FinDB Live highly efficient and suitable for real-time financial analysis.

## Tech Stack
- **Backend**: Flask (Python)
- **Data Retrieval APIs**: `yfinance`, `yahooquery` for live financial data, `requests` for API handling
- **Data Processing**: Pandas for data manipulation
- **User Authentication**: Flask-Login for managing user sessions and accounts
- **String Matching**: FuzzyWuzzy and Levenshtein for flexible search functionality
- **Production Setup**: Gunicorn and Flask-CORS for cross-origin resource sharing

## Usage

1. **Real-Time Data Retrieval**: Retrieve live data on stocks, sectors, and indexes with each request for the latest available information.
   
2. **Simulate Trading**: Use the paper trading feature to execute simulated trades and manage a virtual portfolio, helping you test strategies in a risk-free environment.

3. **Custom Indices and Models**: Define your own financial indices or quantitative models based on real-time data to monitor specific market trends or sectors.

4. **Flexible Search Functionality**: Perform approximate searches to find stocks or sectors by name using fuzzy matching.

### Example Queries
- **On-Demand Stock Data**: Fetch current price, volume, and other metrics for individual stocks by ticker.
- **Real-Time Sector Insights**: View up-to-date metrics for sectors and industries, refreshed at each request.
- **Custom Index Creation**: Create personalized indices to track the performance of a group of stocks or sectors that meet specific criteria.
- **Approximate Search**: Use fuzzy matching to find stocks or indexes by partial names for more user-friendly search results.

## API Integration

FinDB Live uses various tools and APIs to ensure fast, live data retrieval and processing.

- **Real-Time Data**: The `yfinance` and `yahooquery` libraries retrieve live and historical data on stocks, indexes, and other instruments.
- **Data Processing and Analysis**: Pandas enables immediate insights on the latest data, with real-time manipulation and visualization.
- **Search Optimization**: FuzzyWuzzy and Levenshtein provide accurate, approximate matching for enhanced search capabilities.
  
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
