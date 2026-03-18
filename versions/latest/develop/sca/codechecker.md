---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/sca/codechecker.html
original_path: develop/sca/codechecker.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# CodeChecker support

[CodeChecker](https://codechecker.readthedocs.io/) is a static analysis infrastructure.
It executes analysis tools available on the build system, such as
[Clang-Tidy](http://clang.llvm.org/extra/clang-tidy/),
[Clang Static Analyzer](http://clang-analyzer.llvm.org/) and
[Cppcheck](https://cppcheck.sourceforge.io/). Refer to the analyzer’s websites for installation
instructions.

## Installing CodeChecker

CodeChecker itself is a python package available on [pypi](https://pypi.org/project/codechecker/).

```shell
pip install codechecker
```

## Running with CodeChecker

To run CodeChecker, [west build](../west/build-flash-debug.md#west-building) should be
called with a `-DZEPHYR_SCA_VARIANT=codechecker` parameter, e.g.

```shell
west build -b mimxrt1064_evk samples/basic/blinky -- -DZEPHYR_SCA_VARIANT=codechecker
```

## Configuring CodeChecker

To configure CodeChecker or analyzers used, arguments can be passed using the
`CODECHECKER_ANALYZE_OPTS` parameter, e.g.

```shell
west build -b mimxrt1064_evk samples/basic/blinky -- -DZEPHYR_SCA_VARIANT=codechecker \
-DCODECHECKER_ANALYZE_OPTS="--config;$CODECHECKER_CONFIG_FILE;--timeout;60"
```

## Storing CodeChecker results

If a CodeChecker server is active the results can be uploaded and stored for tracking purposes.
Storing is done using the optional `CODECHECKER_STORE=y` or `CODECHECKER_STORE_OPTS="arg;list"`
parameters, e.g.

```shell
west build -b mimxrt1064_evk samples/basic/blinky -- -DZEPHYR_SCA_VARIANT=codechecker \
-DCODECHECKER_STORE_OPTS="--name;build;--url;localhost:8001/Default"
```

Note

If `--name` isn’t passed to either `CODECHECKER_ANALYZE_OPTS` or `CODECHECKER_STORE_OPTS`,
the default `zephyr` is used.

## Exporting CodeChecker reports

Optional reports can be generated using the CodeChecker results, when passing a
`-DCODECHECKER_EXPORT=<type>` parameter. Allowed types are: `html,json,codeclimate,gerrit,baseline`.
Multiple types can be passed as comma-separated arguments.

Optional parser configuration arguments can be passed using the
`CODECHECKER_PARSE_OPTS` parameter, e.g.

```shell
west build -b mimxrt1064_evk samples/basic/blinky -- -DZEPHYR_SCA_VARIANT=codechecker \
-DCODECHECKER_EXPORT=html,json -DCODECHECKER_PARSE_OPTS="--trim-path-prefix;$PWD"
```
