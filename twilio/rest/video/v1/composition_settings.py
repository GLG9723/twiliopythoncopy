r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Video
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class CompositionSettingsList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the CompositionSettingsList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.video.v1.composition_settings.CompositionSettingsList
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}

    def create(
        self,
        friendly_name,
        aws_credentials_sid=values.unset,
        encryption_key_sid=values.unset,
        aws_s3_url=values.unset,
        aws_storage_enabled=values.unset,
        encryption_enabled=values.unset,
    ):
        """
        Create the CompositionSettingsInstance

        :param str friendly_name: A descriptive string that you create to describe the resource and show to the user in the console
        :param str aws_credentials_sid: The SID of the stored Credential resource.
        :param str encryption_key_sid: The SID of the Public Key resource to use for encryption.
        :param str aws_s3_url: The URL of the AWS S3 bucket where the compositions should be stored. We only support DNS-compliant URLs like `https://documentation-example-twilio-bucket/compositions`, where `compositions` is the path in which you want the compositions to be stored. This URL accepts only URI-valid characters, as described in the <a href='https://tools.ietf.org/html/rfc3986#section-2'>RFC 3986</a>.
        :param bool aws_storage_enabled: Whether all compositions should be written to the `aws_s3_url`. When `false`, all compositions are stored in our cloud.
        :param bool encryption_enabled: Whether all compositions should be stored in an encrypted form. The default is `false`.

        :returns: The created CompositionSettingsInstance
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "AwsCredentialsSid": aws_credentials_sid,
                "EncryptionKeySid": encryption_key_sid,
                "AwsS3Url": aws_s3_url,
                "AwsStorageEnabled": aws_storage_enabled,
                "EncryptionEnabled": encryption_enabled,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CompositionSettingsInstance(self._version, payload)

    async def create_async(
        self,
        friendly_name,
        aws_credentials_sid=values.unset,
        encryption_key_sid=values.unset,
        aws_s3_url=values.unset,
        aws_storage_enabled=values.unset,
        encryption_enabled=values.unset,
    ):
        """
        Asynchronously create the CompositionSettingsInstance

        :param str friendly_name: A descriptive string that you create to describe the resource and show to the user in the console
        :param str aws_credentials_sid: The SID of the stored Credential resource.
        :param str encryption_key_sid: The SID of the Public Key resource to use for encryption.
        :param str aws_s3_url: The URL of the AWS S3 bucket where the compositions should be stored. We only support DNS-compliant URLs like `https://documentation-example-twilio-bucket/compositions`, where `compositions` is the path in which you want the compositions to be stored. This URL accepts only URI-valid characters, as described in the <a href='https://tools.ietf.org/html/rfc3986#section-2'>RFC 3986</a>.
        :param bool aws_storage_enabled: Whether all compositions should be written to the `aws_s3_url`. When `false`, all compositions are stored in our cloud.
        :param bool encryption_enabled: Whether all compositions should be stored in an encrypted form. The default is `false`.

        :returns: The created CompositionSettingsInstance
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "AwsCredentialsSid": aws_credentials_sid,
                "EncryptionKeySid": encryption_key_sid,
                "AwsS3Url": aws_s3_url,
                "AwsStorageEnabled": aws_storage_enabled,
                "EncryptionEnabled": encryption_enabled,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CompositionSettingsInstance(self._version, payload)

    def get(self):
        """
        Constructs a CompositionSettingsContext


        :returns: twilio.rest.video.v1.composition_settings.CompositionSettingsContext
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsContext
        """
        return CompositionSettingsContext(self._version)

    def __call__(self):
        """
        Constructs a CompositionSettingsContext


        :returns: twilio.rest.video.v1.composition_settings.CompositionSettingsContext
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsContext
        """
        return CompositionSettingsContext(self._version)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Video.V1.CompositionSettingsList>"


class CompositionSettingsInstance(InstanceResource):
    def __init__(self, version, payload):
        """
        Initialize the CompositionSettingsInstance

        :returns: twilio.rest.video.v1.composition_settings.CompositionSettingsInstance
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "friendly_name": payload.get("friendly_name"),
            "aws_credentials_sid": payload.get("aws_credentials_sid"),
            "aws_s3_url": payload.get("aws_s3_url"),
            "aws_storage_enabled": payload.get("aws_storage_enabled"),
            "encryption_key_sid": payload.get("encryption_key_sid"),
            "encryption_enabled": payload.get("encryption_enabled"),
            "url": payload.get("url"),
        }

        self._context = None
        self._solution = {}

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CompositionSettingsContext for this CompositionSettingsInstance
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsContext
        """
        if self._context is None:
            self._context = CompositionSettingsContext(
                self._version,
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CompositionSettings resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource and that will be shown in the console
        :rtype: str
        """
        return self._properties["friendly_name"]

    @property
    def aws_credentials_sid(self):
        """
        :returns: The SID of the stored Credential resource.
        :rtype: str
        """
        return self._properties["aws_credentials_sid"]

    @property
    def aws_s3_url(self):
        """
        :returns: The URL of the AWS S3 bucket where the compositions are stored. We only support DNS-compliant URLs like `https://documentation-example-twilio-bucket/compositions`, where `compositions` is the path in which you want the compositions to be stored. This URL accepts only URI-valid characters, as described in the <a href='https://tools.ietf.org/html/rfc3986#section-2'>RFC 3986</a>.
        :rtype: str
        """
        return self._properties["aws_s3_url"]

    @property
    def aws_storage_enabled(self):
        """
        :returns: Whether all compositions are written to the `aws_s3_url`. When `false`, all compositions are stored in our cloud.
        :rtype: bool
        """
        return self._properties["aws_storage_enabled"]

    @property
    def encryption_key_sid(self):
        """
        :returns: The SID of the Public Key resource used for encryption.
        :rtype: str
        """
        return self._properties["encryption_key_sid"]

    @property
    def encryption_enabled(self):
        """
        :returns: Whether all compositions are stored in an encrypted form. The default is `false`.
        :rtype: bool
        """
        return self._properties["encryption_enabled"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties["url"]

    def create(
        self,
        friendly_name,
        aws_credentials_sid=values.unset,
        encryption_key_sid=values.unset,
        aws_s3_url=values.unset,
        aws_storage_enabled=values.unset,
        encryption_enabled=values.unset,
    ):
        """
        Create the CompositionSettingsInstance

        :param str friendly_name: A descriptive string that you create to describe the resource and show to the user in the console
        :param str aws_credentials_sid: The SID of the stored Credential resource.
        :param str encryption_key_sid: The SID of the Public Key resource to use for encryption.
        :param str aws_s3_url: The URL of the AWS S3 bucket where the compositions should be stored. We only support DNS-compliant URLs like `https://documentation-example-twilio-bucket/compositions`, where `compositions` is the path in which you want the compositions to be stored. This URL accepts only URI-valid characters, as described in the <a href='https://tools.ietf.org/html/rfc3986#section-2'>RFC 3986</a>.
        :param bool aws_storage_enabled: Whether all compositions should be written to the `aws_s3_url`. When `false`, all compositions are stored in our cloud.
        :param bool encryption_enabled: Whether all compositions should be stored in an encrypted form. The default is `false`.

        :returns: The created CompositionSettingsInstance
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsInstance
        """
        return self._proxy.create(
            friendly_name,
            aws_credentials_sid=aws_credentials_sid,
            encryption_key_sid=encryption_key_sid,
            aws_s3_url=aws_s3_url,
            aws_storage_enabled=aws_storage_enabled,
            encryption_enabled=encryption_enabled,
        )

    async def create_async(
        self,
        friendly_name,
        aws_credentials_sid=values.unset,
        encryption_key_sid=values.unset,
        aws_s3_url=values.unset,
        aws_storage_enabled=values.unset,
        encryption_enabled=values.unset,
    ):
        """
        Asynchronous coroutine to create the CompositionSettingsInstance

        :param str friendly_name: A descriptive string that you create to describe the resource and show to the user in the console
        :param str aws_credentials_sid: The SID of the stored Credential resource.
        :param str encryption_key_sid: The SID of the Public Key resource to use for encryption.
        :param str aws_s3_url: The URL of the AWS S3 bucket where the compositions should be stored. We only support DNS-compliant URLs like `https://documentation-example-twilio-bucket/compositions`, where `compositions` is the path in which you want the compositions to be stored. This URL accepts only URI-valid characters, as described in the <a href='https://tools.ietf.org/html/rfc3986#section-2'>RFC 3986</a>.
        :param bool aws_storage_enabled: Whether all compositions should be written to the `aws_s3_url`. When `false`, all compositions are stored in our cloud.
        :param bool encryption_enabled: Whether all compositions should be stored in an encrypted form. The default is `false`.

        :returns: The created CompositionSettingsInstance
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsInstance
        """
        return await self._proxy.create_async(
            friendly_name,
            aws_credentials_sid=aws_credentials_sid,
            encryption_key_sid=encryption_key_sid,
            aws_s3_url=aws_s3_url,
            aws_storage_enabled=aws_storage_enabled,
            encryption_enabled=encryption_enabled,
        )

    def fetch(self):
        """
        Fetch the CompositionSettingsInstance


        :returns: The fetched CompositionSettingsInstance
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the CompositionSettingsInstance


        :returns: The fetched CompositionSettingsInstance
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Video.V1.CompositionSettingsInstance {}>".format(context)


class CompositionSettingsContext(InstanceContext):
    def __init__(self, version: Version):
        """
        Initialize the CompositionSettingsContext

        :param Version version: Version that contains the resource

        :returns: twilio.rest.video.v1.composition_settings.CompositionSettingsContext
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = "/CompositionSettings/Default".format(**self._solution)

    def create(
        self,
        friendly_name,
        aws_credentials_sid=values.unset,
        encryption_key_sid=values.unset,
        aws_s3_url=values.unset,
        aws_storage_enabled=values.unset,
        encryption_enabled=values.unset,
    ):
        """
        Create the CompositionSettingsInstance

        :param str friendly_name: A descriptive string that you create to describe the resource and show to the user in the console
        :param str aws_credentials_sid: The SID of the stored Credential resource.
        :param str encryption_key_sid: The SID of the Public Key resource to use for encryption.
        :param str aws_s3_url: The URL of the AWS S3 bucket where the compositions should be stored. We only support DNS-compliant URLs like `https://documentation-example-twilio-bucket/compositions`, where `compositions` is the path in which you want the compositions to be stored. This URL accepts only URI-valid characters, as described in the <a href='https://tools.ietf.org/html/rfc3986#section-2'>RFC 3986</a>.
        :param bool aws_storage_enabled: Whether all compositions should be written to the `aws_s3_url`. When `false`, all compositions are stored in our cloud.
        :param bool encryption_enabled: Whether all compositions should be stored in an encrypted form. The default is `false`.

        :returns: The created CompositionSettingsInstance
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "AwsCredentialsSid": aws_credentials_sid,
                "EncryptionKeySid": encryption_key_sid,
                "AwsS3Url": aws_s3_url,
                "AwsStorageEnabled": aws_storage_enabled,
                "EncryptionEnabled": encryption_enabled,
            }
        )

        payload = self._version.create(method="POST", uri=self._uri, data=data)

        return CompositionSettingsInstance(self._version, payload)

    async def create_async(
        self,
        friendly_name,
        aws_credentials_sid=values.unset,
        encryption_key_sid=values.unset,
        aws_s3_url=values.unset,
        aws_storage_enabled=values.unset,
        encryption_enabled=values.unset,
    ):
        """
        Asynchronous coroutine to create the CompositionSettingsInstance

        :param str friendly_name: A descriptive string that you create to describe the resource and show to the user in the console
        :param str aws_credentials_sid: The SID of the stored Credential resource.
        :param str encryption_key_sid: The SID of the Public Key resource to use for encryption.
        :param str aws_s3_url: The URL of the AWS S3 bucket where the compositions should be stored. We only support DNS-compliant URLs like `https://documentation-example-twilio-bucket/compositions`, where `compositions` is the path in which you want the compositions to be stored. This URL accepts only URI-valid characters, as described in the <a href='https://tools.ietf.org/html/rfc3986#section-2'>RFC 3986</a>.
        :param bool aws_storage_enabled: Whether all compositions should be written to the `aws_s3_url`. When `false`, all compositions are stored in our cloud.
        :param bool encryption_enabled: Whether all compositions should be stored in an encrypted form. The default is `false`.

        :returns: The created CompositionSettingsInstance
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "AwsCredentialsSid": aws_credentials_sid,
                "EncryptionKeySid": encryption_key_sid,
                "AwsS3Url": aws_s3_url,
                "AwsStorageEnabled": aws_storage_enabled,
                "EncryptionEnabled": encryption_enabled,
            }
        )

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data
        )

        return CompositionSettingsInstance(self._version, payload)

    def fetch(self):
        """
        Fetch the CompositionSettingsInstance


        :returns: The fetched CompositionSettingsInstance
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return CompositionSettingsInstance(
            self._version,
            payload,
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the CompositionSettingsInstance


        :returns: The fetched CompositionSettingsInstance
        :rtype: twilio.rest.video.v1.composition_settings.CompositionSettingsInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return CompositionSettingsInstance(
            self._version,
            payload,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Video.V1.CompositionSettingsContext {}>".format(context)
