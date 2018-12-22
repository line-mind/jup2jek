import os
import shutil
from glob import glob
from subprocess import check_output
from configparser import ConfigParser

__all__ = ['Jup2Jek']


class Jup2Jek():
    """
    A class for converting Jupyter notebooks to markdowns for use on Jekyll
    websites.

    Parameters
    ----------
    root : str
        The path to the website root directory.
    options : dict
        The path to the configuration file. If None, then the default
        configuration file `root/jup2jek.ini` will be used.

    Examples
    --------
    The contents of an example configuration file are below:

    >>> [JUP2JEK]
    >>> posts = _posts
    >>> assets = assets/jupyter

    posts
        The relative path to the posts directory from the website root.
        This is `_posts` for default Jekyll site configurations.
    assets
        The relative path to the assets folder where generated notebook
        assets will be stored. This is relative to the website root.

        .. warning::
            This folder will be cleared each time `convert_notebooks()`
            is called. Therefore, the folder should be separate from those
            used for other website assets. Otherwise those assets will be
            deleted.

    """
    def __init__(self, root, options=None):
        self.root = root

        if options == None:
            options = os.path.join(self.root, 'jup2jek.ini')

        elif not os.path.exists(options):
            options = os.path.join(self.root, options)

        self.load_options(options)

    @staticmethod
    def write_default_options(path):
        """
        Writes a configuration file with the default options.

        Parameters
        ----------
        path : str
            Directory for writing the configuration file. The file name
            should not be included and will be appended as part of the
            method.
        """
        config = ConfigParser()
        config['JUP2JEK'] = dict(
            posts='_posts',
            assets='assets/jupyter'
        )

        p = os.path.join(path, 'jup2jek.ini')

        with open(p, 'wt') as file:
            file.truncate()
            config.write(file)

    def load_options(self, path):
        """
        Loads the options from the specified configuration file.

        Parameters
        ----------
        path : str
            Configuration file path.
        """
        if os.path.exists(path):
            config = ConfigParser()
            config.read(path)
            self.options = {}
            self.options.update(config['JUP2JEK'])
        else:
            raise ValueError('Configuration file {} does not exist.'.format(path))

    def posts_path(self):
        """Returns the posts path."""
        return os.path.join(self.root, self.options['posts'])

    def assets_path(self):
        """Returns the assets path."""
        return os.path.join(self.root, self.options['assets'])

    def convert(self, path):
        """
        Converts the notebook at the specified path to markdown via the
        `jupyter nbconvert [notebook path] --to markdown` command.

        Parameters
        ----------
        path : str
            Path to the jupyter notebook.
        """
        command = 'jupyter nbconvert {} --to markdown'.format(path)
        check_output(command, shell=True)

    def notebooks(self):
        """Returns a list of notebook paths to be converted."""
        posts = self.posts_path()
        notebooks = []

        for folder, _, _ in os.walk(posts):
            if '.ipynb_checkpoints' not in folder:
                notebooks.extend(glob(os.path.join(folder, '*.ipynb')))

        return notebooks

    def _create_assets_path(self):
        """Creates the new assets path."""
        p = self.assets_path()

        if not os.path.exists(p):
            os.makedirs(p)

    def _remove_assets_path(self):
        """Removes the jupyter assets path."""
        p = self.assets_path()

        if os.path.exists(p):
            shutil.rmtree(p)

    def _update_markdown_paths(self, md_path, rel_assets_path):
        """
        Updates the asset paths within the specified markdown file to that
        of the specified relative asset path. The final path reads as:
        `{{ site.url }}/[relative assets path]/[notebook filename]_files`.
        For example: `{{ site.url }}/[assets/jupyter/category1]/[example4]_files`
        (brackets included for emphasis only).

        Parameters
        ----------
        md_path : str
            The path to the markdown file for which asset reference
            paths will be replaced.
        rel_assets_path : str
            The relative path to the new assets folder from the website
            root. See the above example path declaration.
        """
        p = '{{{{ site.url }}}}/{}/'.format(rel_assets_path)

        with open(md_path, 'rt') as file:
            reader = file.read()
            data = reader.replace('![png](', '![png]({}'.format(p))

        with open(md_path, 'wt') as file:
            file.truncate()
            file.write(data)

    def convert_notebooks(self):
        """
        Converts all Jupyter notebooks within the posts folder specified
        in the class options to markdown for use on Jekyll websites.
        The convert process operates as follows:

            1. All notebooks contained in the designated posts folder are found
               and converted to markdown using the jupyter nbconvert command.
            2. If the nbconvert command generates an assets folder, the assets
               are moved to the designated site assets folder at the same relative
               path.
            3. Asset paths referenced within the markdown files are updated to
               the website path.
        """
        notebooks = self.notebooks()
        assets_path = self.assets_path()
        posts_path = self.posts_path()
        self._remove_assets_path()
        self._create_assets_path()

        for x in notebooks:
            self.convert(x)
            a1 = x[:-6] + '_files'

            if os.path.exists(a1):
                # Move assets from posts to assets
                f = os.path.relpath(a1, posts_path)
                a2 = os.path.join(assets_path, f)
                shutil.move(a1, a2)
                # Update the asset reference paths in markdown file
                m = x[:-6] + '.md'
                p = os.path.relpath(os.path.dirname(a1), posts_path)
                p = os.path.join(assets_path, p)
                p = os.path.relpath(p, self.root)
                self._update_markdown_paths(m, p)
