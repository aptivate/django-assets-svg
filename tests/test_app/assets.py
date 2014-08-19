from __future__ import absolute_import, unicode_literals

from django_assets import register

from django_assets_svg.filter import SvgToPng

register('test_png',
    SvgToPng('Bitmap_VS_SVG.svg', output='Bitmap_VS_SVG.png'))
