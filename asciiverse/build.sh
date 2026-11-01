#!/bin/sh
# Builds sl. Linux: run inside alpine:3.22 for a fully static binary
# (ncurses linked in); macOS: run on the runner with CC_ARCH set to x86_64
# or arm64, linking the system's ncurses. Other Linux (local testing)
# links ncursesw shared.
#   docker run --rm -v "$PWD":/src -w /src alpine:3.22 sh asciiverse/build.sh
# Leaves ./sl. Upstream's Makefile is one cc line with -lncurses fixed in
# it, so the same line is run here with this platform's libraries.
set -eu
if [ -f /etc/alpine-release ]; then
  apk add --no-cache build-base ncurses-dev ncurses-static >/dev/null
  libs="-static -lncursesw"
elif [ "$(uname)" = Darwin ]; then
  libs="-lncurses"
else
  libs="-lncursesw"
fi
cc="cc${CC_ARCH:+ -arch $CC_ARCH}"
rm -f sl
$cc -O2 -Wall -o sl sl.c $libs
strip sl
