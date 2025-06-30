from stats import print_report
import sys

def main():
    print_report(sys.argv[1])

if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()
