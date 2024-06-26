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

from rscapi.models.master_member_sheet import MasterMemberSheet

class TestMasterMemberSheet(unittest.TestCase):
    """MasterMemberSheet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MasterMemberSheet:
        """Test MasterMemberSheet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MasterMemberSheet`
        """
        model = MasterMemberSheet()
        if include_optional:
            return MasterMemberSheet(
                rsc_id = '',
                rsc_name = '0',
                discord_id = 56,
                threes_active = True
            )
        else:
            return MasterMemberSheet(
        )
        """

    def testMasterMemberSheet(self):
        """Test MasterMemberSheet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
