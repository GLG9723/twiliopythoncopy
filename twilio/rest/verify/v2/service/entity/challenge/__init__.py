"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
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
from twilio.base.page import Page
from twilio.rest.verify.v2.service.entity.challenge.notification import NotificationList


class ChallengeList(ListResource):

    def __init__(self, version: Version, service_sid: str, identity: str):
        """
        Initialize the ChallengeList

        :param Version version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.
        :param identity: Customer unique identity for the Entity owner of the Challenge. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
        
        :returns: twilio.rest.verify.v2.service.entity.challenge.ChallengeList
        :rtype: twilio.rest.verify.v2.service.entity.challenge.ChallengeList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'identity': identity,  }
        self._uri = '/Services/{service_sid}/Entities/{identity}/Challenges'.format(**self._solution)
        
        
    
    
    
    def create(self, factor_sid, expiration_date=values.unset, details_message=values.unset, details_fields=values.unset, hidden_details=values.unset, auth_payload=values.unset):
        """
        Create the ChallengeInstance

        :param str factor_sid: The unique SID identifier of the Factor.
        :param datetime expiration_date: The date-time when this Challenge expires, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. The default value is five (5) minutes after Challenge creation. The max value is sixty (60) minutes after creation.
        :param str details_message: Shown to the user when the push notification arrives. Required when `factor_type` is `push`. Can be up to 256 characters in length
        :param list[object] details_fields: A list of objects that describe the Fields included in the Challenge. Each object contains the label and value of the field, the label can be up to 36 characters in length and the value can be up to 128 characters in length. Used when `factor_type` is `push`. There can be up to 20 details fields.
        :param object hidden_details: Details provided to give context about the Challenge. Not shown to the end user. It must be a stringified JSON with only strings values eg. `{\\\"ip\\\": \\\"172.168.1.234\\\"}`. Can be up to 1024 characters in length
        :param str auth_payload: Optional payload used to verify the Challenge upon creation. Only used with a Factor of type `totp` to carry the TOTP code that needs to be verified. For `TOTP` this value must be between 3 and 8 characters long.
        
        :returns: The created ChallengeInstance
        :rtype: twilio.rest.verify.v2.service.entity.challenge.ChallengeInstance
        """
        data = values.of({ 
            'FactorSid': factor_sid,
            'ExpirationDate': serialize.iso8601_datetime(expiration_date),
            'Details.Message': details_message,
            'Details.Fields': serialize.map(details_fields, lambda e: e),
            'HiddenDetails': serialize.object(hidden_details),
            'AuthPayload': auth_payload,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return ChallengeInstance(self._version, payload, service_sid=self._solution['service_sid'], identity=self._solution['identity'])
    
    
    def stream(self, factor_sid=values.unset, status=values.unset, order=values.unset, limit=None, page_size=None):
        """
        Streams ChallengeInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str factor_sid: The unique SID identifier of the Factor.
        :param ChallengeChallengeStatuses status: The Status of the Challenges to fetch. One of `pending`, `expired`, `approved` or `denied`.
        :param ChallengeListOrders order: The desired sort order of the Challenges list. One of `asc` or `desc` for ascending and descending respectively. Defaults to `asc`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.service.entity.challenge.ChallengeInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            factor_sid=factor_sid,
            status=status,
            order=order,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, factor_sid=values.unset, status=values.unset, order=values.unset, limit=None, page_size=None):
        """
        Lists ChallengeInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str factor_sid: The unique SID identifier of the Factor.
        :param ChallengeChallengeStatuses status: The Status of the Challenges to fetch. One of `pending`, `expired`, `approved` or `denied`.
        :param ChallengeListOrders order: The desired sort order of the Challenges list. One of `asc` or `desc` for ascending and descending respectively. Defaults to `asc`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.service.entity.challenge.ChallengeInstance]
        """
        return list(self.stream(
            factor_sid=factor_sid,
            status=status,
            order=order,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, factor_sid=values.unset, status=values.unset, order=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ChallengeInstance records from the API.
        Request is executed immediately
        
        :param str factor_sid: The unique SID identifier of the Factor.
        :param ChallengeChallengeStatuses status: The Status of the Challenges to fetch. One of `pending`, `expired`, `approved` or `denied`.
        :param ChallengeListOrders order: The desired sort order of the Challenges list. One of `asc` or `desc` for ascending and descending respectively. Defaults to `asc`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ChallengeInstance
        :rtype: twilio.rest.verify.v2.service.entity.challenge.ChallengePage
        """
        data = values.of({ 
            'FactorSid': factor_sid,
            'Status': status,
            'Order': order,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ChallengePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ChallengeInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ChallengeInstance
        :rtype: twilio.rest.verify.v2.service.entity.challenge.ChallengePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ChallengePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a ChallengeContext
        
        :param sid: A 34 character string that uniquely identifies this Challenge.
        
        :returns: twilio.rest.verify.v2.service.entity.challenge.ChallengeContext
        :rtype: twilio.rest.verify.v2.service.entity.challenge.ChallengeContext
        """
        return ChallengeContext(self._version, service_sid=self._solution['service_sid'], identity=self._solution['identity'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a ChallengeContext
        
        :param sid: A 34 character string that uniquely identifies this Challenge.
        
        :returns: twilio.rest.verify.v2.service.entity.challenge.ChallengeContext
        :rtype: twilio.rest.verify.v2.service.entity.challenge.ChallengeContext
        """
        return ChallengeContext(self._version, service_sid=self._solution['service_sid'], identity=self._solution['identity'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.ChallengeList>'








class ChallengePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ChallengePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.verify.v2.service.entity.challenge.ChallengePage
        :rtype: twilio.rest.verify.v2.service.entity.challenge.ChallengePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ChallengeInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.verify.v2.service.entity.challenge.ChallengeInstance
        :rtype: twilio.rest.verify.v2.service.entity.challenge.ChallengeInstance
        """
        return ChallengeInstance(self._version, payload, service_sid=self._solution['service_sid'], identity=self._solution['identity'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.ChallengePage>'




class ChallengeContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, identity: str, sid: str):
        """
        Initialize the ChallengeContext

        :param Version version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.:param identity: Customer unique identity for the Entity owner of the Challenge. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.:param sid: A 34 character string that uniquely identifies this Challenge.

        :returns: twilio.rest.verify.v2.service.entity.challenge.ChallengeContext
        :rtype: twilio.rest.verify.v2.service.entity.challenge.ChallengeContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'identity': identity,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Entities/{identity}/Challenges/{sid}'.format(**self._solution)
        
        self._notifications = None
    
    def fetch(self):
        """
        Fetch the ChallengeInstance
        

        :returns: The fetched ChallengeInstance
        :rtype: twilio.rest.verify.v2.service.entity.challenge.ChallengeInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ChallengeInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, auth_payload=values.unset, metadata=values.unset):
        """
        Update the ChallengeInstance
        
        :params str auth_payload: The optional payload needed to verify the Challenge. E.g., a TOTP would use the numeric code. For `TOTP` this value must be between 3 and 8 characters long. For `Push` this value can be up to 5456 characters in length
        :params object metadata: Custom metadata associated with the challenge. This is added by the Device/SDK directly to allow for the inclusion of device information. It must be a stringified JSON with only strings values eg. `{\\\"os\\\": \\\"Android\\\"}`. Can be up to 1024 characters in length.

        :returns: The updated ChallengeInstance
        :rtype: twilio.rest.verify.v2.service.entity.challenge.ChallengeInstance
        """
        data = values.of({ 
            'AuthPayload': auth_payload,
            'Metadata': serialize.object(metadata),
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return ChallengeInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
            sid=self._solution['sid']
        )
        
    
    @property
    def notifications(self):
        """
        Access the notifications

        :returns: twilio.rest.verify.v2.service.entity.challenge.NotificationList
        :rtype: twilio.rest.verify.v2.service.entity.challenge.NotificationList
        """
        if self._notifications is None:
            self._notifications = NotificationList(self._version, self._solution['service_sid'], self._solution['identity'], self._solution['sid'],
            )
        return self._notifications
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.ChallengeContext {}>'.format(context)

class ChallengeInstance(InstanceResource):

    def __init__(self, version, payload, service_sid: str, identity: str, sid: str=None):
        """
        Initialize the ChallengeInstance
        :returns: twilio.rest.verify.v2.service.entity.challenge.ChallengeInstance
        :rtype: twilio.rest.verify.v2.service.entity.challenge.ChallengeInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'entity_sid': payload.get('entity_sid'),
            'identity': payload.get('identity'),
            'factor_sid': payload.get('factor_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'date_responded': deserialize.iso8601_datetime(payload.get('date_responded')),
            'expiration_date': deserialize.iso8601_datetime(payload.get('expiration_date')),
            'status': payload.get('status'),
            'responded_reason': payload.get('responded_reason'),
            'details': payload.get('details'),
            'hidden_details': payload.get('hidden_details'),
            'metadata': payload.get('metadata'),
            'factor_type': payload.get('factor_type'),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'identity': identity, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ChallengeContext for this ChallengeInstance
        :rtype: twilio.rest.verify.v2.service.entity.challenge.ChallengeContext
        """
        if self._context is None:
            self._context = ChallengeContext(self._version, service_sid=self._solution['service_sid'], identity=self._solution['identity'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this Challenge.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The unique SID identifier of the Account.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: The unique SID identifier of the Service.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def entity_sid(self):
        """
        :returns: The unique SID identifier of the Entity.
        :rtype: str
        """
        return self._properties['entity_sid']
    
    @property
    def identity(self):
        """
        :returns: Customer unique identity for the Entity owner of the Challenge. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
        :rtype: str
        """
        return self._properties['identity']
    
    @property
    def factor_sid(self):
        """
        :returns: The unique SID identifier of the Factor.
        :rtype: str
        """
        return self._properties['factor_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date that this Challenge was created, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date that this Challenge was updated, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def date_responded(self):
        """
        :returns: The date that this Challenge was responded, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_responded']
    
    @property
    def expiration_date(self):
        """
        :returns: The date-time when this Challenge expires, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. The default value is five (5) minutes after Challenge creation. The max value is sixty (60) minutes after creation.
        :rtype: datetime
        """
        return self._properties['expiration_date']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: ChallengeChallengeStatuses
        """
        return self._properties['status']
    
    @property
    def responded_reason(self):
        """
        :returns: 
        :rtype: ChallengeChallengeReasons
        """
        return self._properties['responded_reason']
    
    @property
    def details(self):
        """
        :returns: Details provided to give context about the Challenge. Intended to be shown to the end user.
        :rtype: dict
        """
        return self._properties['details']
    
    @property
    def hidden_details(self):
        """
        :returns: Details provided to give context about the Challenge. Intended to be hidden from the end user. It must be a stringified JSON with only strings values eg. `{\"ip\": \"172.168.1.234\"}`
        :rtype: dict
        """
        return self._properties['hidden_details']
    
    @property
    def metadata(self):
        """
        :returns: Custom metadata associated with the challenge. This is added by the Device/SDK directly to allow for the inclusion of device information. It must be a stringified JSON with only strings values eg. `{\"os\": \"Android\"}`. Can be up to 1024 characters in length.
        :rtype: dict
        """
        return self._properties['metadata']
    
    @property
    def factor_type(self):
        """
        :returns: 
        :rtype: ChallengeFactorTypes
        """
        return self._properties['factor_type']
    
    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: Contains a dictionary of URL links to nested resources of this Challenge.
        :rtype: dict
        """
        return self._properties['links']
    
    def fetch(self):
        """
        Fetch the ChallengeInstance
        

        :returns: The fetched ChallengeInstance
        :rtype: twilio.rest.verify.v2.service.entity.challenge.ChallengeInstance
        """
        return self._proxy.fetch()
    
    def update(self, auth_payload=values.unset, metadata=values.unset):
        """
        Update the ChallengeInstance
        
        :params str auth_payload: The optional payload needed to verify the Challenge. E.g., a TOTP would use the numeric code. For `TOTP` this value must be between 3 and 8 characters long. For `Push` this value can be up to 5456 characters in length
        :params object metadata: Custom metadata associated with the challenge. This is added by the Device/SDK directly to allow for the inclusion of device information. It must be a stringified JSON with only strings values eg. `{\\\"os\\\": \\\"Android\\\"}`. Can be up to 1024 characters in length.

        :returns: The updated ChallengeInstance
        :rtype: twilio.rest.verify.v2.service.entity.challenge.ChallengeInstance
        """
        return self._proxy.update(auth_payload=auth_payload, metadata=metadata, )
    
    @property
    def notifications(self):
        """
        Access the notifications

        :returns: twilio.rest.verify.v2.service.entity.challenge.NotificationList
        :rtype: twilio.rest.verify.v2.service.entity.challenge.NotificationList
        """
        return self._proxy.notifications
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.ChallengeInstance {}>'.format(context)


