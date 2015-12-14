# Copyright (c) 2010-2013 OpenStack, LLC.
#
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

import gettext
import pkg_resources


try:
    # First, try to get our version out of PKG-INFO. If we're installed,
    # this'll let us find our version without pulling in pbr. After all, if
    # we're installed on a system, we're not in a Git-managed source tree, so
    # pbr doesn't really buy us anything.
    __version__ = __canonical_version__ = pkg_resources.get_provider(
        pkg_resources.Requirement.parse('swauth')).version
except pkg_resources.DistributionNotFound:
    # No PKG-INFO? We're probably running from a checkout, then. Let pbr do
    # its thing to figure out a version number.
    import pbr.version
    __version__ = pbr.version.VersionInfo(
        'swauth').version_string()

gettext.install('swauth')
