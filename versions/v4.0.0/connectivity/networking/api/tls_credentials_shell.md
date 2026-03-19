---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/networking/api/tls_credentials_shell.html
original_path: connectivity/networking/api/tls_credentials_shell.html
---

# TLS Credentials Shell

The TLS Credentials shell provides a command-line interface for managing installed TLS credentials.

## Commands

### Buffer Credential (`buf`)

Buffer data incrementally into the credential buffer so that it can be added using the [Add Credential (add)](#tls-credentials-shell-add-cred) command.

Alternatively, clear the credential buffer.

#### Usage

To append `<DATA>` to the credential buffer, use:

```shell
cred buf <DATA>
```

Use this as many times as needed to load the full credential into the credential buffer, then use the [Add Credential (add)](#tls-credentials-shell-add-cred) command to store it.

To clear the credential buffer, use:

```shell
cred buf clear
```

#### Arguments

| Argument | Description |
| --- | --- |
| `<DATA>` | Text data to be appended to credential buffer. It can be either text, or base64-encoded binary. See [Add Credential (add)](#tls-credentials-shell-add-cred) and [Storage/Retrieval Formats](#tls-credentials-shell-data-formats) for details. |

### Add Credential (`add`)

Add a TLS credential to the TLS Credential store.

Credential contents can be provided in-line with the call to `cred add`, or will otherwise be sourced from the credential buffer.

#### Usage

To add a TLS credential using the data from the credential buffer, use:

```shell
cred add <SECTAG> <TYPE> <BACKEND> <FORMAT>
```

To add a TLS credential using data provided with the same command, use:

```shell
cred add <SECTAG> <TYPE> <BACKEND> <FORMAT> <DATA>
```

#### Arguments

| Argument | Description |
| --- | --- |
| `<SECTAG>` | The sectag to use for the new credential. Can be any non-negative integer. |
| `<TYPE>` | The type of credential to add. See [Credential Types](#tls-credentials-shell-cred-types) for valid values. |
| `<BACKEND>` | Reserved. Must always be `DEFAULT` (case-insensitive). |
| `<FORMAT>` | Specifies the storage format of the provided credential. See [Storage/Retrieval Formats](#tls-credentials-shell-data-formats) for valid values. |
| `<DATA>` | If provided, this argument will be used as the credential data, instead of any data in the credential buffer. Can be either text, or base64-encoded binary. |

### Delete Credential (`del`)

Delete a specified credential from the credential store.

#### Usage

To delete a credential matching a specified sectag and credential type (if it exists), use:

```shell
cred del <SECTAG> <TYPE>
```

#### Arguments

| Argument | Description |
| --- | --- |
| `<SECTAG>` | The sectag of the credential to delete. Can be any non-negative integer. |
| `<TYPE>` | The type of credential to delete. See [Credential Types](#tls-credentials-shell-cred-types) for valid values. |

### Get Credential Contents (`get`)

Retrieve and print the contents of a specified credential.

#### Usage

To retrieve and print a credential matching a specified sectag and credential type (if it exists), use:

```shell
cred get <SECTAG> <TYPE> <FORMAT>
```

#### Arguments

| Argument | Description |
| --- | --- |
| `<SECTAG>` | The sectag of the credential to get. Can be any non-negative integer. |
| `<TYPE>` | The type of credential to get. See [Credential Types](#tls-credentials-shell-cred-types) for valid values. |
| `<FORMAT>` | Specifies the retrieval format for the provided credential. See [Storage/Retrieval Formats](#tls-credentials-shell-data-formats) for valid values. |

### List Credentials (`list`)

List TLS credentials in the credential store.

#### Usage

To list all available credentials, use:

```shell
cred list
```

To list all credentials with a specified sectag, use:

```shell
cred list <SECTAG>
```

To list all credentials with a specified credential type, use:

```shell
cred list any <TYPE>
```

To list all credentials with a specified credential type and sectag, use:

```shell
cred list <SECTAG> <TYPE>
```

#### Arguments

| Argument | Description |
| --- | --- |
| `<SECTAG>` | Optional. If provided, only list credentials with this sectag. Pass `any` or omit to allow any sectag. Otherwise, can be any non-negative integer. |
| `<TYPE>` | Optional. If provided, only list credentials with this credential type. Pass `any` or omit to allow any credential type. Otherwise, see [Credential Types](#tls-credentials-shell-cred-types) for valid values. |

#### Output

The command outputs all matching credentials in the following (CSV-compliant) format:

```shell
<SECTAG>,<TYPE>,<DIGEST>,<STATUS>
```

Where:

| Symbol | Value |
| --- | --- |
| `<SECTAG>` | The sectag of the listed credential. A non-negative integer. |
| `<TYPE>` | Credential type short-code (see [Credential Types](#tls-credentials-shell-cred-types) for details) of the listed credential. |
| `<DIGEST>` | A string digest representing the credential contents. The exact nature of this digest may vary depending on credentials storage backend, but currently for all backends this is a base64 encoded SHA256 hash of the raw credential contents (so different storage formats for essentially identical credentials will have different digests). |
| `<STATUS>` | Status code indicating success or failure with generating a digest of the listed credential. 0 if successful, negative error code specific to the storage backend otherwise. Lines for which status is not zero will be printed with error formatting. |

After the list is printed, a final summary of the found credentials will be printed in the form:

```shell
<N> credentials found.
```

Where `<N>` is the number of credentials found, and is zero if none are found.

## Credential Types

The following keywords (case-insensitive) may be used to specify a credential type:

| Keyword(s) | Meaning |
| --- | --- |
| `CA_CERT`, `CA` | A trusted CA certificate. |
| `SERVER_CERT`, `SELF_CERT`, `CLIENT_CERT`, `CLIENT`, `SELF`, `SERV` | Self or server certificate. |
| `PRIVATE_KEY`, `PK` | A private key. |
| `PRE_SHARED_KEY`, `PSK` | A pre-shared key. |
| `PRE_SHARED_KEY_ID`, `PSK_ID` | ID for pre-shared key. |

## Storage/Retrieval Formats

The [tls\_credentials](sockets.md#sockets-tls-credentials-subsys) module treats stored credentials as arbitrary binary buffers.

For convenience, the TLS credentials shell offers four formats for providing and later retrieving these buffers using the shell.

These formats and their (case-insensitive) keywords are as follows:

| Keyword | Meaning | Behavior during storage (`cred add`) | Behavior during retrieval (`cred get`) |
| --- | --- | --- | --- |
| `BIN` | Credential is handled by shell as base64 and stored without NULL termination. | Data entered into shell will be decoded from base64 into raw binary before storage. No terminator will be appended. | Stored data will be encoded into base64 before being printed. |
| `BINT` | Credential is handled by shell as base64 and stored with NULL termination. | Data entered into shell will be decoded from base64 into raw binary and a NULL terminator will be appended before storage. | NULL terminator will be truncated from stored data before said data is encoded into base64 and then printed. |
| `STR` | Credential is handled by shell as literal string and stored without NULL termination. | Text data entered into shell will be passed into storage as-written, without a NULL terminator. | Stored data will be printed as text. Non-printable characters will be printed as `?` |
| `STRT` | Credential is handled by shell as literal string and stored with NULL-termination. | Text data entered into shell will be passed into storage as-written, with a NULL terminator. | NULL terminator will be truncated from stored data before said data is printed as text. Non-printable characters will be printed as `?` |

The `BIN` format can be used to install credentials of any type, since base64 can be used to encode any concievable binary buffer.
The remaining three formats are provided for convenience in special use-cases.

For example:

- To install printable pre-shared-keys, use `STR` to enter the PSK without first encoding it.
  This ensures it is stored without a NULL terminator.
- To install DER-formatted X.509 certificates (or other raw-binary credentials, such as non-printable PSKs) base64-encode the binary and use the `BIN` format.
- To install PEM-formatted X.509 certificates or certificate chains, base64 encode the full PEM string (including new-lines and `----BEGIN X ----` / `----END X----` markers), and then use the `BINT` format to make sure the stored string is NULL-terminated.
  This is required because Zephyr does not support multi-line strings in the shell.
  Otherwise, the `STRT` format could be used for this purpose without base64 encoding.
  It is possible to use `BIN` instead if you manually encode a NULL terminator into the base64.
