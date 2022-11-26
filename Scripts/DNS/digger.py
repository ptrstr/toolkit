import pydig
import sys
import tqdm

def scan(domain):
	try:
		cnames = pydig.query(domain, 'CNAME')
		if len(cnames) > 0:
			print('CNAME\t%s\t->\t%r' % (domain, cnames))

		addr = pydig.query(domain, 'A')
		if len(addr) > 0 and all(x not in cnames for x in addr):
			print('A\t%s\t->\t%r' % (domain, addr))
	except Exception as ex:
		if isinstance(ex, KeyboardInterrupt):
			raise ex

def main(argv):
	if len(argv) != 2:
		print('Usage: %s <path to file with domains|- for stdin>' % (argv[0]))
		return 1

	file = sys.stdin if argv[1] == '-' else open(argv[1], 'r')

	for domain in file:
		scan(domain.strip())

	if file != sys.stdin:
		file.close()

	return 0

if __name__ == '__main__':
	exit(main(sys.argv))