# login and authentication

factores:
- something you are: (fingerprints, facial recognition, iris scans)
    - biometrics is based on stats and can result in false positives/negatives
    - fingerprints can be used if a device gets stolen
- somthing you have:
    - can be stolen (need a pin key)
- something you know:
    - can be guessed


methods:
- passwords:
    - known to be stolen (complexity can matter), server leaks
    - most likely one of the factors to stay
    - good for multi-factor authentication
- pin codes: (4-8 digits)
    - vulnarable to brute force attacks
    - convenient
    - not good for first factor
- recovery codes:
    - can be stolen
    - similar to pin but for one time use
    - used as a abackup recovery mechanism
- magic link via email
    - convenient for onboarding
    - email is unreliable
    - use login code via email instead
- login code via email
    - convenient for onboarding
    - email is unreliable
    - preferd over magic link
- login via sms
    - convenient for mobile
    - insecure, dont use
- TOTP/google authenticator
    - device can be lost or stolen
    - used as 2nd factor authentication
- Passkeys, faceID, windown Hello: Webauthn
    - pishing resistant (bound to hostnames)
    - major improvement in security and convenience
    - keys cannot be shared accross domains
- QR code
    - use webauthn with QR code instead
- Social sign-in/Sign-on
    - 