"""Main module."""
import re


def tex_to_tags(tex_files):
    """Extract tags from tex files.

    Given a list of tex files, extract the citation tags which are contained in
    ``\cite{}``. Split multiple citations (e.g. ``\cite{A, B}``) into
    individual tags (A, B).

    Parameters
    ----------
    tex_files : List[str]
        List of tex files.

    Returns
    -------
    all_tags : List[str]
        List of individual tags.

    Notes
    -----
    Assume :

    #. Citation tags are a combination of letters, numbers, underscores(_) and hyphens (-).

    #. Multiple citations are separated by commas.

    #. Spaces on either side of the comma are okay.

    #. The following don't appear within citation tag: newlines, accented characters.
    """

    all_csv_tags = []
    for a_file in tex_files:
        with open(a_file, encoding="utf-8") as f:
            contents = f.read()
        all_csv_tags += list(set(re.findall(r"\\cite{[A-Za-z0-9 ,\-_]+}", contents)))
    all_csv_tags = [a_name[6:-1] for a_name in all_csv_tags]

    all_tags = []
    for each_csv in all_csv_tags:
        this_each_csv = each_csv.replace(" ", "")
        if "," not in this_each_csv:
            all_tags += [this_each_csv]
        else:
            all_tags += this_each_csv.split(",")

    return all_tags
