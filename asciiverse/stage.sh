#!/bin/sh
# Lays out the av archive in stage/: sl has no data files, so the binary
# sits at the top with its licence, readme, manual page and PATCHES.md.
set -eu
rm -rf stage && mkdir -p stage
cp sl stage/sl
cp LICENSE README.md sl.1 PATCHES.md stage/
