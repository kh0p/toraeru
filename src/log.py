import spam
import pictures
import urllib.request

def LogFile():
	getime = spam.get_time()

	log_file_download = open(pictures.cache_dir+"log-"+getime+".txt", "wb")
	log_file_download.write()

LogFile()