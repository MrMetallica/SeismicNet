import wget
import os
from pyunpack import Archive

DATA_URL = 'https://getfile.dokpub.com/yandex/get/https://yadi.sk/d/S1pixQPakJ_nJw'
DATA_NAME = 'data.zip'
EXTRACT_PATH = ''

if __name__ == '__main__':
	#Download the data
	filename = wget.download(DATA_URL)

	#Rename file
	os.rename(filename, DATA_NAME)

	#Unpack data
	Archive(DATA_NAME).extractall(EXTRACT_PATH)

