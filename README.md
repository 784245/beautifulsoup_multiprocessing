# beautifulsoup_multiprocessing

The script targets the Abel & Cole website, renowned for its array of organic and eco-friendly products. This website offers a wide selection of fresh produce, meat, dairy products, and other groceries, focusing on sustainability and ethical sourcing. The script specifically fetches price data, which can be valuable for market analysis, price tracking, or competitive research.

This Python script is designed to efficiently scrape product prices from the Abel & Cole website, a popular online grocer known for organic food and sustainable products. The script uses the Beautiful Soup library to parse HTML and extract price information, leveraging the power of Python's multiprocessing module to handle multiple URLs concurrently.


Features:
  Efficient Data Extraction: Utilizes Beautiful Soup for robust HTML parsing and data extraction.
  Multiprocessing Support: Employs multiprocessing to speed up the scraping process across multiple pages simultaneously.   
  Dynamic Date Handling: Automatically appends the scraped data with the current date to track price changes over time.
  Error Handling: Implements basic error handling to manage and log issues like connection errors or missing data.
