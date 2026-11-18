# Authenticate a message with HMAC: implementation

## What the example does

HMAC combines a secret key and message. Demo keys are public examples only; real keys must come from protected configuration and comparisons must use compare_digest.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
{
  "key": "demo-key",
  "message": "hello"
}
```

Expected result:

```json
"716539aaecf2467fad8e6803563a732ac7b836abab9efceb610b8639bbe8b535"
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
