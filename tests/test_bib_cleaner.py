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
    assert "citation1" in found_citations
    assert "citation2" in found_citations
    assert "citation3" in found_citations
    assert "citation4" in found_citations
    assert "citation5" in found_citations
    assert "ci-tation6" in found_citations
    assert "ci_tation7" in found_citations
    assert "citation-1" in found_citations
    assert "citation_1" in found_citations
    assert "1citation_" in found_citations
    assert "citation" in found_citations
