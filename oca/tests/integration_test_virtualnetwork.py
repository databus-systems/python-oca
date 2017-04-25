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
class IntTestVirtualNetwork(unittest.TestCase):
    def setUp(self):
        try:
            del os.environ["ONE_AUTH"]
        except KeyError:
            pass

        self.c = oca.Client(os.environ['OCA_INT_TESTS_ONE_AUTH'],
                            os.environ['OCA_INT_TESTS_ONE_XMLRPC'])

    def tearDown(self):
        print("teardown")
        vns = oca.VirtualNetworkPool(self.c)
        vns.info()
        for vn in vns:
            if vn.name.startswith('inttest'):
                vn.delete()

    def test_allocate(self):
        oca.VirtualNetwork.allocate(
            self.c, '<VNET><NAME>inttest01</NAME><VN_MAD>fw</VN_MAD>\
            <BRIDGE>virbr0</BRIDGE><TEMPLATE/></VNET>')

        oca.VirtualNetwork.allocate(
            self.c, '<VNET><NAME>inttest02</NAME><VN_MAD>fw</VN_MAD>\
            <BRIDGE>virbr0</BRIDGE><TEMPLATE/></VNET>')

        oca.VirtualNetwork.allocate(
            self.c, '<VNET><NAME>inttest03</NAME><VN_MAD>fw</VN_MAD>\
            <BRIDGE>virbr0</BRIDGE><TEMPLATE/></VNET>')

        oca.VirtualNetwork.allocate(
            self.c, '<VNET><NAME>inttest04</NAME><VN_MAD>fw</VN_MAD>\
            <BRIDGE>virbr0</BRIDGE><TEMPLATE/></VNET>')

    def test_allocate_with_same_name(self):
        with self.assertRaises(OpenNebulaException):
            oca.VirtualNetwork.allocate(
                self.c, '<VNET><NAME>inttest04</NAME><VN_MAD>fw</VN_MAD>\
                <BRIDGE>virbr0</BRIDGE><TEMPLATE/></VNET>')

            oca.VirtualNetwork.allocate(
                self.c, '<VNET><NAME>inttest04</NAME><VN_MAD>fw</VN_MAD>\
                <BRIDGE>virbr0</BRIDGE><TEMPLATE/></VNET>')

    def test_chown(self):
        vns = oca.UserPool(self.c)
        vns.info()
        for vn in vns:
            if vn.name.startswith('inttest'):
                vn.chown(0, -1)

    def test_unpublish(self):
        vns = oca.UserPool(self.c)
        vns.info()
        for vn in vns:
            if vn.name.startswith('inttest'):
                vn.unpublish(0, -1)

    def test_publish(self):
        vns = oca.UserPool(self.c)
        vns.info()
        for vn in vns:
            if vn.name.startswith('inttest'):
                vn.publish(0, -1)

    def test_delete(self):
        vns = oca.UserPool(self.c)
        vns.info()
        for vn in vns:
            if vn.name.startswith('inttest'):
                vn.delete()


if __name__ == "__main__":
    unittest.main()
