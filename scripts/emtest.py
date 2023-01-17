# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import os
from script.python import PlatformEnvirConfigs
from script.python import RootCMakelist
from script.python import Clear
from script.python import CreateData
from script.python import CreateLib
from script.python import CreateAddons


def CompileVersion(option):
    print("CompileVersion__", option)
    RootCMakelist.Build(option)

def ClearFile(option):
    Clear.ClearAll()
    sys.exit(0)

def EnvConfigUpdate(option):
    CreateData.Create(option)
    CreateLib.Create(option)
    CreateAddons.Create(option)

if __name__ == "__main__":
    os.chdir(sys.path[0])
    # 打印当前工作目录
    print(os.getcwd())

    if os.access('./script/config/env_config.ini', os.F_OK):
        PlatformEnvirConfigs.LoadConfig()
    else:
        # 如果当前使用的Python版本号是Python3及以上
        if sys.version_info.major > 2:
            # TX1: 1, PX2: 2, WINDOWS: 3, J6: 4,  LINUX_X86: 5,  QNX: 6,  TDA4: 7,  J3: 8
            PlatformEnvirConfigs.SetConfig(sys.argv[1])
            # C++版本: 0, C版本: 1
            EnvConfigUpdate(str(1))
        else:
            exit("Please Use Python3")
    

    # Buildxx.opt
    CompileVersion(sys.argv[2])