import sys
import requests


def urls(output_file):
    url2 = sys.stdin.read().splitlines()

    good_url = []
    bad_url = []

    for url in url2:
        try:
            response = requests.head(url)

            if response.status_code == 200:
                good_url.append(url)

        except requests.exceptions.MissingSchema:
            bad_url.append(url)


    with open(output_file, 'w') as file:
        file.write('\n'.join(good_url))


    print(f"Saved urls {output_file}")

output_files = input("Enter file name: ")
output_file = "Filtered.txt"
urls(output_file)

