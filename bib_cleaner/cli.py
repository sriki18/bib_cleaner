"""Console script for bib_cleaner."""
import argparse
import sys
from .bib_cleaner import tex_to_tags
import os


def main():
    """Console script for bib_cleaner."""
    parser = argparse.ArgumentParser(description="Produce a minimal bib file with only the entries found in your .tex file(s)")
    parser.add_argument("masterfile", type=str, nargs=1, help="master bib file with used and unused citations (.bib)")
    parser.add_argument(
        "-t",
        "--texfiles",
        type=str,
        nargs="+",
        help="content files to select entries from (.tex)",
    )
    args = parser.parse_args()

    print("Arguments: " + str(args.masterfile))
    bib_file = args.masterfile[0]
    if args.texfiles is None:
        all_files = os.listdir()
        tex_files = []
        for a_file in all_files:
            if a_file.endswith(".tex"):
                if not a_file.startswith("__"):
                    tex_files.append(a_file)
        if tex_files == []:
            print("No .tex files found, aborting!")
            return -1
        print(f"Using the following .tex files {tex_files}")
    else:
        tex_files = args.texfiles

    print("Using tex files : ", tex_files)
    print("Output: ", tex_to_tags(tex_files))
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
