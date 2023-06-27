#10.# Example 10: CWE-295 - Improper Certificate Validation

import websocket

ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})

# Vulnerable line: disabling certificate validation