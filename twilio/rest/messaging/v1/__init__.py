# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.version import Version
from twilio.rest.messaging.v1.brand_registration import BrandRegistrationList
from twilio.rest.messaging.v1.deactivation import DeactivationsList
from twilio.rest.messaging.v1.external_campaign import ExternalCampaignList
from twilio.rest.messaging.v1.service import ServiceList
from twilio.rest.messaging.v1.tollfree_verification import TollfreeVerificationList
from twilio.rest.messaging.v1.usecase import UsecaseList


class V1(Version):

    def __init__(self, domain):
        """
        Initialize the V1 version of Messaging

        :returns: V1 version of Messaging
        :rtype: twilio.rest.messaging.v1.V1.V1
        """
        super(V1, self).__init__(domain)
        self.version = 'v1'
        self._brand_registrations = None
        self._deactivations = None
        self._external_campaign = None
        self._services = None
        self._tollfree_verifications = None
        self._usecases = None

    @property
    def brand_registrations(self):
        """
        :rtype: twilio.rest.messaging.v1.brand_registration.BrandRegistrationList
        """
        if self._brand_registrations is None:
            self._brand_registrations = BrandRegistrationList(self)
        return self._brand_registrations

    @property
    def deactivations(self):
        """
        :rtype: twilio.rest.messaging.v1.deactivation.DeactivationsList
        """
        if self._deactivations is None:
            self._deactivations = DeactivationsList(self)
        return self._deactivations

    @property
    def external_campaign(self):
        """
        :rtype: twilio.rest.messaging.v1.external_campaign.ExternalCampaignList
        """
        if self._external_campaign is None:
            self._external_campaign = ExternalCampaignList(self)
        return self._external_campaign

    @property
    def services(self):
        """
        :rtype: twilio.rest.messaging.v1.service.ServiceList
        """
        if self._services is None:
            self._services = ServiceList(self)
        return self._services

    @property
    def tollfree_verifications(self):
        """
        :rtype: twilio.rest.messaging.v1.tollfree_verification.TollfreeVerificationList
        """
        if self._tollfree_verifications is None:
            self._tollfree_verifications = TollfreeVerificationList(self)
        return self._tollfree_verifications

    @property
    def usecases(self):
        """
        :rtype: twilio.rest.messaging.v1.usecase.UsecaseList
        """
        if self._usecases is None:
            self._usecases = UsecaseList(self)
        return self._usecases

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1>'
