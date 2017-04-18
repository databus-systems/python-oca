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

        self.c = oca.Client(os.environ['OCA_INT_TESTS_ONE_AUTH'], os.environ['OCA_INT_TESTS_ONE_XMLRPC'])

    def tearDown(self):
        print("teardown")
        hosts = oca.HostPool(self.c)
        hosts.info()
        for host in hosts:
            if host.name.startswith('inttest_host_'):
                host.delete()

    def test_allocate(self):
        host = oca.Host.allocate(self.c, 'inttest_host_1', 'im_dummy', 'vmm_dummy', 0)
        host = oca.Host.allocate(self.c, 'inttest_host_2', 'im_dummy', 'vmm_dummy', 0)
        host = oca.Host.allocate(self.c, 'inttest_host_3', 'im_dummy', 'vmm_dummy', 0)
        host = oca.Host.allocate(self.c, 'inttest_host_4', 'im_dummy', 'vmm_dummy', 0)

    # def test_allocate_with_same_name(self):
    #     with self.assertRaises(OpenNebulaException):
    #         host = oca.Host.allocate(self.c, '<HOST><NAME>inttest_host_1</NAME><IM_MAD>im_dummy</IM_MAD<VM_MAD>vmm_dummy</VM_MAD><TM_MAD>tm_dummy</TM_MAD></HOST>')

    # def test_instantiate(self):
    #     host = oca.Host(open(os.path.join(os.path.dirname(oca.__file__), 'tests/fixtures/host.xml')).read(), self.c)
    #     host.allocate()

    def test_delete(self):
        hosts = oca.HostPool(self.c)
        hosts.info()
        for host in hosts:
            if host.name.startswith('inttest'):
                host.delete()

if __name__ == "__main__":
    unittest.main()