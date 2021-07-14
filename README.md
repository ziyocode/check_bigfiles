## check bigfiles

### 디렉터리 내에 사이즈가 큰 파일을 찾습니다. 

❯ ./bigfiles -h            
usage: bigfiles [-h] [-s SDIR] [-n COUNT]

```
optional arguments:
  -h, --help            show this help message and exit
  -s SDIR, --sdir SDIR  디렉터리
  -n COUNT, --count COUNT 갯수
```
```
<Sample>
❯ python big20.py -s /etc/ -n 20
/etc//services                                     2020/01/01-17:00  Perm:644  User:root       Size:0.647 Mbyte
/etc/ssh/moduli                                    2020/01/01-17:00  Perm:644  User:root       Size:0.551 Mbyte
/etc/ssl/cert.pem                                  2020/01/01-17:00  Perm:644  User:root       Size:0.330 Mbyte
/etc/openldap/schema/microsoft.ext.schema          2020/01/01-17:00  Perm:444  User:root       Size:0.169 Mbyte
/etc/openldap/schema/microsoft.schema              2020/01/01-17:00  Perm:444  User:root       Size:0.117 Mbyte
/etc/openldap/AppleOpenLDAP.plist                  2020/01/01-17:00  Perm:644  User:root       Size:0.111 Mbyte
/etc/openldap/schema/cosine.schema                 2020/01/01-17:00  Perm:444  User:root       Size:0.071 Mbyte
/etc//php.ini.default                              2020/01/01-17:00  Perm:444  User:root       Size:0.068 Mbyte
/etc/apache2/mime.types                            2020/01/01-17:00  Perm:644  User:root       Size:0.058 Mbyte
/etc/openldap/schema/apple.schema                  2020/01/01-17:00  Perm:444  User:root       Size:0.046 Mbyte
/etc//pf.os                                        2020/01/01-17:00  Perm:644  User:root       Size:0.027 Mbyte
/etc/postfix/main.cf.default                       2020/01/01-17:00  Perm:644  User:root       Size:0.026 Mbyte
/etc/postfix/main.cf                               2020/01/01-17:00  Perm:644  User:root       Size:0.026 Mbyte
/etc/postfix/main.cf.proto                         2020/01/01-17:00  Perm:644  User:root       Size:0.026 Mbyte
/etc/security/audit_event                          2020/01/01-17:00  Perm:444  User:root       Size:0.025 Mbyte
/etc/postfix/header_checks                         2020/01/01-17:00  Perm:644  User:root       Size:0.023 Mbyte
/etc/apache2/httpd.conf                            2020/01/01-17:00  Perm:644  User:root       Size:0.021 Mbyte
/etc/apache2/original/httpd.conf                   2020/01/01-17:00  Perm:644  User:root       Size:0.021 Mbyte
/etc/postfix/access                                2020/01/01-17:00  Perm:644  User:root       Size:0.021 Mbyte
/etc/openldap/schema/core.ldif                     2020/01/01-17:00  Perm:444  User:root       Size:0.020 Mbyte
```