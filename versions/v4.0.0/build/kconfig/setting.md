---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/kconfig/setting.html
original_path: build/kconfig/setting.html
---

# Setting Kconfig configuration values

The [menuconfig and guiconfig interfaces](menuconfig.md#menuconfig) can be used to test
out configurations during application development. This page explains how to
make settings permanent.

All Kconfig options can be searched in the [Kconfig search page](../../kconfig.md#kconfig-search).

Note

Before making changes to Kconfig files, it’s a good idea to also go through
the [Kconfig - Tips and Best Practices](tips.md#kconfig-tips-and-tricks) page.

## Visible and invisible Kconfig symbols

When making Kconfig changes, it’s important to understand the difference
between *visible* and *invisible* symbols.

- A visible symbol is a symbol defined with a prompt. Visible symbols show
  up in the interactive configuration interfaces (hence *visible*), and can be
  set in configuration files.

  Here’s an example of a visible symbol:

  ```kconfig
  config FPU
     bool "Support floating point operations"
     depends on HAS_FPU
  ```

  The symbol is shown like this in `menuconfig`, where it can be toggled:

  ```text
  [ ] Support floating point operations
  ```
- An *invisible* symbol is a symbol without a prompt. Invisible symbols are
  not shown in the interactive configuration interfaces, and users have no
  direct control over their value. They instead get their value from defaults
  or from other symbols.

  Here’s an example of an invisible symbol:

  ```kconfig
  config CPU_HAS_FPU
     bool
     help
       This symbol is y if the CPU has a hardware floating point unit.
  ```

  In this case, `CPU_HAS_FPU` is enabled through other symbols having
  `select CPU_HAS_FPU`.

## Setting symbols in configuration files

Visible symbols can be configured by setting them in configuration files. The
initial configuration is produced by merging a `*_defconfig` file for the
board with application settings, usually from `prj.conf`. See
[The Initial Configuration](#initial-conf) below for more details.

Assignments in configuration files use this syntax:

```cfg
CONFIG_<symbol name>=<value>
```

There should be no spaces around the equals sign.

`bool` symbols can be enabled or disabled by setting them to `y` or `n`,
respectively. The `FPU` symbol from the example above could be enabled like
this:

```cfg
CONFIG_FPU=y
```

Note

A boolean symbol can also be set to `n` with a comment formatted like
this:

```cfg
# CONFIG_SOME_OTHER_BOOL is not set
```

This is the format you will see in the merged configuration
saved to `zephyr/.config` in the build directory.

This style is accepted for historical reasons: Kconfig configuration files
can be parsed as makefiles (though Zephyr doesn’t use this). Having
`n`-valued symbols correspond to unset variables simplifies tests in Make.

Other symbol types are assigned like this:

```cfg
CONFIG_SOME_STRING="cool value"
CONFIG_SOME_INT=123
```

Comments use a #:

```cfg
# This is a comment
```

Assignments in configuration files are only respected if the dependencies for
the symbol are satisfied. A warning is printed otherwise. To figure out what
the dependencies of a symbol are, use one of the [interactive
configuration interfaces](menuconfig.md#menuconfig) (you can jump directly to a symbol with
`/`), or look up the symbol in the [Kconfig search page](../../kconfig.md#kconfig-search).

## The Initial Configuration

The initial configuration for an application comes from merging configuration
settings from three sources:

1. A `BOARD`-specific configuration file stored in
   `boards/<VENDOR>/<BOARD>/<BOARD>_defconfig`
2. Any CMake cache entries prefix with `CONFIG_`
3. The application configuration

The application configuration can come from the sources below (each file is
known as a Kconfig fragment, which are then merged to get the final
configuration used for a particular build). By default, `prj.conf` is
used.

1. If `CONF_FILE` is set, the configuration file(s) specified in it are
   merged and used as the application configuration. `CONF_FILE` can be set
   in various ways:

   1. In `CMakeLists.txt`, before calling `find_package(Zephyr)`
   2. By passing `-DCONF_FILE=<conf file(s)>`, either directly or via `west`
   3. From the CMake variable cache

   Furthermore if `CONF_FILE` is set as single configuration file of the
   form `prj_<build>.conf` and if file
   `boards/<BOARD>_<build>.conf` exists in same folder as file
   `prj_<build>.conf`, the result of merging `prj_<build>.conf` and
   `boards/<BOARD>_<build>.conf` is used - note that this feature is
   deprecated, [File Suffixes](../../develop/application/index.md#application-file-suffixes) should be used instead.
2. Otherwise, if `boards/<BOARD>.conf` exists in the application
   configuration directory, the result of merging it with `prj.conf` is
   used.
3. Otherwise, if board revisions are used and
   `boards/<BOARD>_<revision>.conf` exists in the application
   configuration directory, the result of merging it with `prj.conf` and
   `boards/<BOARD>.conf` is used.
4. Otherwise, `prj.conf` is used from the application configuration
   directory. If it does not exist then a fatal error will be emitted.

Furthermore, applications can have SoC overlay configuration that is applied to
it, the file `socs/<SOC>_<BOARD_QUALIFIERS>.conf` will be applied if it exists,
after the main project configuration has been applied and before any board overlay
configuration files have been applied.

All configuration files will be taken from the application’s configuration
directory except for files with an absolute path that are given with the
`CONF_FILE`, `EXTRA_CONF_FILE`, `DTC_OVERLAY_FILE`, and
`EXTRA_DTC_OVERLAY_FILE` arguments. For these,
a file in a Zephyr module can be referred by escaping the Zephyr module dir
variable like this `\${ZEPHYR_<module>_MODULE_DIR}/<path-to>/<file>`
when setting any of said variables in the application’s `CMakeLists.txt`.

See [Application Configuration Directory](../../develop/application/index.md#application-configuration-directory)
on how the application configuration directory is defined.

If a symbol is assigned both in `<BOARD>_defconfig` and in the
application configuration, the value set in the application configuration takes
precedence.

The merged configuration is saved to `zephyr/.config` in the build
directory.

As long as `zephyr/.config` exists and is up-to-date (is newer than any
`BOARD` and application configuration files), it will be used in preference
to producing a new merged configuration. `zephyr/.config` is also the
configuration that gets modified when making changes in the [interactive
configuration interfaces](menuconfig.md#menuconfig).

## Tracking Kconfig symbols

It is possible to create Kconfig symbols which takes the default value of
another Kconfig symbol.

This is valuable when you want a symbol specific to an application or subsystem
but do not want to rely directly on the common symbol. For example, you might
want to decouple the settings so they can be independently configured, or to
ensure you always have a locally named setting, even if the external setting name changes.
is later changed.

For example, consider the common `FOO_STRING` setting where a subsystem wants
to have a `SUB_FOO_STRING` but still allow for customization.

This can be done like this:

```kconfig
config FOO_STRING
        string "Foo"
        default "foo"

config SUB_FOO_STRING
        string "Sub-foo"
        default FOO_STRING
```

This ensures that the default value of `SUB_FOO_STRING` is identical to
`FOO_STRING` while still allows users to configure both settings
independently.

It is also possible to make `SUB_FOO_STRING` invisible and thereby keep the
two symbols in sync, unless the value of the tracking symbol is changed in a
`defconfig` file.

```kconfig
config FOO_STRING
        string "Foo"
        default "foo"

config SUB_FOO_STRING
        string
        default FOO_STRING
        help
          Hidden symbol which follows FOO_STRING
          Can be changed through *.defconfig files.
```

## Configuring invisible Kconfig symbols

When making changes to the default configuration for a board, you might have to
configure invisible symbols. This is done in
`boards/<VENDOR>/<BOARD>/Kconfig.defconfig`, which is a regular
`Kconfig` file.

Note

Assignments in `.config` files have no effect on invisible symbols,
so this scheme is not just an organizational issue.

Assigning values in `Kconfig.defconfig` relies on defining a Kconfig
symbol in multiple locations. As an example, say we want to set `FOO_WIDTH`
below to 32:

```kconfig
config FOO_WIDTH
    int
```

To do this, we extend the definition of `FOO_WIDTH` as follows, in
`Kconfig.defconfig`:

```kconfig
if BOARD_MY_BOARD

config FOO_WIDTH
    default 32

endif
```

Note

Since the type of the symbol (`int`) has already been given at the first
definition location, it does not need to be repeated here. Only giving the
type once at the “base” definition of the symbol is a good idea for reasons
explained in [Common Kconfig shorthands](tips.md#kconfig-shorthands).

`default` values in `Kconfig.defconfig` files have priority over
`default` values given on the “base” definition of a symbol. Internally, this
is implemented by including the `Kconfig.defconfig` files first. Kconfig
uses the first `default` with a satisfied condition, where an empty condition
corresponds to `if y` (is always satisfied).

Note that conditions from surrounding top-level `if`s are propagated to
symbol properties, so the above `default` is equivalent to
`default 32 if BOARD_MY_BOARD`.

### Multiple symbol definitions

When a symbol is defined in multiple locations, each definition acts as an
independent symbol that happens to share the same name. This means that
properties are not appended to previous definitions. If the conditions
for **ANY** definition result in the symbol resolving to `y`, the symbol
will be `y`. It is therefore not possible to make the dependencies of a
symbol more restrictive by defining it in multiple locations.

For example, the dependencies of the symbol `FOO` below are satisfied if
either `DEP1` **OR** `DEP2` are true, it does not require both:

```text
config FOO
   ...
   depends on DEP1

config FOO
   ...
   depends on DEP2
```

Warning

Symbols without explicit dependencies still follow the above rule. A
symbol without any dependencies will result in the symbol always being
assignable. The definition below will result in `FOO` always being
enabled by default, regardless of the value of `DEP1`.

```kconfig
config FOO
   bool "FOO"
   depends on DEP1

config FOO
   default y
```

This dependency weakening can be avoided with the [configdefault](extensions.md#kconfig-extensions) extension if the desire is only to add a new default
without modifying any other behaviour of the symbol.

Note

When making changes to `Kconfig.defconfig` files, always check the
symbol’s direct dependencies in one of the [interactive configuration
interfaces](menuconfig.md#menuconfig) afterwards. It is often necessary to repeat
dependencies from the base definition of the symbol to avoid weakening a
symbol’s dependencies.

### Motivation for Kconfig.defconfig files

One motivation for this configuration scheme is to avoid making fixed
`BOARD`-specific settings configurable in the interactive configuration
interfaces. If all board configuration were done via `<BOARD>_defconfig`,
all symbols would have to be visible, as values given in
`<BOARD>_defconfig` have no effect on invisible symbols.

Having fixed settings be user-configurable would clutter up the configuration
interfaces and make them harder to understand, and would make it easier to
accidentally create broken configurations.

When dealing with fixed board-specific settings, also consider whether they
should be handled via [devicetree](../dts/index.md#dt-guide) instead.

### Configuring choices

There are two ways to configure a Kconfig `choice`:

1. By setting one of the choice symbols to `y` in a configuration file.

   Setting one choice symbol to `y` automatically gives all other choice
   symbols the value `n`.

   If multiple choice symbols are set to `y`, only the last one set to `y`
   will be honored (the rest will get the value `n`). This allows a choice
   selection from a board `defconfig` file to be overridden from an
   application `prj.conf` file.
2. By changing the `default` of the choice in `Kconfig.defconfig`.

   As with symbols, changing the default for a choice is done by defining the
   choice in multiple locations. For this to work, the choice must have a name.

   As an example, assume that a choice has the following base definition (here,
   the name of the choice is `FOO`):

   ```kconfig
   choice FOO
       bool "Foo choice"
       default B

   config A
       bool "A"

   config B
       bool "B"

   endchoice
   ```

   To change the default symbol of `FOO` to `A`, you would add the
   following definition to `Kconfig.defconfig`:

   ```kconfig
   choice FOO
       default A
   endchoice
   ```

The `Kconfig.defconfig` method should be used when the dependencies of
the choice might not be satisfied. In that case, you’re setting the default
selection whenever the user makes the choice visible.

#### More Kconfig resources

The [Kconfig - Tips and Best Practices](tips.md#kconfig-tips-and-tricks) page has some tips for writing Kconfig
files.

The [kconfiglib.py ](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/kconfig/kconfiglib.py) docstring
(at the top of the file) goes over how symbol values are calculated in detail.
