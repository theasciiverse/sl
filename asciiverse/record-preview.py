#!/usr/bin/env python3
"""Records asciiverse/sl.cast, sl's catalog preview, at 100x30
(hub/RECORDING.md): the five trains one after another, about 7.5 s each
at 100 columns: plain, -a (an accident: people cry for help), -F (it
flies), -l (a little one) and -c (the C51). sl runs in tmux and
asciinema 3 records inside it.
Usage, from the repo root after asciiverse/build.sh and stage.sh:
    python3 asciiverse/record-preview.py"""
import subprocess, time

s = "sl-preview"
trains = "./stage/sl; ./stage/sl -a; ./stage/sl -F; ./stage/sl -l; ./stage/sl -c"
subprocess.run(["tmux", "kill-session", "-t", s], stderr=subprocess.DEVNULL)
subprocess.run(["tmux", "new-session", "-d", "-s", s, "-x", "100", "-y", "30",
    "TERM=xterm-256color COLORTERM=truecolor LANG=C.UTF-8 "
    "asciinema rec --overwrite -q -i 2 --window-size 100x30 "
    "--capture-env TERM,COLORTERM,LANG "
    f"-c 'sh -c \"{trains}\"' asciiverse/sl.cast"])
while subprocess.run(["tmux", "has-session", "-t", s],
                     stderr=subprocess.DEVNULL).returncode == 0:
    time.sleep(0.5)
