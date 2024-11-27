# library
import os
import shutil
import stat
import sys
import importlib

# function
def go(s_home):
    # set variables
    s_bin = f'{s_home}/tr_Volume/bin'
    s_src = f'{s_home}/tr_Volume/bin/myproj_colab'
    s_exe = f'{s_home}/tr_Volume/bin/myproj'
    s_wd = f'{s_home}/tr_Volume'

    # going home
    os.chdir(s_home)

    # install binary
    if not os.path.exists(s_exe):
        shutil.copy(src=s_src, dst=s_exe)
        os.chmod(s_exe, stat.S_IXOTH)
        sys.path.insert(0, s_bin)

    # load module binary and return gui
    os.chdir(s_wd)
    import tr_Volume
    importlib.reload(tr_Volume)

    # output
    return tr_Volume.gui
