# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from multiprocessing import cpu_count

from .parsers import IniParser

# mongodb database name to connect to
DB_NAME = 'test-informant'

# mongodb host to connect to
DB_HOST = 'localhost'

# mongodb port to connect to
DB_PORT = 27017

# branch to listen for builds on
BRANCH = 'mozilla-inbound'

# number of threads to spawn
NUM_WORKERS = cpu_count()

# the number of builds allowed to queue up before they start getting dropped
MAX_BUILD_QUEUE_SIZE = 100

# the number of tests.zip bundles allowed on the filesystem at once, disabled by default
MAX_TESTS_CACHE_SIZE = 0

# a mapping from suite name to dict containing manifest path and parser type
SUITES = {
    'marionette': {
        'manifests': ['marionette/tests/testing/marionette/client/marionette/tests/unit-tests.ini'],
        'parser': IniParser,
        'relpath': 'marionette/tests',
    },
    'mochitest-a11y': {
        'manifests': ['mochitest/a11y/a11y.ini'],
        'parser': IniParser,
        'relpath': 'mochitest/a11y',
    },
    'mochitest-browser-chrome': {
        'manifests': ['mochitest/browser/browser-chrome.ini'],
        'parser': IniParser,
        'relpath': 'mochitest/browser',
    },
    'mochitest-browser-chrome-e10s': {
        'manifests': ['mochitest/browser/browser-chrome.ini'],
        'parser': IniParser,
        'relpath': 'mochitest/browser',
        'extra_config': {
            'e10s': True,
        },
    },
    'mochitest-chrome': {
        'manifests': ['mochitest/chrome/chrome.ini'],
        'parser': IniParser,
        'relpath': 'mochitest/chrome',
    },
    'mochitest-plain-e10s': {
        'manifests': ['mochitest/tests/mochitest.ini'],
        'parser': IniParser,
        'relpath': 'mochitest/tests',
        'extra_config': {
            'e10s': True,
        },
    },
    'mochitest-plain': {
        'manifests': ['mochitest/tests/mochitest.ini'],
        'parser': IniParser,
        'relpath': 'mochitest/tests',
    },
    'xpcshell': {
        'manifests': ['xpcshell/tests/xpcshell.ini'],
        'parser': IniParser,
        'relpath': 'xpcshell/tests',
    },
    'xpcshell-android': {
        'manifests': ['xpcshell/tests/xpcshell_android.ini'],
        'parser': IniParser,
        'relpath': 'xpcshell/tests',
    },
}

# a mapping from plaform type to enabled suites.
PLATFORMS = {
    'linux-opt': [
        'marionette',
        'mochitest-a11y',
        'mochitest-browser-chrome',
        'mochitest-browser-chrome-e10s',
        'mochitest-chrome',
        'mochitest-plain-e10s',
        'mochitest-plain',
        'xpcshell',
    ],
    'linux-debug': [
        'marionette',
        'mochitest-a11y',
        'mochitest-browser-chrome',
        'mochitest-chrome',
        'mochitest-plain-e10s',
        'mochitest-plain',
        'xpcshell',
    ],
    'linux64-opt': [
        'marionette',
        'mochitest-a11y',
        'mochitest-browser-chrome',
        'mochitest-browser-chrome-e10s',
        'mochitest-chrome',
        'mochitest-plain-e10s',
        'mochitest-plain',
        'xpcshell',
    ],
    'linux64-debug': [
        'marionette',
        'mochitest-a11y',
        'mochitest-browser-chrome',
        'mochitest-chrome',
        'mochitest-plain-e10s',
        'mochitest-plain',
        'xpcshell',
    ],
    'macosx64-opt': [
        'marionette',
        'mochitest-a11y',
        'mochitest-browser-chrome',
        'mochitest-chrome',
        'mochitest-plain',
        'xpcshell',
    ],
    'macosx64-debug': [
        'marionette',
        'mochitest-a11y',
        'mochitest-browser-chrome',
        'mochitest-chrome',
        'mochitest-plain',
        'xpcshell',
    ],
    'win32-opt': [
        'marionette',
        'mochitest-a11y',
        'mochitest-browser-chrome',
        'mochitest-chrome',
        'mochitest-plain',
        'xpcshell',
    ],
    'win32-debug': [
        'marionette',
        'mochitest-a11y',
        'mochitest-browser-chrome',
        'mochitest-chrome',
        'mochitest-plain',
        'xpcshell',
    ],
    'android-opt': [
        'mochitest-plain',
        'xpcshell-android',
    ],
    'linux32_gecko-opt': [
        'mochitest-plain',
    ],
    'linux64_gecko-opt': [
        'mochitest-plain',
    ] ,
    'mulet-opt': [
        'mochitest-plain',
    ],
}
