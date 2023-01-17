"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.domain import Domain
from twilio.rest.preview.sync import Sync

class Preview(Domain):
    def __init__(self, twilio):
        """
        Initialize the Preview Domain

        :returns: Domain for Preview
        :rtype: twilio.rest.sync.Preview
        """
        super(Preview, self).__init__(twilio)
        self.base_url = 'https://Preview.twilio.com'
        self._Sync = None

    @property
    def Sync(self):
        """
        :returns: Versions sync of Preview
        :rtype: twilio.rest.Preview.sync
        """
        if self._Sync is None:
            self._Sync = Sync(self)
        return self._Sync
    

    @property
    def services(self):
        """
        :rtype: twilio.rest.sync.services
        """
        return self.sync.services
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview>'
