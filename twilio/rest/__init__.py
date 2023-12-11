r"""
  This code was generated by
  ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
   |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
   |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""
from typing import TYPE_CHECKING, Optional

from twilio.base.client_base import ClientBase

if TYPE_CHECKING:
    from twilio.rest.accounts import Accounts
    from twilio.rest.api import Api
    from twilio.rest.autopilot import Autopilot
    from twilio.rest.bulkexports import Bulkexports
    from twilio.rest.chat import Chat
    from twilio.rest.content import Content
    from twilio.rest.conversations import Conversations
    from twilio.rest.events import Events
    from twilio.rest.flex_api import FlexApi
    from twilio.rest.frontline_api import FrontlineApi
    from twilio.rest.insights import Insights
    from twilio.rest.intelligence import Intelligence
    from twilio.rest.ip_messaging import IpMessaging
    from twilio.rest.lookups import Lookups
    from twilio.rest.media import Media
    from twilio.rest.messaging import Messaging
    from twilio.rest.microvisor import Microvisor
    from twilio.rest.monitor import Monitor
    from twilio.rest.notify import Notify
    from twilio.rest.numbers import Numbers
    from twilio.rest.preview import Preview
    from twilio.rest.preview_messaging import PreviewMessaging
    from twilio.rest.pricing import Pricing
    from twilio.rest.proxy import Proxy
    from twilio.rest.routes import Routes
    from twilio.rest.serverless import Serverless
    from twilio.rest.studio import Studio
    from twilio.rest.supersim import Supersim
    from twilio.rest.sync import Sync
    from twilio.rest.taskrouter import Taskrouter
    from twilio.rest.trunking import Trunking
    from twilio.rest.trusthub import Trusthub
    from twilio.rest.verify import Verify
    from twilio.rest.video import Video
    from twilio.rest.voice import Voice
    from twilio.rest.wireless import Wireless
    from twilio.rest.api.v2010.account.address import AddressList
    from twilio.rest.api.v2010.account.application import ApplicationList
    from twilio.rest.api.v2010.account.authorized_connect_app import (
        AuthorizedConnectAppList,
    )
    from twilio.rest.api.v2010.account.available_phone_number_country import (
        AvailablePhoneNumberCountryList,
    )
    from twilio.rest.api.v2010.account.balance import BalanceList
    from twilio.rest.api.v2010.account.call import CallList
    from twilio.rest.api.v2010.account.conference import ConferenceList
    from twilio.rest.api.v2010.account.connect_app import ConnectAppList
    from twilio.rest.api.v2010.account.incoming_phone_number import (
        IncomingPhoneNumberList,
    )
    from twilio.rest.api.v2010.account.key import KeyList
    from twilio.rest.api.v2010.account.new_key import NewKeyList
    from twilio.rest.api.v2010.account.message import MessageList
    from twilio.rest.api.v2010.account.signing_key import SigningKeyList
    from twilio.rest.api.v2010.account.new_signing_key import NewSigningKeyList
    from twilio.rest.api.v2010.account.notification import NotificationList
    from twilio.rest.api.v2010.account.outgoing_caller_id import OutgoingCallerIdList
    from twilio.rest.api.v2010.account.validation_request import ValidationRequestList
    from twilio.rest.api.v2010.account.queue import QueueList
    from twilio.rest.api.v2010.account.recording import RecordingList
    from twilio.rest.api.v2010.account.short_code import ShortCodeList
    from twilio.rest.api.v2010.account.sip import SipList
    from twilio.rest.api.v2010.account.token import TokenList
    from twilio.rest.api.v2010.account.transcription import TranscriptionList
    from twilio.rest.api.v2010.account.usage import UsageList


class Client(ClientBase):
    """A client for accessing the Twilio API."""

    def __init__(
        self,
        username=None,
        password=None,
        account_sid=None,
        region=None,
        http_client=None,
        environment=None,
        edge=None,
        user_agent_extensions=None,
    ):
        """
        Initializes the Twilio Client

        :param str username: Username to authenticate with, either account_sid or api_key
        :param str password: Password to authenticate with, auth_token (if using account_sid) or api_secret (if using api_key)
        :param str account_sid: Account SID, required if using api_key to authenticate.
        :param str region: Twilio Region to make requests to, defaults to 'us1' if an edge is provided
        :param HttpClient http_client: HttpClient, defaults to TwilioHttpClient
        :param dict environment: Environment to look for auth details, defaults to os.environ
        :param str edge: Twilio Edge to make requests to, defaults to None
        :param list[str] user_agent_extensions: Additions to the user agent string

        :returns: Twilio Client
        :rtype: twilio.rest.Client
        """
        super().__init__(
            username,
            password,
            account_sid,
            region,
            http_client,
            environment,
            edge,
            user_agent_extensions,
        )

        # Domains
        self._accounts: Optional["Accounts"] = None
        self._api: Optional["Api"] = None
        self._autopilot: Optional["Autopilot"] = None
        self._bulkexports: Optional["Bulkexports"] = None
        self._chat: Optional["Chat"] = None
        self._content: Optional["Content"] = None
        self._conversations: Optional["Conversations"] = None
        self._events: Optional["Events"] = None
        self._flex_api: Optional["FlexApi"] = None
        self._frontline_api: Optional["FrontlineApi"] = None
        self._insights: Optional["Insights"] = None
        self._intelligence: Optional["Intelligence"] = None
        self._ip_messaging: Optional["IpMessaging"] = None
        self._lookups: Optional["Lookups"] = None
        self._media: Optional["Media"] = None
        self._messaging: Optional["Messaging"] = None
        self._microvisor: Optional["Microvisor"] = None
        self._monitor: Optional["Monitor"] = None
        self._notify: Optional["Notify"] = None
        self._numbers: Optional["Numbers"] = None
        self._preview: Optional["Preview"] = None
        self._preview_messaging: Optional["PreviewMessaging"] = None
        self._pricing: Optional["Pricing"] = None
        self._proxy: Optional["Proxy"] = None
        self._routes: Optional["Routes"] = None
        self._serverless: Optional["Serverless"] = None
        self._studio: Optional["Studio"] = None
        self._supersim: Optional["Supersim"] = None
        self._sync: Optional["Sync"] = None
        self._taskrouter: Optional["Taskrouter"] = None
        self._trunking: Optional["Trunking"] = None
        self._trusthub: Optional["Trusthub"] = None
        self._verify: Optional["Verify"] = None
        self._video: Optional["Video"] = None
        self._voice: Optional["Voice"] = None
        self._wireless: Optional["Wireless"] = None

    @property
    def accounts(self) -> "Accounts":
        """
        Access the Accounts Twilio Domain

        :returns: Accounts Twilio Domain
        """
        if self._accounts is None:
            from twilio.rest.accounts import Accounts

            self._accounts = Accounts(self)
        return self._accounts

    @property
    def api(self) -> "Api":
        """
        Access the Api Twilio Domain

        :returns: Api Twilio Domain
        """
        if self._api is None:
            from twilio.rest.api import Api

            self._api = Api(self)
        return self._api

    @property
    def autopilot(self) -> "Autopilot":
        """
        Access the Autopilot Twilio Domain

        :returns: Autopilot Twilio Domain
        """
        if self._autopilot is None:
            from twilio.rest.autopilot import Autopilot

            self._autopilot = Autopilot(self)
        return self._autopilot

    @property
    def bulkexports(self) -> "Bulkexports":
        """
        Access the Bulkexports Twilio Domain

        :returns: Bulkexports Twilio Domain
        """
        if self._bulkexports is None:
            from twilio.rest.bulkexports import Bulkexports

            self._bulkexports = Bulkexports(self)
        return self._bulkexports

    @property
    def chat(self) -> "Chat":
        """
        Access the Chat Twilio Domain

        :returns: Chat Twilio Domain
        """
        if self._chat is None:
            from twilio.rest.chat import Chat

            self._chat = Chat(self)
        return self._chat

    @property
    def content(self) -> "Content":
        """
        Access the Content Twilio Domain

        :returns: Content Twilio Domain
        """
        if self._content is None:
            from twilio.rest.content import Content

            self._content = Content(self)
        return self._content

    @property
    def conversations(self) -> "Conversations":
        """
        Access the Conversations Twilio Domain

        :returns: Conversations Twilio Domain
        """
        if self._conversations is None:
            from twilio.rest.conversations import Conversations

            self._conversations = Conversations(self)
        return self._conversations

    @property
    def events(self) -> "Events":
        """
        Access the Events Twilio Domain

        :returns: Events Twilio Domain
        """
        if self._events is None:
            from twilio.rest.events import Events

            self._events = Events(self)
        return self._events

    @property
    def flex_api(self) -> "FlexApi":
        """
        Access the FlexApi Twilio Domain

        :returns: FlexApi Twilio Domain
        """
        if self._flex_api is None:
            from twilio.rest.flex_api import FlexApi

            self._flex_api = FlexApi(self)
        return self._flex_api

    @property
    def frontline_api(self) -> "FrontlineApi":
        """
        Access the FrontlineApi Twilio Domain

        :returns: FrontlineApi Twilio Domain
        """
        if self._frontline_api is None:
            from twilio.rest.frontline_api import FrontlineApi

            self._frontline_api = FrontlineApi(self)
        return self._frontline_api

    @property
    def insights(self) -> "Insights":
        """
        Access the Insights Twilio Domain

        :returns: Insights Twilio Domain
        """
        if self._insights is None:
            from twilio.rest.insights import Insights

            self._insights = Insights(self)
        return self._insights

    @property
    def intelligence(self) -> "Intelligence":
        """
        Access the Intelligence Twilio Domain

        :returns: Intelligence Twilio Domain
        """
        if self._intelligence is None:
            from twilio.rest.intelligence import Intelligence

            self._intelligence = Intelligence(self)
        return self._intelligence

    @property
    def ip_messaging(self) -> "IpMessaging":
        """
        Access the IpMessaging Twilio Domain

        :returns: IpMessaging Twilio Domain
        """
        if self._ip_messaging is None:
            from twilio.rest.ip_messaging import IpMessaging

            self._ip_messaging = IpMessaging(self)
        return self._ip_messaging

    @property
    def lookups(self) -> "Lookups":
        """
        Access the Lookups Twilio Domain

        :returns: Lookups Twilio Domain
        """
        if self._lookups is None:
            from twilio.rest.lookups import Lookups

            self._lookups = Lookups(self)
        return self._lookups

    @property
    def media(self) -> "Media":
        """
        Access the Media Twilio Domain

        :returns: Media Twilio Domain
        """
        if self._media is None:
            from twilio.rest.media import Media

            self._media = Media(self)
        return self._media

    @property
    def messaging(self) -> "Messaging":
        """
        Access the Messaging Twilio Domain

        :returns: Messaging Twilio Domain
        """
        if self._messaging is None:
            from twilio.rest.messaging import Messaging

            self._messaging = Messaging(self)
        return self._messaging

    @property
    def microvisor(self) -> "Microvisor":
        """
        Access the Microvisor Twilio Domain

        :returns: Microvisor Twilio Domain
        """
        if self._microvisor is None:
            from twilio.rest.microvisor import Microvisor

            self._microvisor = Microvisor(self)
        return self._microvisor

    @property
    def monitor(self) -> "Monitor":
        """
        Access the Monitor Twilio Domain

        :returns: Monitor Twilio Domain
        """
        if self._monitor is None:
            from twilio.rest.monitor import Monitor

            self._monitor = Monitor(self)
        return self._monitor

    @property
    def notify(self) -> "Notify":
        """
        Access the Notify Twilio Domain

        :returns: Notify Twilio Domain
        """
        if self._notify is None:
            from twilio.rest.notify import Notify

            self._notify = Notify(self)
        return self._notify

    @property
    def numbers(self) -> "Numbers":
        """
        Access the Numbers Twilio Domain

        :returns: Numbers Twilio Domain
        """
        if self._numbers is None:
            from twilio.rest.numbers import Numbers

            self._numbers = Numbers(self)
        return self._numbers

    @property
    def preview(self) -> "Preview":
        """
        Access the Preview Twilio Domain

        :returns: Preview Twilio Domain
        """
        if self._preview is None:
            from twilio.rest.preview import Preview

            self._preview = Preview(self)
        return self._preview

    @property
    def preview_messaging(self) -> "PreviewMessaging":
        """
        Access the Preview Messaging Twilio Domain

        :returns: Preview Messaging Twilio Domain
        """
        if self._preview_messaging is None:
            from twilio.rest.preview_messaging import PreviewMessaging

            self._preview_messaging = PreviewMessaging(self)
        return self._preview_messaging

    @property
    def pricing(self) -> "Pricing":
        """
        Access the Pricing Twilio Domain

        :returns: Pricing Twilio Domain
        """
        if self._pricing is None:
            from twilio.rest.pricing import Pricing

            self._pricing = Pricing(self)
        return self._pricing

    @property
    def proxy(self) -> "Proxy":
        """
        Access the Proxy Twilio Domain

        :returns: Proxy Twilio Domain
        """
        if self._proxy is None:
            from twilio.rest.proxy import Proxy

            self._proxy = Proxy(self)
        return self._proxy

    @property
    def routes(self) -> "Routes":
        """
        Access the Routes Twilio Domain

        :returns: Routes Twilio Domain
        """
        if self._routes is None:
            from twilio.rest.routes import Routes

            self._routes = Routes(self)
        return self._routes

    @property
    def serverless(self) -> "Serverless":
        """
        Access the Serverless Twilio Domain

        :returns: Serverless Twilio Domain
        """
        if self._serverless is None:
            from twilio.rest.serverless import Serverless

            self._serverless = Serverless(self)
        return self._serverless

    @property
    def studio(self) -> "Studio":
        """
        Access the Studio Twilio Domain

        :returns: Studio Twilio Domain
        """
        if self._studio is None:
            from twilio.rest.studio import Studio

            self._studio = Studio(self)
        return self._studio

    @property
    def supersim(self) -> "Supersim":
        """
        Access the Supersim Twilio Domain

        :returns: Supersim Twilio Domain
        """
        if self._supersim is None:
            from twilio.rest.supersim import Supersim

            self._supersim = Supersim(self)
        return self._supersim

    @property
    def sync(self) -> "Sync":
        """
        Access the Sync Twilio Domain

        :returns: Sync Twilio Domain
        """
        if self._sync is None:
            from twilio.rest.sync import Sync

            self._sync = Sync(self)
        return self._sync

    @property
    def taskrouter(self) -> "Taskrouter":
        """
        Access the Taskrouter Twilio Domain

        :returns: Taskrouter Twilio Domain
        """
        if self._taskrouter is None:
            from twilio.rest.taskrouter import Taskrouter

            self._taskrouter = Taskrouter(self)
        return self._taskrouter

    @property
    def trunking(self) -> "Trunking":
        """
        Access the Trunking Twilio Domain

        :returns: Trunking Twilio Domain
        """
        if self._trunking is None:
            from twilio.rest.trunking import Trunking

            self._trunking = Trunking(self)
        return self._trunking

    @property
    def trusthub(self) -> "Trusthub":
        """
        Access the Trusthub Twilio Domain

        :returns: Trusthub Twilio Domain
        """
        if self._trusthub is None:
            from twilio.rest.trusthub import Trusthub

            self._trusthub = Trusthub(self)
        return self._trusthub

    @property
    def verify(self) -> "Verify":
        """
        Access the Verify Twilio Domain

        :returns: Verify Twilio Domain
        """
        if self._verify is None:
            from twilio.rest.verify import Verify

            self._verify = Verify(self)
        return self._verify

    @property
    def video(self) -> "Video":
        """
        Access the Video Twilio Domain

        :returns: Video Twilio Domain
        """
        if self._video is None:
            from twilio.rest.video import Video

            self._video = Video(self)
        return self._video

    @property
    def voice(self) -> "Voice":
        """
        Access the Voice Twilio Domain

        :returns: Voice Twilio Domain
        """
        if self._voice is None:
            from twilio.rest.voice import Voice

            self._voice = Voice(self)
        return self._voice

    @property
    def wireless(self) -> "Wireless":
        """
        Access the Wireless Twilio Domain

        :returns: Wireless Twilio Domain
        """
        if self._wireless is None:
            from twilio.rest.wireless import Wireless

            self._wireless = Wireless(self)
        return self._wireless

    @property
    def addresses(self) -> "AddressList":
        return self.api.account.addresses

    @property
    def applications(self) -> "ApplicationList":
        return self.api.account.applications

    @property
    def authorized_connect_apps(self) -> "AuthorizedConnectAppList":
        return self.api.account.authorized_connect_apps

    @property
    def available_phone_numbers(self) -> "AvailablePhoneNumberCountryList":
        return self.api.account.available_phone_numbers

    @property
    def balance(self) -> "BalanceList":
        return self.api.account.balance

    @property
    def calls(self) -> "CallList":
        return self.api.account.calls

    @property
    def conferences(self) -> "ConferenceList":
        return self.api.account.conferences

    @property
    def connect_apps(self) -> "ConnectAppList":
        return self.api.account.connect_apps

    @property
    def incoming_phone_numbers(self) -> "IncomingPhoneNumberList":
        return self.api.account.incoming_phone_numbers

    @property
    def keys(self) -> "KeyList":
        return self.api.account.keys

    @property
    def new_keys(self) -> "NewKeyList":
        return self.api.account.new_keys

    @property
    def messages(self) -> "MessageList":
        return self.api.account.messages

    @property
    def signing_keys(self) -> "SigningKeyList":
        return self.api.account.signing_keys

    @property
    def new_signing_keys(self) -> "NewSigningKeyList":
        return self.api.account.new_signing_keys

    @property
    def notifications(self) -> "NotificationList":
        return self.api.account.notifications

    @property
    def outgoing_caller_ids(self) -> "OutgoingCallerIdList":
        return self.api.account.outgoing_caller_ids

    @property
    def validation_requests(self) -> "ValidationRequestList":
        return self.api.account.validation_requests

    @property
    def queues(self) -> "QueueList":
        return self.api.account.queues

    @property
    def recordings(self) -> "RecordingList":
        return self.api.account.recordings

    @property
    def short_codes(self) -> "ShortCodeList":
        return self.api.account.short_codes

    @property
    def sip(self) -> "SipList":
        return self.api.account.sip

    @property
    def tokens(self) -> "TokenList":
        return self.api.account.tokens

    @property
    def transcriptions(self) -> "TranscriptionList":
        return self.api.account.transcriptions

    @property
    def usage(self) -> "UsageList":
        return self.api.account.usage
