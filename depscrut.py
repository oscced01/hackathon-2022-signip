#!/usr/bin/env python

import subprocess
import re
import sys

from crate import Crate
from package_info import PackageInfo

def main():
    if len(sys.argv) < 2:
        print("Error!")
        print("To run the program please supply at least one path. The path folder should have a Cargo.toml file.")
        return

    merged_info = parse_dependencies(sys.argv[1])
    for path in sys.argv[2:]:
        package_info = parse_dependencies(path_1)
        merged_info = merged_info.merge(package_info)

    
    if not merged_info.scrutinize():
        print("Found no different versions! :)")

def parse_line(line):
    """
    Group 1: dependencies depth
    Group 2: crate name
    Group 3: crate major version
    Group 4: crate minor version
    Group 5: crate patch version
    Group 6: additional
    """
    pattern = "(\d+)([^ ]+) v(\d+)\.(\d+)\.(\d+) ?(.*)"
    regex = re.match(pattern, line)

    if regex:
        return list(regex.groups())
    else: 
        raise Exception("Gosh darnit, we failed! :(")


def parse_dependencies(path):
    command = ["cargo", "tree", "--prefix-depth", "--quiet", "--no-dedupe"]
    result = subprocess.run(command + ["--manifest-path", path + "Cargo.toml"], stdout=subprocess.PIPE).stdout.decode('utf-8')
    if not result:
        raise ValueError(f"Could not read Cargo.toml at path {path}")
    lines = result.splitlines()

    prev_crate = None
    dependency_path = []
    package_info = PackageInfo()

    for line in lines:
        crate_info = parse_line(line)
        depth = int(crate_info[0])

        if prev_crate:
            if prev_crate.depth < depth:
                dependency_path.append(prev_crate.name)
            else:
                diff = prev_crate.depth - depth
                for _ in range(diff):
                    dependency_path.pop()
        
        crate = Crate(*(crate_info + [dependency_path.copy()]))
        prev_crate = crate
        package_info.add(crate)
    
    return package_info

if __name__ == "__main__":
    main()