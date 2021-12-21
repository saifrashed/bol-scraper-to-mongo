# common-bol-com-scraper
Bol.com scraper

# Installation
Clone this repository
- run `pip install Scrapy`
- rund `scrapy crawl bol`  

# Functionality
As a starter this scraper retrieves product-ids and product-names.

### Contribute to this Scraper
If you want to contribute to this scraper: Just create a pull request with you bugfix, addition, typofix or something else you think is valuable.

Thanks for your help!



# notities



## Update een gegeven items zijn quantiteit (en haal dus maximale op) LET OP: Bevat een unieke winkelwagen ID voor gegeven product
https://www.bol.com/nl/order/basket/updateItemQuantity.html?id=61c267b79e110e1ff7ea28ff&quantity=500


## De golden link, Voegt van een gegeven product ID een gegeven hoeveelheid. Hiermee kun je achterhalen wat de voorraden zijn

https://www.bol.com/nl/order/basket/addItems.html?productId=9200000129158728&offerId=0&quantity=1
