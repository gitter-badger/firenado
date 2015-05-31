#!/usr/bin/env python
#
# Copyright 2015 Flavio Garcia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:

import argparse
from gettext import gettext as _


class ArgumentParserException(Exception):
    """ Class to be used IfluxArgumentParser when an error occur.
    """
    pass


class FirenadoArgumentParser(argparse.ArgumentParser):
    """ Argument parser that trows an exception leaving stderr untouched.
    """

    def error(self, message):
        args = {'prog': self.prog, 'message': message}
        message = _('%(prog)s: error: %(message)s\n') % args
        raise ArgumentParserException(message)
