class ConvertBase:
    # Class for assigning attributes common to all echosounders
    def __init__(self):
        self._platform = {
            'platform_name': '',
            'platform_code_ICES': '',
            'platform_type': ''
        }
        self.nc_path = None
        self.zarr_path = None
        self.save_path = None

    @property
    def platform_name(self):
        return self._platform['platform_name']

    @platform_name.setter
    def platform_name(self, platform_name):
        self._platform['platform_name'] = platform_name

    @property
    def platform_type(self):
        return self._platform['platform_type']

    @platform_type.setter
    def platform_type(self, platform_type):
        self._platform['platform_type'] = platform_type

    @property
    def platform_code_ICES(self):
        return self._platform['platform_code_ICES']

    @platform_code_ICES.setter
    def platform_code_ICES(self, platform_code_ICES):
        self._platform['platform_code_ICES'] = platform_code_ICES

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, p):
        if isinstance(p, list):
            self._filename = p
        else:
            self._filename = [p]

    def raw2nc(self, compress=True):
        self.save(".nc", compress)

    def raw2zarr(self, compress=True):
        self.save(".zarr", compress)
