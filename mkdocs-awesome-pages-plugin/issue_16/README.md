https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin/issues/16

# To reproduce:

First install the required dependencies.

Either using `poetry`:
```
$ poetry install
```

Or using plain pip:
```
$ pip install mkdocs mkdocs-awesome-pages-plugin mktheapidocs
```


Next, serve the docs by running the following command (leave out the `poetry run` if you don't use poetry).:
```
poetry run mkdocs serve
```
Then navigate to http://localhost:8000/ to open the docs.

If you check the arrangement of entries in the navigation bar, they should appear in the following, correct order (as specified by the `arrange` key in `docs/.pages`):
```
- Home
- Tutorials
    + First steps
- How-To Guides
    + Setting up a dev environment
    + Running the tests
```

However, if you uncomment the plugin `mktheapidocs` in the file `mkdocs.yml`then the order of the toplevel sections will be wrong (in particular, "Tutorials" and "How-To Guides" will be reversed):
```
- Home
- How-To Guides
    + Setting up a dev environment
    + Running the tests
- Tutorials
    + First steps
- Dummy python module
    + dummy_python_module
    + foo
```

The reason for this bug is that `awesome-pages` tries to determine the directory where to look for the `.pages` file by determining the common subdirectory of the various sections in the nav bar. In our case this directory _should_ be the toplevel `docs/` folder. However, since `mktheapidocs` inserts the additional section "Dummy python module" whose underlying files live in the directory `dummy_python_module` which is _outside_ the docs folder, `awesome-pages` gets confused and can't find the `.pages` file any more.
