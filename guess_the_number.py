import random

correct = 'you guessed correctly!'

too_low = 'Too Low!!!'

too_high = 'too high'


def configure_range():
    """ Set the high and low values for the random number """
    return 1, 1000


def generate_secret(low, high):
    """ Generate a secret number for the user to guess """
    return random.randint(low, high)


def get_guess():
    while True:
        try:
            """ get user's guess, as an integer number """
        
            return int(input('Guess the secret number? '))
        except:
            print("not a correct number")


def check_guess(guess, secret):
    """ compare guess and secret, return string describing result of comparison """
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():
    
    attempts = 0
    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        #Added guess counter to code
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)
        attempts += 1
        

        if result == correct:
            while True:
                answer = str(input('Run again? (y/n): '))
                if answer in ('y', 'n'):
                    break
                print("invalid input.")
            if answer == 'y':
                continue
                
            else:
                break

    print('Thanks for playing the game!')
        

if __name__ == '__main__':
    main()
