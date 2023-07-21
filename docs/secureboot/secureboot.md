# secure boot

chain of trust
- firmware + signature (code + hash + nokia(private key)) -> code+encrypted hash
- boot loader + signature
- sros + signature

public key is embedded in the CPM to verify 

-> What is the lifetime of the public/private key
-> Once secure boot is enabled: you can no longer can downgrade to unsigned SW

is HW coming from Nokia:
- Identity
- TPM has private key => we create a key during manufecturing -> HW ROT (root of trust) for identity
- rmeote integrity verification -> measured boot (attestation)

TPM enables -> HW trust, remote integrity verification, data encryption trust