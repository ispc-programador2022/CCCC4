import sys
import os
from cx_Freeze import setup, Executable

files=['assets','scrapper.py']
exe= Executable(script="app.py", base="Win32GUI")

setup(
    name="Cuenta Regresiva Qatar 2022",
    version="1.0",
    description="Aplicacion de cuenta regresiva para el mundial",
    autor="ISpc-CCC4",
    options={'build_exe':{'include_files': files}},
    executables=[exe]
)