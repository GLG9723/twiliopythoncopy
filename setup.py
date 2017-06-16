from __future__ import with_statement
import sys
from setuptools import setup, find_packages

__version__ = None
with open('twilio/__init__.py') as f:
    exec(f.read())

# To install the twilio-python library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed. Try reading the setuptools
# documentation: http://pypi.python.org/pypi/setuptools
REQUIRES = ["requests >= 2.0.0", "six", "pytz", "PyJWT >= 1.4.2"]
REQUIRES_PY2 = ["cryptography >= 1.3.4", "idna >= 2.0.0", "pyOpenSSL >= 0.14"]
REQUIRES_PY3 = ['pysocks']

if 'bdist_wheel' not in sys.argv:
    # Since wheels don't have setup.py but a static list of dependencies,
    # if install_requires is once made it's fixed to a wheel file.
    # To prevent fixing the following conditional dependencies, opt-out them
    # when building wheels and use "environment markers" instead  (see below).
    if sys.version_info < (3, 0):
        REQUIRES.extend(REQUIRES_PY2)
    if sys.version_info >= (3, 0):
        REQUIRES.extend(REQUIRES_PY3)

# Environment markers
extras_require = {
    # Older versions of pip don't support operators other than ==/!=
    ":python_version=='2.7'": REQUIRES_PY2,
    (":python_version=='3.3' or python_version=='3.4' or"
     " python_version=='3.5' or python_version=='3.6'"): REQUIRES_PY3,
}

setup(
    name = "twilio",
    version = __version__,
    description = "Twilio API client and TwiML generator",
    author = "Twilio",
    author_email = "help@twilio.com",
    url = "https://github.com/twilio/twilio-python/",
    keywords = ["twilio","twiml"],
    install_requires = REQUIRES,
    # bdist conditional requirements support
    extras_require = extras_require,
    packages = find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony",
        ],
    long_description = """\
    Python Twilio Helper Library
    ----------------------------

    DESCRIPTION
    The Twilio REST SDK simplifies the process of making calls using the Twilio REST API.
    The Twilio REST API lets to you initiate outgoing calls, list previous calls,
    and much more.  See https://www.github.com/twilio/twilio-python for more information.

     LICENSE The Twilio Python Helper Library is distributed under the MIT
    License """ )
