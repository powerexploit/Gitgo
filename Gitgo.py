#!/usr/bin/python3
import requests
import bs4 
import argparse
import sys
from colorama import Fore

def gitpinnedrepo(username):
	res = requests.get("https://github.com/%s" %(username))
	soup = bs4.BeautifulSoup(res.text,"html.parser")
	pinned = soup.find_all("span", class_='repo')
	for pinned_repo in range(len(pinned)):
		print(Fore.WHITE + pinned[pinned_repo].text)

def getprofile_stats(username):
	res = requests.get("https://github.com/{}".format(username))
	soup = bs4.BeautifulSoup(res.content,"html.parser")
	name=soup.find('span',{'class':'p-name vcard-fullname d-block overflow-hidden'}).text
	data=soup.find_all('span',{'class':'text-bold text-gray-dark'})
	location=soup.find('span',{'class':'p-label'}).text
	stars=data[2].text
	following=data[1].text
	followers=data[0].text
	data=soup.find('span',{'class':'Counter'})
	repositories=data.text
	profile_data={'name':name,'location':location,'stars':stars,'following':following,'followers':followers,'repositories':repositories}
	return profile_data


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