# Hackathon 2022 SIGNIP
Dependency Scrutinizer Tool for Cargo Projects.
A quick script to easily view differing dependency versions of crates in one or several projects.

To run the program use `./depscrut.py path1 path2 ... pathN` or `python depscrut.py path1 ..` where path is a path to a folder where there is a Config.toml file with dependencies for a program

## Parsec Example
```bash
./get_repos.sh # Git clone example repos
./depscrut.py ./example/parsec/ ./example/parsec-tools/ # Scrutinize between example projects
```

## Set up
* Tested with python version 3.8.10, on Ubuntu 20.04
* Dependent on Cargo