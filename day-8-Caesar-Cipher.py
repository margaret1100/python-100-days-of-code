alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Encoding function - encrypting the message
def encrypt(plain_text, shift_amount):
  encrypted_text = ""
  for letter in plain_text:
    if letter not in alphabet:
      encrypted_text += letter
    else:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      if new_position > 25:
        new_position -= 26
        encrypted_text += alphabet[new_position]
      else:
        encrypted_text += alphabet[new_position]
  return(encrypted_text)

#decoding function - decrypting the message
def decrypt(cipher_text, shift_amount):
  decrypted_text = ""
  for letter in cipher_text:
    if letter not in alphabet:
      decrypted_text += letter
    else:
      position = alphabet.index(letter)
      new_position = position - shift_amount
      decrypted_text += alphabet[new_position]
  return(decrypted_text)

if direction.lower() == 'encode':
  print(encrypt(text, shift))
elif direction.lower() == 'decode':
  print(decrypt(text, shift))
else:
  print("Error, please type encode or decode")
