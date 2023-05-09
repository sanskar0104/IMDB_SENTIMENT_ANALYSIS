from googletrans import Translator,constants

class translate():
    
    ''' Conversion of all other languages other than English into English'''
    
    def __init__(self):
        pass
    
    def conversion(self,sen):
        
        translator = Translator()
        detection = translator.detect(sen)
        
        if (constants.LANGUAGES[detection.lang]=='english'):
            return sen
        else:
            translations = translator.translate(sen)
            return translations.text