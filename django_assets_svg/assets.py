from __future__ import absolute_import, unicode_literals

from django_assets import Bundle, register

replace_svg_js = Bundle(
    'django_assets_svg/replace_svg.js',
    filters=['jsmin'],
    output='django_assets_svg/replace_svg.min.js')

register('django_assets_svg.replace_svg_js', replace_svg_js)
