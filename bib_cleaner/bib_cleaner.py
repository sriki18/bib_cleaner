"""Main module."""
import re


def tex_to_tags(tex_files):
    """Extract tags from TeX files.

    Given a list of TeX files, extract the citation tags which are contained in
    ``\cite{}``. Split multiple citations (e.g. ``\cite{A, B}``) into
    individual tags (A, B).

    Parameters
    ----------
    tex_files : List[str]
        List of TeX files.

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


def get_minimal_bib(master_bib, all_tags):
    """Get the minimal bib file contents.

    Parameters
    ----------
    master_bib : str
        Name of master bibliography file which has all citations.
    all_tags : List[str]
        List of all tags from the TeX files. (where tags are the names that go
        in `cite{}` commands in TeX files.)

    Returns
    -------
    new_contents : str
        Contents of the cleaned bib file.
    n_used_bibs : int
        Number of bib entries used in TeX files.
    n_total_bibs : int
        Number of bib entries in `master.bib`.
    len_contents : int
        Number of lines in `master.bib`.

    """
    # Variable definitions
    add_flag = 0
    n_total_bibs = 0
    n_used_bibs = 0
    this_entry = ""
    new_lines = []
    new_tags = []

    # Extract contents of master bib file
    with open(master_bib, encoding="utf-8") as f:
        contents = f.read()
    contents = contents.split("\n")

    # Convert raw contents into list of bib entries
    for line in contents:
        # Skip blank lines
        if not line:
            continue
        if line[0] == "@":
            add_flag = 1
            n_total_bibs += 1
            # Optionally use a regex
            # this_tag = re.findall(r"\{[\w-]+\,", line)
            # print(f"This line = {line}, tag = {this_tag[0][1:-1]}")
            start_ind = line.find("{")
            end_ind = line.find(",")
            this_tag = line[start_ind + 1 : end_ind]
        if line[0] == "}":
            add_flag = 0
            if this_tag in all_tags:
                this_entry += "}\n"
                new_lines += this_entry
                new_tags += [this_tag]
                n_used_bibs += 1
            this_entry = ""
        if add_flag:
            this_entry += line + "\n"

    diff = set(all_tags) - set(new_tags)
    if len(diff) > 0:
        print(
            f"You used the following {len(diff)} citations in your TeX files, but they are not in {master_bib}!"
        )
        print(diff)
    else:
        print(f"All citations from TeX files were found in {master_bib}")

    new_contents = "".join(new_lines)
    len_contents = len(contents)
    return (new_contents, n_used_bibs, n_total_bibs, len_contents)
