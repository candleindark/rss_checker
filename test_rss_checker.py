from unittest import TestCase
import time
import calendar

DAY_IN_SECONDS = 60 * 60 * 24


class TestRssChecker(TestCase):
    def test_find_inactive(self):
        from rss_checker import find_inactive

        feed_urls_by_companies = {}
        with self.subTest(feed_urls_by_companies=feed_urls_by_companies):
            self.assertEqual([], find_inactive(feed_urls_by_companies, 0))
            self.assertEqual([], find_inactive(feed_urls_by_companies, 1))
            self.assertEqual([], find_inactive(feed_urls_by_companies, 99))

        feed_urls_by_companies = {'bill_maher': 'test_inputs/bill_maher.xml'}
        with self.subTest(feed_urls_by_companies=feed_urls_by_companies):
            # time stamp of the latest item
            bill_maher_latest = calendar.timegm((2019, 7, 1, 20, 25, 4, 0, 182, 0))

            # time elapsed since the latest item
            time_elapsed_bill_maher = time.time() - bill_maher_latest

            days_elapsed_bill_maher = time_elapsed_bill_maher // DAY_IN_SECONDS
            self.assertEqual([], find_inactive(feed_urls_by_companies, days_elapsed_bill_maher + 1))
            self.assertEqual(['bill_maher'], find_inactive(feed_urls_by_companies, days_elapsed_bill_maher - 1))

        feed_urls_by_companies = {'bill_maher': 'test_inputs/bill_maher.xml',
                                  'bill_simmons': 'test_inputs/bill_simmons.xml'}

        with self.subTest(feed_urls_by_companies=feed_urls_by_companies):
            # time stamps of the latest items
            bill_maher_latest = calendar.timegm((2019, 7, 1, 20, 25, 4, 0, 182, 0))
            bill_simmons_latest = calendar.timegm((2019, 7, 2, 23, 25, 38, 1, 183, 0))

            # time elapsed since the latest items
            time_elapsed_bill_maher = time.time() - bill_maher_latest
            time_elapsed_bill_simmons = time.time() - bill_simmons_latest

            days_elapsed_bill_maher = time_elapsed_bill_maher // DAY_IN_SECONDS
            self.assertEqual([], find_inactive(feed_urls_by_companies, days_elapsed_bill_maher + 1))

            days_elapsed_bill_simmons = time_elapsed_bill_simmons // DAY_IN_SECONDS
            self.assertEqual(['bill_maher'], find_inactive(feed_urls_by_companies, days_elapsed_bill_simmons + 1))

        feed_urls_by_companies = {'bill_maher': 'test_inputs/bill_maher.xml',
                                  'bill_simmons': 'test_inputs/bill_simmons.xml',
                                  'bbc_europe': 'test_inputs/bbc_europe.xml'}
        with self.subTest(feed_urls_by_companies=feed_urls_by_companies):
            self.assertEqual(set(['bill_maher', 'bill_simmons', 'bbc_europe']),
                             set(find_inactive(feed_urls_by_companies, 0)))
