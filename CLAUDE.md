# sl (Asciiverse packaging)

sl, Toyoda Masashi's steam locomotive (1993), packaged for the Asciiverse
catalog. No source changes, and keep it that way: ignoring Ctrl+C is the
joke, not a bug.

- Branch `asciiverse` on upstream `master` (5.02 + 2015–2017 fixes);
  `upstream` is github.com/mtoyoda/sl, quiet since 2017.
- Build: `sh asciiverse/build.sh`, then `sh asciiverse/stage.sh`; run
  `stage/sl` (options -a -F -l -c).
- Preview: `python3 asciiverse/record-preview.py` runs all five trains
  (~37 s at 100 columns).
