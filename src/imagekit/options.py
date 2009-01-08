# Imagekit options
from imagekit import processors
from imagekit.specs import ImageSpec
    

class Options(object):
    """ Class handling per-model imagekit options

    """
    image_field = 'image'
    crop_horz_field = 'crop_horz'
    crop_vert_field = 'crop_vert'
    preprocessor_spec = None
    cache_dir = 'images'
    save_count_as = None
    cache_filename_format = "%(filename)s_%(specname)s.%(extension)s"
    config_module = 'imagekit.config'
    
    def __init__(self, opts):        
        for key, value in opts.__dict__.iteritems():
            setattr(self, key, value)
            self.specs = []