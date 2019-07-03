import feedparser
import time
import calendar

DAY_IN_SECONDS = 60 * 60 * 24


def find_inactive(rss_feed_urls, days_of_inactivity):
    """
    Given a dictionary with keys of company names (in str) and values of RSS feed urls (in str) to the corresponding
    companies named. Obtain the list of companies, by name, that have no activity in their RSS feeds for a given number
    of days.
    :param rss_feed_urls: The given dictionary
    :param days_of_inactivity: The given number of days of inactivity
    :return: The list of companies, specified in name, that have no activity in their RSS feeds for a given number
    of days.
    """
    cutoff_time = time.time() - days_of_inactivity * DAY_IN_SECONDS
    latest_publishing_times = {}

    # Obtain the publishing time, in timestamp, of the latest published item of each feed
    for company in rss_feed_urls:
        rss_feed = feedparser.parse(rss_feed_urls[company])

        # Obtain the publishing time of the latest published item in a rss feed
        latest_publishing_time = None
        for entry in rss_feed.entries:
            publishing_time = entry.get('published_parsed', None)

            if publishing_time is not None:
                publishing_time = calendar.timegm(publishing_time)  # Specify publishing time as a timestamp

                if latest_publishing_time is None:
                    latest_publishing_time = publishing_time
                elif publishing_time > latest_publishing_time:
                    latest_publishing_time = publishing_time

        latest_publishing_times[company] = latest_publishing_time

    # Obtain the list of inactive companies within days_of_inactivity days
    inactive_companies = []
    for company in latest_publishing_times:
        latest_publishing_time = latest_publishing_times[company]

        if latest_publishing_time is None or latest_publishing_time < cutoff_time:
            inactive_companies.append(company)

    return inactive_companies
