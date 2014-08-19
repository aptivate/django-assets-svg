from io import BytesIO
from os import path
import os
import subprocess

from webassets.bundle import Bundle
from webassets.filter import Filter
from webassets.merge import FileHunk

class SvgToPng(Bundle):
    """
    def input(self, _in, out, **kwargs):
        out.write(_in.read())

    def output(self, _in, out, **kwargs):
        # import pdb; pdb.set_trace()
        import wand.image
        with wand.image.Image(blob=str(_in.read()), format='svg') as image:
            png_image = image.make_blob("png")

            # Nasty hack to persuade StringIO to work with binary data
            bio = BytesIO()
            bio.write(png_image)
            bio.seek(0)
            data = bio.read()
            # out.buf = data
            # out.len = len(data)
            out.write(unicode(data))
    """

    def build(self, env=None, force=None, output=None, disable_cache=None):
        """Build this bundle, meaning create the file given by the ``output``
        attribute, applying the configured filters etc.

        If the bundle is a container bundle, then multiple files will be built.

        Unless ``force`` is given, the configured ``updater`` will be used to
        check whether a build is even necessary.

        If ``output`` is a file object, the result will be written to it rather
        than to the filesystem.

        The return value is a list of ``FileHunk`` objects, one for each bundle
        that was built.
        """
        version = None

        output_filename = self.resolve_output(self.env, version=version)

        # If it doesn't exist yet, create the target directory.
        output_dir = path.dirname(output_filename)
        if not path.exists(output_dir):
            os.makedirs(output_dir)

        resolved_contents = self.resolve_contents(self.env, force=True)

        from wand.api import library
        import wand.color
        import wand.image

        with wand.image.Image() as image:
            with wand.color.Color('transparent') as background_color:
                library.MagickSetBackgroundColor(image.wand,
                                                 background_color.resource)
            image.read(filename=resolved_contents[0][1])
            png_image = image.make_blob("png32")

        with open(output_filename, "wb") as out:
            # out.write(png_image)
            try:
                proc = subprocess.Popen(["pngquant", "255"], stdin=subprocess.PIPE,
                    stdout=out)
                proc.communicate(png_image)
            except OSError as e:
                raise Exception("Failed to execute pngquant: %s" % e)

        return [FileHunk(output_filename)]
