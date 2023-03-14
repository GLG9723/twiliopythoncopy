from warnings import warn

from twilio.rest.messaging.MessagingBase import MessagingBase
from twilio.rest.messaging.v1.brand_registration import BrandRegistrationList
from twilio.rest.messaging.v1.deactivations import DeactivationsList
from twilio.rest.messaging.v1.domain_certs import DomainCertsList
from twilio.rest.messaging.v1.domain_config import DomainConfigList
from twilio.rest.messaging.v1.external_campaign import ExternalCampaignList
from twilio.rest.messaging.v1.service import ServiceList
from twilio.rest.messaging.v1.tollfree_verification import TollfreeVerificationList
from twilio.rest.messaging.v1.usecase import UsecaseList


class Messaging(MessagingBase):
    @property
    def brand_registrations(self) -> BrandRegistrationList:
        warn(
            "brand_registrations is deprecated. Use v1.brand_registrations instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.brand_registrations

    @property
    def deactivations(self) -> DeactivationsList:
        warn(
            "deactivations is deprecated. Use v1.deactivations instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.deactivations

    @property
    def domain_certs(self) -> DomainCertsList:
        warn(
            "domain_certs is deprecated. Use v1.domain_certs instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.domain_certs

    @property
    def domain_config(self) -> DomainConfigList:
        warn(
            "domain_config is deprecated. Use v1.domain_config instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.domain_config

    @property
    def external_campaign(self) -> ExternalCampaignList:
        warn(
            "external_campaign is deprecated. Use v1.external_campaign instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.external_campaign

    @property
    def services(self) -> ServiceList:
        warn(
            "services is deprecated. Use v1.services instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.services

    @property
    def tollfree_verifications(self) -> TollfreeVerificationList:
        warn(
            "tollfree_verifications is deprecated. Use v1.tollfree_verifications instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.tollfree_verifications

    @property
    def usecases(self) -> UsecaseList:
        warn(
            "usecases is deprecated. Use v1.usecases instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.usecases
