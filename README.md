# quora-crawler
Use selenium, beautiful soup and mongodb to crawl and store data from quora
The reason to use selenium is that sometimes pages are loaded using javascript when new items show up as you scroll down, and simply using beautiful soup won't enable javascript and show all the results. selenium is mostly used to show up all the results, and beautiful soup is easier than selenium to analyze and crawl the data.

# usage
python3 controller.py -u <userid> -d <depth>

python3 controller.py --userid <userid> --depth <depth>

# example
Please go to your personal profile, and you will find your userid in url. For example, mine: https://www.quora.com/profile/Justin-Li-65

python3 controller.py -u Justin-Li-65 -d 1

python3 controller.py --userid Justin-Li-65 --depth 1
