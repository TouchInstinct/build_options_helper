# -*- coding: utf-8 -*-

from __future__ import unicode_literals # python 2/3 support

import argparse
import os
import tempfile

class writeable_dir(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        prospective_dir = values

        if not os.path.isdir(prospective_dir):
            raise argparse.ArgumentTypeError("writeable_dir:{0} is not a valid path".format(prospective_dir))
        if os.access(prospective_dir, os.W_OK):
            setattr(namespace, self.dest, prospective_dir)
        else:
            raise argparse.ArgumentTypeError("writeable_dir:{0} is not a writeable dir".format(prospective_dir))

class ArgumentParser(argparse.ArgumentParser):
    def configure(self):
        self.add_argument('--build-parameters-path', '-bp',
                        default="build_parameters.yaml", type=open,
                        required=True, help="Relative or absolute path to build parameters in yaml format.")

        self.add_argument('--output-folder', '-o',
                        action=writeable_dir, default=tempfile.mkdtemp(),
                        required=True, help="Path to writeable directory for execution results.")

        self.add_argument('--render', '-r',
                        choices=['ios_build_settings', 'team_city_web_parameters'], type=str,
                        required=True, help="Task that should be done.")

        self.add_argument('--platform', '-p',
                        choices=['ios', 'android'], type=str,
                        required=True, help="Platform for which build parameters rules should be applied.")