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

from rscapi.models.temporary_fa_sub import TemporaryFASub  # noqa: E501

class TestTemporaryFASub(unittest.TestCase):
    """TemporaryFASub unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TemporaryFASub:
        """Test TemporaryFASub
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TemporaryFASub`
        """
        model = TemporaryFASub()  # noqa: E501
        if include_optional:
            return TemporaryFASub(
                player_in = 56,
                player_out = 56,
                league = 56,
                executor = 56,
                notes = '',
                admin_override = True
            )
        else:
            return TemporaryFASub(
                player_in = 56,
                player_out = 56,
                league = 56,
                executor = 56,
        )
        """

    def testTemporaryFASub(self):
        """Test TemporaryFASub"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()