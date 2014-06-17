# Django Assets SVG

Django-Assets support for automatically generating optimised PNG files from SVG sources.

## What is it?

[Django-Assets](http://django-assets.readthedocs.org/en/latest/) allows
you to define assets (media files such as CSS and JavaScript) for your
Django project, which you can easily load together, compile into bundles,
compress them, version them, etc.

You might often want to use SVG graphics in the sites that you build.
For example, they scale better and are usually smaller than equivalent
high-quality PNG renderings of the same vector graphics (logos, etc.).

But some common browsers [don't support SVG graphics](http://caniuse.com/svg),
so you need to implement a PNG fallback for these browsers. And you want to
generate these PNG files automatically when the SVG source is updated, and
ensure that they're always properly compressed.

Django Assets SVG does that for you.

## How do I use it?

Ensure that the `pngquant` application is installed on your development box,
and also your servers (unless you keep your generated assets in version
control).

Add django-assets-svg to your project dependencies (e.g. `pip_packages.txt`)
or install it manually with `pip`:

	[pip install] git+https://github.com/aptivate/django-assets-svg.git#egg=django-assets-svg

Define your SVG files as assets in your `assets.py` files like this:

	from django_assets_svg.filter import SvgToPng
	register('logo_png',
	    SvgToPng('images/logo.svg', output='images/logo.png'))

Either load the generated PNG file in your templates, keeping the source SVG
hidden from your browser:

	{% assets "logo_png" %}
	<img src="{{ ASSET_URL }}" alt="My site logo" />
	{% endassets %}

Or load the SVG file and have the browser fall back to PNG on error:

	<img src="{{ STATIC_URL }}images/logo.svg" alt="My site logo"
		onerror="replace_svg_logo_with_png.call(this);" />

In the latter case you should either load the JavaScript bundle that contains
the `replace_svg_logo_with_png` function. To do this, you should add
`django_assets_svg` to your `INSTALLED_APPS`:

	INSTALLED_APPS = [
	    ...
	    'django_assets_svg'
	]

And then either load the script file directly (before load the image!):

	{% assets "django_assets_svg.replace_svg_js" %}
	<script src="{{ ASSET_URL }}" type="text/javascript"></script>
	{% endassets %}

Or incorporate it into your own bundle which you load early, in your
own `assets.py`, for example:

	from django_assets_svg import assets as django_assets_svg
	main_js = Bundle(
	    django_assets_svg.replace_svg_js,
	    'js/mylibrary.js',
	    filters=['jsmin'],
	    output='js/mylibrary.min.js')
	register('main.main_js', main_js)

and template:

	{% assets "main.main_js" %}
	<script src="{{ ASSET_URL }}" type="text/javascript"></script>
	{% endassets %}

Note that you **must** load this JavaScript file early, unlike most of your
files that you should probably defer and load as late as possible. So it's
better not to combine it with your standard bundle. Only combine it with an
early loading bundle if you have one, otherwise load it alone and early.

## How do I get support?

Please file an issue on our [GitHub issue tracker](https://github.com/aptivate/django-assets-svg/issues).
