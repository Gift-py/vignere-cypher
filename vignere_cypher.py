#A simple program that encodes and decodes a text with vignere cypher

#mapping each value character with a corresponding number
map = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5',
       6:'6', 7:'7', 8:'8', 9:'9',
       10:'A', 11:'B', 12:'C', 13:'D', 14:'E',
       15:'F', 16:'G', 17:'H', 18:'I', 19:'J',
       20:'K', 21:'L', 22:'M', 23:'N', 24:'O',
       25:'P', 26:'Q', 27:'R', 28:'S', 29:'T',
       30:'U', 31:'V', 32:'W', 33:'X', 34:'Y',
       35:'Z', 36:'a', 37:'b', 38:'c', 39:'d',
       40:'e', 41:'f', 42:'g', 43:'h', 44:'i',
       45:'j', 46:'k', 47:'l', 48:'m', 49:'n',
       50:'o', 51:'p', 52:'q', 53:'r', 54:'s',
       55:'t', 56:'u', 57:'v', 58:'w', 59:'x',
       60:'y', 61:'z'}




#to convert the key and text to numbers
def convert(word, map):
    #am array to store the converted text into
    num_to_wrd_arr = []

    #using nested loops for iterating through the given text and finding the corresponding value in the map
    for letter in word:
        for key, val in map.items():
            if letter == val:
                #adding the letter value into the array
                num_to_wrd_arr.append(key)
    #return the array (note the array is a list of numbers)
    return num_to_wrd_arr

#function to create the cypher
def create_cypher(word, key, map):
    #here we use the helper function to convert the text and the key into their integer values
    word_number_arr = convert(word, map)
    key_num_arr = convert(key, map)

    cypher_values_arr = []
    cypher_txt = []

    #sometime the key might be shorter than the text that needs to be cyphered
    #we use a loop to fill up the space and make the length of the key to be equal to the text to be cyphered
    #to check and resolve key_num_arr length
    i = 0
    if len(word_number_arr) > len(key_num_arr):
        while len(word_number_arr) > len(key_num_arr):
            key_num_arr.append(key_num_arr[i])
            i += 1
    
    #this adds the values in the converted key array to to the converted text array
    #i.e first number in both arrays are added together and so forth for 2nd, 3rd, ... till the nth value
    for i in range(len(word_number_arr)):
        cypher_values_arr.append(word_number_arr[i]+key_num_arr[i])

    #to convert values in cyper arr to mod 61
    #we do this because the sum of numbers in the same position in the two arrays might be more than 61
    #so we need to mod the numbers
    j = 0
    for num in cypher_values_arr:
        if int(num) > 61:
            num = num - 61
            cypher_values_arr[j] = num
        j+=1   

    #to convert values in cypher arr to string format
    #by looking for the corresponding value of the key in the map dictionary
    for num in cypher_values_arr:
        for key, value in map.items():
            if num == key:
                cypher_txt.append(value)
    
    return cypher_txt



#decode function
def decode(text, key, map):
    # here we convert the cryptic text and key to their array function
    word_number_arr = convert(text, map)
    key_num_arr = convert(key, map)

    print(word_number_arr)
    print(key_num_arr)

    _values_arr = []
    _txt = []

    #to check resolve key_num_arr length
    #sometime the key might be shorter than the text that needs to be cyphered
    #we use a loop to fill up the space and make the length of the key to be equal to the text to be cyphered
    i = 0
    if len(word_number_arr) > len(key_num_arr):
        while len(word_number_arr) > len(key_num_arr):
            key_num_arr.append(key_num_arr[i])
            i += 1
    
    for i in range(len(word_number_arr)):
        _values_arr.append(word_number_arr[i]-key_num_arr[i])

    #to convert values in cyper arr to mod 61
    #we do this because the sum of numbers in the same position in the two arrays might be more than 61
    #so we need to mod the numbers
    j = 0
    for num in _values_arr:
        if int(num) < 0:
            num = 61 + num
            _values_arr[j] = num
        j+=1   

    #to convert values in cypher arr to string format
    for num in _values_arr:
        for key, value in map.items():
            if num == key:
                _txt.append(value)
    
    return _txt


#test case
text = 'IngRouP2CryPtoGraPhyIs4n'
key = 'VEGENIERE'

#concatenating the values in the cypher text array (list)
cryptic_text = ''.join(create_cypher(text, key, map))

#concatenating the values in the cypher text array (list)
text_ = ''.join(decode(cryptic_text, key, map))
print(text_)