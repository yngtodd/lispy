"""Command line interface for lispy."""
import argh


def repl() -> None:
    r"""Say hello, lispy"""
    print(f'Hello, world!')


def main():
    parser = argh.ArghParser()
    parser.add_commands([repl])
    parser.dispatch()


if __name__=='__main__':
    main()
