#
#
#
# Created on Mon Aug 08 2022
# by David J. Clark
# scarletspeedster1729@protonmail.ch
# IOSXE_backup.py
# Copyright (c) 2022
#
import os
from dev import switches
from scrapli import Scrapli
from scrapli.driver.core import IOSXEDriver

for switch in switches:
    s = Scrapli(switch)
    s.open()
    s.get_prompt()
    reply = s.send_command("show run")
    print(reply.result)
    s.close()