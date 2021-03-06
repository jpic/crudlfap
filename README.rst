.. image:: https://img.shields.io/readthedocs/crudlfap.svg
   :target: https://crudlfap.readthedocs.io
.. image:: https://yourlabs.io/oss/crudlfap/badges/master/build.svg
   :target: https://circleci.com/gh/yourlabs/crudlfap
.. image:: https://img.shields.io/codecov/c/github/yourlabs/crudlfap/master.svg
   :target: https://codecov.io/gh/yourlabs/crudlfap
.. image:: https://img.shields.io/npm/v/crudlfap.svg
   :target: https://www.npmjs.com/package/crudlfap
.. image:: https://img.shields.io/pypi/v/crudlfap.svg
   :target: https://pypi.python.org/pypi/crudlfap

Welcome to CRUDLFA+ for Django 3.0: because Django is FUN !
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CRUDLFA+ stands for Create Read Update Delete List Form Autocomplete and more.

This plugin for Django makes a rich user interface from Django models, built
with Material Components Web Ryzom Components, offering optionnal databinding
with channels support.

Demo:

- last release: https://demo.crudlfap.ci.yourlabs.io/
- current master (might be down/broken etc): https://master.crudlfap.ci.yourlabs.io/

Try
===

This should start the example project from ``src/crudlfap_example`` where each
documented example lives::

    # This installs the repo in ./src/crudlfap and in your python user packages, i run this from ~
    pip install --user -e git+https://github.com/yourlabs/crudlfap.git#egg=crudlfap[example]
    cd src/crudlfap

    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py runserver

Features
========

- DRY into ModelRouter for all views of a Model,
- extensive CRUD views, actions, etc
- Rich frontend interface out of the box, MDC/Ryzom/Unpoly

Resources
=========

- `Documentation
  <http://oss.yourlabs.me/crudlfap/>`_
- `ChatRoom graciously hosted by
  <https://www.yourlabs.chat>`_ by `YourLabs Business Service
  <https://www.yourlabs.biz>`_ on `Mattermost
  <https://mattermost.com/>`_
- `Mailing list graciously hosted
  <http://groups.google.com/group/yourlabs>`_ by `Google
  <http://groups.google.com>`_
- For **Security** issues, please contact yourlabs-security@googlegroups.com
- `Git graciously hosted
  <https://yourlabs.io/oss/crudlfap/>`_ by `YourLabs Business Service
  <https://www.yourlabs.biz>`_ with `GitLab
  <https://www.gitlab.org>`_
- `Package graciously hosted
  <http://pypi.python.org/pypi/crudlfap/>`_ by `PyPi
  <http://pypi.python.org/pypi>`_,
- `Continuous integration graciously hosted
  <https://yourlabs.io/oss/crudlfap/pipelines>`_ by YourLabs Business Service
- Browser test graciously hosted by `SauceLabs
  <https://saucelabs.com>`_
