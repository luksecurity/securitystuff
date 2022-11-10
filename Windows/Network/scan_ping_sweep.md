# Scan ping sweep

### with cmd

```
(for /L %a IN (1,1,254) DO ping /n 1 /w 1 10.0.0.%a) | find "Reply"
```
