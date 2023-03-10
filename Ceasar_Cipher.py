def rot(character, key):

    size_of_alphabet = ord('Z') - ord('A') + 1

    key %= size_of_alphabet
    if key < 0: 
        key = size_of_alphabet + key
    new_char = ord(character)
    new_char += key
    

    #check if our character is a letter
    if  'a' <= character <= 'z':
        new_char = (new_char - ord('a')) % size_of_alphabet + ord('a')
    elif 'A' <= character <= 'Z':
        new_char = (new_char - ord('A')) % size_of_alphabet + ord('A')
    else:
        #there was no change so we can return what was passed
        return character
    
    return chr(new_char) #convert ASCII number to char


def rot_whole_string(text,key):
    return "".join(rot(character,key) for character in text)

text = """
Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcenfr fv orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabthu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orgnf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba bg thrff.
Gurer fubhyq or bar-- naq cersrenoylbayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arrire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!
"""


print(rot_whole_string(text, 13))