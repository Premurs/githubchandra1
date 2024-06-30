import speech_recognition as sr




while True:
    r = sr.Recongnizer()
    with sr.Microphone() as source:
        audio = r.listen(source)



        try:
            filename = "draft.txt"
            f = open(filename, "a+")



            recognized_text = r.recognize_google(audio)
            print(reconized_text)
            remainder = recognized_text.split()
            while remainder:
                line, remainder = reminder[:5],remainder[5:]
                f.write(''.join(line) + "/n")
            if recognized_text == 'bye':
                break
            
         except sr.unknownvalueerror:
             print('Google could not understand audio')
         except sr.requesterror as e:
             print('Google error: {0}'.format(e))
