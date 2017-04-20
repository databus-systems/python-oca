##############################################
OCA - OpenNebula Cloud Api
##############################################

:Version: 5.20.0
:TravisCI Status:
  .. image:: https://travis-ci.org/python-oca/python-oca.svg
     :target: https://travis-ci.org/python-oca/python-oca

About
-----

Bindings for XMLRPC OpenNebula Cloud API

Documentation
-------------
See http://python-oca.github.io/python-oca/index.html and https://docs.opennebula.org/5.2/integration/system_interfaces/api.html

All `allocate` functions are implemented as static methods.

Examples
--------

Show all running virtual machines::

   client = oca.Client('user:password', 'http://12.12.12.12:2633/RPC2')
   vm_pool = oca.VirtualMachinePool(client)
   vm_pool.info()
   
   for vm in vm_pool:
       ip_list = ', '.join(v.ip for v in vm.template.nics)
       print("{} {} {} (memory: {} MB)".format(vm.name, ip_list, vm.str_state, vm.template.memory))

License
-------

OCA is under Apache Software License

Authors
-------

See AUTHORS file
