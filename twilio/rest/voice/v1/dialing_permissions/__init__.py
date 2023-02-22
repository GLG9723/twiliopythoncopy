"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Voice
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version

from twilio.rest.voice.v1.dialing_permissions.bulk_country_updates import BulkCountryUpdateList
from twilio.rest.voice.v1.dialing_permissions.countries import CountryList
from twilio.rest.voice.v1.dialing_permissions.settings import SettingsList


class DialingPermissionsList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the DialingPermissionsList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.voice.v1.dialing_permissions.DialingPermissionsList
        :rtype: twilio.rest.voice.v1.dialing_permissions.DialingPermissionsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/DialingPermissions'.format(**self._solution)
        
        self._bulk_country_updates = None
        self._countries = None
        self._settings = None
        

    @property
    def bulk_country_updates(self):
        """
        Access the bulk_country_updates

        :returns: twilio.rest.voice.v1.dialing_permissions.BulkCountryUpdateList
        :rtype: twilio.rest.voice.v1.dialing_permissions.BulkCountryUpdateList
        """
        if self._bulk_country_updates is None:
            self._bulk_country_updates = BulkCountryUpdateList(self._version)
        return self.bulk_country_updates

    @property
    def countries(self):
        """
        Access the countries

        :returns: twilio.rest.voice.v1.dialing_permissions.CountryList
        :rtype: twilio.rest.voice.v1.dialing_permissions.CountryList
        """
        if self._countries is None:
            self._countries = CountryList(self._version)
        return self.countries

    @property
    def settings(self):
        """
        Access the settings

        :returns: twilio.rest.voice.v1.dialing_permissions.SettingsList
        :rtype: twilio.rest.voice.v1.dialing_permissions.SettingsList
        """
        if self._settings is None:
            self._settings = SettingsList(self._version)
        return self.settings


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Voice.V1.DialingPermissionsList>'




