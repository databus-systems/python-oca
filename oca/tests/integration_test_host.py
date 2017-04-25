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
class IntTestHost(unittest.TestCase):
    def setUp(self):
        try:
            del os.environ["ONE_AUTH"]
        except KeyError:
            pass

        self.c = oca.Client(os.environ['OCA_INT_TESTS_ONE_AUTH'],
                            os.environ['OCA_INT_TESTS_ONE_XMLRPC'])

    def tearDown(self):
        print("teardown")
        hosts = oca.HostPool(self.c)
        hosts.info()
        for host in hosts:
            if host.name.startswith('inttest_host_'):
                host.delete()

    def test_allocate(self):
        oca.Host.allocate(
            self.c, 'inttest_host_1', 'im_dummy', 'vmm_dummy', 0)

        oca.Host.allocate(
            self.c, 'inttest_host_2', 'im_dummy', 'vmm_dummy', 0)

        oca.Host.allocate(
            self.c, 'inttest_host_3', 'im_dummy', 'vmm_dummy', 0)

        oca.Host.allocate(
            self.c, 'inttest_host_4', 'im_dummy', 'vmm_dummy', 0)

    def test_allocate_with_same_name(self):
        with self.assertRaises(OpenNebulaException):
            oca.Host.allocate(
                self.c, 'inttest_host_4', 'im_dummy', 'vmm_dummy', 0)

    def test_update(self):
        hosts = oca.HostPool(self.c)
        hosts.info()
        for host in hosts:
            if host.name.startswith('inttest'):
                host.update(open(os.path.join(os.path.dirname(oca.__file__),
                            'tests/fixtures/host.xml')).read())

    def test_enable(self):
        hosts = oca.HostPool(self.c)
        hosts.info()
        for host in hosts:
            if host.name.startswith('inttest'):
                host.enable()

    def test_disable(self):
        hosts = oca.HostPool(self.c)
        hosts.info()
        for host in hosts:
            if host.name.startswith('inttest'):
                host.disable()

    def test_delete(self):
        hosts = oca.HostPool(self.c)
        hosts.info()
        for host in hosts:
            if host.name.startswith('inttest'):
                host.delete()


if __name__ == "__main__":
    unittest.main()
