# coding: utf-8

"""
    RSC API Docs

    RSC API Documentation

    The version of the OpenAPI document: v1
    Contact: contact@snippets.local
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from rscapi.models.trade_value import TradeValue  # noqa: E501

class TestTradeValue(unittest.TestCase):
    """TradeValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TradeValue:
        """Test TradeValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TradeValue`
        """
        model = TradeValue()  # noqa: E501
        if include_optional:
            return TradeValue(
                player = 56,
                pick = rscapi.models.draft_pick.Draft Pick(
                    tier = '', 
                    round = 56, 
                    number = 56, 
                    future = True, )
            )
        else:
            return TradeValue(
        )
        """

    def testTradeValue(self):
        """Test TradeValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()