from platformio.project.helpers import get_project_dir
from os.path import join, isfile, relpath

Import("env")

nimble_dir = join(env["PROJECT_DIR"], ".pio", "libdeps", env["PIOENV"], "NimBLE-Arduino")

orig_file = join(nimble_dir, "src", "nimble", "nimble", "host", "src", "ble_gap.c")
patch_file = join("patches", "ble_gap.patch")

print(orig_file, patch_file)
assert isfile(orig_file) and isfile(patch_file)

env.Execute("/cygwin64/bin/patch.exe  --forward -b -p0 %s %s" % (orig_file, patch_file))
    # env.Execute("touch " + patchflag_path)

 
