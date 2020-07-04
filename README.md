<h1 align="center">:snake: holbertonschool-higher_level_programming :snake:</h1>

# Zen
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
# Install PEP8

`Pycodestyle` is now the [new standard of Python style code](https://github.com/PyCQA/pycodestyle/issues/466), but at school we will use `PEP8`, `version 1.7.*` Don’t worry, `pycodestyle` is based on `pep8`. The hardest part now is to install it for Python 3:

### Regular Ubuntu 14.04 install
``` 
$ sudo apt-get install python3-pep8
```

### Using Pip3
#### Install Pip3
```
$ sudo apt-get install python3-pip
```

### Install Pep8
```
$ pip3 install pep8
```

### Make sure you have the right version
```
$ pep8 --version
1.7
$
```

If it’s not the case, it means PEP8 is installed but not linked in your `PATH`. You should look at these folders to find where it has been installed:
- `/usr/local/lib/python3*/dist-packages/pep8.py`
- `/usr/lib/python3*/dist-packages/pep8.py`

Don’t hesitate to delete `/usr/bin/pep8` and replace by one of those `pep8.py`:
- `cp pep8.py /usr/bin/pep8`
- `chmod u+x /usr/bin/pep8`

Finally, if you can’t make it work, please use the “container-on-demand” tool to “PEP8” your files in a pre-configured container.

## :black_nib: Authors

- Juliana Chois - [Github](https://github.com/julianachois)
