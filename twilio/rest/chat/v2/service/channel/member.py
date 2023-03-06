"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Chat
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class MemberList(ListResource):

    def __init__(self, version: Version, service_sid: str, channel_sid: str):
        """
        Initialize the MemberList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the Member resources from.
        :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Member resources to read belong to. This value can be the Channel resource's `sid` or `unique_name`.
        
        :returns: twilio.rest.chat.v2.service.channel.member.MemberList
        :rtype: twilio.rest.chat.v2.service.channel.member.MemberList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'channel_sid': channel_sid,  }
        self._uri = '/Services/{service_sid}/Channels/{channel_sid}/Members'.format(**self._solution)
        
        
    
    
    
    
    def create(self, identity, x_twilio_webhook_enabled=values.unset, role_sid=values.unset, last_consumed_message_index=values.unset, last_consumption_timestamp=values.unset, date_created=values.unset, date_updated=values.unset, attributes=values.unset):
        """
        Create the MemberInstance

        :param str identity: The `identity` value that uniquely identifies the new resource's [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/chat/rest/service-resource). See [access tokens](https://www.twilio.com/docs/chat/create-tokens) for more info.
        :param MemberInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str role_sid: The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) to assign to the member. The default roles are those specified on the [Service](https://www.twilio.com/docs/chat/rest/service-resource).
        :param int last_consumed_message_index: The index of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) in the [Channel](https://www.twilio.com/docs/chat/channels) that the Member has read. This parameter should only be used when recreating a Member from a backup/separate source.
        :param datetime last_consumption_timestamp: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) read event for the Member within the [Channel](https://www.twilio.com/docs/chat/channels).
        :param datetime date_created: The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service.  Note that this parameter should only be used when a Member is being recreated from a backup/separate source.
        :param datetime date_updated: The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated. The default value is `null`. Note that this parameter should only be used when a Member is being recreated from a backup/separate source and where a Member was previously updated.
        :param str attributes: A valid JSON string that contains application-specific data.
        
        :returns: The created MemberInstance
        :rtype: twilio.rest.chat.v2.service.channel.member.MemberInstance
        """
        data = values.of({ 
            'Identity': identity,
            'RoleSid': role_sid,
            'LastConsumedMessageIndex': last_consumed_message_index,
            'LastConsumptionTimestamp': serialize.iso8601_datetime(last_consumption_timestamp),
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
            'Attributes': attributes,
        })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })
        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers)

        return MemberInstance(self._version, payload, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'])
    
    
    def stream(self, identity=values.unset, limit=None, page_size=None):
        """
        Streams MemberInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param list[str] identity: The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s `identity` value of the Member resources to read. See [access tokens](https://www.twilio.com/docs/chat/create-tokens) for more details.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v2.service.channel.member.MemberInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            identity=identity,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, identity=values.unset, limit=None, page_size=None):
        """
        Lists MemberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param list[str] identity: The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s `identity` value of the Member resources to read. See [access tokens](https://www.twilio.com/docs/chat/create-tokens) for more details.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v2.service.channel.member.MemberInstance]
        """
        return list(self.stream(
            identity=identity,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, identity=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of MemberInstance records from the API.
        Request is executed immediately
        
        :param list[str] identity: The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s `identity` value of the Member resources to read. See [access tokens](https://www.twilio.com/docs/chat/create-tokens) for more details.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MemberInstance
        :rtype: twilio.rest.chat.v2.service.channel.member.MemberPage
        """
        data = values.of({ 
            'Identity': serialize.map(identity, lambda e: e),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return MemberPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MemberInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MemberInstance
        :rtype: twilio.rest.chat.v2.service.channel.member.MemberPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return MemberPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a MemberContext
        
        :param sid: The SID of the Member resource to update. This value can be either the Member's `sid` or its `identity` value.
        
        :returns: twilio.rest.chat.v2.service.channel.member.MemberContext
        :rtype: twilio.rest.chat.v2.service.channel.member.MemberContext
        """
        return MemberContext(self._version, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a MemberContext
        
        :param sid: The SID of the Member resource to update. This value can be either the Member's `sid` or its `identity` value.
        
        :returns: twilio.rest.chat.v2.service.channel.member.MemberContext
        :rtype: twilio.rest.chat.v2.service.channel.member.MemberContext
        """
        return MemberContext(self._version, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat.V2.MemberList>'










class MemberPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the MemberPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.chat.v2.service.channel.member.MemberPage
        :rtype: twilio.rest.chat.v2.service.channel.member.MemberPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MemberInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.chat.v2.service.channel.member.MemberInstance
        :rtype: twilio.rest.chat.v2.service.channel.member.MemberInstance
        """
        return MemberInstance(self._version, payload, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat.V2.MemberPage>'




class MemberContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, channel_sid: str, sid: str):
        """
        Initialize the MemberContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the Member resource in.:param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Member resource to update belongs to. This value can be the Channel resource's `sid` or `unique_name`.:param sid: The SID of the Member resource to update. This value can be either the Member's `sid` or its `identity` value.

        :returns: twilio.rest.chat.v2.service.channel.member.MemberContext
        :rtype: twilio.rest.chat.v2.service.channel.member.MemberContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'channel_sid': channel_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}'.format(**self._solution)
        
    
    def delete(self, x_twilio_webhook_enabled=values.unset):
        """
        Deletes the MemberInstance

        :param MemberInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })
        
        return self._version.delete(method='DELETE', uri=self._uri, headers=headers)
        
    def fetch(self):
        """
        Fetch the MemberInstance
        

        :returns: The fetched MemberInstance
        :rtype: twilio.rest.chat.v2.service.channel.member.MemberInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return MemberInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, x_twilio_webhook_enabled=values.unset, role_sid=values.unset, last_consumed_message_index=values.unset, last_consumption_timestamp=values.unset, date_created=values.unset, date_updated=values.unset, attributes=values.unset):
        """
        Update the MemberInstance
        
        :params MemberInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :params str role_sid: The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) to assign to the member. The default roles are those specified on the [Service](https://www.twilio.com/docs/chat/rest/service-resource).
        :params int last_consumed_message_index: The index of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) that the Member has read within the [Channel](https://www.twilio.com/docs/chat/channels).
        :params datetime last_consumption_timestamp: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) read event for the Member within the [Channel](https://www.twilio.com/docs/chat/channels).
        :params datetime date_created: The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service.  Note that this parameter should only be used when a Member is being recreated from a backup/separate source.
        :params datetime date_updated: The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated.
        :params str attributes: A valid JSON string that contains application-specific data.

        :returns: The updated MemberInstance
        :rtype: twilio.rest.chat.v2.service.channel.member.MemberInstance
        """
        data = values.of({ 
            'RoleSid': role_sid,
            'LastConsumedMessageIndex': last_consumed_message_index,
            'LastConsumptionTimestamp': serialize.iso8601_datetime(last_consumption_timestamp),
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
            'Attributes': attributes,
        })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers)

        return MemberInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Chat.V2.MemberContext {}>'.format(context)

class MemberInstance(InstanceResource):

    class WebhookEnabledType(object):
        TRUE = "true"
        FALSE = "false"

    def __init__(self, version, payload, service_sid: str, channel_sid: str, sid: str=None):
        """
        Initialize the MemberInstance
        :returns: twilio.rest.chat.v2.service.channel.member.MemberInstance
        :rtype: twilio.rest.chat.v2.service.channel.member.MemberInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'channel_sid': payload.get('channel_sid'),
            'service_sid': payload.get('service_sid'),
            'identity': payload.get('identity'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'role_sid': payload.get('role_sid'),
            'last_consumed_message_index': deserialize.integer(payload.get('last_consumed_message_index')),
            'last_consumption_timestamp': deserialize.iso8601_datetime(payload.get('last_consumption_timestamp')),
            'url': payload.get('url'),
            'attributes': payload.get('attributes'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'channel_sid': channel_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: MemberContext for this MemberInstance
        :rtype: twilio.rest.chat.v2.service.channel.member.MemberContext
        """
        if self._context is None:
            self._context = MemberContext(self._version, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Member resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Member resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def channel_sid(self):
        """
        :returns: The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Member resource belongs to.
        :rtype: str
        """
        return self._properties['channel_sid']
    
    @property
    def service_sid(self):
        """
        :returns: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) the Member resource is associated with.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def identity(self):
        """
        :returns: The application-defined string that uniquely identifies the resource's [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/chat/rest/service-resource). See [access tokens](https://www.twilio.com/docs/chat/create-tokens) for more info.
        :rtype: str
        """
        return self._properties['identity']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def role_sid(self):
        """
        :returns: The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) assigned to the member.
        :rtype: str
        """
        return self._properties['role_sid']
    
    @property
    def last_consumed_message_index(self):
        """
        :returns: The index of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) in the [Channel](https://www.twilio.com/docs/chat/channels) that the Member has read.
        :rtype: int
        """
        return self._properties['last_consumed_message_index']
    
    @property
    def last_consumption_timestamp(self):
        """
        :returns: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) read event for the Member within the [Channel](https://www.twilio.com/docs/chat/channels).
        :rtype: datetime
        """
        return self._properties['last_consumption_timestamp']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Member resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def attributes(self):
        """
        :returns: The JSON string that stores application-specific data. If attributes have not been set, `{}` is returned.
        :rtype: str
        """
        return self._properties['attributes']
    
    def delete(self, x_twilio_webhook_enabled=values.unset):
        """
        Deletes the MemberInstance
        
        :params MemberInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete(x_twilio_webhook_enabled=x_twilio_webhook_enabled, )
    
    def fetch(self):
        """
        Fetch the MemberInstance
        

        :returns: The fetched MemberInstance
        :rtype: twilio.rest.chat.v2.service.channel.member.MemberInstance
        """
        return self._proxy.fetch()
    
    def update(self, x_twilio_webhook_enabled=values.unset, role_sid=values.unset, last_consumed_message_index=values.unset, last_consumption_timestamp=values.unset, date_created=values.unset, date_updated=values.unset, attributes=values.unset):
        """
        Update the MemberInstance
        
        :params MemberInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :params str role_sid: The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) to assign to the member. The default roles are those specified on the [Service](https://www.twilio.com/docs/chat/rest/service-resource).
        :params int last_consumed_message_index: The index of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) that the Member has read within the [Channel](https://www.twilio.com/docs/chat/channels).
        :params datetime last_consumption_timestamp: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) read event for the Member within the [Channel](https://www.twilio.com/docs/chat/channels).
        :params datetime date_created: The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service.  Note that this parameter should only be used when a Member is being recreated from a backup/separate source.
        :params datetime date_updated: The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated.
        :params str attributes: A valid JSON string that contains application-specific data.

        :returns: The updated MemberInstance
        :rtype: twilio.rest.chat.v2.service.channel.member.MemberInstance
        """
        return self._proxy.update(x_twilio_webhook_enabled=x_twilio_webhook_enabled, role_sid=role_sid, last_consumed_message_index=last_consumed_message_index, last_consumption_timestamp=last_consumption_timestamp, date_created=date_created, date_updated=date_updated, attributes=attributes, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Chat.V2.MemberInstance {}>'.format(context)


