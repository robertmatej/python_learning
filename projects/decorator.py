def dekor(funkcja):
    def wew():
        print("Dekorujemy funkcję")
        return funkcja()
    return wew

@dekor
def zwykłaFunkcja():
    print("To jest zwykła funkcja")

zwykłaFunkcja()