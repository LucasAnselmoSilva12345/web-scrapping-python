# Web Scraping Python

Python application that allows users to check the structure and content of web pages. The tool uses the `requests` and `BeautifulSoup` libraries to make HTTP requests and parse the HTML of web pages.

## Overview

This script-based tool provides the following functionalities:

1. **HTML Tag Verification**: The tool checks if essential HTML tags such as `<html>`, `<head>`, and `<body>` are present on the page and if they have been properly opened and closed.

2. **CSS and JS Verification**: The tool checks for the presence of inline CSS and JS in the page's code and identifies import links for external CSS and JS files.

3. **Tag Ordering**: The tool verifies if essential HTML tags are correctly ordered on the page, meaning if `<head>` is above `<body>`.

4. **Script and NoScript Tag**: The tool checks for the existence of the `<script>` tag and, if it exists, reports whether the `<noscript>` tag is present.

5. **Images with `.gif` Extension**: The tool checks for the existence of images with the `.gif` extension.

6. **Language Information Existence**: The tool verifies if the `lang` attribute is present to indicate the language of the application.

## Technologies Used

The Web Page Verification Tool was developed in Python and utilizes the following libraries:

- `requests`: Used to make HTTP requests to the provided web page.
- `BeautifulSoup`: Used to parse the HTML of the page and extract specific information.

## How to Run the Tool

To execute the Web Page Verification Tool, follow the instructions below:

1. **Prerequisites**:

   Ensure that Python is installed on your system. You can check the Python version by running the command:

   ```sh
   python --version
   ```

   Additionally, install the `requests` and `BeautifulSoup` libraries using `pip` if they are not already installed:

   ```sh
   pip install requests beautifulsoup4
   ```

2. **Download the Source Code**:

   Download the source code of the tool or clone the Git repository if available.

3. **Run the Tool**:

   Execute the Python script by providing the URL of the web page you want to check as the argument. For example:

   ```sh
   python3 tool.py https://www.example.com
   ```

   Be sure to replace `tool.py` with the actual script filename, `https://www.example.com` with the URL you want to verify, and specify the desired output filename.

4. **Results**:

   The tool will check the web page, analyze its content, and save the results to the specified output file. You will receive messages indicating the obtained results.

## Conclusion

This script is a useful tool for checking the structure and content of web pages, identifying potential issues, and providing useful information about the page's code.