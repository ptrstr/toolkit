import requests
import sys
from multiprocessing.pool import ThreadPool as Pool
from tqdm import tqdm

def get_tor_session():
	session = requests.Session()
	session.proxies = {
		'http': 'socks5h://127.0.0.1:9150',
		'https': 'socks5h://127.0.0.1:9150'
	}

	return session

SESS = get_tor_session()

def test_wordpress_page_id(endpoint, page_id):
	url = f'{endpoint}/?page_id={page_id}'
	url = f'{endpoint}/?p={page_id}'

	resp = SESS.get(url, allow_redirects=False)

	if resp.status_code != 404:
		print(f'{url}\t\t->\t\t{resp.headers.get("Location", "<self>")}')
		sys.stdout.flush()
		return True

	return False


def wordpress_enum(endpoint, min_len, max_len, workers=10):
	pool = Pool(workers)

	for page_id in range(min_len, max_len):
		pool.apply_async(test_wordpress_page_id, (endpoint, page_id))

	pool.close()
	pool.join()

def main(argv):
	if len(argv) not in [3, 4]:
		print('Usage: %s WORDPRESS_URL page_id_max' % (argv[0]))
		return 1

	min_len = 0
	max_len = int(argv[2])

	if len(argv) == 4:
		min_len = max_len
		max_len = int(argv[3])

	wordpress_enum(argv[1], min_len, max_len)

	return 0

if __name__ == '__main__':
	exit(main(sys.argv))
