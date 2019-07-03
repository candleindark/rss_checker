# rss_checker

## Usage: ##
The purpose and interface of `find_inactive` in `rss_checker.py` is specified in the docstring of the function. To avoid
unneeded duplication, they will not be restated here. Here is, however, an example of its usage.

```
import rss_checker

rss_feeds_by_company_names = {'bill_maher': 'http://billmaher.hbo.libsynpro.com/rss',
                              'bill_simmons': 'https://rss.art19.com/the-bill-simmons-podcast',
                              'bbc_europe': 'http://feeds.bbci.co.uk/news/world/europe/rss.xml'}
days_of_inactivity = 1

inactive_feeds = rss_checker.find_inactive(rss_feeds_by_company_names, days_of_inactivity)
```

## Assumptions: ##

## Execution Environment: ##

