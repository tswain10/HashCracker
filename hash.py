import binascii
import hashlib

def hash(salt, passwd):
    sx = binascii.unhexlify(salt)
    pb = passwd.encode("utf-8")
    md5sum = hashlib.md5(sx + pb).digest()
    return hashlib.sha1(sx + md5sum + pb).hexdigest()

def checkOneWord(name, salt, myhash):
    with open('c:\\Users\\TreyS\\OneDrive\\Desktop\\cracklib-small.txt', 'r') as wordfile:
        for word in wordfile:
            newhash = hash(salt,word.strip())
            if (newhash == myhash): #if one word pass
                print(name + ' - '+word.strip())
                return True
            newhash = hash(salt,word.strip()[::-1]) #reverse word
            if (newhash == myhash): #if one word pass
                print(name + ' - '+word.strip())
                return True
            
def checkTwoWords(name, salt, myhash):
    with open('c:\\Users\\TreyS\\OneDrive\\Desktop\\cracklib-small.txt', 'r') as wordfile:
        for word in wordfile:
            for word2 in wordfile:
                twowords = word.strip()+word2.strip()
                newhash2 = hash(salt,twowords)
                if (newhash2 == myhash): #if two word pass
                    print(name + ' - '+twowords)
                    return True
                twowords = word.strip()[::-1]+word2.strip() #1st word flipped
                newhash2 = hash(salt,twowords)
                if (newhash2 == myhash): #if two word pass
                    print(name + ' - '+twowords)
                    return True
                twowords = word.strip()+word2.strip()[::-1] #2nd word flipped
                newhash2 = hash(salt,twowords)
                if (newhash2 == myhash): #if two word pass
                    print(name + ' - '+twowords)
                    return True
                twowords = word.strip()[::-1]+word2.strip()[::-1] #both words flipped
                newhash2 = hash(salt,twowords)
                if (newhash2 == myhash): #if two word pass
                    print(name + ' - '+twowords)
                    return True
                
def checkThreeWords(name, salt, myhash):
    with open('c:\\Users\\TreyS\\OneDrive\\Desktop\\cracklib-small.txt', 'r') as wordfile:
        for word in wordfile:
            for word2 in wordfile:
                for word3 in wordfile:
                    threewords = word.strip()+word2.strip()+word3.strip()
                    newhash3 = hash(salt,threewords)
                    if (newhash3 == myhash): #if threewords word pass
                        print(name + ' - '+threewords)
                        return True

with open('c:\\Users\\TreyS\\OneDrive\\Desktop\\hashes.txt', 'r') as hashfile:
    for thehash in hashfile:
        #found = False
        name = thehash.split(':')[0].strip()
        salt = thehash.split(':',1)[1][6:22].strip()
        myhash = thehash.split(':',1)[1][23:70].strip()
        print(name + ' '+salt+' '+myhash)
        found1 = checkOneWord(name, salt, myhash)
        if found1: print('Found '+name)
        else: 
            found2 = checkTwoWords(name, salt, myhash)
            if found2: print('Found '+name)
            else: 
                found3 = checkThreeWords(name, salt, myhash)
                if found3: print('Found '+name)

        # with open('c:\\Users\\TreyS\\OneDrive\\Desktop\\cracklib-small.txt', 'r') as wordfile:
                        
        #         for word in wordfile:
        #             if found == True: break
        #             newhash = hash(salt,word.strip())
        #             if (newhash == myhash): #if one word pass
        #                 print(name + ' - '+word.strip())
        #                 found = True
        #                 break
        #             else:
        #                 for word2 in wordfile:
        #                     if found == True: break
        #                     twowords = word.strip()+word2.strip()
        #                     newhash2 = hash(salt,twowords)
        #                     if (newhash2 == myhash): #if two word pass
        #                         print(name + ' - '+twowords) 
        #                         found = True
        #                         break
                        
                            # for word3 in wordfile:
                            #     threewords = word.strip()+word2.strip()+word3.strip()
                            #     newhash3 = hash(salt,threewords)
                            #     if (newhash3 == myhash): #if three word pass
                            #         print(name + ' - '+threewords)
                            #         found = True
                        
                    
