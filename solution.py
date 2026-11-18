import hmac
import hashlib

def solve(value):
    return hmac.new(value['key'].encode(), value['message'].encode(), hashlib.sha256).hexdigest()
