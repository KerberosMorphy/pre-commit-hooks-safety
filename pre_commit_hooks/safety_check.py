from __future__ import print_function
import sys
from safety.cli import check


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    try:
        check.main(['--full-report'] + sum(([arg] if arg.startswith('-') else ['--file', arg] for arg in argv), []))
        return 0
    except SystemExit as error:
        if error.code == 0:
            return 0
        return 1


if __name__ == '__main__':
    sys.exit(main())
