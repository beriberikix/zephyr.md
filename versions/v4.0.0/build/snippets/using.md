---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/build/snippets/using.html
original_path: build/snippets/using.html
---

# Using Snippets

Tip

See [Built-in snippets](../../snippets/index.md#built-in-snippets) for a list of snippets that are provided by
Zephyr.

Snippets have names. You use snippets by giving their names to the build
system.

## With west build

To use a snippet named `foo` when building an application `app`:

```shell
west build -S foo app
```

To use multiple snippets:

```shell
west build -S snippet1 -S snippet2 [...] app
```

## With cmake

If you are running CMake directly instead of using `west build`, use the
`SNIPPET` variable. This is a whitespace- or semicolon-separated list of
snippet names you want to use. For example:

```shell
cmake -Sapp -Bbuild -DSNIPPET="snippet1;snippet2" [...]
cmake --build build
```

## Application required snippets

If an application should always be compiled with a given snippet, it
can be added to that application’s `CMakeLists.txt` file. For example:

```cmake
if(NOT snippet1 IN_LIST SNIPPET)
  set(SNIPPET snippet1 ${SNIPPET} CACHE STRING "" FORCE)
endif()

find_package(Zephyr ....)
```
