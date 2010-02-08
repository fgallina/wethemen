Django compressor
=================

Compresses linked and inline javascript or CSS into a single cached file.

Syntax::

    {% compress <js/css> %}
    <html of inline or linked JS/CSS>
    {% endcompress %}

Examples::

    {% compress css %}
    <link rel="stylesheet" href="/media/css/one.css" type="text/css" charset="utf-8">
    <style type="text/css">p { border:5px solid green;}</style>
    <link rel="stylesheet" href="/media/css/two.css" type="text/css" charset="utf-8">
    {% endcompress %}

Which would be rendered something like::

    <link rel="stylesheet" href="/media/CACHE/css/f7c661b7a124.css" type="text/css" media="all" charset="utf-8">

or::

    {% compress js %}
    <script src="/media/js/one.js" type="text/javascript" charset="utf-8"></script>
    <script type="text/javascript" charset="utf-8">obj.value = "value";</script>
    {% endcompress %}

Which would be rendered something like::

    <script type="text/javascript" src="/media/CACHE/js/3f33b9146e12.js" charset="utf-8"></script>

Linked files must be on your COMPRESS_URL (which defaults to MEDIA_URL).
If DEBUG is true off-site files will throw exceptions. If DEBUG is false
they will be silently stripped.

If COMPRESS is False (defaults to the opposite of DEBUG) the compress tag
simply returns exactly what it was given, to ease development.


CSS Notes:
**********

All relative url() bits specified in linked CSS files are automatically
converted to absolute URLs while being processed. Any local absolute URLs (those
starting with a '/') are left alone.

Stylesheets that are @import'd are not compressed into the main file. They are
left alone.

Set the media attribute as normal on your <style> and <link> elements and
the combined CSS will be wrapped in @media blocks as necessary.

**Recommendations:**

* Use only relative or full domain absolute URLs in your CSS files.
* Avoid @import! Simply list all your CSS files in the HTML, they'll be combined anyway.


Why another static file combiner for django?
********************************************

Short version: None of them did exactly what I needed.

Long version:

**JS/CSS belong in the templates**
  Every static combiner for django I've seen makes you configure
  your static files in your settings.py. While that works, it doesn't make
  sense. Static files are for display. And it's not even an option if your
  settings are in completely different repositories and use different deploy
  processes from the templates that depend on them.

**Flexibility**
  django_compressor doesn't care if different pages use different combinations
  of statics. It doesn't care if you use inline scripts or styles. It doesn't
  get in the way.

**Automatic regeneration and cache-foreverable generated output**
  Statics are never stale and browsers can be told to cache the output forever.

**Full test suite**
  I has one.


Settings
********

Django compressor has a number of settings that control it's behavior.
They've been given sensible defaults.

`COMPRESS` default: the opposite of `DEBUG`
  Boolean that decides if compression will happen.

`COMPRESS_URL` default: `MEDIA_URL`
  Controls the URL that linked media will be read from and compressed media
  will be written to.

`COMPRESS_ROOT` default: `MEDIA_ROOT`
  Controls the absolute file path that linked media will be read from and
  compressed media will be written to.

`COMPRESS_OUTPUT_DIR` default: `"CACHE"`
  Conttrols the directory inside `COMPRESS_ROOT` that compressed files will
  be written to.

`COMPRESS_CSS_FILTERS` default: []
  A list of filters that will be applied to CSS.

`COMPRESS_JS_FILTERS` default: ['compressor.filters.jsmin.JSMinFilter'])
  A list of filters that will be applied to javascript.


Dependecies
***********

* BeautifulSoup

