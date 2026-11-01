# Asciiverse patches

sl by Toyoda Masashi, from [mtoyoda/sl](https://github.com/mtoyoda/sl) at
`master` (5.02 plus the 2015–2017 fixes), packaged for the Asciiverse.

**No changes.** The train runs exactly as it always has, including the
part where Ctrl+C doesn't stop it.

## Packaging

- Built by `asciiverse/build.sh`: upstream's one compile line, with this
  platform's curses library. Linux builds are static (Alpine); macOS
  uses the system's ncurses.
- The av archive holds the `sl` binary, LICENSE, README.md, the manual
  page `sl.1` and this file.
