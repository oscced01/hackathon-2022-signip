
class Crate:

    def __init__(
        self, 
        depth, 
        name, 
        major_version, 
        minor_version, 
        patch_version, 
        additional, 
        dependency_path
    ):
        self.depth: int = int(depth)
        self.name: str = name
        self.major_version: int = int(major_version)
        self.minor_version: int = int(minor_version)
        self.patch_version: int = int(patch_version)
        self.additional: str = additional
        self.dependency_path: list = dependency_path
    
    def __repr__(self):
        return f"{self.name} v{self.major_version}.{self.minor_version}.{self.patch_version}"


    def version(self):
        return f"v{self.major_version}.{self.minor_version}.{self.patch_version}"