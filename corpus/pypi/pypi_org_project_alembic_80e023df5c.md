---
title: "PyPI: alembic v1.18.4"
url: "https://pypi.org/project/alembic/"
source: "pypi"
category: "skill"
tags: ["pypi", "python", "package", "alembic"]
date: "2026-05-30T14:32:08Z"
metadata:
  version: "1.18.4"
  package: "alembic"
---

# PyPI: alembic v1.18.4

> Source: pypi | Category: skill | 2026-05-30T14:32:08Z

**alembic** v1.18.4

A database migration tool for SQLAlchemy.

Alembic is a database migrations tool written by the author
of `SQLAlchemy <http://www.sqlalchemy.org>`_.  A migrations tool
offers the following functionality:

* Can emit ALTER statements to a database in order to change
  the structure of tables and other constructs
* Provides a system whereby "migration scripts" may be constructed;
  each script indicates a particular series of steps that can "upgrade" a
  target database to a new version, and optionally a series of steps that can
  "downgrade" similarly, doing the same steps in reverse.
* Allows the scripts to execute in some sequential manner.

The goals of Alembic are:

* Very open ended and transparent configuration and operation.   A new
  Alembic environment is generated from a set of templates which is selected
  among a set of options when setup first occurs. The templates then deposit a
  series of scripts that define fully how database connectivity is established
  and how migration scripts are invoked; the migration scripts themselves are
  generated from a template within that series of scripts. The scripts can
  then be further customized to define exactly how databases will be
  interacted with and what structure new migration files should take.
* Full support for transactional DDL.   The default scripts ensure that all
  migrations occur within a transaction - for those databases which support
  this (Postgresql, Microsoft SQL Server), migrations can be tested with no
  need to manually undo changes upon failure.
* Minimalist script construction.  Basic operations like renaming
  tables/columns, adding/removing columns, changing column attributes can be
  performed through one line commands like alter_column(), rename_table(),
  add_constraint(). There is no need to recreate full SQLAlchemy Table
  structures for simple operations like these - the functions themselves
  generate minimalist schema structures behind the scenes to achieve the given
  DDL sequence.
* "auto generation" of migrations. While real world migrations are far more
  complex than what can be automatically determined, Alembic can still
  eliminate the initial grunt work in generating new migration directives
  from an altered schema.  The ``--autogenerate`` feature will inspect the
  current status of a database using SQLAlchemy's schema inspection
  capabilities, compare it to the current state of the database model as
  specified in Python, and generate a series of "candidate" migrations,
  rendering them into a new
