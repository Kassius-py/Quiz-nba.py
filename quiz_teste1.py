pontos = 0

print("QUIZ NBA\n")

# pergunta 1
print("Quem ganhou o MVP em 2016?")
print("A) LeBron James")
print("B) Stephen Curry")
print("C) Kevin Durant")
print("D) James Harden")

r = input("Resposta: ")

if r == "B" or r == "b":
    print("acertou\n")
    pontos = pontos + 1
else:
    print("errou, era B\n")

# pergunta 2
print("Quem é o Greek Freak?")
print("A) Jokic")
print("B) Giannis")
print("C) Embiid")
print("D) Luka")

r = input("Resposta: ")

if r == "B" or r == "b":
    print("acertou\n")
    pontos = pontos + 1
else:
    print("errou, era B\n")

# pergunta 3
print("Quem ganhou a NBA em 2019?")
print("A) Lakers")
print("B) Warriors")
print("C) Raptors")
print("D) Heat")

r = input("Resposta: ")

if r == "C" or r == "c":
    print("acertou\n")
    pontos = pontos + 1
else:
    print("errou, era C\n")

# pergunta 4
print("Quem jogava com Curry no Warriors?")
print("A) Draymond Green")
print("B) Kobe Bryant")
print("C) Derrick Rose")
print("D) Westbrook")

r = input("Resposta: ")

if r == "A" or r == "a":
    print("acertou\n")
    pontos = pontos + 1
else:
    print("errou, era A\n")

# pergunta 5
print("Quem fez 'The Decision'?")
print("A) Wade")
print("B) LeBron")
print("C) Bosh")
print("D) Melo")

r = input("Resposta: ")

if r == "B" or r == "b":
    print("acertou\n")
    pontos = pontos + 1
else:
    print("errou, era B\n")

print("fim do quiz")
print("pontos:", pontos)
