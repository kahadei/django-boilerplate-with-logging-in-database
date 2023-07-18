================
Django boilerplate with logging in separate database(for small projects)
================



Dependency
----------
* Django>=3.5
* Python 3.7+

License
-------
WTFPL

Quick start
-----------

1. Install

.. code-block:: bash

    pip install -r requirements.txt

2. Add ``.env`` file in project ROOT  to save variables

.. code-block:: python

    DEBUG=1 # 1 - True, 0 - False
    SECRET_KEY='YOUR_KEY'

3. Run ``python manage.py makemigrations``
4. Run ``python manage.py migrate``


================
Screenshot
================
.. code-block:: python

    import logging
    db_logger = logging.getLogger('db')

    db_logger.info('info message')
    db_logger.warning('warning message')

    try:
        1/0
    except Exception as e:
        db_logger.exception(e)

================
Logger usege
================


Thanks
-------
Logger inspired by:
.. _django-db-logger: https://travis-ci.org/CiCiUi/django-db-logger