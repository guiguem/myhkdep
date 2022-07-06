from hkpilot.utils.cmake import CMake


class myhkdep(CMake):

    def __init__(self, path):
        super().__init__(path)
        self._package_name = "myhkdep"
        # self._package_version = "1.4.0"
