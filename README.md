# angelListCsv
uses Selenuim and BeautifulSoup to scrape info from Angel List's database of companies into your own csv file. 

Takes a full url as input. Start at https://angel.co/companies , use any filters to narrow your search, and then paste the new url into the running script. 

Notes/Places to Improve: neither implicit nor explicit waits in Selenium worked while clicking the 'more' button to display the max number of companies possible. They caused the same 20 companies to be appended to the page's list, resulting in nothing but repetitions. Instead, I used sleep statements; they produced the desired outcome, but are inherently worse otherwise (longer waits / incomplete csv if the page doesn't load in time). 
Also, angellist only allows a user to hit 'more' 20 times, limiting the scope of the project somewhat.
