# AsymmetricEncryption

The beginnings of an implementation for Asymmetric Encryption. Essentially an attemp to recreate RSA using knowledge gleaned from the internet (and much smaller scales than actual RSA). Result will hopefully be relatively secure for sending messages between users, but obviously not on the same level as real RSA encryption.

Note: Use of python was for my own personal benefit, as I find it very nice to work with. Python is terrible for this kind of work in the real world because it is so slow

Second Note: Never roll your own crypto in production. Seriously. This was just a learning exercise. Notably, I doubt the builtin random function of Python is sufficient for crypto key generation.  

Third Note: These keys are generated randomly every time you run this, and are just toy examples, hence why it's fine for me to put them on GitHub. Naturally don't put private keys on GitHub if they're really private. 
