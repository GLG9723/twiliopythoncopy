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

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class UserChannelList(ListResource):

    def __init__(self, version: Version, service_sid: str, user_sid: str):
        """
        Initialize the UserChannelList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to read the resources from.
        :param user_sid: The SID of the [User](https://www.twilio.com/docs/api/chat/rest/users) to read the User Channel resources from.
        
        :returns: twilio.rest.chat.v1.service.user.user_channel.UserChannelList
        :rtype: twilio.rest.chat.v1.service.user.user_channel.UserChannelList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'user_sid': user_sid,  }
        self._uri = '/Services/{service_sid}/Users/{user_sid}/Channels'.format(**self._solution)
        
        
    
    def stream(self, limit=None, page_size=None):
        """
        Streams UserChannelInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.chat.v1.service.user.user_channel.UserChannelInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists UserChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v1.service.user.user_channel.UserChannelInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of UserChannelInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UserChannelInstance
        :rtype: twilio.rest.chat.v1.service.user.user_channel.UserChannelPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return UserChannelPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of UserChannelInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UserChannelInstance
        :rtype: twilio.rest.chat.v1.service.user.user_channel.UserChannelPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return UserChannelPage(self._version, response, self._solution)



    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat.V1.UserChannelList>'


class UserChannelPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the UserChannelPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.chat.v1.service.user.user_channel.UserChannelPage
        :rtype: twilio.rest.chat.v1.service.user.user_channel.UserChannelPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UserChannelInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.chat.v1.service.user.user_channel.UserChannelInstance
        :rtype: twilio.rest.chat.v1.service.user.user_channel.UserChannelInstance
        """
        return UserChannelInstance(self._version, payload, service_sid=self._solution['service_sid'], user_sid=self._solution['user_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat.V1.UserChannelPage>'





class UserChannelInstance(InstanceResource):

    class ChannelStatus(object):
        JOINED = "joined"
        INVITED = "invited"
        NOT_PARTICIPATING = "not_participating"

    def __init__(self, version, payload, service_sid: str, user_sid: str):
        """
        Initialize the UserChannelInstance
        :returns: twilio.rest.chat.v1.service.user.user_channel.UserChannelInstance
        :rtype: twilio.rest.chat.v1.service.user.user_channel.UserChannelInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'channel_sid': payload.get('channel_sid'),
            'member_sid': payload.get('member_sid'),
            'status': payload.get('status'),
            'last_consumed_message_index': deserialize.integer(payload.get('last_consumed_message_index')),
            'unread_messages_count': deserialize.integer(payload.get('unread_messages_count')),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'user_sid': user_sid,  }
    
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/api/rest/account) that created the User Channel resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) the resource is associated with.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def channel_sid(self):
        """
        :returns: The SID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the resource belongs to.
        :rtype: str
        """
        return self._properties['channel_sid']
    
    @property
    def member_sid(self):
        """
        :returns: The SID of a [Member](https://www.twilio.com/docs/api/chat/rest/members) that represents the User on the Channel.
        :rtype: str
        """
        return self._properties['member_sid']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: ChannelStatus
        """
        return self._properties['status']
    
    @property
    def last_consumed_message_index(self):
        """
        :returns: The index of the last [Message](https://www.twilio.com/docs/api/chat/rest/messages) in the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) that the Member has read.
        :rtype: int
        """
        return self._properties['last_consumed_message_index']
    
    @property
    def unread_messages_count(self):
        """
        :returns: The number of unread Messages in the Channel for the User. Note that retrieving messages on a client endpoint does not mean that messages are consumed or read. See [Consumption Horizon feature](/docs/api/chat/guides/consumption-horizon) to learn how to mark messages as consumed.
        :rtype: int
        """
        return self._properties['unread_messages_count']
    
    @property
    def links(self):
        """
        :returns: The absolute URLs of the [Members](https://www.twilio.com/docs/chat/api/members), [Messages](https://www.twilio.com/docs/chat/api/messages) , [Invites](https://www.twilio.com/docs/chat/api/invites) and, if it exists, the last [Message](https://www.twilio.com/docs/chat/api/messages) for the Channel.
        :rtype: dict
        """
        return self._properties['links']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Chat.V1.UserChannelInstance {}>'.format(context)


