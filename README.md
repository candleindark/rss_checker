# rss_checker

## Usage ##
The purpose and interface of `find_inactive` in `rss_checker.py` is specified in the docstring of the function. To avoid
unneeded duplication, they will not be restated here. Here is, however, an example of its usage.

```python
import rss_checker

rss_feeds_by_company_names = {'bill_maher': 'http://billmaher.hbo.libsynpro.com/rss',
                              'bill_simmons': 'https://rss.art19.com/the-bill-simmons-podcast',
                              'bbc_europe': 'http://feeds.bbci.co.uk/news/world/europe/rss.xml'}
days_of_inactivity = 1

inactive_feeds = rss_checker.find_inactive(rss_feeds_by_company_names, days_of_inactivity)
```

## Assumptions ##
* According to [RSS Specification](http://www.rssboard.org/rss-specification "RSS Specification"), the `pubDate` element
is optional in both the `channel` element and any `item` element in a RSS feed. Assuming the intent of the 
`find_inactive` function is to identify RSS feeds that are without any new items for a specified number of days, the
`pubDate` elements in items are the only `pubDate` elements in a RSS feed that are used to determine the output of the 
function. Additionally, an item is always considered to be older than the specified number of days given to the function
if the item doesn't have an `pubDate` element.

* The problem specifies that one argument to `find_inactive` is a dictionary keyed by "Company". I assume this means the
dictionary is one that has company names, in the form of a character string, as the keys, and each key in the dictionary
uniquely identifies a company. However, this seems to contradict with the hint given in the problem specification that 
"some companies might have more than one feed". I requested clarification from the recruiter yesterday and am yet to 
receive a response (possibly because Independent's Day being tomorrow). Without any clarification for the apparent
contradiction, I construct my solution based on my said assumption and ignoring the hint.

## Execution Environment ##
The `find_inactive` function requires [feedparser](https://github.com/kurtmckee/feedparser) to function. To install
feedparser in your Python environment, type the following command in your Unix terminal.
```
pip install feedparser
```

`find_inactive` has been tested in Python 3.7.3 with feedparser 5.2.1. 
