def order(sentence):
  risultato = ''
  
  if len(sentence) != 0:
      dizionario = {'vuoto':''}
      lista = sentence.split()
      for parola in lista:
          for lettera in parola:
              if lettera.isdigit():
                  print('lettera:', lettera, 'parola:', parola)
                  dizionario[str(lettera)] = parola
        
      print('dizionario:', dizionario)
                  
      for indice in range(1, 10):
          if str(indice) in dizionario.keys():
              risultato += dizionario[str(indice)] + ' '

  risultato = risultato[:len(risultato)-1]
  
  return risultato
