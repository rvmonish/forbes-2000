# *Task 1*
* Create crawler/Scraper using Python [Preferable using Scrapy] to scrape data from ***https://www.forbes.com/lists/global2000/?sh=45f017755ac0*** and save data in JSON format, attribute-wise.
* Get the list of all ***2000*** companies.
* Final Json document should contain
    * Rank
    * Organisation Name
    * Country Name
    * revenue
    * Profit
    * Asset
    * Market Value
    * Link to individual company profile
    
## Example
```
    {
    rank : 1,
    organisation_name : Berkshire Hathaway,
    country_name : United States,
    revenue : $276.09B,
    profit : $89.8B,
    asset : $959.4B,
    market_value : $700B,
    link :https://www.forbes.com/companies/berkshire-hathaway/?list=global2000&sh=4616376fbef8
    }
```
### *Bonus:*
* Use parallel processing in the script.
