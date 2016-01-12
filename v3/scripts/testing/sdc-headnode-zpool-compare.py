#!/usr/bin/env python
# -*- coding: utf8 -*-

# Checking zpool devices with list of available devices


import re


zpoolList = ['c0t1d0','c0t1d1','c0t1d4','c0t1d6','c0t1d7','c0t2d0','c0t2d1','c0t2d2','c0t2d3','c2t0d0','c2t1d0','c2t2d0','c2t3d0','c2t5d0']

diskList = '''
AVAILABLE DISK SELECTIONS:
       0. c0t0d0 <TOSHIBA-DT01ACA300-R001-2.73TB>
          /pci@0,0/pci8086,65f8@4/pci17d3,1280@0/disk@0,0
       1. c0t0d1 <TOSHIBA-DT01ACA300-R001-2.73TB>
          /pci@0,0/pci8086,65f8@4/pci17d3,1280@0/disk@0,1
       2. c0t0d2 <Seagate-ST3000DM001-1ER1-R001-2.73TB>
          /pci@0,0/pci8086,65f8@4/pci17d3,1280@0/disk@0,2
       3. c0t0d3 <TOSHIBA-DT01ACA300-R001-2.73TB>
          /pci@0,0/pci8086,65f8@4/pci17d3,1280@0/disk@0,3
       4. c0t0d4 <TOSHIBA-DT01ACA300-R001-2.73TB>
          /pci@0,0/pci8086,65f8@4/pci17d3,1280@0/disk@0,4
       5. c0t0d5 <TOSHIBA-DT01ACA300-R001-2.73TB>
          /pci@0,0/pci8086,65f8@4/pci17d3,1280@0/disk@0,5
       6. c0t0d6 <TOSHIBA-DT01ACA300-R001-2.73TB>
          /pci@0,0/pci8086,65f8@4/pci17d3,1280@0/disk@0,6
       7. c0t0d7 <TOSHIBA-DT01ACA300-R001-2.73TB>
          /pci@0,0/pci8086,65f8@4/pci17d3,1280@0/disk@0,7
       8. c0t1d0 <Seagate-ST3000DM001-1ER1-R001-2.73TB>
          /pci@0,0/pci8086,65f8@4/pci17d3,1280@0/disk@1,0
       9. c0t1d1 <Seagate-ST3000DM001-1ER1-R001-2.73TB>
          /pci@0,0/pci8086,65f8@4/pci17d3,1280@0/disk@1,1
      10. c0t1d4 <Seagate-ST2000DL003-9VT1-R001-1.82TB>
          /pci@0,0/pci8086,65f8@4/pci17d3,1280@0/disk@1,4
      11. c0t1d6 <Seagate-ST3250310NS-R001-232.89GB>
          /pci@0,0/pci8086,65f8@4/pci17d3,1280@0/disk@1,6
      12. c0t1d7 <Seagate-ST3250310NS-R001-232.89GB>
          /pci@0,0/pci8086,65f8@4/pci17d3,1280@0/disk@1,7
      13. c0t2d0 <WDC-WD1001FALS-00E3A-R001-931.51GB>
          /pci@0,0/pci8086,65f8@4/pci17d3,1280@0/disk@2,0
      14. c0t2d1 <WDC-WD6400AAKS-00A7B-R001-596.17GB>
          /pci@0,0/pci8086,65f8@4/pci17d3,1280@0/disk@2,1
      15. c0t2d2 <WDC-WD6400AAKS-00A7B-R001-596.17GB>
          /pci@0,0/pci8086,65f8@4/pci17d3,1280@0/disk@2,2
      16. c0t2d3 <WDC-WD1600AAJS-55B4A-R001-149.05GB>
          /pci@0,0/pci8086,65f8@4/pci17d3,1280@0/disk@2,3
      17. c2t0d0 <INTEL-SSDSC2CT060A3-300i-55.90GB>
          /pci@0,0/pci15d9,a480@1f,2/disk@0,0
      18. c2t1d0 <SAMSUNG-MCCOE1HG5MXP-0VBD3-VBC3AD3Q-93.16GB>
          /pci@0,0/pci15d9,a480@1f,2/disk@1,0
      19. c2t2d0 <INTEL-SSDSA2M040G2GC-2CV102M3-37.27GB>
          /pci@0,0/pci15d9,a480@1f,2/disk@2,0
      20. c2t3d0 <INTEL-SSDSA2M160G2GC-2CV102M3-149.05GB>
          /pci@0,0/pci15d9,a480@1f,2/disk@3,0
      21. c2t5d0 <INTEL-SSDSA2M160G2GC-2CV102M3-149.05GB>
          /pci@0,0/pci15d9,a480@1f,2/disk@5,0
'''




def main():
    diskCount = 0
    findCount = 0
    for disk in zpoolList:
        diskCount += 1
        if re.findall(disk, diskList, re.I):
            print(disk, 'exists on server')
            findCount += 1
    if findCount == diskCount:
        print('All', findCount, 'disks were found')
    else:
        print('Only', findCount, 'out of', diskCount, 'disks were found')

if __name__ == "__main__":
    main()