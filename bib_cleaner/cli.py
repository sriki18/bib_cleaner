"""Console script for bib_cleaner."""
import argparse
import sys
from .bib_cleaner import tex_to_tags, get_minimal_bib
import os


def main():
    """Console script for bib_cleaner."""
    parser = argparse.ArgumentParser(
        description="Produce a minimal bib file with only the entries found in your .tex file(s)"
    )
    parser.add_argument(
        "masterfile",
        type=str,
        nargs=1,
        help="master bib file with used and unused citations (.bib)",
    )
    parser.add_argument(
        "-t",
        "--texfiles",
        type=str,
        nargs="+",
        help="content files to select entries from (.tex)",
    )
    parser.add_argument(
        "-o",
        "--outputbib",
        type=str,
        nargs=1,
        help="output file name with extension",
        default=["new.bib"],
    )
    # parser.add_argument('--version', action='version', version='%(prog)s')
    args = parser.parse_args()

    bib_file = args.masterfile[0]
    if args.texfiles is None:
        all_files = os.listdir()
        tex_files = []
        for a_file in all_files:
            if a_file.endswith(".tex"):
                if not a_file.startswith("__"):
                    tex_files.append(a_file)
        if tex_files == []:
            print("No TeX files found, aborting!")
            return -1
        print(f"Using TeX files {tex_files}")
    else:
        tex_files = args.texfiles

    all_tags = tex_to_tags(tex_files=tex_files)
    new_contents, used_bibs, total_bibs, len_contents = get_minimal_bib(
        master_bib=bib_file, all_tags=all_tags
    )
    with open(args.outputbib[0], "w", encoding="utf-8") as f:
        f.write(new_contents)

    with open(args.outputbib[0]) as f:
        new_contents_verify = f.read()
    new_lines_verify = new_contents_verify.split("\n")
    delta = len_contents - len(new_lines_verify)
    pct_change = delta / len_contents * 100
    delta_citations = total_bibs - used_bibs
    pct_change_citations = delta_citations / total_bibs * 100
    print(
        f"Removed {delta} lines ({delta_citations} citations) with {pct_change:.2f}%  ({pct_change_citations:.2f}%) reduction!"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
