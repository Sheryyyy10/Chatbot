1. # Data Extraction & Validation 

This repository contains a Python script for scraping product data from Amazon using Selenium. The AmazonScraper class allows you to extract product titles, images, and prices from a given Amazon URL.

# Code Explanation

AmazonScraper Class
__init__ Method: Initializes the AmazonScraper class. Sets up the Chrome WebDriver with headless options to run the browser in the background. If initialization fails, an exception is raised.

normalize_text Method: Normalizes text by removing single quotes, stripping whitespace, and converting to lowercase. This is used to clean the extracted text.

# scrape Method:

Takes a URL as input and navigates to it using the WebDriver.
Waits for product elements to be present on the page.
Extracts product details (title, image, and price) using CSS selectors.
Normalizes the extracted data and stores it in a list of dictionaries.
Handles errors during the extraction process and logs them.
Finally, quits the WebDriver.
Error Handling
Initialization Errors: Raised when WebDriver initialization fails.
Scraping Errors: Raised when there is an issue during the scraping process.
Product Extraction Errors: Logged for individual products if extraction fails.


# get Method:
Uses a predefined Amazon URL to scrape product data.
Initializes an AmazonScraper instance and calls the scrape method.
Returns the scraped data as a JSON response.
Handles and returns error messages in case of failures.


# Notes
The scrape method includes a time.sleep(5) call to allow the page to load. Adjust this delay as needed based on your network speed and page load times.


2. # Scalable Scraping 

# Unsplash Scraper
This repository contains a Python script for scraping image URLs from Unsplash using Selenium, integrated with Django. The scrape_unsplash function navigates to Unsplash, scrolls to load more images, and collects the image URLs.

# scrape_unsplash Function
User-Agent Handling: Utilizes the fake_useragent library to generate a random user-agent string for the WebDriver, helping to avoid detection and potential blocking.

Chrome WebDriver Configuration: Sets up the Chrome WebDriver with headless options to run in the background, and applies the random user-agent string.

Page Interaction:
# Navigates to Unsplash.
Scrolls down the page a specified number of times (num_scrolls) to load more images.
Uses random delays between actions to mimic human browsing behavior.

# Image Extraction:
Finds image elements on the page using CSS selectors.
Extracts the src attribute from each image element to get the image URLs.

# Response Handling:
Returns a JSON response containing the list of image URLs or an error message if something goes wrong.

# Error Handling
Scraping Errors: Raised and handled if there is an issue during the scraping process, such as element not found or WebDriver failures.

# Notes
Random Delays: The use of time.sleep(random.uniform(1, 3)) helps to reduce the risk of detection and blocking by simulating more realistic browsing behavior.
Compliance: Ensure you comply with Unsplash's terms of service and robots.txt guidelines when scraping their site.
-- > using fake User Agent for bypass User Agent detection

3. # Proxy Rotation (Bypass IP blocking)

Proxy Rotation:

get_random_proxy Function: Returns a random proxy address from a predefined list. This helps in rotating proxies to avoid detection and blocking.
Proxy Configuration: Configures Selenium to use the chosen proxy address for HTTP and SSL connections.
User-Agent Handling: Utilizes the fake_useragent library to generate a random user-agent string for the WebDriver, further helping to avoid detection.

Chrome WebDriver Configuration: Sets up the Chrome WebDriver with headless options to run in the background and applies the random user-agent string and proxy settings.

# Page Interaction:
Navigates to Unsplash.
Scrolls down the page a specified number of times (num_scrolls) to load more images.
Uses random delays between actions to mimic human browsing behavior.\

# Image Extraction:
Finds image elements on the page using CSS selectors.
Extracts the src attribute from each image element to get the image URLs.
Response Handling:

Returns a JSON response containing the list of image URLs or an error message if something goes wrong.

# Error Handling
Scraping Errors: Raised and handled if there is an issue during the scraping process, such as element not found or WebDriver failures.

# Notes
Random Delays: The use of time.sleep(random.uniform(1, 3)) helps to reduce the risk of detection and blocking by simulating more realistic browsing behavior.
Proxy List: Customize the get_random_proxy function with your own proxy list. Ensure that the proxies are reliable and have the appropriate credentials.
Compliance: Ensure you comply with Unsplash's terms of service and robots.txt guidelines when scraping their site.

