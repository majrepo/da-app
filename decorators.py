# Stwórz dekorator greetings, który opakowuje funkcję zwracającą stringa zawierającego
# imię bądź imiona oraz nazwisko. Dekorator ma sformatować tego stringa tak, 
# że pierwsza litera każdego z imion oraz nazwiska ma być pisana z dużej litery. 
# Pozostałe litery mają być z małej. Ponad to, dekorator ma również dodać Hello na początek string'a.


# def greetings(fn):
#     def wrapper(*args, **kwars):
#         return f"Hello {fn(*args, **kwars)}"   
#     return wrapper

# @greetings
# def name_surname(name):
#     return name.lower().title()

# print(name_surname("anna kowalska"))


# Kolejne zadanie to stworzenie dekoratora is_palindrome, opakowującego funkcję zwracającego stringa. 
# Zadaniem tego dekoratora jest doklejenie do wartości zwróconej przez funkcję - is palindrome lub - is not palindrome 
# w zależności czy to co zwróciła funkcja jest palindromem czy też nie. 
# Przy określaniu czy dane słowo/zdanie jest palindromem bierzemy pod uwagę tylko litery oraz cyfry. Resztę pomijamy.

# import string

# def is_palindrome(fn):
#     def wrapper(*args, **kwars):
#         val = fn(*args, **kwars)
#         if val == val[::-1]:
#             return f"{val}- is palindrome"
#         else:
#             return f"{val}- is not palindrome"   
#     return wrapper

# @is_palindrome
# def palindrome(s):
#     s = s.lower()
#     s = s.replace(" ", "")
#     s = s.translate(str.maketrans('', '', string.punctuation))
#     return s


import string

def is_palindrome(fn):
    def wrapper(*args, **kwars):
        def palindrome(s):
            s = s.lower()
            s = s.replace(" ", "")
            s = s.translate(str.maketrans('', '', string.punctuation))
            return s
        val = palindrome(fn(*args, **kwars))
        if val == val[::-1]:
            return f"{val} - is palindrome"
        else:
            return f"{val} - is not palindrome"   
    return wrapper
@is_palindrome
def hehe(name):
    return name

print(hehe("alaggg"))


# Napisz dekorator format_output, który przyjmuje argumenty pozycyjne w postaci stringów oraz opakowuje funkcję 
# zwracającą dict'a. Zadaniem dekoratora jest przeformatowanie dict'a pozostawiając tylko kluczę z argumentów dekoratora 
# i odpowiadające im wartości. Uwaga! Jednakże niektóre klucze w argumentach dekoratora są dosyć nietypowe, 
# gdyż mogą składać się z kilku pojedynczych kluczy. Wtedy takie klucze są połączone podwójną podłogą __, 
# wartością nowo utworzonego klucza będą wartośi kluczy składowych połączone pojedynczą spacją. 
# W przypadku podania nieistniejącego klucza lub klucza źle zdefiniowanego, dekorator ma rzucić wyjątkiem ValueError.
