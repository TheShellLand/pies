#!/usr/bin/env python
# -*- coding: utf8 -*-

'''
# Found from
xml = xml.dom.minidom.parse(xml_fname) # or xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = xml.toprettyxml()
'''

import os
import sys
import xml.dom.minidom
from itertools import groupby



def xmltableprint():
    # See http://stackoverflow.com/questions/8528825/printing-data-to-list-styled-table-from-xml-in-python
    servers = []
    for AllConfigurations in yXML.getElementsByTagName('AllConfigurations'):
        for DeployConfigurations in AllConfigurations.getElementsByTagName('DeployConfigurations'):
            for Servers in DeployConfigurations.getElementsByTagName('Servers'):
                for Group in Servers.getElementsByTagName('Group'):
                    for GApp in Group.getElementsByTagName('GApp'):
                        for Server in Group.getElementsByTagName('Server'):
                            servers.append((Server.getAttribute('name'),
                                    Group.getAttribute('name'),
                                    Server.getAttribute('ip'),
                                    GApp.getAttribute('type')))

    def line(machine, group, ip, services):
        return " | ".join([machine.ljust(8), group.ljust(20), ip.ljust(15), services])

    print (line("Machine", "Group", "IP", "Services"))
    for server, services in groupby(sorted(servers), lambda server: server[0:3]):
        print (line("- " + server[0], server[1], server[2],
                ", ".join(service[3] for service in set(services))))



if len(sys.argv) > 1:
    uglyf = sys.argv[1]
    pretty = xml.dom.minidom.parse(uglyf)
    xmltableprint()
else:
    help = 'Usage: ' + os.path.basename(__file__) + ' <input file>'
    print(help)
