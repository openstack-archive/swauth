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
#
# Pablo Llopis 2011

import mock
from swauth import authtypes
import unittest


class TestPlaintext(unittest.TestCase):

    def setUp(self):
        self.auth_encoder = authtypes.Plaintext()

    def test_plaintext_encode(self):
        enc_key = self.auth_encoder.encode('keystring')
        self.assertEqual('plaintext:keystring', enc_key)

    def test_plaintext_valid_match(self):
        creds = 'plaintext:keystring'
        match = self.auth_encoder.match('keystring', creds)
        self.assertEqual(match, True)

    def test_plaintext_invalid_match(self):
        creds = 'plaintext:other-keystring'
        match = self.auth_encoder.match('keystring', creds)
        self.assertEqual(match, False)


class TestSha1(unittest.TestCase):

    def setUp(self):
        self.auth_encoder = authtypes.Sha1()
        self.auth_encoder.salt = 'salt'

    @mock.patch('swauth.authtypes.os')
    def test_sha1_encode(self, os):
        os.urandom.return_value.encode.return_value.rstrip \
            .return_value = 'salt'
        enc_key = self.auth_encoder.encode('keystring')
        self.assertEqual('sha1:salt$d50dc700c296e23ce5b41f7431a0e01f69010f06',
                          enc_key)

    def test_sha1_valid_match(self):
        creds = 'sha1:salt$d50dc700c296e23ce5b41f7431a0e01f69010f06'
        match = self.auth_encoder.match('keystring', creds)
        self.assertEqual(match, True)

    def test_sha1_invalid_match(self):
        creds = 'sha1:salt$deadbabedeadbabedeadbabec0ffeebadc0ffeee'
        match = self.auth_encoder.match('keystring', creds)
        self.assertEqual(match, False)

        creds = 'sha1:salt$d50dc700c296e23ce5b41f7431a0e01f69010f06'
        match = self.auth_encoder.match('keystring2', creds)
        self.assertEqual(match, False)


class TestSha512(unittest.TestCase):

    def setUp(self):
        self.auth_encoder = authtypes.Sha512()
        self.auth_encoder.salt = 'salt'

    @mock.patch('swauth.authtypes.os')
    def test_sha512_encode(self, os):
        os.urandom.return_value.encode.return_value.rstrip \
            .return_value = 'salt'
        enc_key = self.auth_encoder.encode('keystring')
        self.assertEqual('sha512:salt$482e73705fac6909e2d78e8bbaf65ac3ca1473'
                         '8f445cc2367b7daa3f0e8f3dcfe798e426b9e332776c8da59c'
                         '0c11d4832931d1bf48830f670ecc6ceb04fbad0f', enc_key)

    def test_sha512_valid_match(self):
        creds = ('sha512:salt$482e73705fac6909e2d78e8bbaf65ac3ca14738f445cc2'
                 '367b7daa3f0e8f3dcfe798e426b9e332776c8da59c0c11d4832931d1bf'
                 '48830f670ecc6ceb04fbad0f')
        match = self.auth_encoder.match('keystring', creds)
        self.assertEqual(match, True)

    def test_sha512_invalid_match(self):
        creds = ('sha512:salt$deadbabedeadbabedeadbabedeadbabedeadbabedeadba'
                 'bedeadbabedeadbabedeadbabedeadbabedeadbabedeadbabedeadbabe'
                 'c0ffeebadc0ffeeec0ffeeba')
        match = self.auth_encoder.match('keystring', creds)
        self.assertEqual(match, False)

        creds = ('sha512:salt$482e73705fac6909e2d78e8bbaf65ac3ca14738f445cc2'
                 '367b7daa3f0e8f3dcfe798e426b9e332776c8da59c0c11d4832931d1bf'
                 '48830f670ecc6ceb04fbad0f')
        match = self.auth_encoder.match('keystring2', creds)
        self.assertEqual(match, False)

if __name__ == '__main__':
    unittest.main()
