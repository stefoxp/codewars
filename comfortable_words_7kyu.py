def comfortable_word(word):
  risultato = False
  lista = []
  dx = ('y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm')
  
  for i in range(1, len(word)):
      if (word[i] in dx):
          if (not (word[i - 1] in dx)):
              lista.append(True)
          else:
              lista.append(False)
      else:
          if word[i - 1] in dx:
              lista.append(True)
          else:
              lista.append(False)
              
  if not(False in lista):
      risultato = True
  
  return risultato
