import sys
import os
from cx_Freeze import setup, Executable

build_exe_options = {'packages': [], 'excludes' : []}
base = 'Win32GUI'
exe = Executable(
    script = 'algoritmocongrafica.py',
    initScript = None,
    base = 'Win32GUI',
    targetName = 'MedicaidAid.exe',
    compress = True,
    appendScriptToExe = True,
    appendScriptToLibrary = True,
    icon = None
)

setup( name = 'MedicaidAid', 
        version = '0.85',
        description = 'MedicaidAid Software',
        options = {'build_exe': build_exe_options},
        executables = [Executable('algoritmocongrafica.py', base = base)])