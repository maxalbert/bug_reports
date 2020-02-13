## Bug report

https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin/issues/17

## To reproduce

1) Clone this repo and change into the appropriate subfolder.
```
$ git clone https://github.com/maxalbert/bug_reports.git
$ cd bug_reports/mkdocs-awesome-pages-plugin/issue_17/
```

2) Install the required dependencies.

If you use `poetry`, you can simply run:
```
$ poetry install
```

If you don't use `poetry`, you will need to install the dependencies manually via pip:
```
$ pip install mkdocs mkdocs-awesome-pages-plugin mktheapidocs
$ pip install ./dummy_python_module
```

3) Next, serve the docs by running the following command (leave out the `poetry run` if you don't use poetry).:
```
poetry run mkdocs serve
```
Then navigate to http://localhost:8000/ to open the docs.

4) Check that the arrangement of entries in the navigation bar is as expected. They should appear in the following order (as specified by the `arrange` key in `docs/.pages`):
```
- Home
- Tutorials
    + First steps
- How-To Guides
    + Setting up a dev environment
    + Running the tests
```

5) Uncomment the `mktheapidocs` section in the file `mkdocs.yml`. Then reload the docs page in your browser. Check that there is an additional section called "Dummy python module" (with API docs for the dummy python module) and that the order of the toplevel sections is now wrong - in particular, "Tutorials" and "How-To Guides" are reversed:
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

## Analysis of the bug

The reason for this bug is that `awesome-pages` tries to determine the directory where to look for the `.pages` file by determining the common subdirectory of the various sections in the nav bar (see the helper methods [_gather_metadata](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin/blob/master/mkdocs_awesome_pages_plugin/navigation.py#L135-L145) and [_common_dirname](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin/blob/master/mkdocs_awesome_pages_plugin/navigation.py#L147-L152)). In our case this directory _should_ be the toplevel `docs/` folder. However, since `mktheapidocs` inserts the additional section "Dummy python module" whose underlying files live in the directory `dummy_python_module` which is _outside_ the docs folder, `awesome-pages` gets confused and can't find the `.pages` file any more.
