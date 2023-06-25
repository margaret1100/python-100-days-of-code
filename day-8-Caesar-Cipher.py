alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Encoding function - encrypting the message
def caesar(given_text, shift_amount, cipher_direction):
  returned_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  # Handle non-alphabetic code 
  for letter in given_text:
      if letter not in alphabet:
        returned_text += letter
      else:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        returned_text += alphabet[new_position]
  return (returned_text)

print(caesar(text, shift, direction))