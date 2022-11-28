import requests
import sys
from multiprocessing.pool import ThreadPool as Pool
from tqdm import tqdm

def test_drupal_node(endpoint, node):
	url = f'{endpoint}/node/{node}'

	resp = requests.get(url, allow_redirects=False)

	if resp.status_code != 404:
		print(f'{url}\t\t->\t\t{resp.headers["Location"]}')
		sys.stdout.flush()
		return True

	return False


def drupal_enum(endpoint, max, workers=10):
	pool = Pool(workers)

	for node in range(max):
		pool.apply_async(test_drupal_node, (endpoint, node))

	pool.close()
	pool.join()

def main(argv):
	if len(argv) != 3:
		print('Usage: %s DRUPAL_URL node_max' % (argv[0]))

	drupal_enum(argv[1], int(argv[2]))

	return 0

if __name__ == '__main__':
	exit(main(sys.argv))
