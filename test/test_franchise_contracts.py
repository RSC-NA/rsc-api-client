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

from rscapi.models.franchise_contracts import FranchiseContracts

class TestFranchiseContracts(unittest.TestCase):
    """FranchiseContracts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FranchiseContracts:
        """Test FranchiseContracts
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FranchiseContracts`
        """
        model = FranchiseContracts()
        if include_optional:
            return FranchiseContracts(
                name = '0',
                gm = '0',
                prefix = '0'
            )
        else:
            return FranchiseContracts(
                gm = '0',
        )
        """

    def testFranchiseContracts(self):
        """Test FranchiseContracts"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
