---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/build/kconfig/extensions.html
original_path: build/kconfig/extensions.html
---

# Kconfig extensions

Zephyr uses the [Kconfiglib](https://github.com/ulfalizer/Kconfiglib)
implementation of [Kconfig](https://docs.kernel.org/kbuild/kconfig-language.html),
which includes some Kconfig extensions:

- Default values can be applied to existing symbols without
  [weakening](setting.md#multiple-symbol-definitions) the symbols dependencies
  through the use of `configdefault`.

  ```text
  config FOO
      bool "FOO"
      depends on BAR

  configdefault FOO
      default y if FIZZ
  ```

  The statement above is equivalent to:

  ```text
  config FOO
      bool "Foo"
      default y if FIZZ
      depends on BAR
  ```

  `configdefault` symbols cannot contain any fields other than `default`,
  however they can be wrapped in `if` statements. The two statements below
  are equivalent:

  ```text
  configdefault FOO
      default y if BAR

  if BAR
  configdefault FOO
      default y
  endif # BAR
  ```
- Environment variables in `source` statements are expanded directly, meaning
  no “bounce” symbols with `option env="ENV_VAR"` need to be defined.

  Note

  `option env` has been removed from the C tools as of Linux 4.18 as well.

  The recommended syntax for referencing environment variables is `$(FOO)`
  rather than `$FOO`. This uses the new [Kconfig preprocessor](https://docs.kernel.org/kbuild/kconfig-macro-language.html).
  The `$FOO` syntax for expanding environment variables is only supported for
  backwards compatibility.
- The `source` statement supports glob patterns and includes each matching
  file. A pattern is required to match at least one file.

  Consider the following example:

  ```kconfig
  source "foo/bar/*/Kconfig"
  ```

  If the pattern `foo/bar/*/Kconfig` matches the files
  `foo/bar/baz/Kconfig` and `foo/bar/qaz/Kconfig`, the statement
  above is equivalent to the following two `source` statements:

  ```kconfig
  source "foo/bar/baz/Kconfig"
  source "foo/bar/qaz/Kconfig"
  ```

  If no files match the pattern, an error is generated.

  The wildcard patterns accepted are the same as for the Python [glob](https://docs.python.org/3/library/glob.html) module.

  For cases where it’s okay for a pattern to match no files (or for a plain
  filename to not exist), a separate `osource` (*optional source*) statement
  is available. `osource` is a no-op if no file matches.

  Note

  `source` and `osource` are analogous to `include` and
  `-include` in Make.
- An `rsource` statement is available for including files specified with a
  relative path. The path is relative to the directory of the `Kconfig`
  file that contains the `rsource` statement.

  As an example, assume that `foo/Kconfig` is the top-level
  `Kconfig` file, and that `foo/bar/Kconfig` has the following
  statements:

  ```kconfig
  source "qaz/Kconfig1"
  rsource "qaz/Kconfig2"
  ```

  This will include the two files `foo/qaz/Kconfig1` and
  `foo/bar/qaz/Kconfig2`.

  `rsource` can be used to create `Kconfig` “subtrees” that can be
  moved around freely.

  `rsource` also supports glob patterns.

  A drawback of `rsource` is that it can make it harder to figure out where a
  file gets included, so only use it if you need it.
- An `orsource` statement is available that combines `osource` and
  `rsource`.

  For example, the following statement will include `Kconfig1` and
  `Kconfig2` from the current directory (if they exist):

  ```kconfig
  orsource "Kconfig[12]"
  ```
- `def_int`, `def_hex`, and `def_string` keywords are available,
  analogous to `def_bool`. These set the type and add a `default` at the
  same time.
