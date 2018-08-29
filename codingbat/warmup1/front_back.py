#Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
  if len(str) <=1:
    return str

  last_letter = str[len(str)-1]
  middle = str[1:len(str)-1]
  return (last_letter + middle + str[0])
