from cx_Freeze import setup, Executable

executables = [
    Executable(script="main.py", icon="icone.ico", base="Win32GUI")
]


buildOptions = dict(
    includes=[],
    include_files=[ "icone.ico"]
)

setup(
    name="trieur PDF",
    version="0.1",
    description="Trieur PDF",
    author="BAYCHE Baptiste",
    options=dict(build_exe=buildOptions),
    executables=executables
)