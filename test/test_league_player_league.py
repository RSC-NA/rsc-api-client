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

from rscapi.models.league_player_league import LeaguePlayerLeague  # noqa: E501

class TestLeaguePlayerLeague(unittest.TestCase):
    """LeaguePlayerLeague unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LeaguePlayerLeague:
        """Test LeaguePlayerLeague
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LeaguePlayerLeague`
        """
        model = LeaguePlayerLeague()  # noqa: E501
        if include_optional:
            return LeaguePlayerLeague(
                id = 56,
                name = '0',
                guild_id = -9223372036854775808
            )
        else:
            return LeaguePlayerLeague(
                name = '0',
                guild_id = -9223372036854775808,
        )
        """

    def testLeaguePlayerLeague(self):
        """Test LeaguePlayerLeague"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()