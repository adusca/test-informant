# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from mongoengine import (
    DateTimeField,
    DictField,
    Document,
    IntField,
    ListField,
    ReferenceField,
    StringField,
)

class Suite(Document):
    name = StringField(required=True)
    active_tests = ListField(required=True)
    skipped_tests = ListField(required=True)

class Build(Document):
    buildid = StringField(primary_key=True)
    config = DictField(required=True)
    date = DateTimeField(required=True)
    revision = StringField(required=True)
    total_active_tests = IntField(default=0)
    total_skipped_tests = IntField(default=0)
    suites = ListField(field=ReferenceField(Suite))
