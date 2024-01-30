mport sys

def main(argv):
    if len(argv) > 1:
        print(f"Hello {argv[1]}")
    else:
        print("Usage: python hello.py [arg0]")

if __name_ == "__main__":
    main(sys.argv[1:])
