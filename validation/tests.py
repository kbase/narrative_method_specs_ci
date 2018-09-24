import json
import os
import unittest

import yaml
from cerberus import Validator

types_dir = os.path.join(os.path.dirname(__file__), "..", "types")


class ConditionUtilsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(os.path.dirname(__file__)+'/TypeSpecSchema.yaml') as in_file:
            type_schema = yaml.load(in_file)
            cls.type_spec_validatator = Validator(type_schema)
        with open(os.path.dirname(__file__)+'/TypeDisplaySchema.yaml') as in_file:
            type_schema = yaml.load(in_file)
            cls.type_display_validatator = Validator(type_schema)

    def test_validate_type_specs(self):
        for file in os.listdir(types_dir):
            with open(os.path.join(types_dir, file, 'spec.json')) as infile:
                type_spec = json.load(infile)
                self.assertTrue(self.type_spec_validatator.validate(type_spec),
                                "{} failed validation {}".format(file, self.type_spec_validatator.errors))

    def test_validate_type_displays(self):
        for file in os.listdir(types_dir):
            with open(os.path.join(types_dir, file, 'display.yaml')) as infile:
                type_spec = yaml.load(infile)
                self.assertTrue(self.type_display_validatator.validate(type_spec),
                                "{} failed validation {}".format(file, self.type_display_validatator.errors))