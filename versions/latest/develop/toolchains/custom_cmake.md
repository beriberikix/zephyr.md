---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/toolchains/custom_cmake.html
original_path: develop/toolchains/custom_cmake.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Custom CMake Toolchains

To use a custom toolchain defined in an external CMake file, [set these
environment variables](../env_vars.md#env-vars):

- Set [`ZEPHYR_TOOLCHAIN_VARIANT`](../env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) to your toolchain’s name
- Set `TOOLCHAIN_ROOT` to the path to the directory containing your
  toolchain’s CMake configuration files.

Zephyr will then include the toolchain cmake files located in the
`TOOLCHAIN_ROOT` directory:

- `cmake/toolchain/<toolchain name>/generic.cmake`: configures the
  toolchain for “generic” use, which mostly means running the C preprocessor
  on the generated
  [Devicetree](../../build/dts/index.md#devicetree) file.
- `cmake/toolchain/<toolchain name>/target.cmake`: configures the
  toolchain for “target” use, i.e. building Zephyr and your application’s
  source code.

Here <toolchain name> is the same as the name provided in
[`ZEPHYR_TOOLCHAIN_VARIANT`](../env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT)
See the zephyr files [cmake/modules/FindHostTools.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/main/cmake/modules/FindHostTools.cmake) and
[cmake/modules/FindTargetTools.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/main/cmake/modules/FindTargetTools.cmake) for more details on what your
`generic.cmake` and `target.cmake` files should contain.

You can also set `ZEPHYR_TOOLCHAIN_VARIANT` and `TOOLCHAIN_ROOT` as CMake
variables when generating a build system for a Zephyr application, like so:

```shell
west build ... -- -DZEPHYR_TOOLCHAIN_VARIANT=... -DTOOLCHAIN_ROOT=...
```

```shell
cmake -DZEPHYR_TOOLCHAIN_VARIANT=... -DTOOLCHAIN_ROOT=...
```

If you do this, `-C <initial-cache>` [cmake option](https://cmake.org/cmake/help/latest/manual/cmake.1.html#options) may useful. If you save
your **ZEPHYR\_TOOLCHAIN\_VARIANT**, **TOOLCHAIN\_ROOT**, and other
settings in a file named `my-toolchain.cmake`, you can then invoke cmake
as `cmake -C my-toolchain.cmake ...` to save typing.

Zephyr includes `include/toolchain.h` which again includes a toolchain
specific header based on the compiler identifier, such as `__llvm__` or
`__GNUC__`.
Some custom compilers identify themselves as the compiler on which they are
based, for example `llvm` which then gets the `toolchain/llvm.h` included.
This included file may though not be right for the custom toolchain. In order
to solve this, and thus to get the `include/other.h` included instead,
add the set(TOOLCHAIN\_USE\_CUSTOM 1) cmake line to the generic.cmake and/or
target.cmake files located under
`<TOOLCHAIN_ROOT>/cmake/toolchain/<toolchain name>/`.

When **TOOLCHAIN\_USE\_CUSTOM** is set, the `other.h` must be
available out-of-tree and it must include the correct header for the custom
toolchain.
A good location for the `other.h` header file, would be a
directory under the directory specified in `TOOLCHAIN_ROOT` as
`include/toolchain`.
To get the toolchain header included in zephyr’s build, the
**USERINCLUDE** can be set to point to the include directory, as shown
here:

```shell
west build -- -DZEPHYR_TOOLCHAIN_VARIANT=... -DTOOLCHAIN_ROOT=... -DUSERINCLUDE=...
```
