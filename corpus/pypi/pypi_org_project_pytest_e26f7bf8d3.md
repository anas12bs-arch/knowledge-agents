---
title: "PyPI: pytest v9.0.3"
url: "https://pypi.org/project/pytest/"
source: "pypi"
category: "skill"
tags: ["pypi", "python", "package", "pytest"]
date: "2026-05-30T14:32:10Z"
metadata:
  version: "9.0.3"
  package: "pytest"
---

# PyPI: pytest v9.0.3

> Source: pypi | Category: skill | 2026-05-30T14:32:10Z

**pytest** v9.0.3

pytest: simple powerful testing with Python

.. image:: https://github.com/pytest-dev/pytest/raw/main/doc/en/img/pytest_logo_curves.svg
   :target: https://docs.pytest.org/en/stable/
   :align: center
   :height: 200
   :alt: pytest


------

.. image:: https://img.shields.io/pypi/v/pytest.svg
    :target: https://pypi.org/project/pytest/

.. image:: https://img.shields.io/conda/vn/conda-forge/pytest.svg
    :target: https://anaconda.org/conda-forge/pytest

.. image:: https://img.shields.io/pypi/pyversions/pytest.svg
    :target: https://pypi.org/project/pytest/

.. image:: https://codecov.io/gh/pytest-dev/pytest/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/pytest-dev/pytest
    :alt: Code coverage Status

.. image:: https://github.com/pytest-dev/pytest/actions/workflows/test.yml/badge.svg
    :target: https://github.com/pytest-dev/pytest/actions?query=workflow%3Atest

.. image:: https://results.pre-commit.ci/badge/github/pytest-dev/pytest/main.svg
   :target: https://results.pre-commit.ci/latest/github/pytest-dev/pytest/main
   :alt: pre-commit.ci status

.. image:: https://www.codetriage.com/pytest-dev/pytest/badges/users.svg
    :target: https://www.codetriage.com/pytest-dev/pytest

.. image:: https://readthedocs.org/projects/pytest/badge/?version=latest
    :target: https://pytest.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/Discord-pytest--dev-blue
    :target: https://discord.com/invite/pytest-dev
    :alt: Discord

.. image:: https://img.shields.io/badge/Libera%20chat-%23pytest-orange
    :target: https://web.libera.chat/#pytest
    :alt: Libera chat


The ``pytest`` framework makes it easy to write small tests, yet
scales to support complex functional testing for applications and libraries.

An example of a simple test:

.. code-block:: python

    # content of test_sample.py
    def inc(x):
        return x + 1


    def test_answer():
        assert inc(3) == 5


To execute it::

    $ pytest
    ============================= test session starts =============================
    collected 1 items

    test_sample.py F

    ================================== FAILURES ===================================
    _________________________________ test_answer _________________________________

        def test_answer():
    >       assert inc(3) == 5
    E       assert 4 == 5
    E        +  where 4 = inc(3)

    test_sample.py:5: AssertionError
    ========================== 1 failed in 0.04 seconds ================
