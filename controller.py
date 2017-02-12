import sys, getopt
from crawler import Crawler

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[2:], "u:d:", ["userid=", "depth="])
    except getopt.GetoptError:
        print("python3 crawler.py ")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-u", "--userid"):
            userid = arg
        elif opt in ("-d", "--depth"):
            depth = int(arg)

    crawler = Crawler()
    crawler.crawl(userid, depth)