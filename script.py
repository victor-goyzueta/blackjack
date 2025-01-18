import random
import time

def crear_baraja():
    valores = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    palos = ['♥', '♦', '♣', '♠']
    baraja = [(valor, palo) for valor in valores for palo in palos]
    random.shuffle(baraja)
    return baraja

def mostrar_mano(mano):
    return ', '.join([f"{valor}{palo}" for valor, palo in mano])

def calcular_puntaje(mano):
    valores = {'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    total = sum(valores.get(carta[0], carta[0]) for carta in mano)
    ases = sum(1 for carta in mano if carta[0] == 'A')

    while total > 21 and ases > 0:
        total -= 10
        ases -= 1

    return total

def turno_jugador(baraja, mano):
    while True:
        print(f"\nYour hand: {mostrar_mano(mano)} (Score: {calcular_puntaje(mano)})")
        if calcular_puntaje(mano) > 21:
            print("You are over 21. You lose.")
            break
        elif calcular_puntaje(mano) == 21:
            print("Blackjack!")
            break

        accion = input("What do you want to do? (1: Give me a card, 2: I don't want any more cards): ").strip()

        if accion == '1':
            carta = baraja.pop()
            mano.append(carta)
            print(f"You have received: {carta[0]}{carta[1]}")
        elif accion == '2':
            break
        else:
            print("Invalid option. Please choose 1 or 2.")

    return True

def turno_crupier(baraja, mano):
    print(f"\nDealer's turn. Their starting hand: {mostrar_mano(mano)}")

    while calcular_puntaje(mano) < 17:
        time.sleep(2)
        carta = baraja.pop()
        mano.append(carta)
        print(f"The dealer receives: {carta[0]}{carta[1]} (Score: {calcular_puntaje(mano)})")

    puntaje = calcular_puntaje(mano)
    if puntaje > 21:
        print("The dealer has gone over 21. You win!")
    else:
        print(f"The dealer ends with: {mostrar_mano(mano)} (Score: {puntaje})")

    return puntaje

def determinar_ganador(puntaje_jugador, puntaje_crupier):
    if puntaje_jugador > 21:
        print("You lose. You exceeded 21.")
        return False
    elif puntaje_crupier > 21 or puntaje_jugador > puntaje_crupier:
        print("You win!")
        return True
    elif puntaje_jugador < puntaje_crupier:
        print("You lose. Dealer has a higher score.")
        return False
    else:
        print("It's a draw.")

def main():
    print("\nWelcome to Blackjack")
    dinero = 1000

    while dinero > 0:
        print(f"\nCurrent money: {dinero}€")
        apuesta = int(input(f"How much do you want to bet? (1-{dinero}): "))
        if apuesta <= 0 or apuesta > dinero:
            print("Invalid bet. Try again.")
            continue

        baraja = crear_baraja()

        mano_jugador = [baraja.pop(), baraja.pop()]
        mano_crupier = [baraja.pop(), baraja.pop()]

        if turno_jugador(baraja, mano_jugador):
            puntaje_jugador = calcular_puntaje(mano_jugador)
            puntaje_crupier = turno_crupier(baraja, mano_crupier)
            resultado = determinar_ganador(puntaje_jugador, puntaje_crupier)

            if resultado == True:
                dinero += apuesta
            elif resultado == False:
                dinero -= apuesta

        if dinero <= 0:
            print("\nYou have run out of money - the game is over!")
            break

    print("\nThanks for playing Blackjack, see you next time!")

if __name__ == "__main__":
    main()