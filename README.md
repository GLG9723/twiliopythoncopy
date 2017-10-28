# twilio-python

[![Build Status](https://secure.travis-ci.org/twilio/twilio-python.png?branch=master)](http://travis-ci.org/twilio/twilio-python)
[![PyPI](https://img.shields.io/pypi/v/twilio.svg)](https://pypi.python.org/pypi/twilio)
[![PyPI](https://img.shields.io/pypi/pyversions/twilio.svg)](https://pypi.python.org/pypi/twilio)

A module for using the Twilio REST API and generating valid
[TwiML](http://www.twilio.com/docs/api/twiml/ "TwiML -
Twilio Markup Language").

## Recent Update

As of release 6.5.0, Beta and Developer Preview products are now exposed via
the main `twilio-python` artifact. Releases of the `alpha` branch have been
discontinued.

If you were using the `alpha` release line, you should be able to switch back
to the normal release line without issue.

If you were using the normal release line, you should now see several new
product lines that were historically hidden from you due to their Beta or
Developer Preview status. Such products are explicitly documented as
Beta/Developer Preview both in the Twilio docs and console, as well as through
in-line code documentation here in the library.

## Installation

Install from PyPi using [pip](http://www.pip-installer.org/en/latest/), a
package manager for Python.

    pip install twilio

Don't have pip installed? Try installing it, by running this from the command
line:

    $ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

Or, you can [download the source code
(ZIP)](https://github.com/twilio/twilio-python/zipball/master "twilio-python
source code") for `twilio-python`, and then run:

    python setup.py install

You may need to run the above commands with `sudo`.

### Migrate from 5.x
Please consult the [official migration guide](https://www.twilio.com/docs/libraries/python/migration-guide) for information on upgrading your application using twilio-python 5.x to 6.x

## Feedback
Report any feedback or problems with this Release Candidate to the [Github Issues](https://github.com/twilio/twilio-python/issues) for twilio-python.

## Getting Started

Getting started with the Twilio API couldn't be easier. Create a
`Client` and you're ready to go.

### API Credentials

The `Twilio` needs your Twilio credentials. You can either pass these
directly to the constructor (see the code below) or via environment variables.

```python
from twilio.rest import Client

account = "ACXXXXXXXXXXXXXXXXX"
token = "YYYYYYYYYYYYYYYYYY"
client = Client(account, token)
```

Alternately, a `Client` constructor without these parameters will
look for `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` variables inside the
current environment.

#### Proxy Configuration

If you need to configure a proxy to access the Internet, you can set the
environment variables `HTTP_PROXY` and/or `HTTPS_PROXY`, or alternatively
pass in a dictionary with the proxy configuration to the client.

```python
from twilio.rest import Client

proxy_config = {'http': 'http://user:password@example.com:80'}
account = 'ACXXXXXXXXXXXXX'
token = 'YYYYYYYYYYYYYYYYY'
client = Client(account, token, proxies=proxy_config)
```

Note: proxy urls must include the scheme.

We suggest storing your credentials as environment variables. Why? You'll never
have to worry about committing your credentials and accidentally posting them
somewhere public.


```python
from twilio.rest import Client
client = Client()
```

### Make a Call

```python
from twilio.rest import Client

account = "ACXXXXXXXXXXXXXXXXX"
token = "YYYYYYYYYYYYYYYYYY"
client = Client(account, token)

call = client.calls.create(to="9991231234",
                           from_="9991231234",
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print(call.sid)
```

### Send an SMS

```python
from twilio.rest import Client

account = "ACXXXXXXXXXXXXXXXXX"
token = "YYYYYYYYYYYYYYYYYY"
client = Client(account, token)

message = client.messages.create(to="+12316851234", from_="+15555555555",
                                 body="Hello there!")
```

### Handling a call using TwiML

To control phone calls, your application needs to output
[TwiML](http://www.twilio.com/docs/api/twiml/ "TwiML - Twilio Markup
Language"). Use `twilio.twiml.Response` to easily create such responses.

```python
from twilio.twiml.voice_response import VoiceResponse

r = VoiceResponse()
r.say("Welcome to twilio!")
print(str(r))
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<Response><Say>Welcome to twilio!</Say></Response>
```
