import os
from ..jup2jek import Jup2Jek


def root_dir():
    return os.path.dirname(os.path.abspath(__file__))


def Jup2Jek_init():
    p = root_dir()
    return Jup2Jek(p)


def test_write_default_options():
    p = root_dir()
    Jup2Jek.write_default_options(p)
    assert os.path.exists(p) == True


def test_load_options():
    j = Jup2Jek_init()
    assert j.options == {'posts': '_posts',
                         'assets': 'assets/jupyter'}


def test_notebooks():
    j = Jup2Jek_init()
    p = root_dir()
    nb = set(os.path.relpath(x, p) for x in j.notebooks())
    assert nb == {'_posts/example1.ipynb',
                  '_posts/example2.ipynb',
                  '_posts/example3.ipynb',
                  '_posts/category1/example4.ipynb'}


def test_create_assets_path():
    j = Jup2Jek_init()
    j.create_assets_path()
    p = root_dir()
    p = os.path.join(p, 'assets/jupyter')
    assert os.path.exists(p) == True


def test_remove_assets_path():
    j = Jup2Jek_init()
    j.create_assets_path()
    j.remove_assets_path()
    p = root_dir()
    p = os.path.join(p, 'assets/jupyter')
    assert os.path.exists(p) == False


def test_convert_notebooks():
    j = Jup2Jek_init()
    j.convert_notebooks()
