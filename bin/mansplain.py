import sys
import time
from subprocess import Popen, PIPE


class Mansplainer:
    def __init__(self, output):
        self.output = output
        self.index = 0
        self.interrupt_counter = -1
        self.was_interrupted = False
        self.interrupt_messages = (
            "I wasn't finished yet",
            "I'm still not finished",
            "To be fair you need to have a very high iq to understand {}".format(sys.argv[1])
        )

    def begin_mansplaining(self):
        print('Well basically,\n')
        while self.index < len(self.output):
            try:
                if self.was_interrupted:
                    self.handle_interrupt()
                self.print_characters()
            except KeyboardInterrupt:
                self.was_interrupted = True

    def handle_interrupt(self):
        self.was_interrupted = False
        self.interrupt_counter += 1

        # Catch if the last interruption gets interrupted
        if self.interrupt_counter >= len(self.interrupt_messages):
            sys.exit(0)

        print("\n" + self.interrupt_messages[self.interrupt_counter], end='')

        for i in range(3):
            time.sleep(0.33)
            sys.stdout.write('.')
            sys.stdout.flush()

        time.sleep(1)

        if self.interrupt_counter == len(self.interrupt_messages) - 1:
            sys.exit(0)

        for c in ' As I was saying...\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.06)

    def print_characters(self):
        while self.index < len(self.output):
            c = self.output[self.index]
            sys.stdout.write(c)
            sys.stdout.flush()
            self.index += 1
            time.sleep(0.01)


def mansplain() -> None:
    if len(sys.argv) != 2:
        print("Well basically, this script takes 1 argument from the command line.")
        sys.exit(1)
    man_pipe = Popen(["man", sys.argv[1]], stdout=PIPE)
    mansplainer = Mansplainer(man_pipe.communicate()[0].decode("utf-8"))
    mansplainer.begin_mansplaining()


if __name__ == '__main__':
    mansplain()
