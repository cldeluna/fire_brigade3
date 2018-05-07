#!/usr/bin/python -tt
# Project: Dropbox (Indigo Wire Networks)
# Filename: first_brigade
# claudia
# PyCharm
# Python3

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "5/7/18"
__copyright__ = "Copyright (c) 2018 Claudia"
__license__ = "Python"

import argparse
from brigade.core import InitBrigade
from brigade.plugins.tasks.networking import napalm_get
from brigade.plugins.functions.text import print_result


def main():

    # Create instance using default hosts.yaml and groups.yaml
    brg = InitBrigade()

    # print(dir(brg))
    print("Hosts derived from the Inventory file are: \t{}".format(brg.inventory.hosts))
    print("Groups derived from the Inventory file are: \t{}".format(brg.inventory.groups))

    print("\nDecomposing Groups...")
    my_groups = brg.inventory.groups
    # print(type(my_groups))
    # print(my_groups.keys())
    group_keys = list(my_groups.keys())
    print("Group keys = {} of type {} ".format(group_keys, type(group_keys)))
    # print(len(group_keys))
    for i in group_keys:
        print(i)

    print("\nDecomposing Hosts...")
    my_hosts = brg.inventory.hosts
    print("Type of my_hosts is {}".format(type(my_hosts)))
    # print(my_hosts.keys())
    host_keys = list(my_hosts.keys())
    print("Host keys = {} of type {} ".format(host_keys, type(host_keys)))
    # print(len(host_keys))
    for i in host_keys:
        print(i)

    print("\n")

    result = brg.run(
        napalm_get,
        getters=['get_facts'])

    print("\nDecomposing Result Object...")
    # print_result(result)
    # print("What type is result? {}".format(type(result)))
    # print(dir(result))
    # print(result.values)
    # print(dir(result.values))

    x = dict(result)
    for i in x:

        # print(type(i))
        # print(dir(i))
        # print(i)
        li = list(x[i])
        # print(type(li))
        # print(li[0])
        # print(li[0].result['get_facts'].keys())
        li_keys = li[0].result['get_facts'].keys()
        # dict_keys(['uptime', 'vendor', 'os_version', 'serial_number', 'model', 'hostname', 'fqdn', 'interface_list'])
        #
        print("\tDecomposing Result Object for hostname {}...".format(li[0].result['get_facts']['hostname']))
        for k in li_keys:
            print("\t\tKey {} \t : Value = {}".format(k, li[0].result['get_facts'][k]))
        # print(li[0].result['get_facts']['uptime'])
        #
        # print(li[0].result['get_facts']['os_version'])
        print("\n")


    print("Print run results with the print_result module (this is an Ansible like run status)...")
    print_result(result)



# Standard call to the main() function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="First Brigade Script - Discovery",
                                     epilog="Usage: ' python first_brigade.py' ")

    #parser.add_argument('all', help='Execute all ')
    # parser.add_argument('-a', '--all', help='Execute all exercises in week 4 assignment', action='store_true',
    #                     default=False)
    arguments = parser.parse_args()
    main()
