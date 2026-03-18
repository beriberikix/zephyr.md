---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/build/version/index.html
original_path: build/version/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Application version management

Zephyr supports an application version management system for applications which is built around the
system that Zephyr uses for its own version system management. This allows applications to define a
version file and have application (or module) code include the auto-generated file and be able to
access it, just as they can with the kernel version. This version information is available from
multiple scopes, including:

- Code (C/C++)
- Kconfig
- CMake

which makes it a very versatile system for lifecycle management of applications. In addition, it
can be used when building applications which target supported bootloaders (e.g. MCUboot) allowing
images to be signed with correct version of the application automatically - no manual signing
steps are required.

## VERSION file

Application version information is set on a per-application basis in a file named `VERSION`,
which must be placed at the base directory of the application, where the CMakeLists.txt file is
located. This is a simple text file which contains the various version information fields, each on
a newline. The basic `VERSION` file has the following structure:

```cfg
VERSION_MAJOR =
VERSION_MINOR =
PATCHLEVEL =
VERSION_TWEAK =
EXTRAVERSION =
```

Each field and the values it supports is described below. Zephyr limits the value of each numeric
field to a single byte (note that there may be further restrictions depending upon what the version
is used for, e.g. bootloaders might only support some of these fields or might place limits on the
maximum values of fields):

| Field | Data type |
| --- | --- |
| VERSION\_MAJOR | Numerical (0-255) |
| VERSION\_MINOR | Numerical (0-255) |
| PATCHLEVEL | Numerical (0-255) |
| VERSION\_TWEAK | Numerical (0-255) |
| EXTRAVERSION | Alphanumerical (Lowercase a-z and 0-9) |

When an application is configured using CMake, the version file will be automatically processed,
and will be checked automatically each time the version is changed, so CMake does not need to be
manually re-ran for changes to this file.

For the sections below, examples are provided for the following `VERSION` file:

```cfg
VERSION_MAJOR = 1
VERSION_MINOR = 2
PATCHLEVEL = 3
VERSION_TWEAK = 4
EXTRAVERSION = unstable
```

## Use in code

To use the version information in application code, the version file must be included, then the
fields can be freely used. The include file name is `app_version.h` (no path is needed), the
following defines are available:

| Define | Type | Field(s) | Example |
| --- | --- | --- | --- |
| APPVERSION | Numerical | `VERSION_MAJOR` (left shifted by 24 bits),   `VERSION_MINOR` (left shifted by 16 bits),   `PATCHLEVEL` (left shifted by 8 bits),   `VERSION_TWEAK` | 0x1020304 |
| APP\_VERSION\_NUMBER | Numerical | `VERSION_MAJOR` (left shifted by 16 bits),   `VERSION_MINOR` (left shifted by 8 bits),   `PATCHLEVEL` | 0x10203 |
| APP\_VERSION\_MAJOR | Numerical | `VERSION_MAJOR` | 1 |
| APP\_VERSION\_MINOR | Numerical | `VERSION_MINOR` | 2 |
| APP\_PATCHLEVEL | Numerical | `PATCHLEVEL` | 3 |
| APP\_TWEAK | Numerical | `VERSION_TWEAK` | 4 |
| APP\_VERSION\_STRING | String (quoted) | `VERSION_MAJOR`,   `VERSION_MINOR`,   `PATCHLEVEL`,   `EXTRAVERSION` | “1.2.3-unstable” |
| APP\_VERSION\_EXTENDED\_STRING | String (quoted) | `VERSION_MAJOR`,   `VERSION_MINOR`,   `PATCHLEVEL`,   `EXTRAVERSION`   `VERSION_TWEAK` | “1.2.3-unstable+4” |
| APP\_VERSION\_TWEAK\_STRING | String (quoted) | `VERSION_MAJOR`,   `VERSION_MINOR`,   `PATCHLEVEL`,   `VERSION_TWEAK` | “1.2.3+4” |
| APP\_BUILD\_VERSION | String (unquoted) | None (value of `git describe --abbrev=12 --always` from application repository) | v3.3.0-18-g2c85d9224fca |

## Use in Kconfig

The following variables are available for usage in Kconfig files:

| Variable | Type | Field(s) | Example |
| --- | --- | --- | --- |
| $(VERSION\_MAJOR) | Numerical | `VERSION_MAJOR` | 1 |
| $(VERSION\_MINOR) | Numerical | `VERSION_MINOR` | 2 |
| $(PATCHLEVEL) | Numerical | `PATCHLEVEL` | 3 |
| $(VERSION\_TWEAK) | Numerical | `VERSION_TWEAK` | 4 |
| $(APPVERSION) | String | `VERSION_MAJOR`,   `VERSION_MINOR`,   `PATCHLEVEL`,   `EXTRAVERSION` | 1.2.3-unstable |
| $(APP\_VERSION\_EXTENDED\_STRING) | String | `VERSION_MAJOR`,   `VERSION_MINOR`,   `PATCHLEVEL`,   `EXTRAVERSION`,   `VERSION_TWEAK` | 1.2.3-unstable+4 |
| $(APP\_VERSION\_TWEAK\_STRING) | String | `VERSION_MAJOR`,   `VERSION_MINOR`,   `PATCHLEVEL`,   `VERSION_TWEAK` | 1.2.3+4 |

## Use in CMake

The following variable are available for usage in CMake files:

| Variable | Type | Field(s) | Example |
| --- | --- | --- | --- |
| APPVERSION | Numerical (hex) | `VERSION_MAJOR` (left shifted by 24 bits),   `VERSION_MINOR` (left shifted by 16 bits),   `PATCHLEVEL` (left shifted by 8 bits),   `VERSION_TWEAK` | 0x1020304 |
| APP\_VERSION\_NUMBER | Numerical (hex) | `VERSION_MAJOR` (left shifted by 16 bits),   `VERSION_MINOR` (left shifted by 8 bits),   `PATCHLEVEL` | 0x10203 |
| APP\_VERSION\_MAJOR | Numerical | `VERSION_MAJOR` | 1 |
| APP\_VERSION\_MINOR | Numerical | `VERSION_MINOR` | 2 |
| APP\_PATCHLEVEL | Numerical | `PATCHLEVEL` | 3 |
| APP\_VERSION\_TWEAK | Numerical | `VERSION_TWEAK` | 4 |
| APP\_VERSION\_STRING | String | `VERSION_MAJOR`,   `VERSION_MINOR`,   `PATCHLEVEL`,   `EXTRAVERSION` | 1.2.3-unstable |
| APP\_VERSION\_EXTENDED\_STRING | String | `VERSION_MAJOR`,   `VERSION_MINOR`,   `PATCHLEVEL`,   `EXTRAVERSION`,   `VERSION_TWEAK` | 1.2.3-unstable+4 |
| APP\_VERSION\_TWEAK\_STRING | String | `VERSION_MAJOR`,   `VERSION_MINOR`,   `PATCHLEVEL`,   `VERSION_TWEAK` | 1.2.3+4 |

## Use in MCUboot-supported applications

No additional configuration needs to be done to the target application so long as it is configured
to support MCUboot and a signed image is generated, the version information will be automatically
included in the image data.
