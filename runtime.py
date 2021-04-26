#!/usr/bin/env python3

"""Execute command and display run time."""

import datetime
import os
import pipes
import subprocess
import sys
import time


def PrintCommand(argv):
  sys.stderr.write('< %s\n' % os.getcwd())
  sys.stderr.write('>')
  length = 0
  first = True
  for q in argv:
    out = pipes.quote(q)
    if not first and length + len(out) > 100:
      sys.stderr.write(' \\\n ')
      length = 0
    sys.stderr.write(' %s' % out)
    length += 1 + len(out)
    first = False
  sys.stderr.write('\n\n')


def main(argv):
  argv.pop(0)
  if not argv:
    return 0

  start_time = time.time()
  sys.stderr.write('----------------------------------------\n')
  sys.stderr.write(' Start Time: %s\n' % time.strftime(
      '%Y/%m/%d %H:%M:%S', time.localtime(start_time)))
  sys.stderr.write('----------------------------------------\n')
  sys.stderr.write('\n')

  PrintCommand(argv)

  exit_status = 1
  try:
    exit_status = subprocess.call(['/usr/bin/env'] + argv)
  except KeyboardInterrupt:
    sys.stderr.write('\n')
  end_time = time.time()
  delta = datetime.timedelta(microseconds=(end_time - start_time)*1e6)

  sys.stderr.write('\n')
  sys.stderr.write('----------------------------------------\n')

  if exit_status:
    sys.stderr.write('        FAILED! FAILED! FAILED!\n')
    sys.stderr.write('----------------------------------------\n')

  sys.stderr.write(' End Time: %s\n' % time.strftime(
      '%Y/%m/%d %H:%M:%S', time.localtime(end_time)))
  sys.stderr.write(' Elapsed Time: %s\n' % delta)
  sys.stderr.write('----------------------------------------\n')

  return exit_status

if __name__ == '__main__':
  sys.exit(main(sys.argv))
