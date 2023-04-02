#for english and german people (language)

def QUIZ():
    chooseLanguage = input('Choose your Language(German/English): ')
    if chooseLanguage == 'German' or chooseLanguage == 'G':
        schwierigkeit = input('Wähle deinen Schwierigkeitsgrad(Schwer(s), Mittel(m), Leicht(l)): ')
        if schwierigkeit == 'Schwer' or schwierigkeit == 's':
            frage1 = input('Wieviele Atome gibt es im Universum?: ')
            if frage1 == '10-80':
                print('Richtig!')
            else:
                print('Leider Falsch!')

            frage2 = input('Was ist das älteste bekannte Lebenswesen?: ')
            if frage2 == 'Great Basin-Bristlecone-Kiefer' or frage2 == 'Pinus longaeva':
                print('Richtig!')
            else:
                print('Falsch.')

            frage3 = input('Was war das stärkste, jemals aufgezeichnete Lebewesen?: ')
            if frage3 == 'Valdivia Chile' or frage3 == 'Valdivia' or frage3 == 'Chile':
                print('Richtig!')
            else:
                print('Falsch')

            frage4 = input('Wieviele Menschliche Sprachen gibt es auf der Welt?: ')
            if frage4 == '7000':
                print('Richtig!')
            else:
                print('Falsch!')

            frage5 = input('Wieviele Sterne gibt es in unserer Milchstraße?(circa): ')
            if frage5 == '100 Milliarden' or frage5 == '100000000000':
                print('Richtig!')
            else:
                print('Leider Falsch!')

            frage6 = input('Was ist (circa) die Größe des Universums?(Durchmesser in Lichtjahre): ')
            if frage6 == '93' or frage6 == '93 Milliarden' or frage6 == '93000000000':
                print('Richtig!')
            else:
                print('Hmmm...Leider Falsch!')

            frage7 = input('Masterfrage! Wie lautet die genaue Zahl von Pi auf die 100.000ste Nachkommastelle?: ')
            if frage7 == '3,1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679':
                print('WOW! DU BIST KRASSS!')
            else: 
                print('Ja, das wahr klar du es nicht weißt. :)')
        
        elif schwierigkeit == 'Mittel' or schwierigkeit == 'm':
            frage8 = input('Was ist der Höchste Berg der Welt?: ')
            if frage8 == 'Mount Everest':
                print('Richtig! Aber das wahr erst der Anfang!')
            else:
                print('Leider Falsch!')

            frage9 = input('Wieviele Kontinente gibt es auf der Erde?: ')
            if frage9 == '5' or frage9 == 'fünf' or frage9 == '5 Kontinente' or frage9 == 'Fünf Kontinente':
                print('Richtig')
            else:
                print('Nicht Richtig!!')

            frage10 = input('Was ist der kleinste Planet in unserem Sonnensystem?(ausgenommen Pluto): ')
            if frage10 == 'Merkur':
                print('Richtig!')
            else:
                print('Falsch!')

            frage11 = input('Wie heißt die Hauptstadt von Kanada?: ')
            if frage11 == 'Ottawa':
                print('Richtige Hauptstadt!')
            else: 
                print('Leider Falsch!')

            frage12 = input('Wer schrieb das Buch "Der kleine Prinz"?: ')
            if frage12 == 'Antoine de Saint-Exupéry' or frage12 == 'Antoine de Saint-Exupery':
                print('Richtig!')
            else:
                print('Falsch!')

            frage13 = input('Wieviele Bundesstaatten hat die USA?: ')
            if frage13 == '50':
                print('Richtig')
            else:
                print('Falsch')

            frage14 = input('Was ist das am meisten vorkommende chemische Element in unserem menschlichen Körper?: ')
            if frage14 == 'Sauerstoff' or frage14 == 'Wasser':
                print('Richtig!')
            else:
                print('Falsch')

        elif schwierigkeit == 'Leicht' or schwierigkeit == 'l':
            frage15 = input('Wieviele Monate haben mindestens 28 Tage?: ')
            if frage15 == 'Alle':
                print('Richtig!')
            else:
                print('Falsch!')

            frage16 = input('Wer hat das Telefon erfunden?: ')
            if frage16 == 'Alexander Graham Bell':
                print('Sehr richtig!')
            else: 
                print('Falsch...')

            frage17 = input('Was ist die Hauptstadt von Berlin?: ')
            if frage17 == 'Berlin':
                print('Richtig!')
            else:
                print('Falsch!!')

            frage18 = input('Wieviele Beine hat eine Spinne?: ')
            if frage18 == '8' or frage18 == 'acht':
                print('Richtig!')
            else: 
                print('Falsch!')

            frage19 = input('Was ist das größte Tier der Welt?: ')
            if frage19 == 'Giraffe':
                print('Das war leicht. Richtig!')
            else:
                print('Schade!')

            frage20 = input('Was ist das Symbol für Wasserstoff im Periodensystem?: ')
            if frage20 == 'H':
                print('Richtig!')
            else: 
                print('Falsch')

            frage21 = input('Bist du gut in/m Quizzen?(j/n): ')
            if frage21 == 'j' or frage21 == 'J' or frage21 == 'n' or frage21 == 'N':
                print('JA DAS WUSSTE ICH!')
    
    elif chooseLanguage == 'English' or chooseLanguage == 'E':
        level = input('Choose your Level(Easy, Medium, Hard): ')
        if level == 'Easy' or level == 'E':
            question1 = input('Who is the current president from the USA?: ')
            if question1 == 'Joe Biden':
                print('Yes, your right!')
            else:
                print('No, thats wrong!')

            question2 = input('What is the capital City of Germany?: ')
            if question2 == 'Berlin':
                print('Yeah, of course!')
            else:
                print('Wrong!')

            question3 = input('What is the largest planet in our solar system?: ')
            if question3 == 'Jupiter':
                print('Yes!')
            else:
                print('Soryy, thats wrong')

            question4 = input('What is the smallest continent in the world?: ')
            if question4 == 'Australia' or question4 == 'australia':
                print('Right.')
            else:
                print('False')

            question5 = input('Whats the name of the famous detective?: ')
            if question5 == 'Sherlock Holmes':
                print('Right!')
            else:
                print('False')

            question6 = input('What is the largest mammel on earth?: ')
            if question6 == 'Blue Whale':
                print('Yes your right')
            else:
                print('False.')

            question7 = input('Who painted the famous work of art called "Mona Lisa"?: ')
            if question7 == 'Leonardo da Vinci':
                print('Yes!')
            else:
                print('Not correct.')

        elif level == 'Medium' or level == 'M':
            question8 = input('Who is the author from "To kill a Mockingbird"?: ')
            if question8 == 'Harper Lee':
                print('Correct.')
            else:
                print('No, its Harper Lee.')

            question9 = input('Whats the world largest dessert?')
            if question9 == 'Sahara' or question9 == 'Sahara Dessert':
                print('OK. Thats right.')
            else:
                print('False.')

            question10 = input('Who wrote the famous play "Romeo and Juliet"?: ')
            if question10 == 'William Shakespeare' or question10 == 'Shakespeare':
                print('YES.')
            else:
                print('False.')

            question11 = input('Who is the current Prime Minister of Canada?: ')
            if question11 == 'Justin Trudeau':
                print('Right.')
            else:
                print('False.')

            question12 = input('What is the smallest country in the world by land area?: ')
            if question12 == 'Vatican City' or question12 == 'Vatican':
                print('Yes.')#
            else:
                print('No.')

            question13 = input('Which gas makes up the majority of Earths atmosphere?: ')
            if question13 == 'Nitrogen':
                 print('Yes')
            else:
                print('False.')

            question14 = input('Who was the first woman to win a Nobel Prize (in any category)?: ')
            if question14 == 'Marie Curie':
                print('Right.')
            else:
                print('Wrong')

        elif level == 'H' or level == 'Hard':
            question15 = input('What is the mathematical constant e (Eulers number) approximately equal to?: ')
            if question15 == '271828' or question15 == '2.71828':
                print('WOW. Your good.')
            else:
                print('No one said its easy.')

            question16 = input('Who invented the first practical telephone?: ')
            if question16 == 'Alexander Graham Bell':
                print('Right.')
            else:
                print('False.')

            question17 = input('Which element has the highest melting point?: ')
            if question17 == 'Tungsten':
                print('Yes.')
            else:
                print('No')

            question18 = input('What is the name of the highest Mountain in Africa?: ')
            if question18 == 'Kilimanjaro' or question18 == 'Mountain Kilimanjaro':
                print('Yes. Thats correct.')
            else:
                print('False.')

            question19 = input('Who won the 1983 Nobel Prize in Physics for their work on the discovery of the W and Z bosons?: ')
            if question19 == 'Carlo Rubbia and Simon van der Meer' or 'Carlo Rubbia' or 'Simon van der Meer':
                print('Yes.')
            else:
                print('False.')

            question20 = input('Which painter created the famous "Guernica" mural, depicting the bombing of a Spanish town during the Spanish Civil War?: ')    
            if question20 == 'Pablo Picasso':
                print('Right.')
            else:
                print('False.')

            question21 = input('What is the longest river in Asia?: ')      
            if question21 == 'Yangtze River' or  question21 == 'Yangtze' or question21 == 'Changjiang' or question21 == 'Changjiang River':
                print('Yes. Ur good.')
            else:
                print('Not correct.')   

    
QUIZ()