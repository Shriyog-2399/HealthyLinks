# URL Filtering Tool

This Python script reads URLs from standard input, checks their HTTP status, and filters out URLs that return a 200 OK status. The valid URLs are saved in a specified output file, making it easier to identify active URLs.

## Features

- **URL Filtering**: Only saves URLs that return a 200 OK status, indicating they are accessible.
- **Error Handling**: Catches and logs URLs with missing schema errors.
- **Easy Output Management**: Saves filtered URLs to a specified output file for further analysis.

## Installation

Ensure you have Python 3 and the `requests` library installed. If `requests` is not installed, you can install it using:

```bash
pip install requests

Usage

    Save the script to a file, for example, url_filter.py.
    Run the script and provide URLs through standard input.

python3 url_filter.py < input_urls.txt

Replace input_urls.txt with your file containing the list of URLs.
Example

python3 url_filter.py < urls.txt

The script will prompt you for the output filename:

Enter file name: 

After entering a name, it will save valid URLs to Filtered.txt or any name you provide.
Output

    Filtered.txt: A file containing only the URLs that return a 200 OK status.
    Error Handling: URLs without a valid schema (e.g., missing http:// or https://) are skipped and added to the bad_url list.

Example Output

Saved URLs to Filtered.txt

Requirements

    Python 3.x
    Requests Library

Notes

    Ensure your input URLs file uses one URL per line.
    Only URLs with a 200 response code are saved; all others are ignored.
