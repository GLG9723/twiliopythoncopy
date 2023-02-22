"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
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
from twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_invite import InteractionChannelInviteList
from twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant import InteractionChannelParticipantList


class InteractionChannelList(ListResource):

    def __init__(self, version: Version, interaction_sid: str):
        """
        Initialize the InteractionChannelList

        :param Version version: Version that contains the resource
        :param interaction_sid: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
        
        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelList
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'interaction_sid': interaction_sid,  }
        self._uri = '/Interactions/${interaction_sid}/Channels'.format(**self._solution)
        
        
    
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams InteractionChannelInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists InteractionChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of InteractionChannelInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InteractionChannelInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return InteractionChannelPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of InteractionChannelInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InteractionChannelInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return InteractionChannelPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a InteractionChannelContext
        
        :param sid: The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
        
        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelContext
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelContext
        """
        return InteractionChannelContext(self._version, interaction_sid=self._solution['interaction_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a InteractionChannelContext
        
        :param sid: The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
        
        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelContext
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelContext
        """
        return InteractionChannelContext(self._version, interaction_sid=self._solution['interaction_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InteractionChannelList>'






class InteractionChannelPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the InteractionChannelPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelPage
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of InteractionChannelInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelInstance
        """
        return InteractionChannelInstance(self._version, payload, interaction_sid=self._solution['interaction_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InteractionChannelPage>'





class InteractionChannelContext(InstanceContext):
    def __init__(self, version: Version, interaction_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'interaction_sid': interaction_sid, 'sid': sid,  }
        self._uri = '/Interactions/${interaction_sid}/Channels/${sid}'
        
        self._invites = None
        self._participants = None
    
    def fetch(self):
        
        """
        Fetch the InteractionChannelInstance

        :returns: The fetched InteractionChannelInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return InteractionChannelInstance(self._version, payload, interaction_sid=self._solution['interaction_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, status, routing):
        data = values.of({
            'status': status,'routing': routing,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return InteractionChannelInstance(self._version, payload, interaction_sid=self._solution['interaction_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InteractionChannelContext>'



class InteractionChannelInstance(InstanceResource):
    def __init__(self, version, payload, interaction_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'interaction_sid' : payload.get('interaction_sid'),
            'type' : payload.get('type'),
            'status' : payload.get('status'),
            'error_code' : payload.get('error_code'),
            'error_message' : payload.get('error_message'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'interaction_sid': interaction_sid or self._properties['interaction_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = InteractionChannelContext(
                self._version,
                interaction_sid=self._solution['interaction_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def invites(self):
        return self._proxy.invites
    @property
    def participants(self):
        return self._proxy.participants
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InteractionChannelInstance {}>'.format(context)



