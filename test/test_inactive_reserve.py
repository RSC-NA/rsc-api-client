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

from rscapi.models.inactive_reserve import InactiveReserve  # noqa: E501

class TestInactiveReserve(unittest.TestCase):
    """InactiveReserve unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InactiveReserve:
        """Test InactiveReserve
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InactiveReserve`
        """
        model = InactiveReserve()  # noqa: E501
        if include_optional:
            return InactiveReserve(
                player = 56,
                league = 56,
                executor = 56,
                notes = '',
                admin_override = True,
                remove_from_ir = True
            )
        else:
            return InactiveReserve(
                player = 56,
                league = 56,
                executor = 56,
        )
        """

    def testInactiveReserve(self):
        """Test InactiveReserve"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()