# Ordered batch processing for Authenticate a message with HMAC

`batch.py` accepts an outer JSON array containing separate inputs. This is an extra level of nesting when `solve` itself accepts a list. It produces one result envelope per item, preserving input order and zero-based position.

```sh
python3 batch.py < samples/batch.json
```

The batch covers these three input/output pairs:

## Case 1

Input:
```json
{
  "key": "demo-key",
  "message": "hello"
}
```

Result:
```json
"716539aaecf2467fad8e6803563a732ac7b836abab9efceb610b8639bbe8b535"
```

## Case 2

Input:
```json
{
  "key": "demo-key",
  "message": "hello!"
}
```

Result:
```json
"da66fb53f5e72828df93c751b69afdd9d6e5982eae6caa9cb7aa2ca1e149244d"
```

## Case 3

Input:
```json
{
  "key": "other-demo",
  "message": "hello"
}
```

Result:
```json
"cad9bf85974b9311d151a620f97421008f5661ed3033dd25a38698c8c0d2a218"
```

## Partial failures

Each successful item has `ok: true` and `result`. A failed item has `ok: false` and an exception type; later items still run. Exit status 1 means at least one item failed, while status 2 means the batch envelope itself was invalid. An empty outer array is a valid empty batch.

HMAC combines a secret key and message. Demo keys are public examples only; real keys must come from protected configuration and comparisons must use compare_digest.

The implementation processes sequentially, avoiding shared-state concurrency and keeping output order predictable. Input is limited to one MiB and 1000 items; this version materializes all results in memory. The next lesson removes that whole-batch memory requirement with line-oriented processing.
