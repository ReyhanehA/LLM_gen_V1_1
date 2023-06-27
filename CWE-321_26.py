#7.# Example 7: CWE-321 - Use of Insecure Communication Protocol
import http.client
conn = http.client.HTTPSConnection("www.example.com")

# The use of HTTP protocol instead of HTTPS is vulnerable to attacks as it can be easily intercepted and manipulated.