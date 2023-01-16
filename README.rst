=======
AppName
=======

Lorem ipsum


Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Install app

.. code-block:: bash

    $ pip install -U dj-dbchiro-roles



2. Configure ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        (...),
        'rest_framework',
        'roles',
        (...),
    )


3. Configure ``urls.py``:

.. code-block:: python

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api-auth/', include('rest_framework.urls')),
        (...),
        path('api/v1/', include('app_name.urls')),
        (...),
    ]

4. Run ``python manage.py migrate`` to create the polls models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a role (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/api/v1/... to view roles API.
