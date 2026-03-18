---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/develop/sca/index.html
original_path: develop/sca/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Static Code Analysis (SCA)

Support for static code analysis tools in Zephyr is possible through CMake.

The build setting **ZEPHYR\_SCA\_VARIANT** can be used to specify the SCA
tool to use. `ZEPHYR_SCA_VARIANT` is also supported as
[environment variable](../env_vars.md#env-vars).

Use `-DZEPHYR_SCA_VARIANT=<tool>`, for example `-DZEPHYR_SCA_VARIANT=sparse`
to enable the static analysis tool `sparse`.

## SCA Tool infrastructure

Support for an SCA tool is implemented in a file:sca.cmake file.
The file:sca.cmake must be placed under file:<SCA\_ROOT>/cmake/sca/<tool>/sca.cmake.
Zephyr itself is always added as an **SCA\_ROOT** but the build system offers the
possibility to add additional folders to the **SCA\_ROOT** setting.

You can provide support for out of tree SCA tools by creating the following
structure:

```text
<sca_root>/                 # Custom SCA root
└── cmake/
    └── sca/
        └── <tool>/         # Name of SCA tool, this is the value given to ZEPHYR_SCA_VARIANT
            └── sca.cmake   # CMake code that configures the tool to be used with Zephyr
```

To add `foo` under `/path/to/my_tools/cmake/sca` create the following structure:

```text
/path/to/my_tools
         └── cmake/
             └── sca/
                 └── foo/
                     └── sca.cmake
```

To use `foo` as SCA tool you must then specify `-DZEPHYR_SCA_VARIANT=foo`.

Remember to add `/path/to/my_tools` to **SCA\_ROOT**.

**SCA\_TOOL** can be set as a regular CMake setting using
`-DSCA_ROOT=<sca_root>`, or added by a Zephyr module in its `module.yml`
file, see [Zephyr Modules - Build settings](../modules.md#modules-build-settings)

## Native SCA Tool support

The following is a list of SCA tools natively supported by Zephyr build system.
