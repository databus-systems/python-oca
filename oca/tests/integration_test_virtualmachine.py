# vim:  set fileencoding=utf8
# encoding:utf8
#
# Author: Matthias Schmitz <matthias@sigxcpu.org>

import os
import unittest

import oca
from oca.exceptions import OpenNebulaException


@unittest.skipUnless(os.environ.get('OCA_INT_TESTS', False),
                     "Skipping integration tests")
class IntTestTemplate(unittest.TestCase):
    def setUp(self):
        try:
            del os.environ["ONE_AUTH"]
        except KeyError:
            pass

        self.c = oca.Client(os.environ['OCA_INT_TESTS_ONE_AUTH'], os.environ['OCA_INT_TESTS_ONE_XMLRPC'])

    def tearDown(self):
        print("teardown")
        vmp = oca.VirtualMachinePool(self.c)
        vmp.info()
        for vm in vmp:
            if vm.name.startswith('inttest_vm_'):
                vm.delete()

    def test_allocate(self):
        vm = oca.VirtualMachine.allocate(self.c, '<VM><NAME>vm-example1</NAME><MEMORY>512</MEMORY><CPU>1</CPU><TEMPLATE/></VM>')
        vm = oca.VirtualMachine.allocate(self.c, '<VM><NAME>vm-example2</NAME><MEMORY>512</MEMORY><CPU>1</CPU><TEMPLATE/></VM>')
        vm = oca.VirtualMachine.allocate(self.c, '<VM><NAME>vm-example3</NAME><MEMORY>512</MEMORY><CPU>1</CPU><TEMPLATE/></VM>')
        vm = oca.VirtualMachine.allocate(self.c, '<VM><NAME>vm-example4</NAME><MEMORY>512</MEMORY><CPU>1</CPU><TEMPLATE/></VM>')

    def test_allocate_with_same_name(self):
        with self.assertRaises(OpenNebulaException):
            vm = oca.VirtualMachine.allocate(self.c, '<VM><NAME>vm-example1</NAME><TEMPLATE/></VM>')

    # def test_update(self):
    #     oca.VmTemplate.allocate(self.c, '<VMTEMPLATE><NAME>inttest_update01</NAME><TEMPLATE/></VMTEMPLATE>')
    #     tp = oca.VmTemplatePool(self.c)
    #     tp.info()
    #     templ = tp.get_by_name('inttest_update01')
    #     templ.update('MEMORY=1024 CPU=2')

    def test_delete(self):
        vms = oca.VirtualMachinePool(self.c)
        vms.info()
        for vm in vms:
            if vm.name.startswith('vm-example'):
                vm.delete()

    # def test_instantiate(self):
    #     templ = oca.VmTemplate.allocate(self.c,
    #                                     '<VMTEMPLATE><NAME>inttest_instantiate_me01</NAME><MEMORY>1234</MEMORY><CPU>2</CPU></VMTEMPLATE>')
    #     tp = oca.VmTemplatePool(self.c)
    #     tp.info()
    #     templ = tp.get_by_name('inttest_instantiate_me01')
    #     templ.instantiate('inttest_vm_instantiate_me01')
    #     vmpool = oca.VirtualMachinePool(self.c)
    #     vmpool.info()
    #     vm = vmpool.get_by_name('inttest_vm_instantiate_me01')
    #     self.assertEqual(vm.name, 'inttest_vm_instantiate_me01')

if __name__ == "__main__":
    unittest.main()