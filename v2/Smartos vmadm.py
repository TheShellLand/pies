#!/usr/bin/env python2.7
from subprocess import check_output

def list_vms(state):
  vlr = check_output([
    "vmadm",
    "list",
    "-p",
    "-o",
    "alias,max_physical_memory,nics.0.ip,uuid",
    "state=%s" % state
  ])

  vlr = [vm for vm in vlr.split("\n") if len(vm)]
  if len(vlr):
    print state.capitalize().center(80)
    print "=" * 80
  for vm in vlr:
    vm = vm.split(":")
    print "%s%s" % (
      vm[0],
      vm[3].rjust(80 - len(vm[0]))
    )
    print "%s%s" % (
      "IP: %s" % vm[2],
      ("Memory: %s MB" % vm[1]).rjust(80 - 4 - len(vm[2]))
    )
    print

if __name__ == "__main__":
  list_vms("running")
  list_vms("stopped")