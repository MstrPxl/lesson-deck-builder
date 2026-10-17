#!/usr/bin/env python3
# quiz_walk_phone.py DECK [OUTDIR]  — the rulebook's quiz walk in a 390x844 touch context      (deck-tools 1.4)
# Since 1.4 this is a thin wrapper around quiz_walk_x.py --phone, which also walks the newer quiz kinds.
import sys, os, runpy
if len(sys.argv) < 2: print('usage: quiz_walk_phone.py DECK [OUTDIR]'); sys.exit(2)
sys.argv = ['quiz_walk_x.py', sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'quiz-shots-phone', '--phone']
runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'quiz_walk_x.py'), run_name='__main__')
