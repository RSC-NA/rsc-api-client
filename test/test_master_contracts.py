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

from rscapi.models.master_contracts import MasterContracts

class TestMasterContracts(unittest.TestCase):
    """MasterContracts unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MasterContracts:
        """Test MasterContracts
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MasterContracts`
        """
        model = MasterContracts()
        if include_optional:
            return MasterContracts(
                active = True,
                rsc_id = '0',
                name = '0',
                franchise = '',
                contract_length = -2147483648,
                current_mmr = -2147483648,
                status = '',
                base_mmr = -2147483648,
                team_name = '',
                waiver_period_end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return MasterContracts(
                active = True,
                rsc_id = '0',
                name = '0',
                contract_length = -2147483648,
        )
        """

    def testMasterContracts(self):
        """Test MasterContracts"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
