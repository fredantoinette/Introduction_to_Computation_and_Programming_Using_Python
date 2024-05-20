"""
If a character occurs in the plain text but not in the book, something bad 
happens. The code_keys dictionary will map each such character to -1, and 
decode_keys will map -1 to whatever the last character in the book happens to 
be.

Remedy the problem described above. Hint: a simple way to do this is to create 
a new book by appending something to the original book.
"""

gen_code_keys = (lambda book, plain_text, new: (
    {c: str(book.find(c)) if book.find(c) != -1 else str((book + new).find(c)) 
     for c in plain_text}))

Don_Quixote = 'In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing.'

            
new_book = 'the quick brown fox jumps over the lazy dog. THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG. numbers: 0123456789. some symbols: ,.!"£$%^&*()_+-=:;@?'

print(gen_code_keys(Don_Quixote, 'This is about dictionary comprehension :)', new_book))

#encoder = (lambda code_keys, plain_text: 
#           ''.join(['*' + code_keys[c] for c in plain_text])[1:])
    
encoder = (lambda code_keys, plain_text: 
           '*'.join([code_keys[c] for c in plain_text]))

encrypt = (lambda book, plain_text, new = '': 
           encoder(gen_code_keys(book, plain_text, new), plain_text))

print(encrypt(Don_Quixote, 'no is no'))

print(encrypt(Don_Quixote, 'This is about dictionary comprehension :)', new_book))

gen_decode_keys = (lambda book, cipher_text, new = '':
                   {s: (book + new)[int(s)] for s in cipher_text.split('*')})

print(gen_decode_keys(Don_Quixote, '1*13*2*6*57*2*1*13'))
print(gen_decode_keys(Don_Quixote, '269*23*6*57*2*6*57*2*3*173*13*174*27*2*55*6*22*27*6*13*1*3*59*204*2*22*13*33*137*59*11*23*11*1*57*6*13*1*2*321*360', new_book))
