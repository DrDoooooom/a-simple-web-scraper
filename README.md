# **A Simple Web Scraper**

This is a simple Python script that utilizes web scraping to search Google and return the most relevant answer for a user's query.

**Usage:**

Run the script in a Python environment and provide a search query when prompted. The script will search Google, scrape the results, and return the most likely answer text.

**Tools Used:**

   * Python
   * BeautifulSoup
   * Requests

**How it Works:**

The script uses the Requests library to download the Google search results page for the given query. It then parses the HTML using BeautifulSoup to identify elements that commonly contain the answer text - such as class names like .RqBzHd and .AZCkJd. The script searches these elements for answer text and returns the first relevant result.

**Limitations**

   * Only searches Google.com in English
   * Focuses on grabbing short answer text, not comprehensive results
   * Won't necessarily find/return answers to complex queries
