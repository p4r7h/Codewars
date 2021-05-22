#Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

def reverse_words(text):
    return ' '.join(text.split(' ')[::-1])[::-1]
  
# test case 
"""
test.assert_equals(reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god')
        test.assert_equals(reverse_words('apple'), 'elppa')
        test.assert_equals(reverse_words('a b c d'), 'a b c d')
        test.assert_equals(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')  
"""
