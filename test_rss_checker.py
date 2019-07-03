from unittest import TestCase
import time
import calendar

DAY_IN_SECONDS = 60 * 60 * 24


class TestRssChecker(TestCase):
    def test_find_inactive(self):
        from rss_checker import find_inactive
        feed_urls_by_companies = {'bill_maher': 'test_inputs/bill_maher.xml',
                                  'bill_simmons': 'test_inputs/bill_simmons.xml'}

        # time stamps of the latest items
        bill_maher_latest = calendar.timegm((2019, 7, 1, 20, 25, 4, 0, 182, 0))
        bill_simmons_latest = calendar.timegm((2019, 7, 2, 23, 25, 38, 1, 183, 0))

        # time elapsed since the latest items
        time_elapsed_bill_maher = time.time() - bill_maher_latest
        time_elapsed_bill_simmons = time.time() - bill_simmons_latest

        # The number of days elapsed since the feed with the earliest latest activity
        max_days_elapsed = max(time_elapsed_bill_maher, time_elapsed_bill_simmons) // DAY_IN_SECONDS

        self.assertEqual(find_inactive(feed_urls_by_companies, max_days_elapsed), [])
