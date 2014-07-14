import nose
import sys


def main():
    success = nose.run()
    sys.exit(0) if success else sys.exit(1)

if __name__ == '__main__':

    main()