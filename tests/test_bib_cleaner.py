#!/usr/bin/env python

"""Tests for `bib_cleaner` package."""

import pytest
from bib_cleaner import bib_cleaner


@pytest.fixture
def tex_contents():
    """TeX file content fixture.
    """
    return ["tests/data/contents.tex"]


@pytest.fixture
def master_bib():
    """Master bib file fixture.
    """
    return ["tests/data/master.bib"]


def test_tex_to_tags(tex_contents):
    """Test tex_to_tags function."""
    found_citations = bib_cleaner.tex_to_tags(tex_contents)
    # base test
    assert "citation1" in found_citations
    # multiple, separated by comma, no space
    assert "citation2" in found_citations
    assert "citation3" in found_citations
    # multiple separated by comma, with space
    assert "citation4" in found_citations
    assert "citation5" in found_citations
    # with hyphen
    assert "ci-tation6" in found_citations
    # with underscore
    assert "ci_tation7" in found_citations
    # multiple separated by comma, with and without space, with hyphen, with underscore
    assert "citation-1" in found_citations
    assert "citation_1" in found_citations
    assert "citation" in found_citations
    # end with underscore
    assert "1citation_" in found_citations


def test_get_minimal_bib(master_bib, tex_contents):
    # Check all used
    all_tags = sorted(bib_cleaner.tex_to_tags(tex_contents))
    _, n_used, n_tot, _ = bib_cleaner.get_minimal_bib(master_bib[0], all_tags)
    assert n_used == 12
    assert n_tot == 12
    # Check only one used
    new_tags = all_tags[:1]
    cont, n_used, n_tot, _ = bib_cleaner.get_minimal_bib(master_bib[0], new_tags)
    assert n_used == len(new_tags)
    assert n_tot == 12
    # Check some used, some not used
    for each in new_tags:
        assert each in cont
    new_tags = all_tags[:6]
    cont, n_used, n_tot, _ = bib_cleaner.get_minimal_bib(master_bib[0], new_tags)
    assert n_used == len(new_tags)
    assert n_tot == 12
    # Verify used tags exist in contents
    for each in new_tags:
        assert each in cont
    # Verify unused tags don't exist in contents
    unused_tags = list(set(all_tags) - set(new_tags))
    for each in unused_tags:
        assert each not in cont
