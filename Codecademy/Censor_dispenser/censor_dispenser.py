negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censorone(string):
  for i in range(len(string)):
    if string[i:i+19]=="learning algorithms":
      email=string.replace(string[i:i+19],"-"*19)
  return email

#print(censorone(email_one))
def censortwo(email):
  for word in proprietary_terms:
      if word in email:
          email=email.replace(word,len(word)*"*",-1)
  return email
#print(censortwo(email_two))
def censorthree(email):
  for word in proprietary_terms:
    if word in email:
        email=email.replace(word,len(word)*"*",-1)
  i=0
  for word in negative_words:
    email.count(word)
    i+=1
    if i>=2:
      email=email.replace(word,len(word)*"*",-1)
  return email

#print(censorthree(email_three))
"""def censorfour(email):
  for word in proprietary_terms:
    if word in email:
        email=email.replace(word,len(word)*"*",-1)
  i=0
  for word in negative_words:
    email.count(word)
    i+=1
    if i>=2:
      email=email.replace(word,len(word)*"*",-1)
  return email""" 
"""Test of multiples lines comment
"""  
def censor_four(email, a=proprietary_terms, b=negative_words):
    email=email.strip()
    email=email.split()
    output = []
    censored = set(a+b)
    censor_next = False

    for word in email:
        if censor_next:
            output.append("/" * len(word))
            censor_next = False
        elif word in censored:
            if output:
                before_word = output.pop(-1)
                output.append("0" * len(before_word))
            output.append("*" * len(word))
            censor_next = True
        else:
            output.append(word)

    return " ".join(output)

print(censor_four(email_four,proprietary_terms,negative_words))
    