def displayInstructions():
    while True:
        langCode=int(input(f'1 - English or 2 - Espanol >> '))
        if langCode == 1:
            ENGLISH_PROMPT = 'Please enter your weight in pounds >> '
            return ENGLISH_PROMPT
        elif langCode == 2:
            SPANISH_PROMPT = "Por favor entre en su peso en libras >> "
            return SPANISH_PROMPT
        continue

#MOON_FACTOR= 0.166
#weight=int(input(displayInstructions()))
#moonWeight = weight * MOON_FACTOR
#print(f'Your weight on the moon would be {round(moonWeight, 2)} pounds!')
print(f'Your weight on the moon would be {round(float(input(displayInstructions())) * 0.166, 2)} pounds!')