# quora-crawler
Use selenium, beautiful soup and mongodb to crawl and store data from quora
The reason to use selenium is that sometimes pages are loaded using javascript when new items show up as you scroll down, and simply using beautiful soup won't enable javascript and show all the results. selenium is mostly used to show up all the results, and beautiful soup is easier than selenium to analyze and crawl the data.

# precondition
1. install python3
https://www.python.org/downloads/
2. install selenium
3. install beautiful soup
4. install pymongo
5. run pymongo on localhost (command line: mongod)

# usage
userid is your personal userid and depth means how many steps you will crawl from your followers. (1 means one-step followers, 2 means two-step followers, etc). Please go to your personal profile, and you will find your userid in url. For example, mine: https://www.quora.com/profile/Justin-Li-65

python3 controller.py -u \<userid\> -d \<depth\>

python3 controller.py --userid \<userid\> --depth \<depth\>

# example

python3 controller.py -u Justin-Li-65 -d 1

python3 controller.py --userid Justin-Li-65 --depth 1
