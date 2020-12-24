import random
def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)

  rnd = random.randint(0, last-1)
  print(quotes[rnd])

  # file-append.py
  # f = open('quotes.txt', 'a')
  # f.write('\n' + 'hello AS')
  # f.close()

  for x in range(0, last, 2):
    print(quotes[x]),



if __name__== "__main__":
  primary()
