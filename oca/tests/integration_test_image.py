# vim:  set fileencoding=utf8
# encoding:utf8
#
# Author: Alin Floare <alin.floare@databus.systems>

import os
import unittest

import oca
from oca.exceptions import OpenNebulaException

condition = bool(os.environ.get('OCA_INT_TESTS', False)) & bool(os.environ.get('OCA_INT_IMAGE_TESTS', False))


@unittest.skipUnless(condition, "Skipping integration tests")
class IntTestImage(unittest.TestCase):
    def setUp(self):
        try:
            del os.environ["ONE_AUTH"]
        except KeyError:
            pass

        self.c = oca.Client(os.environ['OCA_INT_TESTS_ONE_AUTH'], os.environ['OCA_INT_TESTS_ONE_XMLRPC'])

    def tearDown(self):
        print("teardown")
        imgs = oca.ImagePool(self.c)
        imgs.info()
        for img in imgs:
            if img.name.startswith('inttest_img_'):
                img.delete()

    def test_allocate(self):
        path = os.environ.get('OCA_INT_TEST_IMAGE_PATH', '~/ttyvd-context.qcow2')
        # img = oca.Image.allocate(self.c, '<TEMPLATE><NAME>inttest_img_1</NAME><PATH>{p}</PATH></TEMPLATE>'.format(p=path), 1)

        img = oca.Image.allocate(self.c, '<TEMPLATE><NAME>inttest_img_4</NAME><TYPE>DATABLOCK</TYPE><SIZE>382</SIZE></TEMPLATE>', 1)
        img = oca.Image.allocate(self.c, '<TEMPLATE><NAME>inttest_img_5</NAME><TYPE>DATABLOCK</TYPE><SIZE>382</SIZE></TEMPLATE>', 1)
        img = oca.Image.allocate(self.c, '<TEMPLATE><NAME>inttest_img_6</NAME><TYPE>DATABLOCK</TYPE><SIZE>382</SIZE></TEMPLATE>', 1)

    def test_allocate_with_same_name(self):
        with self.assertRaises(OpenNebulaException):
            img = oca.Image.allocate(self.c, '<TEMPLATE><NAME>inttest_img_6</NAME><TYPE>DATABLOCK</TYPE><SIZE>382</SIZE></TEMPLATE>', 1)
            img = oca.Image.allocate(self.c, '<TEMPLATE><NAME>inttest_img_6</NAME><TYPE>DATABLOCK</TYPE><SIZE>382</SIZE></TEMPLATE>', 1)

    def test_delete(self):
        imgs = oca.ImagePool(self.c)
        imgs.info()
        for img in imgs:
            if img.name.startswith('inttest'):
                img.delete()


if __name__ == "__main__":
    unittest.main()
