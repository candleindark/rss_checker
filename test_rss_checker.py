from unittest import TestCase
import time
import calendar

SECONDS_IN_DAY = 60 * 60 * 24


class TestRssChecker(TestCase):
    def test_find_inactive(self):
        from rss_checker import find_inactive
        feed_urls_by_companies = {'bill_maher': 'test_inputs/bill_maher.xml',
                                  'bill_simmons': 'test_inputs/bill_simmons.xml'}

        # time stamps of the latest items
        bill_maher_latest = calendar.timegm(time.struct_time(tm_year=2019, tm_mon=7, tm_mday=1, tm_hour=20, tm_min=25,
                                                             tm_sec=4, tm_wday=0, tm_yday=182, tm_isdst=0))
        bill_simmons_latest = calendar.timegm(time.struct_time(tm_year=2019, tm_mon=7, tm_mday=2, tm_hour=23, tm_min=25,
                                                               tm_sec=38, tm_wday=1, tm_yday=183, tm_isdst=0))

        # time elapsed since the latest items
        time_elapsed_bill_maher = time.time() - bill_maher_latest
        time_elapsed_bill_simmons = time.time() - bill_simmons_latest

        # The number of days elapsed since the feed with the earliest latest activity
        max_days_elapsed = max(time_elapsed_bill_maher, time_elapsed_bill_simmons) // SECONDS_IN_DAY

        self.assertEqual(find_inactive(feed_urls_by_companies, max_days_elapsed), [])
