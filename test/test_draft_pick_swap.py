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

from rscapi.models.draft_pick_swap import DraftPickSwap

class TestDraftPickSwap(unittest.TestCase):
    """DraftPickSwap unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DraftPickSwap:
        """Test DraftPickSwap
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DraftPickSwap`
        """
        model = DraftPickSwap()
        if include_optional:
            return DraftPickSwap(
                from_gm = 56,
                to_gm = 56,
                round = 56,
                tier = '0',
                league = 56,
                season = 56
            )
        else:
            return DraftPickSwap(
                from_gm = 56,
                to_gm = 56,
                round = 56,
                tier = '0',
                season = 56,
        )
        """

    def testDraftPickSwap(self):
        """Test DraftPickSwap"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()