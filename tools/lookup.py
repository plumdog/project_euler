#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup


URL = 'https://projecteuler.net'


def lookup(problem_number):
    resp = requests.get(URL + '/problem=' + str(problem_number))
    html = resp.content.decode('utf-8')

    bs = BeautifulSoup(html)
    content = bs.find('div', 'problem_content')
    return content.get_text().strip()


def main():
    import sys
    try:
        num = sys.argv[1]
    except IndexError:
        num = 1

    print(lookup(num))


if __name__ == '__main__':
    main()
