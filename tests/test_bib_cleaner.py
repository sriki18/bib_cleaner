#!/usr/bin/env python

"""Tests for `bib_cleaner` package."""

import pytest


from bib_cleaner import bib_cleaner


@pytest.fixture
def tex_contents():
    """TeX file content fixture.
    """
    return ["tests/data/contents.tex"]


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
    assert "citation" in found_citations
