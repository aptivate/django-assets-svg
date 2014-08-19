from __future__ import absolute_import, unicode_literals

import re

from django.core.management import call_command
from django.template import Context, Template
from django.test import TestCase

class SimpleTest(TestCase):
    def test_can_build_assets(self):
        call_command('assets', 'build')
