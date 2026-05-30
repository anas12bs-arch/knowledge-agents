---
title: "PyPI: sqlalchemy v2.0.50"
url: "https://pypi.org/project/SQLAlchemy/"
source: "pypi"
category: "skill"
tags: ["pypi", "python", "package", "sqlalchemy"]
date: "2026-05-30T14:32:08Z"
metadata:
  version: "2.0.50"
  package: "sqlalchemy"
---

# PyPI: sqlalchemy v2.0.50

> Source: pypi | Category: skill | 2026-05-30T14:32:08Z

**sqlalchemy** v2.0.50

Database Abstraction Library

SQLAlchemy
==========

|PyPI| |Python| |Downloads|

.. |PyPI| image:: https://img.shields.io/pypi/v/sqlalchemy
    :target: https://pypi.org/project/sqlalchemy
    :alt: PyPI

.. |Python| image:: https://img.shields.io/pypi/pyversions/sqlalchemy
    :target: https://pypi.org/project/sqlalchemy
    :alt: PyPI - Python Version

.. |Downloads| image:: https://static.pepy.tech/badge/sqlalchemy/month
    :target: https://pepy.tech/project/sqlalchemy
    :alt: PyPI - Downloads


The Python SQL Toolkit and Object Relational Mapper

Introduction
-------------

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper
that gives application developers the full power and
flexibility of SQL. SQLAlchemy provides a full suite
of well known enterprise-level persistence patterns,
designed for efficient and high-performing database
access, adapted into a simple and Pythonic domain
language.

Major SQLAlchemy features include:

* An industrial strength ORM, built
  from the core on the identity map, unit of work,
  and data mapper patterns.   These patterns
  allow transparent persistence of objects
  using a declarative configuration system.
  Domain models
  can be constructed and manipulated naturally,
  and changes are synchronized with the
  current transaction automatically.
* A relationally-oriented query system, exposing
  the full range of SQL's capabilities
  explicitly, including joins, subqueries,
  correlation, and most everything else,
  in terms of the object model.
  Writing queries with the ORM uses the same
  techniques of relational composition you use
  when writing SQL.  While you can drop into
  literal SQL at any time, it's virtually never
  needed.
* A comprehensive and flexible system
  of eager loading for related collections and objects.
  Collections are cached within a session,
  and can be loaded on individual access, all
  at once using joins, or by query per collection
  across the full result set.
* A Core SQL construction system and DBAPI
  interaction layer.  The SQLAlchemy Core is
  separate from the ORM and is a full database
  abstraction layer in its own right, and includes
  an extensible Python-based SQL expression
  language, schema metadata, connection pooling,
  type coercion, and custom types.
* All primary and foreign key constraints are
  assumed to be composite and natural.  Surrogate
  integer primary keys are of course still the
  norm, but SQLAlchemy never assumes or hardcodes
  to this model.
* Database introspect
