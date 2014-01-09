django-omero-cbvtest
====================

CBV Test for https://github.com/openmicroscopy/openmicroscopy/pull/1928

Setup required
==============

Clone this repository into `components/tools/OmeroWeb/omeroweb/`, probably easiest to clone into `cbvtest`.

```
git clone https://github.com/dpwrussell/django-omero-cbvtest.git cbvtest
```

In `components/tools/OmeroWeb/omeroweb/urls.py` add a url to test this view at, e.g.

```python
(r'^(?i)cbvtest/', include('cbvtest.urls'))
```

Without https://github.com/openmicroscopy/openmicroscopy/pull/1928
===================================================================

When not logged in, this should fail.
If logged in it should display 'Hello World'.

With https://github.com/openmicroscopy/openmicroscopy/pull/1928
================================================================

When not logged in, should redirect to login page.
If logged in it should display 'Hello World'.