"""
Using encoder and encrypt as models, implement the functions decoder and 
decrypt. Use them to decrypt the message
22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*137*59*11*23*11*1*57*6*173*7*11
which was encrypted using the opening of Don Quixote.
"""

Don_Quixote = 'In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing.'
       
encrypted_message = '22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*137*59*11*23*11*1*57*6*173*7*11'

gen_decode_keys = (lambda book, cipher_text:
                   {s: book[int(s)] for s in cipher_text.split('*')})

#print(gen_decode_keys(Don_Quixote, encrypted_message))

decoder = (lambda decode_keys, cipher_text:
           ''.join(decode_keys[i] for i in cipher_text.split('*')))
    
#print(decoder(gen_decode_keys(Don_Quixote, encrypted_message), encrypted_message))
    
decrypt = (lambda book, cipher_text:
           decoder(gen_decode_keys(book, cipher_text), cipher_text))

print(decrypt(Don_Quixote, encrypted_message))
