import sys
import time
from subprocess import Popen, PIPE


def _slow_read(output) -> None:
    print("Well basically,")
    print()

    for line in output:
        for c in line:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.01)


def mansplain(command: str) -> None:
    man_pipe = Popen(["man", command], stdout=PIPE)
    _slow_read(man_pipe.communicate()[0].decode("utf-8"))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Well basically, this script takes 1 argument from the command line.")

    mansplain(sys.argv[1])
