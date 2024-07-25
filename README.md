[![ci](https://github.com/CodeCraftingWithAnton/conan2-cmake-template/actions/workflows/ci.yml/badge.svg)](https://github.com/CodeCraftingWithAnton/conan2-cmake-template/actions/workflows/ci.yml)

- [conan2-cmake-template](#conan2-cmake-template)
  - [How to use this template](#how-to-use-this-template)
  - [Why does this template exist?](#why-does-this-template-exist)
  - [What's inside](#whats-inside)

# conan2-cmake-template

This is a template repository for C++ projects that use [Conan 2 package manager][conan] and [VSCode IDE][vscode].

[Micromamba][micromamba] is used to reproducibly provision python, compilers and other build tools within isolated environment on local machine and in CI.

[GitHub Actions][gha] is used for continuous integration.

## How to use this template

 1. Create a new repo from this template repository. [Detailed docs on how to do that](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
 2. Clone new repo locally and open folder in VSCode
 3. Instal all recommended extensions
    1. Install local extensions via `Show Private Extensions` command (if any in `.vscode/extensions`)
 4. Modify versions of python, cmake, ninja, clang in [`environment.yml`](environment.yml)
 5. Initialize environment using `Micromamba: create environment`. This will install python, clang, conan and all other tools
 6. Reload VSCode to activate environment. This will make `conan` available in the terminal
 7. Use `conan new` to create new library (`cmake_lib`) or executable (`cmake_exe`) from template. Pick the `<name>` and `<version>` and run `conan new cmake_lib -d name=<name> -d version=<version>`. For more details see [official `conan new` doc](https://docs.conan.io/2/reference/commands/new.html)
 8. Update all the template fields the files created by `conan`
 9. Remove all the `Remove me:` steps from `.github/workflows/ci.yml`
 10. Replace `https://github.com/CodeCraftingWithAnton/conan2-cmake-template` with your repo URL
 11. Learn more about [conan](https://docs.conan.io/2/tutorial/consuming_packages/build_simple_cmake_project.html)
 12. Happy coding!

## Why does this template exist?

Modern hardware is becoming more and more powerful, allowing building the most audacious software projects. However with great power comes great ~~responsibility~~ complexity. Modern software projects consist of hundreds and sometimes even thousands of cross interacting modules. Managing all of them as a single monolithic chunk of code is generally undesirable and in the world of open source software is simply impossible.
Most of modern programming languages came up with the toolchain and package manager solutions. NodeJS comes with [NPM](https://www.npmjs.com/) or [yarn](https://yarnpkg.com/) package managers, [Rust](https://www.rust-lang.org/) comes with [rustup](https://rustup.rs/) toolchain manager and [Cargo](https://doc.rust-lang.org/cargo/) package manager.

In the best traditions of the C++ development, there is no standard set of tools to do toolchain or package management. Nevertheless the need is still there and community came up with great solutions to it. However with many solutions available picking the matching set of tools is increasingly hard. This is exactly the problem this template is attempting to address.

[Conan 2][conan] is the open source, decentralized and multi-platform package manager for C++. It is written in python, allowing to run anywhere where python can run, but it means you have to install python in addition to package manager itself. Moreover it has a major limitation, it doesn't handle installation of the compiler and expects it to be preinstalled on the system

[Micromamba][micromamba] is lightweight and blazing fast version of [conda](https://anaconda.org/) which was originally designed to manage python environment and packages along with their native dependencies. However it proved to be well suited for handling native tools independently of python. Therefore it is used to install [Python][conda-python] for Conan along with [CMake][conda-cmake], [Ninja][conda-ninja] and [Clang][conda-clang]. In order to achieve reproducible results, environment uses [conda-forge][conda-forge] remote only.

"Wait, Conda is a package manager of its own, why do we need Conan" you might ask and will be absolutely correct. Conda is a package manager, but it is focused on python and many C++ packages exist there only by chance, because they were needed for some python native dependency. [conda-forge][conda-forge] has more C++ packages, but it comes with a twist, you have to build, test and distribute using their infrastructure and compilers, which is not what most C++ projects want or need. Hence conda is not really well suited for generic C++ package management and [Conan 2][conan] is still the right solution. On top of that conda environment provides no isolation between packages, meaning any package can access headers, libs and binaries from any other, no matter if it was an explicit or implicit dependency. [Conan 2][conan] has strict dependency model and provides clean isolation of dependencies, even allowing having multiple versions of the same library as long as they don't conflict at runtime.

## What's inside

[conan]: https://conan.io/
[vscode]: https://code.visualstudio.com/
[micromamba]: https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html
[gha]: https://docs.github.com/en/actions
[conda-python]: https://anaconda.org/conda-forge/python
[conda-clang]: https://anaconda.org/conda-forge/clang
[conda-cmake]: https://anaconda.org/conda-forge/cmake
[conda-ninja]: https://anaconda.org/conda-forge/ninja
[conda-forge]: https://conda-forge.org/
