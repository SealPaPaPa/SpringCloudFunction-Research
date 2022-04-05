# SpringCloudFunction-Research
CVE-2022-22963 research

# 環境
* vulfocus/spring-cloud-function-rce:latest

# 成因
* Request Header 中 `spring.cloud.function.routing-expression` 參數解析問題，造成注入Payload攻擊。

# Reference
* https://hosch3n.github.io/2022/03/26/SpringCloudFunction%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90/
* https://www.kitploit.com/2022/03/spring-spel-0day-poc-spring-cloud.html
* [spring-cloud-function](https://github.com/spring-cloud/spring-cloud-function)
