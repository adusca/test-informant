# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from collections import Iterable

from manifestparser import TestManifest

from .base import AbstractParser

class IniParser(AbstractParser):

    def __call__(self, manifests, buildconfig):
        if not isinstance(manifests, Iterable):
            manifests = [manifests]

        m = TestManifest(manifests)

        active = [t['relpath'] for t in m.active_tests(exists=False, disabled=False, **buildconfig)]
        skipped = [t['relpath'] for t in m.tests if t['relpath'] not in active]

        return active, skipped