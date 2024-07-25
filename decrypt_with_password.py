import cv2
import numpy as np

def get_key_from_password(password):
    # Convert the password to a key by taking its ASCII values and summing them
    key = sum([ord(char) for char in password]) % 256
    return key

# Decryption function
def decrypt(password):
    try:
        # Encrypted image
        img = cv2.imread('encryptedImage.png')
        if img is None:
            raise FileNotFoundError("encryptedImage.png not found or cannot be read.")
        
        width = img.shape[0]
        height = img.shape[1]

        # img1 and img2 are two blank images
        img1 = np.zeros((width, height, 3), np.uint8)
        img2 = np.zeros((width, height, 3), np.uint8)

        key = get_key_from_password(password)

        for i in range(width):
            for j in range(height):
                for l in range(3):
                    v1 = format(img[i][j][l] ^ key, '08b')

                    # Extracting 4 MSBs and 4 LSBs to form img1 and img2
                    v2 = v1[:4] + '0000'
                    v3 = v1[4:] + '0000'

                    # Appending data to img1 and img2
                    img1[i][j][l] = int(v2, 2) ^ key
                    img2[i][j][l] = int(v3, 2) ^ key

        # These are two images produced from the encrypted image
        cv2.imwrite('decrypted_cover.png', img1)
        cv2.imwrite('decrypted_secret.png', img2)
        print("Decryption completed. The decrypted images are saved as 'decrypted_cover.png' and 'decrypted_secret.png'.")
    
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"An error occurred: {e}")

# Driver's code
if __name__ == "__main__":
    password = input("Enter the password for decryption: ")
    decrypt(password)
