r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Events
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version

from twilio.rest.events.v1.schema.schema_version import SchemaVersionList


class SchemaList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the SchemaList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.events.v1.schema.SchemaList
        :rtype: twilio.rest.events.v1.schema.SchemaList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}

    def get(self, id):
        """
        Constructs a SchemaContext

        :param id: The unique identifier of the schema. Each schema can have multiple versions, that share the same id.

        :returns: twilio.rest.events.v1.schema.SchemaContext
        :rtype: twilio.rest.events.v1.schema.SchemaContext
        """
        return SchemaContext(self._version, id=id)

    def __call__(self, id):
        """
        Constructs a SchemaContext

        :param id: The unique identifier of the schema. Each schema can have multiple versions, that share the same id.

        :returns: twilio.rest.events.v1.schema.SchemaContext
        :rtype: twilio.rest.events.v1.schema.SchemaContext
        """
        return SchemaContext(self._version, id=id)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Events.V1.SchemaList>"


class SchemaInstance(InstanceResource):
    def __init__(self, version, payload, id: str | None = None):
        """
        Initialize the SchemaInstance

        :returns: twilio.rest.events.v1.schema.SchemaInstance
        :rtype: twilio.rest.events.v1.schema.SchemaInstance
        """
        super().__init__(version)

        self._properties = {
            "id": payload.get("id"),
            "url": payload.get("url"),
            "links": payload.get("links"),
            "latest_version_date_created": deserialize.iso8601_datetime(
                payload.get("latest_version_date_created")
            ),
            "latest_version": deserialize.integer(payload.get("latest_version")),
        }

        self._context = None
        self._solution = {
            "id": id or self._properties["id"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SchemaContext for this SchemaInstance
        :rtype: twilio.rest.events.v1.schema.SchemaContext
        """
        if self._context is None:
            self._context = SchemaContext(
                self._version,
                id=self._solution["id"],
            )
        return self._context

    @property
    def id(self):
        """
        :returns: The unique identifier of the schema. Each schema can have multiple versions, that share the same id.
        :rtype: str
        """
        return self._properties["id"]

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: str
        """
        return self._properties["url"]

    @property
    def links(self):
        """
        :returns: Contains a dictionary of URL links to nested resources of this schema.
        :rtype: dict
        """
        return self._properties["links"]

    @property
    def latest_version_date_created(self):
        """
        :returns: The date that the latest schema version was created, given in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties["latest_version_date_created"]

    @property
    def latest_version(self):
        """
        :returns: The latest version published of this schema.
        :rtype: int
        """
        return self._properties["latest_version"]

    def fetch(self):
        """
        Fetch the SchemaInstance


        :returns: The fetched SchemaInstance
        :rtype: twilio.rest.events.v1.schema.SchemaInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the SchemaInstance


        :returns: The fetched SchemaInstance
        :rtype: twilio.rest.events.v1.schema.SchemaInstance
        """
        return await self._proxy.fetch_async()

    @property
    def versions(self):
        """
        Access the versions

        :returns: twilio.rest.events.v1.schema.SchemaVersionList
        :rtype: twilio.rest.events.v1.schema.SchemaVersionList
        """
        return self._proxy.versions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Events.V1.SchemaInstance {}>".format(context)


class SchemaContext(InstanceContext):
    def __init__(self, version: Version, id: str):
        """
        Initialize the SchemaContext

        :param Version version: Version that contains the resource
        :param id: The unique identifier of the schema. Each schema can have multiple versions, that share the same id.

        :returns: twilio.rest.events.v1.schema.SchemaContext
        :rtype: twilio.rest.events.v1.schema.SchemaContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "id": id,
        }
        self._uri = "/Schemas/{id}".format(**self._solution)

        self._versions = None

    def fetch(self):
        """
        Fetch the SchemaInstance


        :returns: The fetched SchemaInstance
        :rtype: twilio.rest.events.v1.schema.SchemaInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SchemaInstance(
            self._version,
            payload,
            id=self._solution["id"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the SchemaInstance


        :returns: The fetched SchemaInstance
        :rtype: twilio.rest.events.v1.schema.SchemaInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SchemaInstance(
            self._version,
            payload,
            id=self._solution["id"],
        )

    @property
    def versions(self):
        """
        Access the versions

        :returns: twilio.rest.events.v1.schema.SchemaVersionList
        :rtype: twilio.rest.events.v1.schema.SchemaVersionList
        """
        if self._versions is None:
            self._versions = SchemaVersionList(
                self._version,
                self._solution["id"],
            )
        return self._versions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Events.V1.SchemaContext {}>".format(context)
