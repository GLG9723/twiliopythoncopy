"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Taskrouter
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


class ActivityList(ListResource):

    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the ActivityList

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the Activity resources to read.
        
        :returns: twilio.rest.taskrouter.v1.workspace.activity.ActivityList
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid,  }
        self._uri = '/Workspaces/{workspace_sid}/Activities'.format(**self._solution)
        
        
    
    
    
    
    def create(self, friendly_name, available=values.unset):
        """
        Create the ActivityInstance

        :param str friendly_name: A descriptive string that you create to describe the Activity resource. It can be up to 64 characters long. These names are used to calculate and expose statistics about Workers, and provide visibility into the state of each Worker. Examples of friendly names include: `on-call`, `break`, and `email`.
        :param bool available: Whether the Worker should be eligible to receive a Task when it occupies the Activity. A value of `true`, `1`, or `yes` specifies the Activity is available. All other values specify that it is not. The value cannot be changed after the Activity is created.
        
        :returns: The created ActivityInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'Available': available,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return ActivityInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'])
    
    
    def stream(self, friendly_name=values.unset, available=values.unset, limit=None, page_size=None):
        """
        Streams ActivityInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str friendly_name: The `friendly_name` of the Activity resources to read.
        :param str available: Whether return only Activity resources that are available or unavailable. A value of `true` returns only available activities. Values of '1' or `yes` also indicate `true`. All other values represent `false` and return activities that are unavailable.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.activity.ActivityInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            friendly_name=friendly_name,
            available=available,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, friendly_name=values.unset, available=values.unset, limit=None, page_size=None):
        """
        Lists ActivityInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str friendly_name: The `friendly_name` of the Activity resources to read.
        :param str available: Whether return only Activity resources that are available or unavailable. A value of `true` returns only available activities. Values of '1' or `yes` also indicate `true`. All other values represent `false` and return activities that are unavailable.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.activity.ActivityInstance]
        """
        return list(self.stream(
            friendly_name=friendly_name,
            available=available,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, friendly_name=values.unset, available=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ActivityInstance records from the API.
        Request is executed immediately
        
        :param str friendly_name: The `friendly_name` of the Activity resources to read.
        :param str available: Whether return only Activity resources that are available or unavailable. A value of `true` returns only available activities. Values of '1' or `yes` also indicate `true`. All other values represent `false` and return activities that are unavailable.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ActivityInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityPage
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'Available': available,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ActivityPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ActivityInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ActivityInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ActivityPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a ActivityContext
        
        :param sid: The SID of the Activity resource to update.
        
        :returns: twilio.rest.taskrouter.v1.workspace.activity.ActivityContext
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityContext
        """
        return ActivityContext(self._version, workspace_sid=self._solution['workspace_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a ActivityContext
        
        :param sid: The SID of the Activity resource to update.
        
        :returns: twilio.rest.taskrouter.v1.workspace.activity.ActivityContext
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityContext
        """
        return ActivityContext(self._version, workspace_sid=self._solution['workspace_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.ActivityList>'










class ActivityPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ActivityPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.activity.ActivityPage
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ActivityInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.activity.ActivityInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityInstance
        """
        return ActivityInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.ActivityPage>'




class ActivityContext(InstanceContext):

    def __init__(self, version: Version, workspace_sid: str, sid: str):
        """
        Initialize the ActivityContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the Activity resources to update.
        :param sid: The SID of the Activity resource to update.

        :returns: twilio.rest.taskrouter.v1.workspace.activity.ActivityContext
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'workspace_sid': workspace_sid,
            'sid': sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Activities/{sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the ActivityInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the ActivityInstance
        

        :returns: The fetched ActivityInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ActivityInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, friendly_name=values.unset):
        """
        Update the ActivityInstance
        
        :params str friendly_name: A descriptive string that you create to describe the Activity resource. It can be up to 64 characters long. These names are used to calculate and expose statistics about Workers, and provide visibility into the state of each Worker. Examples of friendly names include: `on-call`, `break`, and `email`.

        :returns: The updated ActivityInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return ActivityInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.ActivityContext {}>'.format(context)

class ActivityInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid: str, sid: str=None):
        """
        Initialize the ActivityInstance
        :returns: twilio.rest.taskrouter.v1.workspace.activity.ActivityInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'available': payload.get('available'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'friendly_name': payload.get('friendly_name'),
            'sid': payload.get('sid'),
            'workspace_sid': payload.get('workspace_sid'),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'workspace_sid': workspace_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ActivityContext for this ActivityInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityContext
        """
        if self._context is None:
            self._context = ActivityContext(self._version, workspace_sid=self._solution['workspace_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Activity resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def available(self):
        """
        :returns: Whether the Worker is eligible to receive a Task when it occupies the Activity. A value of `true`, `1`, or `yes` indicates the Activity is available. All other values indicate that it is not. The value cannot be changed after the Activity is created.
        :rtype: bool
        """
        return self._properties['available']
    
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
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the Activity resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Activity resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def workspace_sid(self):
        """
        :returns: The SID of the Workspace that contains the Activity.
        :rtype: str
        """
        return self._properties['workspace_sid']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Activity resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['links']
    
    def delete(self):
        """
        Deletes the ActivityInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the ActivityInstance
        

        :returns: The fetched ActivityInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityInstance
        """
        return self._proxy.fetch()
    
    def update(self, friendly_name=values.unset):
        """
        Update the ActivityInstance
        
        :params str friendly_name: A descriptive string that you create to describe the Activity resource. It can be up to 64 characters long. These names are used to calculate and expose statistics about Workers, and provide visibility into the state of each Worker. Examples of friendly names include: `on-call`, `break`, and `email`.

        :returns: The updated ActivityInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.activity.ActivityInstance
        """
        return self._proxy.update(friendly_name=friendly_name, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.ActivityInstance {}>'.format(context)


