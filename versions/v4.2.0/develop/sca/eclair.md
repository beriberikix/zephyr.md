---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/develop/sca/eclair.html
original_path: develop/sca/eclair.html
---

# ECLAIR support

Bugseng [ECLAIR](https://www.bugseng.com/eclair/) is a certified
static analysis tool and platform for software verification.
Applications range from coding rule validation, with a
particular emphasis on the MISRA and BARR-C coding standards, to the
computation of software metrics, to the checking of independence and
freedom from interference among software components, to the automatic
detection of important classes of software errors.

## Prerequisites

The ECLAIR tool must be installed and made available in the operating system’s
PATH variable.

To verify the installation, you can run:

```shell
eclair -version
```

A valid license or trial license is required to use ECLAIR. To request a trial
license, visit [this page](https://www.bugseng.com/eclair/free-trial).

## Running ECLAIR

To run ECLAIR, [west build](../west/build-flash-debug.md#west-building) should be
called with a `-DZEPHYR_SCA_VARIANT=eclair` parameter.

```shell
west build -b mimxrt1064_evk samples/basic/blinky -- -DZEPHYR_SCA_VARIANT=eclair
```

Note

This will only invoke the ECLAIR analysis with the predefined ruleset `first_analysis`. If you
want to use a different ruleset, you need to provide a configuration file. See the next section
for more information.

## Configurations

The configuration of the ECLAIR SCA environment can either be done via a CMake
options file or with adapted options as command line arguments.

To invoke a CMake options file into the ECLAIR call, you can define the
`ECLAIR_OPTIONS_FILE` variable, for example:

```shell
west build -b mimxrt1064_evk samples/basic/blinky -- -DZEPHYR_SCA_VARIANT=eclair -DECLAIR_OPTIONS_FILE=my_options.cmake
```

The default (if no config file is given) configuration is always
`first_analysis`, which is a tiny selection of rules to verify that
everything is correctly working.

If the default configuration wants to be overwritten via the command line and
not via an options file, that can be achieved by giving the argument
`-DOption=ON|OFF`.

For example:

```shell
west build -b mimxrt1064_evk samples/basic/blinky -- -DZEPHYR_SCA_VARIANT=eclair -DECLAIR_REPORTS_SARIF=ON
```

Zephyr is a large and complex project, so the configuration sets are split into
the Zephyr’s guidelines selection
(taken from [https://docs.zephyrproject.org/latest/contribute/coding\_guidelines/index.html](https://docs.zephyrproject.org/latest/contribute/coding_guidelines/index.html))
in five sets to make it more digestible to use on a private machine:

- first\_analysis (default): a tiny selection of the project’s coding guidelines to verify that
  everything is correctly working.
- STU: Selection of the project’s coding guidelines, which can be verified by analyzing the single
  translation units independently.
- STU\_heavy: Selection of complex STU project coding guidelines that require a significant amount
  of time.
- WP: All whole program project coding guidelines (“system” in MISRA’s parlance).
- std\_lib: Project coding guidelines about the C Standard Library.

In addition, the zephyr\_guidelines ruleset contains all the main rules
listed in the [Coding Guidelines](https://docs.zephyrproject.org/latest/contribute/coding_guidelines/index.html).

Related CMake options:

- `ECLAIR_RULESET_FIRST_ANALYSIS`
- `ECLAIR_RULESET_STU`
- `ECLAIR_RULESET_STU_HEAVY`
- `ECLAIR_RULESET_WP`
- `ECLAIR_RULESET_STD_LIB`
- `ECLAIR_RULESET_ZEPHYR_GUIDELINES`

### User-defined ruleset

If you want to use your own defined ruleset instead of the predefined Zephyr coding guidelines
rulesets, you can do so by setting `ECLAIR_RULESET_USER=ON`.
Create your own ruleset file for ECLAIR with the following naming format:
`analysis_<RULESET>.ecl`. After creating the file, define the name of the ruleset for ECLAIR
with the CMake variable `ECLAIR_USER_RULESET_NAME`.
If the ruleset file is not in the application source directory, you can define the path to the
ruleset file with the CMake variable `ECLAIR_USER_RULESET_PATH`. This configuration takes
relative paths and absolute paths.

Related CMake options and variables:

- `ECLAIR_RULESET_USER`
- `ECLAIR_USER_RULESET_NAME`
- `ECLAIR_USER_RULESET_PATH`

## Generate additional report formats

ECLAIR can generate additional report formats (e.g., DOC, ODT, XLSX) and
different variants of reports in addition to the
default ecd file. Following additional reports and report formats can be generated:

- Metrics in spreadsheet format.
- Findings in spreadsheet format.
- Findings in SARIF format.
- Summary report in plain textual format.
- Summary report in DOC format.
- Summary report in ODT format.
- Summary report in HTML format.
- Detailed reports in txt format.
- Detailed report in DOC format.
- Detailed report in ODT format.
- Detailed report in HTML format.

Related CMake options:

- `ECLAIR_METRICS_TAB`
- `ECLAIR_REPORTS_TAB`
- `ECLAIR_REPORTS_SARIF`
- `ECLAIR_SUMMARY_TXT`
- `ECLAIR_SUMMARY_DOC`
- `ECLAIR_SUMMARY_ODT`
- `ECLAIR_SUMMARY_HTML`
- `ECLAIR_FULL_TXT`
- `ECLAIR_FULL_DOC`
- `ECLAIR_FULL_ODT`
- `ECLAIR_FULL_HTML`

### Detail level of full reports

The detail level of the txt and doc full reports can also be adapted by a configuration.
In this case, the following configurations are available:

- Show all areas
- Show only the first area

Related CMake options:

- `ECLAIR_FULL_DOC_ALL_AREAS`
- `ECLAIR_FULL_DOC_FIRST_AREA`
- `ECLAIR_FULL_TXT_ALL_AREAS`
- `ECLAIR_FULL_TXT_FIRST_AREA`
