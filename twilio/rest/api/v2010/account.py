"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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

from twilio.base.page import Page

from twilio.rest.account.address import AddressListInstancefrom twilio.rest.account.application import ApplicationListInstancefrom twilio.rest.account.authorized_connect_app import AuthorizedConnectAppListInstancefrom twilio.rest.account.available_phone_number_country import AvailablePhoneNumberCountryListInstancefrom twilio.rest.account.balance import BalanceListInstancefrom twilio.rest.account.call import CallListInstancefrom twilio.rest.account.conference import ConferenceListInstancefrom twilio.rest.account.connect_app import ConnectAppListInstancefrom twilio.rest.account.incoming_phone_number import IncomingPhoneNumberListInstancefrom twilio.rest.account.key import KeyListInstancefrom twilio.rest.account.message import MessageListInstancefrom twilio.rest.account.new_key import NewKeyListInstancefrom twilio.rest.account.new_signing_key import NewSigningKeyListInstancefrom twilio.rest.account.notification import NotificationListInstancefrom twilio.rest.account.outgoing_caller_id import OutgoingCallerIdListInstancefrom twilio.rest.account.queue import QueueListInstancefrom twilio.rest.account.recording import RecordingListInstancefrom twilio.rest.account.short_code import ShortCodeListInstancefrom twilio.rest.account.signing_key import SigningKeyListInstancefrom twilio.rest.account.sip import SipListInstancefrom twilio.rest.account.token import TokenListInstancefrom twilio.rest.account.transcription import TranscriptionListInstancefrom twilio.rest.account.usage import UsageListInstancefrom twilio.rest.account.validation_request import ValidationRequestListInstance


class AccountContext(InstanceContext):
    def __init__(self, version: V2010, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid,  }
        self._uri = '/Accounts/${sid}.json'
        
        self._addresses = None
        self._applications = None
        self._authorized_connect_apps = None
        self._available_phone_numbers = None
        self._balance = None
        self._calls = None
        self._conferences = None
        self._connect_apps = None
        self._incoming_phone_numbers = None
        self._keys = None
        self._messages = None
        self._new_keys = None
        self._new_signing_keys = None
        self._notifications = None
        self._outgoing_caller_ids = None
        self._queues = None
        self._recordings = None
        self._short_codes = None
        self._signing_keys = None
        self._sip = None
        self._tokens = None
        self._transcriptions = None
        self._usage = None
        self._validation_requests = None
    
    def fetch(self):
        
        """
        Fetch the AccountInstance

        :returns: The fetched AccountInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )
        return AccountInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
        )
        
        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return AccountInstance(self._version, payload, sid=self._solution['sid'], )
        
        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AccountContext>'



class AccountInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super().__init__(version)
        self._properties = { 
            'auth_token' : payload.get('auth_token'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'friendly_name' : payload.get('friendly_name'),
            'owner_account_sid' : payload.get('owner_account_sid'),
            'sid' : payload.get('sid'),
            'status' : payload.get('status'),
            'subresource_uris' : payload.get('subresource_uris'),
            'type' : payload.get('type'),
            'uri' : payload.get('uri'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = AccountContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def addresses(self):
        return self._proxy.addresses
    @property
    def applications(self):
        return self._proxy.applications
    @property
    def authorized_connect_apps(self):
        return self._proxy.authorized_connect_apps
    @property
    def available_phone_numbers(self):
        return self._proxy.available_phone_numbers
    @property
    def balance(self):
        return self._proxy.balance
    @property
    def calls(self):
        return self._proxy.calls
    @property
    def conferences(self):
        return self._proxy.conferences
    @property
    def connect_apps(self):
        return self._proxy.connect_apps
    @property
    def incoming_phone_numbers(self):
        return self._proxy.incoming_phone_numbers
    @property
    def keys(self):
        return self._proxy.keys
    @property
    def messages(self):
        return self._proxy.messages
    @property
    def new_keys(self):
        return self._proxy.new_keys
    @property
    def new_signing_keys(self):
        return self._proxy.new_signing_keys
    @property
    def notifications(self):
        return self._proxy.notifications
    @property
    def outgoing_caller_ids(self):
        return self._proxy.outgoing_caller_ids
    @property
    def queues(self):
        return self._proxy.queues
    @property
    def recordings(self):
        return self._proxy.recordings
    @property
    def short_codes(self):
        return self._proxy.short_codes
    @property
    def signing_keys(self):
        return self._proxy.signing_keys
    @property
    def sip(self):
        return self._proxy.sip
    @property
    def tokens(self):
        return self._proxy.tokens
    @property
    def transcriptions(self):
        return self._proxy.transcriptions
    @property
    def usage(self):
        return self._proxy.usage
    @property
    def validation_requests(self):
        return self._proxy.validation_requests
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.AccountInstance {}>'.format(context)



class AccountListInstance(ListResource):
    def __init__(self, version: V2010):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Accounts.json'
        
    
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return AccountInstance(self._version, payload, )
        
    
    def page(self, friendly_name, status, page_size):
        
        data = values.of({
            'friendly_name': friendly_name,'status': status,'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return AccountPage(self._version, payload, )
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AccountListInstance>'

