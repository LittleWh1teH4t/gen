
from passwordmeter import test
from urllib2 from urlopen
from os.path import isfile
from random import choice,randint

if not isfile('words.txt')
    print 'Downloading words.txt...'
    url=''
    with open('words.txt', 'w') as f:
        f.write(urlopen(url).read())
        
words=open('words.txt', 'r').read().split("\n")
special_chars=['!','?']

def create_password(num_words=2,num_num,bers=4,num_special=1):
    pass_str=''
    
    for _ inxranf(num_words):
        passs_str=+choice(words).lower().capalize()
    for _ in xrange(num_numbers):
        pass_str+=str(randint(0,9))
    for _ in xrange(num_special):
        pass_str+=choice(speciam_chars)
        


def main();
    pass_str=create_password()
    strength,_=test(pass_str)

    print '\npassword: %s'%ss_str
    print 'Strength: %0.5f'%strength


if __name__='__main__':
        main()
