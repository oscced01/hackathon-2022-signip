class PackageInfo:
    
    def __init__(self):
        self.crates = dict()

    def add(self, crate):
        if crate.name in self.crates:
            self.crates[crate.name].append(crate)
        else:
            self.crates[crate.name] = [crate]

    def print(self):
        for key, value in self.crates.items():
            print(f"{key}:")
            for crate in value:
                print(f"\tv{crate.major_version}.{crate.minor_version}.{crate.patch_version}")
                print(f"\t{crate.dependency_path}")

    def merge(self, other):
        merged_pack_info = PackageInfo()
        merged_pack_info.crates = self.crates.copy()

        for _, value in other.crates.items():
            for crate in value:
                merged_pack_info.add(crate)
        
        return merged_pack_info

    def scrutinize(self):
        diff_found = False
        for key, value in self.crates.items():
            if len(value) == 1:
                continue

            diff_found = True
            versions = set()
            for crate in value:
                versions.add(crate.version())
            if len(versions) == 1:
                continue
            
            crates = self.crates[key]
            print(key)
            for version in versions:
                print(f"\t{version}")
                crates_of_ver = list(filter(lambda crate: crate.version() == version, crates))
                paths = [crate.dependency_path for crate in crates_of_ver]
                paths.sort(key=lambda path: len(path), reverse=False)
                for path in paths:
                    print("\t\t" + " ".join(path))
            print()
        return diff_found
