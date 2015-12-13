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

import swift


MAJOR = None
MINOR = None
REVISION = None
FINAL = None


def parse(value):
    parts = value.split('.')
    if parts[-1].endswith('-dev'):
        final = False
        parts[-1] = parts[-1][:-4]
    else:
        final = True
    major = int(parts.pop(0))
    minor = int(parts.pop(0))
    if parts:
        revision = int(parts.pop(0).split('-', 1)[0])
    else:
        revision = 0
    return major, minor, revision, final


def newer_than(value):
    global MAJOR, MINOR, REVISION, FINAL
    try:
        major, minor, revision, final = parse(value)
        if MAJOR is None:
            MAJOR, MINOR, REVISION, FINAL = parse(swift.__version__)
        if MAJOR < major:
            return False
        elif MAJOR == major:
            if MINOR < minor:
                return False
            elif MINOR == minor:
                if REVISION < revision:
                    return False
                elif REVISION == revision:
                    if not FINAL or final:
                        return False
    except Exception:
        # Unable to detect if it's newer, better to fail
        return False
    return True


def at_least(value):
    global MAJOR, MINOR, REVISION, FINAL
    try:
        major, minor, revision, final = parse(value)
        if MAJOR is None:
            MAJOR, MINOR, REVISION, FINAL = parse(swift.__version__)
        if MAJOR < major:
            return False
        elif MAJOR == major:
            if MINOR < minor:
                return False
            elif MINOR == minor:
                if REVISION < revision:
                    return False
                elif REVISION == revision:
                    if not FINAL and final:
                        return False
    except Exception:
        # Unable to detect if it's newer, better to fail
        return False
    return True
