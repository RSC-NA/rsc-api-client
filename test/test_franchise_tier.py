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

from rscapi.models.franchise_tier import FranchiseTier  # noqa: E501

class TestFranchiseTier(unittest.TestCase):
    """FranchiseTier unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FranchiseTier:
        """Test FranchiseTier
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FranchiseTier`
        """
        model = FranchiseTier()  # noqa: E501
        if include_optional:
            return FranchiseTier(
                name = '0',
                id = 56
            )
        else:
            return FranchiseTier(
        )
        """

    def testFranchiseTier(self):
        """Test FranchiseTier"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
