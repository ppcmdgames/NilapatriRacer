import cx_Freeze

executables = [cx_Freeze.Executable("src.py")]

cx_Freeze.setup(
    name="Nilapatri Racer",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["car.png"]}},
    executables = executables

    )
