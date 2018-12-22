# Jup2Jek

[![Build Status](https://travis-ci.com/mpewsey/jup2jek.svg?branch=master)](https://travis-ci.com/mpewsey/jup2jek)
[![Documentation Status](https://readthedocs.org/projects/jup2jek/badge/?version=latest)](https://jup2jek.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/mpewsey/jup2jek/branch/master/graph/badge.svg)](https://codecov.io/gh/mpewsey/jup2jek)


## About

The Jup2Jek package is a tool for converting Jupyter notebooks to
markdown for use as posts on Jekyll websites, such those hosted using GitHub
Pages.


## Installation & Usage

To use the package, first install it via pip:

```
pip install git+https://github.com/mpewsey/jup2jek#egg=jup2jek
```

Next, create a configuration file `jup2jek.ini`, with the following sections
and place it in your website project's root directory. Configure the options
as you feel is suited to your particular project.

```
# jup2jek.ini
[JUP2JEK]
# The directory containing your posts and Jupyter notebooks to be converted
posts = _posts
# The directory where assets generated by converted notebooks will be placed
# !!! This path should contain no other files. Otherwise those files
# will be deleted during the conversion process !!!
assets = assets/jupyter
```

From your root directory, run the below command to convert notebooks.

```
jup2jek
```

The method performs the following actions:

1. All notebooks contained in the designated posts folder are found
   and converted to markdown using the jupyter nbconvert command.
2. If the nbconvert command generates an assets folder, the assets
   are moved to the designated site assets folder at the same relative
   path.
3. Asset paths referenced within the markdown files are updated to
   the website path.

Each time you add additional notebooks, you will need to run this command again.

Notebooks should be named in the same format as typical Jekyll posts, i.e.
YYYY-MM-DD-post.ipynb. In addition, the first cell of the Jupyter notebook
should contain YAML front matter, as would be contained in an typical post.
This cell should be formatted as an nbconvert cell so that is it converted
exactly as entered. For example:

```
---
layout: post
title: Post Title
categories: jekyll
date: 2018-03-28
---
```
