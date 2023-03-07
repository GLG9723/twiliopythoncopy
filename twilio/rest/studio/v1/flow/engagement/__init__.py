"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Studio
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
from twilio.rest.studio.v1.flow.engagement.engagement_context import EngagementContextList
from twilio.rest.studio.v1.flow.engagement.step import StepList


class EngagementList(ListResource):

    def __init__(self, version: Version, flow_sid: str):
        """
        Initialize the EngagementList

        :param Version version: Version that contains the resource
        :param flow_sid: The SID of the Flow to read Engagements from.
        
        :returns: twilio.rest.studio.v1.flow.engagement.EngagementList
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'flow_sid': flow_sid,  }
        self._uri = '/Flows/{flow_sid}/Engagements'.format(**self._solution)
        
        
    
    
    
    def create(self, to, from_, parameters=values.unset):
        """
        Create the EngagementInstance

        :param str to: The Contact phone number to start a Studio Flow Engagement, available as variable `{{contact.channel.address}}`.
        :param str from_: The Twilio phone number to send messages or initiate calls from during the Flow Engagement. Available as variable `{{flow.channel.address}}`
        :param object parameters: A JSON string we will add to your flow's context and that you can access as variables inside your flow. For example, if you pass in `Parameters={'name':'Zeke'}` then inside a widget you can reference the variable `{{flow.data.name}}` which will return the string 'Zeke'. Note: the JSON value must explicitly be passed as a string, not as a hash object. Depending on your particular HTTP library, you may need to add quotes or URL encode your JSON string.
        
        :returns: The created EngagementInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementInstance
        """
        data = values.of({ 
            'To': to,
            'From': from_,
            'Parameters': serialize.object(parameters),
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return EngagementInstance(self._version, payload, flow_sid=self._solution['flow_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams EngagementInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.studio.v1.flow.engagement.EngagementInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists EngagementInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.studio.v1.flow.engagement.EngagementInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of EngagementInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of EngagementInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return EngagementPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of EngagementInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of EngagementInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return EngagementPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a EngagementContext
        
        :param sid: The SID of the Engagement resource to fetch.
        
        :returns: twilio.rest.studio.v1.flow.engagement.EngagementContext
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementContext
        """
        return EngagementContext(self._version, flow_sid=self._solution['flow_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a EngagementContext
        
        :param sid: The SID of the Engagement resource to fetch.
        
        :returns: twilio.rest.studio.v1.flow.engagement.EngagementContext
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementContext
        """
        return EngagementContext(self._version, flow_sid=self._solution['flow_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V1.EngagementList>'








class EngagementPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the EngagementPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.studio.v1.flow.engagement.EngagementPage
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of EngagementInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.studio.v1.flow.engagement.EngagementInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementInstance
        """
        return EngagementInstance(self._version, payload, flow_sid=self._solution['flow_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V1.EngagementPage>'




class EngagementContext(InstanceContext):

    def __init__(self, version: Version, flow_sid: str, sid: str):
        """
        Initialize the EngagementContext

        :param Version version: Version that contains the resource
        :param flow_sid: The SID of the Flow.
        :param sid: The SID of the Engagement resource to fetch.

        :returns: twilio.rest.studio.v1.flow.engagement.EngagementContext
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'flow_sid': flow_sid,
            'sid': sid,
        }
        self._uri = '/Flows/{flow_sid}/Engagements/{sid}'.format(**self._solution)
        
        self._engagement_context = None
        self._steps = None
    
    def delete(self):
        """
        Deletes the EngagementInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the EngagementInstance
        

        :returns: The fetched EngagementInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return EngagementInstance(
            self._version,
            payload,
            flow_sid=self._solution['flow_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    @property
    def engagement_context(self):
        """
        Access the engagement_context

        :returns: twilio.rest.studio.v1.flow.engagement.EngagementContextList
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementContextList
        """
        if self._engagement_context is None:
            self._engagement_context = EngagementContextList(
                self._version, 
                self._solution['flow_sid'],
                self._solution['sid'],
            )
        return self._engagement_context
    
    @property
    def steps(self):
        """
        Access the steps

        :returns: twilio.rest.studio.v1.flow.engagement.StepList
        :rtype: twilio.rest.studio.v1.flow.engagement.StepList
        """
        if self._steps is None:
            self._steps = StepList(
                self._version, 
                self._solution['flow_sid'],
                self._solution['sid'],
            )
        return self._steps
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V1.EngagementContext {}>'.format(context)

class EngagementInstance(InstanceResource):

    class Status(object):
        ACTIVE = "active"
        ENDED = "ended"

    def __init__(self, version, payload, flow_sid: str, sid: str=None):
        """
        Initialize the EngagementInstance
        :returns: twilio.rest.studio.v1.flow.engagement.EngagementInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'flow_sid': payload.get('flow_sid'),
            'contact_sid': payload.get('contact_sid'),
            'contact_channel_address': payload.get('contact_channel_address'),
            'context': payload.get('context'),
            'status': payload.get('status'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'flow_sid': flow_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: EngagementContext for this EngagementInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementContext
        """
        if self._context is None:
            self._context = EngagementContext(self._version, flow_sid=self._solution['flow_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Engagement resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Engagement resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def flow_sid(self):
        """
        :returns: The SID of the Flow.
        :rtype: str
        """
        return self._properties['flow_sid']
    
    @property
    def contact_sid(self):
        """
        :returns: The SID of the Contact.
        :rtype: str
        """
        return self._properties['contact_sid']
    
    @property
    def contact_channel_address(self):
        """
        :returns: The phone number, SIP address or Client identifier that triggered this Engagement. Phone numbers are in E.164 format (+16175551212). SIP addresses are formatted as `name@company.com`. Client identifiers are formatted `client:name`.
        :rtype: str
        """
        return self._properties['contact_channel_address']
    
    @property
    def context(self):
        """
        :returns: The current state of the execution flow. As your flow executes, we save the state in a flow context. Your widgets can access the data in the flow context as variables, either in configuration fields or in text areas as variable substitution.
        :rtype: dict
        """
        return self._properties['context']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: EngagementInstance.Status
        """
        return self._properties['status']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the Engagement was created in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the Engagement was updated in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: The URLs of the Engagement's nested resources.
        :rtype: dict
        """
        return self._properties['links']
    
    def delete(self):
        """
        Deletes the EngagementInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the EngagementInstance
        

        :returns: The fetched EngagementInstance
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementInstance
        """
        return self._proxy.fetch()
    
    @property
    def engagement_context(self):
        """
        Access the engagement_context

        :returns: twilio.rest.studio.v1.flow.engagement.EngagementContextList
        :rtype: twilio.rest.studio.v1.flow.engagement.EngagementContextList
        """
        return self._proxy.engagement_context
    
    @property
    def steps(self):
        """
        Access the steps

        :returns: twilio.rest.studio.v1.flow.engagement.StepList
        :rtype: twilio.rest.studio.v1.flow.engagement.StepList
        """
        return self._proxy.steps
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V1.EngagementInstance {}>'.format(context)


