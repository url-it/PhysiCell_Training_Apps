# library
import os
import shutil
import stat
import sys
import importlib

def go(s_home):
    s_bin = f'{s_home}/tr_microenvironment/bin'
    s_src = f'{s_home}/tr_microenvironment/bin/myproj'
    s_exe = f'{s_home}/tr_microenvironment/bin/myproj'
    s_wd = f'{s_home}/tr_microenvironment'

    # going home
    os.chdir(s_home)

    # install binary
    if not os.path.exists(s_exe):
        shutil.copy(src=s_src, dst =s_exe)
        os.chmod(s_exe, stat.S_IXOTH)
        sys.path.insert(0, s_bin)
    
    os.chdir(s_wd)
    import tr_microenvironment_nanohub
    importlib.reload(tr_microenvironment_nanohub)

    return tr_microenvironment_nanohub.gui