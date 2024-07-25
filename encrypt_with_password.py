import cv2
import numpy as np

def get_key_from_password(password):
    # Convert the password to a key by taking its ASCII values and summing them
    key = sum([ord(char) for char in password]) % 256
    return key

# Encryption function
def encrypt(password):
    try:
        # img1 and img2 are the two input images
        img1 = cv2.imread('cover5.jpg')
        img2 = cv2.imread('secret5.jpg')
        
        if img1 is None:
            raise FileNotFoundError("cover5.jpg not found or cannot be read.")
        if img2 is None:
            raise FileNotFoundError("secret5.jpg not found or cannot be read.")
        
        if img1.shape[0] < img2.shape[0] or img1.shape[1] < img2.shape[1]:
            raise ValueError("The cover image must be equal or larger than the secret image in both dimensions.")
        
        key = get_key_from_password(password)
        
        for i in range(img2.shape[0]):
            for j in range(img2.shape[1]):
                for l in range(3):
                    # v1 and v2 are 8-bit pixel values of img1 and img2 respectively
                    v1 = format(img1[i][j][l] ^ key, '08b')
                    v2 = format(img2[i][j][l] ^ key, '08b')

                    # Taking 4 MSBs of each image
                    v3 = v1[:4] + v2[:4]

                    img1[i][j][l] = int(v3, 2) ^ key

        cv2.imwrite('encryptedImage.png', img1)
        print("Encryption completed. The encrypted image is saved as 'encryptedImage.png'.")
    
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except ValueError as val_error:
        print(val_error)
    except Exception as e:
        print(f"An error occurred: {e}")

# Driver's code
if __name__ == "__main__":
    password = input("Enter the password for encryption: ")
    encrypt(password)
