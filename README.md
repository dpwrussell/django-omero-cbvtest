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

This should fail unless https://github.com/openmicroscopy/openmicroscopy/pull/1928 has been applied.