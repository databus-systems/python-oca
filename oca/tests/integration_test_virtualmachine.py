# encoding:utf8
#
# Author: Alin Floare <alin.floare@databus.systems>

import os
import unittest

import oca
from oca.exceptions import OpenNebulaException


@unittest.skipUnless(os.environ.get('OCA_INT_TESTS', False),
                     "Skipping integration tests")
class IntTestVm(unittest.TestCase):
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

    def test_restart(self):
        vms = oca.VirtualMachinePool(self.c)
        vms.info()
        for vm in vms:
            if vm.name.startswith('vm-example'):
                vm.restart()

    def test_resubmit(self):
        vms = oca.VirtualMachinePool(self.c)
        vms.info()
        for vm in vms:
            if vm.name.startswith('vm-example'):
                vm.resubmit()

    def test_release(self):
        vms = oca.VirtualMachinePool(self.c)
        vms.info()
        for vm in vms:
            if vm.name.startswith('vm-example'):
                vm.release()

    def test_stop(self):
        vms = oca.VirtualMachinePool(self.c)
        vms.info()
        for vm in vms:
            if vm.name.startswith('vm-example'):
                vm.stop()

    def test_resume(self):
        vms = oca.VirtualMachinePool(self.c)
        vms.info()
        for vm in vms:
            if vm.name.startswith('vm-example'):
                vm.resume()

    # def test_cancel(self):
    #     vms = oca.VirtualMachinePool(self.c)
    #     vms.info()
    #     for vm in vms:
    #         if vm.name.startswith('vm-example'):
    #             vm.cancel()

    def test_deploy(self):
        vms = oca.VirtualMachinePool(self.c)
        vms.info()
        for vm in vms:
            if vm.name.startswith('vm-example'):
                vm.deploy()

    def test_finalize(self):
        vms = oca.VirtualMachinePool(self.c)
        vms.info()
        for vm in vms:
            if vm.name.startswith('vm-example'):
                vm.finalize()

    def test_live_migrate(self):
        vms = oca.VirtualMachinePool(self.c)
        vms.info()
        for vm in vms:
            if vm.name.startswith('vm-example'):
                vm.live_migrate('http://python-oca:2633/RPC2')

    def test_migrate(self):
        vms = oca.VirtualMachinePool(self.c)
        vms.info()
        for vm in vms:
            if vm.name.startswith('vm-example'):
                vm.migrate('http://python-oca:2633/RPC2')

    def test_hold(self):
        vms = oca.VirtualMachinePool(self.c)
        vms.info()
        for vm in vms:
            if vm.name.startswith('vm-example'):
                vm.hold()

    def test_suspend(self):
        vms = oca.VirtualMachinePool(self.c)
        vms.info()
        for vm in vms:
            if vm.name.startswith('vm-example'):
                vm.suspend()

    def test_shutdown(self):
        vms = oca.VirtualMachinePool(self.c)
        vms.info()
        for vm in vms:
            if vm.name.startswith('vm-example'):
                vm.shutdown()

    # def test_save_disk(self):
    #     vms = oca.VirtualMachinePool(self.c)
    #     vms.info()
    #     for vm in vms:
    #         if vm.name.startswith('vm-example1'):
    #             vm.save_disk(1, '~')

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