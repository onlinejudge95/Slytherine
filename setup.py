__author__ = 'capt_MAKO'
import cx_Freeze

executables = [cx_Freeze.Executable("Slytherine.py")]
cx_Freeze.setup(name='Slytherine', options={"build_exe":{"packages":["pygame"], "include_files":["apple.png", "snake_head.png"]}}, description='Slytherine', executables=executables)
