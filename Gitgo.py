#!/usr/bin/python3
import requests
import bs4 
import argparse
from colorama import Fore

def gitpinnedrepo(username):
	res = requests.get("https://github.com/%s" %(username))
	soup = bs4.BeautifulSoup(res.text,"html.parser")
	pinned = soup.find_all("span", class_='repo')
	for pinned_repo in range(len(pinned)):
		print(Fore.WHITE + pinned[pinned_repo].text)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--gitusername',help='Github username')
	args = parser.parse_args()
	print(Fore.RED + '''


  ▄████  ██▓▄▄▄█████▓  ▄████  ▒█████  
 ██▒ ▀█▒▓██▒▓  ██▒ ▓▒ ██▒ ▀█▒▒██▒  ██▒
▒██░▄▄▄░▒██▒▒ ▓██░ ▒░▒██░▄▄▄░▒██░  ██▒
░▓█  ██▓░██░░ ▓██▓ ░ ░▓█  ██▓▒██   ██░
░▒▓███▀▒░██░  ▒██▒ ░ ░▒▓███▀▒░ ████▓▒░
 ░▒   ▒ ░▓    ▒ ░░    ░▒   ▒ ░ ▒░▒░▒░ 
  ░   ░  ▒ ░    ░      ░   ░   ░ ▒ ▒░ 
░ ░   ░  ▒ ░  ░      ░ ░   ░ ░ ░ ░ ▒  
      ░  ░                 ░     ░ ░   > v1.0

''')

	if args.gitusername:
		gitpinnedrepo(args.gitusername)
		exit()