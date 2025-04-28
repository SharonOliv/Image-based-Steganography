# Image-based-Steganography
**Hidden messages visible disguise**
 
This project implements **image steganography** by embedding a secret image (`secret5.jpg`) into a cover image (`cover5.jpg`) using Python and OpenCV, protected by a user-provided password.

The final output (`encryptedImage.png`) visually looks like the original cover image but secretly contains the hidden secret image.

## Project Overview

This project demonstrates:
- **Steganography**: Hiding a secret image inside a cover image.
- **Encryption**: Using a password to securely encrypt and decrypt the hidden data.
- **Secure Data Hiding**: The cover image appears unchanged to an observer, concealing the secret communication.

## Features

- Embed (hide) a secret image within a cover image with password protection.
- Extract and decrypt the hidden image using the correct password.
- Maintain the visual integrity of the cover image.
- Secure communication with encrypted hidden data.

## Technologies Used

- Python 3
- OpenCV (`cv2`)
- Numpy
- Cryptography libraries

## How to Run

1. Install dependencies:
   ```bash
   pip install opencv-python numpy cryptography
   ```

2. To encrypt and embed the secret image:
   ```bash
   python encrypt_with_password.py
   ```
   - You will be asked to enter a **password**.
   - The output will be `encryptedImage.png`.

3. To decrypt and extract the hidden secret:
   ```bash
   python decrypt_with_password.py
   ```
   - Enter the **same password** used during encryption.
   - Outputs: 
     - `decrypted_secret.png` (the extracted secret image)
     - `decrypted_cover.png` (the reconstructed cover image)

## File Structure

| File Name              | Description                                       |
|-------------------------|---------------------------------------------------|
| `cover5.jpg`            | Original cover image used for hiding             |
| `secret5.jpg`           | Secret image to embed                             |
| `encrypt_with_password.py` | Script to encrypt and embed the secret image   |
| `decrypt_with_password.py` | Script to extract and decrypt the secret image |
| `encryptedImage.png`    | Output image containing hidden secret             |
| `decrypted_cover.png`   | Reconstructed cover image after decryption        |
| `decrypted_secret.png`  | Extracted secret image after decryption           |
| `README.md`             | Project documentation                             |

---

## Notes

- The password must match exactly during encryption and decryption.
- Using a strong password enhances the security of the hidden message.
- This project demonstrates basic concepts of steganography combined with encryption for secure hidden communication.

## Internship

This project was developed as part of my **Cybersecurity Virtual Internship** conducted by **Eduskills**.
