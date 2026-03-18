---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/application/index.html
original_path: develop/application/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Application Development

Note

In this document, we’ll assume:

- your **application directory**, `<app>`, is something like `<home>/zephyrproject/app`
- its **build directory** is `<app>/build`

These terms are defined below. On Linux/macOS, <home> is equivalent to
`~`. On Windows, it’s `%userprofile%`.

Keeping your application inside the workspace (`<home>/zephyrproject`)
makes it easier to use `west build` and other commands with it. (You can
put your application anywhere as long as [ZEPHYR\_BASE](#important-build-vars) is set appropriately, though.)

## Overview

Zephyr’s build system is based on [CMake](https://www.cmake.org).

The build system is application-centric, and requires Zephyr-based applications
to initiate building the Zephyr source code. The application build controls
the configuration and build process of both the application and Zephyr itself,
compiling them into a single binary.

The main zephyr repository contains Zephyr’s source code, configuration files,
and build system. You also likely have installed various [Modules (External projects)](../modules.md#modules)
alongside the zephyr repository, which provide third party source code
integration.

The files in the **application directory** link Zephyr and any modules with the
application. This directory contains all application-specific files, such as
application-specific configuration files and source code.

Here are the files in a simple Zephyr application:

```text
<app>
├── CMakeLists.txt
├── app.overlay
├── prj.conf
├── VERSION
└── src
    └── main.c
```

These contents are:

- **CMakeLists.txt**: This file tells the build system where to find the other
  application files, and links the application directory with Zephyr’s CMake
  build system. This link provides features supported by Zephyr’s build system,
  such as board-specific configuration files, the ability to run and
  debug compiled binaries on real or emulated hardware, and more.
- **app.overlay**: This is a devicetree overlay file that specifies
  application-specific changes which should be applied to the base devicetree
  for any board you build for. The purpose of devicetree overlays is
  usually to configure something about the hardware used by the application.

  The build system looks for `app.overlay` by default, but you can add
  more devicetree overlays, and other default files are also searched for.

  See [Devicetree](../../build/dts/index.md#devicetree) for more information about devicetree.
- **prj.conf**: This is a Kconfig fragment that specifies application-specific
  values for one or more Kconfig options. These application settings are merged
  with other settings to produce the final configuration. The purpose of
  Kconfig fragments is usually to configure the software features used by
  the application.

  The build system looks for `prj.conf` by default, but you can add more
  Kconfig fragments, and other default files are also searched for.

  See [Kconfig Configuration](#application-kconfig) below for more information.
- **VERSION**: A text file that contains several version information fields.
  These fields let you manage the lifecycle of the application and automate
  providing the application version when signing application images.

  See [Application version management](../../build/version/index.md#app-version-details) for more information about this file and how to use it.
- **main.c**: A source code file. Applications typically contain source files
  written in C, C++, or assembly language. The Zephyr convention is to place
  them in a subdirectory of `<app>` named `src`.

Once an application has been defined, you will use CMake to generate a **build
directory**, which contains the files you need to build the application and
Zephyr, then link them together into a final binary you can run on your board.
The easiest way to do this is with [west build](../west/build-flash-debug.md#west-building), but you
can use CMake directly also. Application build artifacts are always generated
in a separate build directory: Zephyr does not support “in-tree” builds.

The following sections describe how to create, build, and run Zephyr
applications, followed by more detailed reference material.

## Application types

We distinguish three basic types of Zephyr application based on where
`<app>` is located:

| Application type | `<app>` location |
| --- | --- |
| [repository](#zephyr-repo-app) | zephyr repository |
| [workspace](#zephyr-workspace-app) | west workspace where Zephyr is installed |
| [freestanding](#zephyr-freestanding-app) | other locations |

We’ll discuss these more below. To learn how the build system supports each
type, see [Zephyr CMake Package](../../build/zephyr_cmake_package.md#cmake-pkg).

### Zephyr repository application

An application located within the `zephyr` source code repository in a Zephyr
[west workspace](../west/workspaces.md#west-workspaces) is referred to as a Zephyr repository
application. In the following example, the [hello\_world sample](../../samples/hello_world/README.md#hello-world) is a Zephyr repository application:

```text
zephyrproject/
├─── .west/
│    └─── config
└─── zephyr/
     ├── arch/
     ├── boards/
     ├── cmake/
     ├── samples/
     │    ├── hello_world/
     │    └── ...
     ├── tests/
     └── ...
```

### Zephyr workspace application

An application located within a [workspace](../west/workspaces.md#west-workspaces), but outside
the zephyr repository itself, is referred to as a Zephyr workspace application.
In the following example, `app` is a Zephyr workspace application:

```text
zephyrproject/
├─── .west/
│    └─── config
├─── zephyr/
├─── bootloader/
├─── modules/
├─── tools/
├─── <vendor/private-repositories>/
└─── applications/
     └── app/
```

### Zephyr freestanding application

A Zephyr application located outside of a Zephyr [workspace](../west/workspaces.md#west-workspaces) is referred to as a Zephyr freestanding application. In the
following example, `app` is a Zephyr freestanding application:

```text
<home>/
├─── zephyrproject/
│     ├─── .west/
│     │    └─── config
│     ├── zephyr/
│     ├── bootloader/
│     ├── modules/
│     └── ...
│
└─── app/
     ├── CMakeLists.txt
     ├── prj.conf
     └── src/
         └── main.c
```

## Creating an Application

In Zephyr, you can either use a reference workspace application or create your application by hand.

### Using a Reference Workspace Application

The [example-application](https://github.com/zephyrproject-rtos/example-application) Git repository contains a reference [workspace
application](#zephyr-workspace-app). It is recommended to use it as a reference
when creating your own application as described in the following sections.

The example-application repository demonstrates how to use several
commonly-used features, such as:

- Custom [board ports](../../hardware/porting/board_porting.md#board-porting-guide)
- Custom [devicetree bindings](../../build/dts/bindings.md#dt-bindings)
- Custom [device drivers](../../kernel/drivers/index.md#device-model-api)
- Continuous Integration (CI) setup, including using [twister](../test/twister.md#twister-script)
- A custom west [extension command](../west/extensions.md#west-extensions)

#### Basic example-application Usage

The easiest way to get started with the example-application repository within
an existing Zephyr workspace is to follow these steps:

```shell
cd <home>/zephyrproject
git clone https://github.com/zephyrproject-rtos/example-application my-app
```

The directory name `my-app` above is arbitrary: change it as needed. You
can now go into this directory and adapt its contents to suit your needs. Since
you are using an existing Zephyr workspace, you can use `west build` or any
other west commands to build, flash, and debug.

#### Advanced example-application Usage

You can also use the example-application repository as a starting point for
building your own customized Zephyr-based software distribution. This lets you
do things like:

- remove Zephyr modules you don’t need
- add additional custom repositories of your own
- override repositories provided by Zephyr with your own versions
- share the results with others and collaborate further

The example-application repository contains a `west.yml` file and is
therefore also a west [manifest repository](../west/basics.md#west-workspace). Use this to
create a new, customized workspace by following these steps:

```shell
cd <home>
mkdir my-workspace
cd my-workspace
git clone https://github.com/zephyrproject-rtos/example-application my-manifest-repo
west init -l my-manifest-repo
```

This will create a new workspace with the [T2 topology](../west/workspaces.md#west-t2), with
`my-manifest-repo` as the manifest repository. The `my-workspace`
and `my-manifest-repo` names are arbitrary: change them as needed.

Next, customize the manifest repository. The initial contents of this
repository will match the example-application’s contents when you clone it. You
can then edit `my-manifest-repo/west.yml` to your liking, changing the
set of repositories in it as you wish. See [Manifest Imports](../west/manifest.md#west-manifest-import) for many
examples of how to add or remove different repositories from your workspace as
needed. Make any other changes you need to other files.

When you are satisfied, you can run:

```text
west update
```

and your workspace will be ready for use.

If you push the resulting `my-manifest-repo` repository somewhere else,
you can share your work with others. For example, let’s say you push the
repository to `https://git.example.com/my-manifest-repo`. Other people can
then set up a matching workspace by running:

```text
west init -m https://git.example.com/my-manifest-repo my-workspace
cd my-workspace
west update
```

From now on, you can collaborate on the shared software by pushing changes to
the repositories you are using and updating `my-manifest-repo/west.yml`
as needed to add and remove repositories, or change their contents.

### Creating an Application by Hand

You can follow these steps to create a basic application directory from
scratch. However, using the [example-application](https://github.com/zephyrproject-rtos/example-application) repository or one of
Zephyr’s [Samples and Demos](../../samples/index.md#samples-and-demos) as a starting point is likely to be easier.

1. Create an application directory.

   For example, in a Unix shell or Windows `cmd.exe` prompt:

   ```shell
   mkdir app
   ```

   Warning

   Building Zephyr or creating an application in a directory with spaces
   anywhere on the path is not supported. So the Windows path
   `C:\Users\YourName\app` will work, but
   `C:\Users\Your Name\app` will not.
2. Create your source code files.

   It’s recommended to place all application source code in a subdirectory
   named `src`. This makes it easier to distinguish between project
   files and sources.

   Continuing the previous example, enter:

   ```shell
   cd app
   mkdir src
   ```
3. Place your application source code in the `src` sub-directory. For
   this example, we’ll assume you created a file named `src/main.c`.
4. Create a file named `CMakeLists.txt` in the `app` directory with the
   following contents:

   ```cmake
   cmake_minimum_required(VERSION 3.20.0)

   find_package(Zephyr)
   project(my_zephyr_app)

   target_sources(app PRIVATE src/main.c)
   ```

   Notes:

   - The `cmake_minimum_required()` call is required by CMake. It is also
     invoked by the Zephyr package on the next line. CMake will error out if
     its version is older than either the version in your
     `CMakeLists.txt` or the version number in the Zephyr package.
   - `find_package(Zephyr)` pulls in the Zephyr build system, which creates a
     CMake target named `app` (see [Zephyr CMake Package](../../build/zephyr_cmake_package.md#cmake-pkg)). Adding sources to this
     target is how you include them in the build. The Zephyr package will
     define `Zephyr-Kernel` as a CMake project and enable support for the
     `C`, `CXX`, `ASM` languages.
   - `project(my_zephyr_app)` defines your application’s CMake
     project. This must be called after `find_package(Zephyr)` to avoid
     interference with Zephyr’s `project(Zephyr-Kernel)`.
   - `target_sources(app PRIVATE src/main.c)` is to add your source file to
     the `app` target. This must come after `find_package(Zephyr)` which
     defines the target. You can add as many files as you want with
     `target_sources()`.
5. Create at least one Kconfig fragment for your application (usually named
   `prj.conf`) and set Kconfig option values needed by your application
   there. See [Kconfig Configuration](#application-kconfig). If no Kconfig options need to be set,
   create an empty file.
6. Configure any devicetree overlays needed by your application, usually in a
   file named `app.overlay`. See [Set devicetree overlays](../../build/dts/howtos.md#set-devicetree-overlays).
7. Set up any other files you may need, such as [twister](../test/twister.md#twister-script)
   configuration files, continuous integration files, documentation, etc.

## Important Build System Variables

You can control the Zephyr build system using many variables. This
section describes the most important ones that every Zephyr developer
should know about.

Note

The variables **BOARD**, **CONF\_FILE**, and
**DTC\_OVERLAY\_FILE** can be supplied to the build system in
3 ways (in order of precedence):

- As a parameter to the `west build` or `cmake` invocation via the
  `-D` command-line switch. If you have multiple overlay files, you should
  use quotations, `"file1.overlay;file2.overlay"`
- As [Environment Variables](../env_vars.md#env-vars).
- As a `set(<VARIABLE> <VALUE>)` statement in your `CMakeLists.txt`

- **ZEPHYR\_BASE**: Zephyr base variable used by the build system.
  `find_package(Zephyr)` will automatically set this as a cached CMake
  variable. But `ZEPHYR_BASE` can also be set as an environment variable in
  order to force CMake to use a specific Zephyr installation.
- **BOARD**: Selects the board that the application’s build
  will use for the default configuration. See [Supported Boards](../../boards/index.md#boards) for
  built-in boards, and [Board Porting Guide](../../hardware/porting/board_porting.md#board-porting-guide) for information on
  adding board support.
- **CONF\_FILE**: Indicates the name of one or more Kconfig configuration
  fragment files. Multiple filenames can be separated with either spaces or
  semicolons. Each file includes Kconfig configuration values that override
  the default configuration values.

  See [The Initial Configuration](../../build/kconfig/setting.md#initial-conf) for more information.
- **EXTRA\_CONF\_FILE**: Additional Kconfig configuration fragment files.
  Multiple filenames can be separated with either spaces or semicolons. This
  can be useful in order to leave **CONF\_FILE** at its default value,
  but “mix in” some additional configuration options.
- **DTC\_OVERLAY\_FILE**: One or more devicetree overlay files to use.
  Multiple files can be separated with semicolons.
  See [Set devicetree overlays](../../build/dts/howtos.md#set-devicetree-overlays) for examples and [Introduction to devicetree](../../build/dts/intro.md#devicetree-intro)
  for information about devicetree and Zephyr.
- **EXTRA\_DTC\_OVERLAY\_FILE**: Additional devicetree overlay files to use.
  Multiple files can be separated with semicolons. This can be useful to leave
  **DTC\_OVERLAY\_FILE** at its default value, but “mix in” some additional
  overlay files.
- **SHIELD**: see [Shields](../../hardware/porting/shields.md#shields)
- **ZEPHYR\_MODULES**: A [CMake list](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#lists) containing absolute paths of
  additional directories with source code, Kconfig, etc. that should be used in
  the application build. See [Modules (External projects)](../modules.md#modules) for details. If you set this
  variable, it must be a complete list of all modules to use, as the build
  system will not automatically pick up any modules from west.
- **EXTRA\_ZEPHYR\_MODULES**: Like **ZEPHYR\_MODULES**, except these
  will be added to the list of modules found via west, instead of replacing it.
- **FILE\_SUFFIX**: Optional suffix for filenames that will be added to Kconfig
  fragments and devicetree overlays (if these files exists, otherwise will fallback to
  the name without the prefix). See [File Suffixes](#application-file-suffixes) for details.

Note

You can use a [Zephyr Build Configuration CMake packages](../../build/zephyr_cmake_package.md#cmake-build-config-package) to share common settings for
these variables.

## Application CMakeLists.txt

Every application must have a `CMakeLists.txt` file. This file is the
entry point, or top level, of the build system. The final `zephyr.elf`
image contains both the application and the kernel libraries.

This section describes some of what you can do in your `CMakeLists.txt`.
Make sure to follow these steps in order.

1. If you only want to build for one board, add the name of the board
   configuration for your application on a new line. For example:

   ```cmake
   set(BOARD qemu_x86)
   ```

   Refer to [Supported Boards](../../boards/index.md#boards) for more information on available boards.

   The Zephyr build system determines a value for **BOARD** by checking
   the following, in order (when a BOARD value is found, CMake stops looking
   further down the list):

   - Any previously used value as determined by the CMake cache takes highest
     precedence. This ensures you don’t try to run a build with a different
     **BOARD** value than you set during the build configuration step.
   - Any value given on the CMake command line (directly or indirectly via
     `west build`) using `-DBOARD=YOUR_BOARD` will be checked for and
     used next.
   - If an [environment variable](../env_vars.md#env-vars) `BOARD` is set, its value
     will then be used.
   - Finally, if you set `BOARD` in your application `CMakeLists.txt`
     as described in this step, this value will be used.
2. If your application uses a configuration file or files other than
   the usual `prj.conf` (or `prj_YOUR_BOARD.conf`, where
   `YOUR_BOARD` is a board name), add lines setting the
   **CONF\_FILE** variable to these files appropriately.
   If multiple filenames are given, separate them by a single space or
   semicolon. CMake lists can be used to build up configuration fragment
   files in a modular way when you want to avoid setting **CONF\_FILE**
   in a single place. For example:

   ```cmake
   set(CONF_FILE "fragment_file1.conf")
   list(APPEND CONF_FILE "fragment_file2.conf")
   ```

   See [The Initial Configuration](../../build/kconfig/setting.md#initial-conf) for more information.
3. If your application uses devicetree overlays, you may need to set
   [DTC\_OVERLAY\_FILE](#important-build-vars).
   See [Set devicetree overlays](../../build/dts/howtos.md#set-devicetree-overlays).
4. If your application has its own kernel configuration options,
   create a `Kconfig` file in the same directory as your
   application’s `CMakeLists.txt`.

   See [the Kconfig section of the manual](../../build/kconfig/index.md#kconfig) for detailed
   Kconfig documentation.

   An (unlikely) advanced use case would be if your application has its own
   unique configuration **options** that are set differently depending on the
   build configuration.

   If you just want to set application specific **values** for existing Zephyr
   configuration options, refer to the **CONF\_FILE** description above.

   Structure your `Kconfig` file like this:

   ```kconfig
   # SPDX-License-Identifier: Apache-2.0

   mainmenu "Your Application Name"

   # Your application configuration options go here

   # Sources Kconfig.zephyr in the Zephyr root directory.
   #
   # Note: All 'source' statements work relative to the Zephyr root directory (due
   # to the $srctree environment variable being set to $ZEPHYR_BASE). If you want
   # to 'source' relative to the current Kconfig file instead, use 'rsource' (or a
   # path relative to the Zephyr root).
   source "Kconfig.zephyr"
   ```

   Note

   Environment variables in `source` statements are expanded directly, so
   you do not need to define an `option env="ZEPHYR_BASE"` Kconfig
   “bounce” symbol. If you use such a symbol, it must have the same name as
   the environment variable.

   See [Kconfig extensions](../../build/kconfig/extensions.md#kconfig-extensions) for more information.

   The `Kconfig` file is automatically detected when placed in
   the application directory, but it is also possible for it to be
   found elsewhere if the CMake variable **KCONFIG\_ROOT** is
   set with an absolute path.
5. Specify that the application requires Zephyr on a new line, **after any
   lines added from the steps above**:

   ```cmake
   find_package(Zephyr)
   project(my_zephyr_app)
   ```

   Note

   `find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})` can be used if
   enforcing a specific Zephyr installation by explicitly
   setting the `ZEPHYR_BASE` environment variable should be
   supported. All samples in Zephyr supports the `ZEPHYR_BASE`
   environment variable.
6. Now add any application source files to the ‘app’ target
   library, each on their own line, like so:

   ```cmake
   target_sources(app PRIVATE src/main.c)
   ```

Below is a simple example `CMakeList.txt`:

```cmake
set(BOARD qemu_x86)

find_package(Zephyr)
project(my_zephyr_app)

target_sources(app PRIVATE src/main.c)
```

The Cmake property `HEX_FILES_TO_MERGE`
leverages the application configuration provided by
Kconfig and CMake to let you merge externally built hex files
with the hex file generated when building the Zephyr application.
For example:

```cmake
set_property(GLOBAL APPEND PROPERTY HEX_FILES_TO_MERGE
    ${app_bootloader_hex}
    ${PROJECT_BINARY_DIR}/${KERNEL_HEX_NAME}
    ${app_provision_hex})
```

## CMakeCache.txt

CMake uses a CMakeCache.txt file as persistent key/value string
storage used to cache values between runs, including compile and build
options and paths to library dependencies. This cache file is created
when CMake is run in an empty build folder.

For more details about the CMakeCache.txt file see the official CMake
documentation [runningcmake](http://cmake.org/runningcmake/) .

## Application Configuration

### Application Configuration Directory

Zephyr will use configuration files from the application’s configuration
directory except for files with an absolute path provided by the arguments
described earlier, for example `CONF_FILE`, `EXTRA_CONF_FILE`,
`DTC_OVERLAY_FILE`, and `EXTRA_DTC_OVERLAY_FILE`.

The application configuration directory is defined by the
`APPLICATION_CONFIG_DIR` variable.

`APPLICATION_CONFIG_DIR` will be set by one of the sources below with the
highest priority listed first.

1. If `APPLICATION_CONFIG_DIR` is specified by the user with
   `-DAPPLICATION_CONFIG_DIR=<path>` or in a CMake file before
   `find_package(Zephyr)` then this folder is used a the application’s
   configuration directory.
2. The application’s source directory.

### Kconfig Configuration

Application configuration options are usually set in `prj.conf` in the
application directory. For example, C++ support could be enabled with this
assignment:

```text
CONFIG_CPP=y
```

Looking at [existing samples](../../samples/index.md#samples-and-demos) is a good way to get
started.

See [Setting Kconfig configuration values](../../build/kconfig/setting.md#setting-configuration-values) for detailed documentation on setting
Kconfig configuration values. The [The Initial Configuration](../../build/kconfig/setting.md#initial-conf) section on the same page
explains how the initial configuration is derived. See [Kconfig Search](../../kconfig.md#kconfig-search)
for a complete list of configuration options.
See [Hardening Tool](../../security/hardening-tool.md#hardening) for security information related with Kconfig options.

The other pages in the [Kconfig section of the manual](../../build/kconfig/index.md#kconfig) are also
worth going through, especially if you planning to add new configuration
options.

#### Experimental features

Zephyr is a project under constant development and thus there are features that
are still in early stages of their development cycle. Such features will be
marked `[EXPERIMENTAL]` in their Kconfig title.

The [`CONFIG_WARN_EXPERIMENTAL`](../../kconfig.md#CONFIG_WARN_EXPERIMENTAL "CONFIG_WARN_EXPERIMENTAL") setting can be used to enable warnings
at CMake configure time if any experimental feature is enabled.

```text
CONFIG_WARN_EXPERIMENTAL=y
```

For example, if option `CONFIG_FOO` is experimental, then enabling it and
[`CONFIG_WARN_EXPERIMENTAL`](../../kconfig.md#CONFIG_WARN_EXPERIMENTAL "CONFIG_WARN_EXPERIMENTAL") will print the following warning at
CMake configure time when you build an application:

```text
warning: Experimental symbol FOO is enabled.
```

### Devicetree Overlays

See [Set devicetree overlays](../../build/dts/howtos.md#set-devicetree-overlays).

### File Suffixes

Zephyr applications might want to have a single code base with multiple configurations for
different build/product variants which would necessitate different Kconfig options and devicetree
configuration. In order to better configure this, Zephyr provides a **FILE\_SUFFIX** option
when configuring applications that can be automatically appended to filenames. This is applied to
Kconfig fragments and board overlays but with a fallback so that if such files do not exist, the
files without these suffixes will be used instead.

Given the following example project layout:

```text
<app>
├── CMakeLists.txt
├── prj.conf
├── prj_mouse.conf
├── boards
│   ├── native_posix.overlay
│   └── qemu_cortex_m3_mouse.overlay
└── src
    └── main.c
```

- If this is built normally without `FILE_SUFFIX` being defined for `native_posix` then
  `prj.conf` and `boards/native_posix.overlay` will be used.
- If this is build normally without `FILE_SUFFIX` being defined for `qemu_cortex_m3` then
  `prj.conf` will be used, no application devicetree overlay will be used.
- If this is built with `FILE_SUFFIX` set to `mouse` for `native_posix` then
  `prj_mouse.conf` and `boards/native_posix.overlay` will be used (there is no
  `native_posix_mouse.overlay` file so it falls back to `native_posix.overlay`).
- If this is build with `FILE_SUFFIX` set to `mouse` for `qemu_cortex_m3` then
  `prj_mouse.conf` will be used and `boards/qemu_cortex_m3_mouse.overlay` will be used.

Note

When `CONF_FILE` is set in the form of `prj_X.conf` then the `X` will be used as the
build type. If this is combined with `FILE_SUFFIX` then the file suffix option will take
priority over the build type.

## Application-Specific Code

Application-specific source code files are normally added to the
application’s `src` directory. If the application adds a large
number of files the developer can group them into sub-directories
under `src`, to whatever depth is needed.

Application-specific source code should not use symbol name prefixes that have
been reserved by the kernel for its own use. For more information, see [Naming
Conventions](https://github.com/zephyrproject-rtos/zephyr/wiki/Naming-Conventions).

### Third-party Library Code

It is possible to build library code outside the application’s `src`
directory but it is important that both application and library code targets
the same Application Binary Interface (ABI). On most architectures there are
compiler flags that control the ABI targeted, making it important that both
libraries and applications have certain compiler flags in common. It may also
be useful for glue code to have access to Zephyr kernel header files.

To make it easier to integrate third-party components, the Zephyr
build system has defined CMake functions that give application build
scripts access to the zephyr compiler options. The functions are
documented and defined in [cmake/modules/extensions.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/main/cmake/modules/extensions.cmake)
and follow the naming convention `zephyr_get_<type>_<format>`.

The following variables will often need to be exported to the
third-party build system.

- `CMAKE_C_COMPILER`, `CMAKE_AR`.
- `ARCH` and `BOARD`, together with several variables that identify the
  Zephyr kernel version.

[samples/application\_development/external\_lib](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/application_development/external_lib) is a sample
project that demonstrates some of these features.

## Building an Application

The Zephyr build system compiles and links all components of an application
into a single application image that can be run on simulated hardware or real
hardware.

Like any other CMake-based system, the build process takes place [in
two stages](../../build/cmake/index.md#cmake-details). First, build files (also known as a buildsystem)
are generated using the `cmake` command-line tool while specifying a
generator. This generator determines the native build tool the buildsystem
will use in the second stage.
The second stage runs the native build tool to actually build the
source files and generate an image. To learn more about these concepts refer to
the [CMake introduction](https://cmake.org/cmake/help/latest/manual/cmake.1.html#description) in the official CMake documentation.

Although the default build tool in Zephyr is [west](../west/index.md#west), Zephyr’s
meta-tool, which invokes `cmake` and the underlying build tool (`ninja` or
`make`) behind the scenes, you can also choose to invoke `cmake` directly if
you prefer. On Linux and macOS you can choose between the `make` and
`ninja`
generators (i.e. build tools), whereas on Windows you need to use `ninja`,
since `make` is not supported on this platform.
For simplicity we will use `ninja` throughout this guide, and if you
choose to use `west build` to build your application know that it will
default to `ninja` under the hood.

As an example, let’s build the Hello World sample for the `reel_board`:

Using west:

```shell
west build -b reel_board samples/hello_world
```

Using CMake and ninja:

```shell
# Use cmake to configure a Ninja-based buildsystem:
cmake -Bbuild -GNinja -DBOARD=reel_board samples/hello_world

# Now run the build tool on the generated build system:
ninja -Cbuild
```

On Linux and macOS, you can also build with `make` instead of `ninja`:

Using west:

- to use `make` just once, add `-- -G"Unix Makefiles"` to the west build
  command line; see the [west build](../west/build-flash-debug.md#west-building-generator)
  documentation for an example.
- to use `make` by default from now on, run `west config build.generator
  "Unix Makefiles"`.

Using CMake directly:

```shell
# Use cmake to configure a Make-based buildsystem:
cmake -Bbuild -DBOARD=reel_board samples/hello_world

# Now run the build tool on the generated build system:
make -Cbuild
```

### Basics

1. Navigate to the application directory `<app>`.
2. Enter the following commands to build the application’s `zephyr.elf`
   image for the board specified in the command-line parameters:

   Using west:

   ```shell
   west build -b <board>
   ```

   Using CMake and ninja:

   ```shell
   mkdir build && cd build

   # Use cmake to configure a Ninja-based buildsystem:
   cmake -GNinja -DBOARD=<board> ..

   # Now run the build tool on the generated build system:
   ninja
   ```

   If desired, you can build the application using the configuration settings
   specified in an alternate `.conf` file using the `CONF_FILE`
   parameter. These settings will override the settings in the application’s
   `.config` file or its default `.conf` file. For example:

   Using west:

   ```shell
   west build -b <board> -- -DCONF_FILE=prj.alternate.conf
   ```

   Using CMake and ninja:

   ```shell
   mkdir build && cd build
   cmake -GNinja -DBOARD=<board> -DCONF_FILE=prj.alternate.conf ..
   ninja
   ```

   As described in the previous section, you can instead choose to permanently
   set the board and configuration settings by either exporting **BOARD**
   and **CONF\_FILE** environment variables or by setting their values
   in your `CMakeLists.txt` using `set()` statements.
   Additionally, `west` allows you to [set a default board](../west/build-flash-debug.md#west-building-config).

### Build Directory Contents

When using the Ninja generator a build directory looks like this:

```text
<app>/build
├── build.ninja
├── CMakeCache.txt
├── CMakeFiles
├── cmake_install.cmake
├── rules.ninja
└── zephyr
```

The most notable files in the build directory are:

- `build.ninja`, which can be invoked to build the application.
- A `zephyr` directory, which is the working directory of the
  generated build system, and where most generated files are created and
  stored.

After running `ninja`, the following build output files will be written to
the `zephyr` sub-directory of the build directory. (This is **not the
Zephyr base directory**, which contains the Zephyr source code etc. and is
described above.)

- `.config`, which contains the configuration settings
  used to build the application.

  Note

  The previous version of `.config` is saved to `.config.old`
  whenever the configuration is updated. This is for convenience, as
  comparing the old and new versions can be handy.
- Various object files (`.o` files and `.a` files) containing
  compiled kernel and application code.
- `zephyr.elf`, which contains the final combined application and
  kernel binary. Other binary output formats, such as `.hex` and
  `.bin`, are also supported.

### Rebuilding an Application

Application development is usually fastest when changes are continually tested.
Frequently rebuilding your application makes debugging less painful
as the application becomes more complex. It’s usually a good idea to
rebuild and test after any major changes to the application’s source files,
CMakeLists.txt files, or configuration settings.

Important

The Zephyr build system rebuilds only the parts of the application image
potentially affected by the changes. Consequently, rebuilding an application
is often significantly faster than building it the first time.

Sometimes the build system doesn’t rebuild the application correctly
because it fails to recompile one or more necessary files. You can force
the build system to rebuild the entire application from scratch with the
following procedure:

1. Open a terminal console on your host computer, and navigate to the
   build directory `<app>/build`.
2. Enter one of the following commands, depending on whether you want to use
   `west` or `cmake` directly to delete the application’s generated
   files, except for the `.config` file that contains the
   application’s current configuration information.

   ```shell
   west build -t clean
   ```

   or

   ```shell
   ninja clean
   ```

   Alternatively, enter one of the following commands to delete *all*
   generated files, including the `.config` files that contain
   the application’s current configuration information for those board
   types.

   ```shell
   west build -t pristine
   ```

   or

   ```shell
   ninja pristine
   ```

   If you use west, you can take advantage of its capability to automatically
   [make the build folder pristine](../west/build-flash-debug.md#west-building-config) whenever it is
   required.
3. Rebuild the application normally following the steps specified
   in [Building an Application](#build-an-application) above.

### Building for a board revision

The Zephyr build system has support for specifying multiple hardware revisions
of a single board with small variations. Using revisions allows the board
support files to make minor adjustments to a board configuration without
duplicating all the files described in [Create your board directory](../../hardware/porting/board_porting.md#create-your-board-directory) for
each revision.

To build for a particular revision, use `<board>@<revision>` instead of plain
`<board>`. For example:

Using west:

```shell
west build -b <board>@<revision>
```

Using CMake and ninja:

```shell
mkdir build && cd build
cmake -GNinja -DBOARD=<board>@<revision> ..
ninja
```

Check your board’s documentation for details on whether it has multiple
revisions, and what revisions are supported.

When targeting a board revision, the active revision will be printed at CMake
configure time, like this:

```shell
-- Board: plank, Revision: 1.5.0
```

## Run an Application

An application image can be run on a real board or emulated hardware.

### Running on a Board

Most boards supported by Zephyr let you flash a compiled binary using
the `flash` target to copy the binary to the board and run it.
Follow these instructions to flash and run an application on real
hardware:

1. Build your application, as described in [Building an Application](#build-an-application).
2. Make sure your board is attached to your host computer. Usually, you’ll do
   this via USB.
3. Run one of these console commands from the build directory,
   `<app>/build`, to flash the compiled Zephyr image and run it on
   your board:

   ```shell
   west flash
   ```

   or

   ```shell
   ninja flash
   ```

The Zephyr build system integrates with the board support files to
use hardware-specific tools to flash the Zephyr binary to your
hardware, then run it.

Each time you run the flash command, your application is rebuilt and flashed
again.

In cases where board support is incomplete, flashing via the Zephyr build
system may not be supported. If you receive an error message about flash
support being unavailable, consult [your board’s documentation](../../boards/index.md#boards)
for additional information on how to flash your board.

Note

When developing on Linux, it’s common to need to install
board-specific udev rules to enable USB device access to
your board as a non-root user. If flashing fails,
consult your board’s documentation to see if this is
necessary.

### Running in an Emulator

Zephyr has built-in emulator support for QEMU.
It allows you to run and test an application virtually, before
(or in lieu of) loading and running it on actual target hardware.

Check out [Beyond the Getting Started Guide](../beyond-GSG.md#beyond-gsg) for additional steps needed on Windows.

Follow these instructions to run an application via QEMU:

1. Build your application for one of the QEMU boards, as described in
   [Building an Application](#build-an-application).

   For example, you could set `BOARD` to:

   - `qemu_x86` to emulate running on an x86-based board
   - `qemu_cortex_m3` to emulate running on an ARM Cortex M3-based board
2. Run one of these console commands from the build directory,
   `<app>/build`, to run the Zephyr binary in QEMU:

   ```shell
   west build -t run
   ```

   or

   ```shell
   ninja run
   ```
3. Press `Ctrl A, X` to stop the application from running
   in QEMU.

   The application stops running and the terminal console prompt
   redisplays.

Each time you execute the run command, your application is rebuilt and run
again.

Note

If the (Linux only) [Zephyr SDK](../toolchains/zephyr_sdk.md#toolchain-zephyr-sdk) is installed, the `run`
target will use the SDK’s QEMU binary by default. To use another version of
QEMU, [set the environment variable](../env_vars.md#env-vars) `QEMU_BIN_PATH`
to the path of the QEMU binary you want to use instead.

Note

You can choose a specific emulator by appending `_<emulator>` to your
target name, for example `west build -t run_qemu` or `ninja run_qemu`
for QEMU.

## Custom Board, Devicetree and SOC Definitions

In cases where the board or platform you are developing for is not yet
supported by Zephyr, you can add board, Devicetree and SOC definitions
to your application without having to add them to the Zephyr tree.

The structure needed to support out-of-tree board and SOC development
is similar to how boards and SOCs are maintained in the Zephyr tree. By using
this structure, it will be much easier to upstream your platform related work into
the Zephyr tree after your initial development is done.

Add the custom board to your application or a dedicated repository using the
following structure:

```shell
boards/
soc/
CMakeLists.txt
prj.conf
README.rst
src/
```

where the `boards` directory hosts the board you are building for:

```shell
.
├── boards
│   └── x86
│       └── my_custom_board
│           ├── doc
│           │   └── img
│           └── support
└── src
```

and the `soc` directory hosts any SOC code. You can also have boards that are
supported by a SOC that is available in the Zephyr tree.

### Boards

Use the proper architecture folder name (e.g., `x86`, `arm`, etc.)
under `boards` for `my_custom_board`. (See [Supported Boards](../../boards/index.md#boards) for a
list of board architectures.)

Documentation (under `doc/`) and support files (under `support/`) are optional, but
will be needed when submitting to Zephyr.

The contents of `my_custom_board` should follow the same guidelines for any
Zephyr board, and provide the following files:

```text
my_custom_board_defconfig
my_custom_board.dts
my_custom_board.yaml
board.cmake
board.h
CMakeLists.txt
doc/
Kconfig.board
Kconfig.defconfig
pinmux.c
support/
```

Once the board structure is in place, you can build your application
targeting this board by specifying the location of your custom board
information with the `-DBOARD_ROOT` parameter to the CMake
build system:

Using west:

```shell
west build -b <board name> -- -DBOARD_ROOT=<path to boards>
```

Using CMake and ninja:

```shell
cmake -Bbuild -GNinja -DBOARD=<board name> -DBOARD_ROOT=<path to boards> .
ninja -Cbuild
```

This will use your custom board configuration and will generate the
Zephyr binary into your application directory.

You can also define the `BOARD_ROOT` variable in the application
`CMakeLists.txt` file. Make sure to do so **before** pulling in the Zephyr
boilerplate with `find_package(Zephyr ...)`.

Note

When specifying `BOARD_ROOT` in a CMakeLists.txt, then an absolute path must
be provided, for example `list(APPEND BOARD_ROOT ${CMAKE_CURRENT_SOURCE_DIR}/<extra-board-root>)`.
When using `-DBOARD_ROOT=<board-root>` both absolute and relative paths can
be used. Relative paths are treated relatively to the application directory.

### SOC Definitions

Similar to board support, the structure is similar to how SOCs are maintained in
the Zephyr tree, for example:

```text
soc
└── arm
    └── st_stm32
            ├── common
            └── stm32l0
```

The file [soc/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/Kconfig) will create the top-level
`SoC/CPU/Configuration Selection` menu in Kconfig.

Out of tree SoC definitions can be added to this menu using the `SOC_ROOT`
CMake variable. This variable contains a semicolon-separated list of directories
which contain SoC support files.

Following the structure above, the following files can be added to load
more SoCs into the menu.

```text
soc
└── arm
    └── st_stm32
            ├── Kconfig
            ├── Kconfig.soc
            └── Kconfig.defconfig
```

The Kconfig files above may describe the SoC or load additional SoC Kconfig files.

An example of loading `stm31l0` specific Kconfig files in this structure:

```text
soc
└── arm
    └── st_stm32
            ├── Kconfig.soc
            └── stm32l0
                └── Kconfig.series
```

can be done with the following content in `st_stm32/Kconfig.soc`:

```text
rsource "*/Kconfig.series"
```

Once the SOC structure is in place, you can build your application
targeting this platform by specifying the location of your custom platform
information with the `-DSOC_ROOT` parameter to the CMake
build system:

Using west:

```shell
west build -b <board name> -- -DSOC_ROOT=<path to soc> -DBOARD_ROOT=<path to boards>
```

Using CMake and ninja:

```shell
cmake -Bbuild -GNinja -DBOARD=<board name> -DSOC_ROOT=<path to soc> -DBOARD_ROOT=<path to boards> .
ninja -Cbuild
```

This will use your custom platform configurations and will generate the
Zephyr binary into your application directory.

See [Build settings](../modules.md#modules-build-settings) for information on setting SOC\_ROOT in a module’s
`zephyr/module.yml` file.

Or you can define the `SOC_ROOT` variable in the application
`CMakeLists.txt` file. Make sure to do so **before** pulling in the
Zephyr boilerplate with `find_package(Zephyr ...)`.

Note

When specifying `SOC_ROOT` in a CMakeLists.txt, then an absolute path must
be provided, for example `list(APPEND SOC_ROOT ${CMAKE_CURRENT_SOURCE_DIR}/<extra-soc-root>`.
When using `-DSOC_ROOT=<soc-root>` both absolute and relative paths can be
used. Relative paths are treated relatively to the application directory.

### Devicetree Definitions

Devicetree directory trees are found in `APPLICATION_SOURCE_DIR`,
`BOARD_DIR`, and `ZEPHYR_BASE`, but additional trees, or DTS\_ROOTs,
can be added by creating this directory tree:

```text
include/
dts/common/
dts/arm/
dts/
dts/bindings/
```

Where ‘arm’ is changed to the appropriate architecture. Each directory
is optional. The binding directory contains bindings and the other
directories contain files that can be included from DT sources.

Once the directory structure is in place, you can use it by specifying
its location through the `DTS_ROOT` CMake Cache variable:

Using west:

```shell
west build -b <board name> -- -DDTS_ROOT=<path to dts root>
```

Using CMake and ninja:

```shell
cmake -Bbuild -GNinja -DBOARD=<board name> -DDTS_ROOT=<path to dts root> .
ninja -Cbuild
```

You can also define the variable in the application `CMakeLists.txt`
file. Make sure to do so **before** pulling in the Zephyr boilerplate with
`find_package(Zephyr ...)`.

Note

When specifying `DTS_ROOT` in a CMakeLists.txt, then an absolute path must
be provided, for example `list(APPEND DTS_ROOT ${CMAKE_CURRENT_SOURCE_DIR}/<extra-dts-root>`.
When using `-DDTS_ROOT=<dts-root>` both absolute and relative paths can be
used. Relative paths are treated relatively to the application directory.

Devicetree source are passed through the C preprocessor, so you can
include files that can be located in a `DTS_ROOT` directory. By
convention devicetree include files have a `.dtsi` extension.

You can also use the preprocessor to control the content of a devicetree
file, by specifying directives through the `DTS_EXTRA_CPPFLAGS` CMake
Cache variable:

Using west:

```shell
west build -b <board name> -- -DDTS_EXTRA_CPPFLAGS=-DTEST_ENABLE_FEATURE
```

Using CMake and ninja:

```shell
cmake -Bbuild -GNinja -DBOARD=<board name> -DDTS_EXTRA_CPPFLAGS=-DTEST_ENABLE_FEATURE .
ninja -Cbuild
```
