# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from swauth import swift_version as ver
import swift


class TestSwiftVersion(unittest.TestCase):
    def test_parse(self):
        tests = {
            "1.2": (1, 2, 0, True),
            "1.2.3": (1, 2, 3, True),
            "1.2.3-dev": (1, 2, 3, False)
        }

        for (input, ref_out) in tests.items():
            out = ver.parse(input)
            self.assertEqual(ref_out, out)

    def test_newer_than(self):
        orig_version = swift.__version__

        swift.__version__ = '1.3'
        ver.MAJOR = None
        self.assertTrue(ver.newer_than('1.2'))
        self.assertTrue(ver.newer_than('1.2.9'))
        self.assertTrue(ver.newer_than('1.3-dev'))
        self.assertTrue(ver.newer_than('1.3.0-dev'))
        self.assertFalse(ver.newer_than('1.3'))
        self.assertFalse(ver.newer_than('1.3.0'))
        self.assertFalse(ver.newer_than('1.3.1-dev'))
        self.assertFalse(ver.newer_than('1.3.1'))
        self.assertFalse(ver.newer_than('1.4-dev'))
        self.assertFalse(ver.newer_than('1.4'))
        self.assertFalse(ver.newer_than('2.0-dev'))
        self.assertFalse(ver.newer_than('2.0'))

        swift.__version__ = '1.3-dev'
        ver.MAJOR = None
        self.assertTrue(ver.newer_than('1.2'))
        self.assertTrue(ver.newer_than('1.2.9'))
        self.assertFalse(ver.newer_than('1.3-dev'))
        self.assertFalse(ver.newer_than('1.3.0-dev'))
        self.assertFalse(ver.newer_than('1.3'))
        self.assertFalse(ver.newer_than('1.3.0'))
        self.assertFalse(ver.newer_than('1.3.1-dev'))
        self.assertFalse(ver.newer_than('1.3.1'))
        self.assertFalse(ver.newer_than('1.4-dev'))
        self.assertFalse(ver.newer_than('1.4'))
        self.assertFalse(ver.newer_than('2.0-dev'))
        self.assertFalse(ver.newer_than('2.0'))

        swift.__version__ = '1.5.6'
        ver.MAJOR = None
        self.assertTrue(ver.newer_than('1.4'))
        self.assertTrue(ver.newer_than('1.5'))
        self.assertTrue(ver.newer_than('1.5.5-dev'))
        self.assertTrue(ver.newer_than('1.5.5'))
        self.assertTrue(ver.newer_than('1.5.6-dev'))
        self.assertFalse(ver.newer_than('1.5.6'))
        self.assertFalse(ver.newer_than('1.5.7-dev'))
        self.assertFalse(ver.newer_than('1.5.7'))
        self.assertFalse(ver.newer_than('1.6-dev'))
        self.assertFalse(ver.newer_than('1.6'))
        self.assertFalse(ver.newer_than('2.0-dev'))
        self.assertFalse(ver.newer_than('2.0'))

        swift.__version__ = '1.5.6-dev'
        ver.MAJOR = None
        self.assertTrue(ver.newer_than('1.4'))
        self.assertTrue(ver.newer_than('1.5'))
        self.assertTrue(ver.newer_than('1.5.5-dev'))
        self.assertTrue(ver.newer_than('1.5.5'))
        self.assertFalse(ver.newer_than('1.5.6-dev'))
        self.assertFalse(ver.newer_than('1.5.6'))
        self.assertFalse(ver.newer_than('1.5.7-dev'))
        self.assertFalse(ver.newer_than('1.5.7'))
        self.assertFalse(ver.newer_than('1.6-dev'))
        self.assertFalse(ver.newer_than('1.6'))
        self.assertFalse(ver.newer_than('2.0-dev'))
        self.assertFalse(ver.newer_than('2.0'))

        swift.__version__ = '1.10.0-2.el6'
        ver.MAJOR = None
        self.assertTrue(ver.newer_than('1.9'))
        self.assertTrue(ver.newer_than('1.10.0-dev'))
        self.assertFalse(ver.newer_than('1.10.0'))
        self.assertFalse(ver.newer_than('1.11'))
        self.assertFalse(ver.newer_than('2.0'))

        swift.__version__ = 'garbage'
        ver.MAJOR = None
        self.assertFalse(ver.newer_than('2.0'))

        swift.__version__ = orig_version

    def test_at_least(self):
        orig_version = swift.__version__

        swift.__version__ = '1.3'
        ver.MAJOR = None
        self.assertTrue(ver.at_least('1.2'))
        self.assertTrue(ver.at_least('1.2.9'))
        self.assertTrue(ver.at_least('1.3-dev'))
        self.assertTrue(ver.at_least('1.3.0-dev'))
        self.assertTrue(ver.at_least('1.3'))
        self.assertTrue(ver.at_least('1.3.0'))
        self.assertFalse(ver.at_least('1.3.1-dev'))
        self.assertFalse(ver.at_least('1.3.1'))
        self.assertFalse(ver.at_least('1.4-dev'))
        self.assertFalse(ver.at_least('1.4'))
        self.assertFalse(ver.at_least('2.0-dev'))
        self.assertFalse(ver.at_least('2.0'))

        swift.__version__ = '1.3-dev'
        ver.MAJOR = None
        self.assertTrue(ver.at_least('1.2'))
        self.assertTrue(ver.at_least('1.2.9'))
        self.assertTrue(ver.at_least('1.3-dev'))
        self.assertTrue(ver.at_least('1.3.0-dev'))
        self.assertFalse(ver.at_least('1.3'))
        self.assertFalse(ver.at_least('1.3.0'))
        self.assertFalse(ver.at_least('1.3.1-dev'))
        self.assertFalse(ver.at_least('1.3.1'))
        self.assertFalse(ver.at_least('1.4-dev'))
        self.assertFalse(ver.at_least('1.4'))
        self.assertFalse(ver.at_least('2.0-dev'))
        self.assertFalse(ver.at_least('2.0'))

        swift.__version__ = '1.5.6'
        ver.MAJOR = None
        self.assertTrue(ver.at_least('1.4'))
        self.assertTrue(ver.at_least('1.5'))
        self.assertTrue(ver.at_least('1.5.5-dev'))
        self.assertTrue(ver.at_least('1.5.5'))
        self.assertTrue(ver.at_least('1.5.6-dev'))
        self.assertTrue(ver.at_least('1.5.6'))
        self.assertFalse(ver.at_least('1.5.7-dev'))
        self.assertFalse(ver.at_least('1.5.7'))
        self.assertFalse(ver.at_least('1.6-dev'))
        self.assertFalse(ver.at_least('1.6'))
        self.assertFalse(ver.at_least('2.0-dev'))
        self.assertFalse(ver.at_least('2.0'))

        swift.__version__ = '1.5.6-dev'
        ver.MAJOR = None
        self.assertTrue(ver.at_least('1.4'))
        self.assertTrue(ver.at_least('1.5'))
        self.assertTrue(ver.at_least('1.5.5-dev'))
        self.assertTrue(ver.at_least('1.5.5'))
        self.assertTrue(ver.at_least('1.5.6-dev'))
        self.assertFalse(ver.at_least('1.5.6'))
        self.assertFalse(ver.at_least('1.5.7-dev'))
        self.assertFalse(ver.at_least('1.5.7'))
        self.assertFalse(ver.at_least('1.6-dev'))
        self.assertFalse(ver.at_least('1.6'))
        self.assertFalse(ver.at_least('2.0-dev'))
        self.assertFalse(ver.at_least('2.0'))

        swift.__version__ = '1.10.0-2.el6'
        ver.MAJOR = None
        self.assertTrue(ver.at_least('1.9'))
        self.assertTrue(ver.at_least('1.10.0-dev'))
        self.assertTrue(ver.at_least('1.10.0'))
        self.assertFalse(ver.at_least('1.11'))
        self.assertFalse(ver.at_least('2.0'))

        swift.__version__ = 'garbage'
        ver.MAJOR = None
        self.assertFalse(ver.at_least('2.0'))

        swift.__version__ = orig_version
