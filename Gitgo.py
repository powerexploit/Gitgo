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
	print(Fore.BLUE + "\n [+] Gitgo scraping pinned_repo Name of user..... \n")
	for pinned_repo in range(len(pinned)):
		print(Fore.WHITE + pinned[pinned_repo].text)
	print("...............................................................")

def gistrepo(username):
	res = requests.get("https://gist.github.com/%s" %(username))
	soup = bs4.BeautifulSoup(res.text,"html.parser")
	gist = soup.find_all("strong", class_='css-truncate-target')
	print(Fore.BLUE + "\n\n [+] Gitgo scraping all gist Name of user..... \n")
	for gist_repo in range(len(gist)):
		print(Fore.WHITE + gist[gist_repo].text)
	print("...............................................................")
		
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
	print(Fore.RED + "\n\n [+] Gitgo scraping profile_data of user \n")
	print(profile_data)


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
░ ░   ░  ▒ ░  ░      ░ ░   ░ ░ ░ ░ ▒   > v1.0
      ░  ░                 ░     ░ ░   > By ankitdobhal , mdb571 , anisha282000

''')

	if args.gitusername:
		gitpinnedrepo(args.gitusername)
		gistrepo(args.gitusername)
		getprofile_stats(args.gitusername)
		exit()