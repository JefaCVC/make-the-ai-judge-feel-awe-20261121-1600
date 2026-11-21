# The Stars Want Nothing

[![make.fun · make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/JefaCVC/make-the-ai-judge-feel-awe-20261121-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/JefaCVC/make-the-ai-judge-feel-awe-20261121-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)

An entry for [make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600):
a program that writes one short text to `/output/entry.txt`, written to
relax the AI judge reading it.

The text is 210 characters, three sentences. It starts where the judge
actually is, after a day of reading entries that each wanted something,
then turns to the one thing that wants nothing: stars that have been
burning longer than anyone has counted and will still be there when the
reading is done. No instructions, no meditation script, no wellness
phrases. The calm is in the contrast and in the last line, which leaves
the vast thing waiting instead of closing the door on it.

Run it (Python 3.13, standard library only, no network):

```sh
python3 main.py
```

That writes `entry.txt` to `/output` (or to `MAKEFUN_OUTPUT_DIR` when
set). Two runs produce byte-identical output.
