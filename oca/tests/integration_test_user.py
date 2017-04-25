# vim:  set fileencoding=utf8
# encoding:utf8
#
# Author: Alin Floare <alin.floare@databus.systems>

import os
import unittest

import oca
from oca.exceptions import OpenNebulaException


@unittest.skipUnless(os.environ.get('OCA_INT_TESTS', False),
                     "Skipping integration tests")
class IntTestUser(unittest.TestCase):
    def setUp(self):
        try:
            del os.environ["ONE_AUTH"]
        except KeyError:
            pass

        self.c = oca.Client(os.environ['OCA_INT_TESTS_ONE_AUTH'],
                            os.environ['OCA_INT_TESTS_ONE_XMLRPC'])

    def tearDown(self):
        print("teardown")
        users = oca.UserPool(self.c)
        users.info()
        for user in users:
            if user.name.startswith('inttest_user_'):
                user.delete()

    def test_allocate(self):
        oca.User.allocate(self.c, 'inttest_user_1', 'inttest_user_1')
        oca.User.allocate(self.c, 'inttest_user_2', 'inttest_user_2')
        oca.User.allocate(self.c, 'inttest_user_3', 'inttest_user_3')
        oca.User.allocate(self.c, 'inttest_user_4', 'inttest_user_4')

    def test_allocate_with_same_name(self):
        with self.assertRaises(OpenNebulaException):
            oca.User.allocate(self.c, 'inttest_user_2', 'inttest_user_2')
            oca.User.allocate(self.c, 'inttest_user_2', 'inttest_user_2')

    def test_change_passwd(self):
        users = oca.UserPool(self.c)
        users.info()
        for user in users:
            if user.name.startswith('inttest_user_'):
                user.change_passwd('new_password')

    def test_chgrp(self):
        users = oca.UserPool(self.c)
        users.info()
        for user in users:
            if user.name.startswith('inttest_user_'):
                user.chgrp(0)

    def test_delete(self):
        users = oca.UserPool(self.c)
        users.info()
        for user in users:
            if user.name.startswith('inttest_user_'):
                user.delete()


if __name__ == "__main__":
    unittest.main()
