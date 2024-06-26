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

from rscapi.models.tracker_links_list200_response import TrackerLinksList200Response  # noqa: E501

class TestTrackerLinksList200Response(unittest.TestCase):
    """TrackerLinksList200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrackerLinksList200Response:
        """Test TrackerLinksList200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrackerLinksList200Response`
        """
        model = TrackerLinksList200Response()  # noqa: E501
        if include_optional:
            return TrackerLinksList200Response(
                count = 56,
                next = '',
                previous = '',
                results = [
                    rscapi.models.tracker_link.TrackerLink(
                        link = '0', 
                        discord_id = 56, 
                        id = 56, 
                        name = '', 
                        platform = 'STEAM', 
                        status = 'NEW', 
                        last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        member_name = '0', 
                        platform_id = '', 
                        rscid = '0', )
                    ]
            )
        else:
            return TrackerLinksList200Response(
                count = 56,
                results = [
                    rscapi.models.tracker_link.TrackerLink(
                        link = '0', 
                        discord_id = 56, 
                        id = 56, 
                        name = '', 
                        platform = 'STEAM', 
                        status = 'NEW', 
                        last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        member_name = '0', 
                        platform_id = '', 
                        rscid = '0', )
                    ],
        )
        """

    def testTrackerLinksList200Response(self):
        """Test TrackerLinksList200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
