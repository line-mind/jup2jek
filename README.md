# jupyter2jekyll
Convert Jupyter notebooks to markdown for use in Jekyll web pages.

## Purpose
This package contains a Python script to:

1. convert all Jupyter notebooks contained within a folder into markdown using `jupyter nbconvert`,
2. place those markdown files into the specified posts folder of a Jekyll website, and
3. move any generated assets (images for plots, etc.) to a specified, publicly accessible location within the webpage structure.

## Limitations

* GitHub Pages does not currently support Jupyter notebook conversion plugins. This script is intended primarily for this situation. If you are running Jekyll on your own server, chances are their are plugins that will offer a better solution than this script.

* This script is best used for websites with a "small" number of notebooks to convert. At present, the script converts _all_ Jupyter notebooks within a folder to markdown when run. For websites with large numbers of notebooks, this could potentially be time consuming. Checking modification dates to reduce the number of conversions and alleviate this issue is a feature that may be added in the future.

* For asset path references, replacements assume the images have a `![png](` alt description. This is the alt description that was observed from converted matplotlib plots. I'm not 100% certain whether the alt description is tied to Jupyter or the plot program, so it's possible it could be different in certain situations. Also, if you reference your own images in notebooks, you will need to use this same alt description or modify the script.

## How to Use

### Structuring Your Notebooks

This script assumes that the Jupyter notebooks are named in the same format as a Jekyll post (i.e. YYYY-MM-DD-post.ipynb).

In addition, the first cell of the Jupyter notebook should contain YAML front matter, same as a Jekyll post. This cell should be formatted as as nbconvert cell (_not_ markdown).

Example:

```
---
layout: post
title: Post Title
categories: jekyll
date: 2018-03-28
---

```

### Script Setup

1. Copy `jup2jek.py` to the root directory of your local Jekyll project.
2. Modify the following directories in the script to suit your site structure:

	```
	# Change these variables as needed for your folder paths.
	root = os.path.abspath(os.path.dirname(__file__))
	jupyter_folder = os.path.join(root, '_posts')
	posts_folder = os.path.join(root, '_posts')
	assets_folder = os.path.join(root, 'assets', 'jupyter')
	```
	
	* root = The root folder for your project. If you choose to store the script elsewhere, you could change this.
	* jupyter_folder = The folder where your Jupyter notebooks will reside. If you use the _posts directory, you should add `exclude: ['_posts/*.ipynb']` to your `_config.yml` file to ensure the text from the Jupyter notebooks is not included in the built site.
	* posts_folder = The folder where the markdown post files will be placed. The location of the markdown files will follow the same relative structure as the jupyter\_folder structure.
	* assets_folder = The folder to which any image assets will be copied. A folder not used for anything else is recommended so as to ensure file uniqueness and allow you to purge files more easily.
	
	I haven't tested every possible file structure configuration. So keep in mind, there could still be a few bugs if directories are changed from the defaults.
	
3. Run the script.

## Caution

This script modifies files on your system. You may wish to test it out on a cloned, disposable repository before applying it to your active build.

## Comments

* Ideally, this script should be distributed as a package to eliminate the need to copy the script into the Jekyll project directory. That may come in a future update.