# library
import os
import shutil
import stat
import sys
import importlib

# function
def go(s_home):
    # set variables
    s_bin = f'{s_home}/Death_Models_Training/bin'
    s_src = f'{s_home}/Death_Models_Training/bin/myproj_colab'
    s_exe = f'{s_home}/Death_Models_Training/bin/myproj'
    s_wd = f'{s_home}/Death_Models_Training'

    # going home
    os.chdir(s_home)

    # install binary
    if not os.path.exists(s_exe):
        shutil.copy(src=s_src, dst=s_exe)
        os.chmod(s_exe, stat.S_IXOTH)
        sys.path.insert(0, s_bin)

    # load module binary and return gui
    os.chdir(s_wd)
    import Death_Models_Training
    importlib.reload(Death_Models_Training)

    # output
    return Death_Models_Training.gui
