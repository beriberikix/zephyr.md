---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/snippets/writing.html
original_path: build/snippets/writing.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Writing Snippets

## [Basics](#id1)

Snippets are defined using YAML files named `snippet.yml`.

A `snippet.yml` file contains the name of the snippet, along with
additional build system settings, like this:

```yaml
name: snippet-name
# ... build system settings go here ...
```

Build system settings go in other keys in the file as described later on in
this page.

You can combine settings whenever they appear under the same keys. For example,
you can combine a snippet-specific devicetree overlay and a `.conf` file like
this:

```yaml
name: foo
append:
  EXTRA_DTC_OVERLAY_FILE: foo.overlay
  EXTRA_CONF_FILE: foo.conf
```

## [Namespacing](#id2)

When writing devicetree overlays in a snippet, use `snippet_<name>` or
`snippet-<name>` as a namespace prefix when choosing names for node labels,
node names, etc. This avoids namespace conflicts.

For example, if your snippet is named `foo-bar`, write your devicetree
overlays like this:

```dts
chosen {
        zephyr,baz = &snippet_foo_bar_dev;
};

snippet_foo_bar_dev: device@12345678 {
        /* ... */
};
```

## [Where snippets are located](#id3)

The build system looks for snippets in these places:

1. In directories configured by the **SNIPPET\_ROOT** CMake variable.
   This always includes the zephyr repository (so
   [snippets/](https://github.com/zephyrproject-rtos/zephyr/blob/main/snippets/) is always a source of snippets) and the
   application source directory (so `<app>/snippets` is also).

   Additional directories can be added manually at CMake time.

   The variable is a whitespace- or semicolon-separated list of directories
   which may contain snippet definitions.

   For each directory in the list, the build system looks for
   `snippet.yml` files underneath a subdirectory named `snippets/`,
   if one exists.

   For example, if **SNIPPET\_ROOT** is set to `/foo;/bar`, the build
   system will look for `snippet.yml` files underneath the following
   subdirectories:

   - `/foo/snippets/`
   - `/bar/snippets/`

   The `snippet.yml` files can be nested anywhere underneath these
   locations.
2. In any [module](../../develop/modules.md#modules) whose `module.yml` file provides a
   `snippet_root` setting.

   For example, in a zephyr module named `baz`, you can add this to your
   `module.yml` file:

   ```yaml
   settings:
     snippet_root: .
   ```

   And then any `snippet.yml` files in `baz/snippets` will
   automatically be discovered by the build system, just as if
   the path to `baz` had appeared in **SNIPPET\_ROOT**.

## [Processing order](#id4)

Snippets are processed in the order they are listed in the **SNIPPET**
variable, or in the order of the `-S` arguments if using west.

To apply `bar` after `foo`:

```shell
cmake -Sapp -Bbuild -DSNIPPET="foo;bar" [...]
cmake --build build
```

The same can be achieved with west as follows:

```shell
west build -S foo -S bar [...] app
```

When multiple snippets set the same configuration, the configuration value set
by the last processed snippet ends up in the final configurations.

For instance, if `foo` sets `CONFIG_FOO=1` and `bar` sets
`CONFIG_FOO=2` in the above example, the resulting final configuration will
be `CONFIG_FOO=2` because `bar` is processed after `foo`.

This principle applies to both Kconfig fragments (`.conf` files) and
devicetree overlays (`.overlay` files).

## [Devicetree overlays (`.overlay`)](#id5)

This `snippet.yml` adds `foo.overlay` to the build:

```yaml
name: foo
append:
  EXTRA_DTC_OVERLAY_FILE: foo.overlay
```

The path to `foo.overlay` is relative to the directory containing
`snippet.yml`.

## [`.conf` files](#id6)

This `snippet.yml` adds `foo.conf` to the build:

```yaml
name: foo
append:
  EXTRA_CONF_FILE: foo.conf
```

The path to `foo.conf` is relative to the directory containing
`snippet.yml`.

## [`DTS_EXTRA_CPPFLAGS`](#id7)

This `snippet.yml` adds `DTS_EXTRA_CPPFLAGS` CMake Cache variables
to the build:

```yaml
name: foo
append:
  DTS_EXTRA_CPPFLAGS: -DMY_DTS_CONFIGURE
```

Adding these flags enables control over the content of a devicetree file.

## [Board-specific settings](#id8)

You can write settings that only apply to some boards.

The settings described here are applied in **addition** to snippet settings
that apply to all boards. (This is similar, for example, to the way that an
application with both `prj.conf` and `boards/foo.conf` files will
use both `.conf` files in the build when building for board `foo`, instead
of just `boards/foo.conf`)

### [By name](#id9)

```yaml
name: ...
boards:
  bar: # settings for board "bar" go here
    append:
      EXTRA_DTC_OVERLAY_FILE: bar.overlay
  baz: # settings for board "baz" go here
    append:
      EXTRA_DTC_OVERLAY_FILE: baz.overlay
```

The above example uses `bar.overlay` when building for board `bar`, and
`baz.overlay` when building for `baz`.

### [By regular expression](#id10)

You can enclose the board name in slashes (`/`) to match the name against a
regular expression in the [CMake syntax](https://cmake.org/cmake/help/latest/command/string.html#regex-specification). The regular expression must match
the entire board name.

For example:

```yaml
name: foo
boards:
  /my_vendor_.*/:
    append:
      EXTRA_DTC_OVERLAY_FILE: my_vendor.overlay
```

The above example uses devicetree overlay `my_vendor.overlay` when
building for either board `my_vendor_board1` or `my_vendor_board2`. It
would not use the overlay when building for either `another_vendor_board` or
`x_my_vendor_board`.
