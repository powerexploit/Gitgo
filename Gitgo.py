#!/usr/bin/python3
import requests as res
import bs4 
import argparse
from colorama import Fore, Back, Style

def gitpinnedrepo(username):
	res = requests.get("https://github.com/%s" %(username)).text
	soup = bs4.BeautifulSoup(res.txt,"html.parser")
	pinned = soup.find_all("span", class_='repo')
	for pinned_repo in range(len(pinned)):
		return pinned[pinned_repo].text



if __name__ == '__main__':
	main()