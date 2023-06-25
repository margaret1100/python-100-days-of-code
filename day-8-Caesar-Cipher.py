alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Encoding function - encrypting the message
def encrypt(text, shift):
  encrypted_text = ""
  for letter in text:
    if letter not in alphabet:
      encrypted_text += letter
    else:
      new_letter = alphabet.index(letter) + shift
      if new_letter > 25:
        new_letter -= 26
        encrypted_text += alphabet[new_letter]
      else:
        encrypted_text += alphabet[new_letter]
  return(encrypted_text)

print(encrypt(text, shift))
