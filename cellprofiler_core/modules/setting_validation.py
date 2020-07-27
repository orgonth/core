import os.path
import urllib.parse

from ..module import Module
from ..pipeline import ImagePlane
from ..utilities.pathname import pathname2url


def modpath_to_url(modpath):
    if modpath[0] in ("http", "https", "ftp", "s3"):
        if len(modpath) == 1:
            return modpath[0] + ":"
        elif len(modpath) == 2:
            return modpath[0] + ":" + modpath[1]
        else:
            return modpath[0] + ":" + modpath[1] + "/" + "/".join([urllib.parse.quote(part) for part in modpath[2:]])

    path = os.path.join(*modpath)

    return pathname2url(path)


class SettingValidation(Module):
    """A fake module for setting validation"""

    @staticmethod
    def get_image_plane_details(modpath):
        url = modpath_to_url(modpath)

        return ImagePlane(url)
