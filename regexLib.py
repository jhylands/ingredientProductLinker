#libary of regex
import re
class libRegex():
    self.models = {}
    #https://stackoverflow.com/questions/51828712/r-regular-expression-for-extracting-uk-postcode-from-an-address-is-not-ordered
    self.models['postcode'] = r'\b(?:([Gg][Ii][Rr] ?0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([AZa-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) ?[0-9][A-Za-z]{2}))\b'

    #http://emailregex.com/
    self.models['email'] = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"

    #https://stackoverflow.com/questions/2577236/regex-for-zip-code
    self.mode['zip_code'] = r"^\d{5}(?:[-\s]\d{4})?$"

    self.mode['number']

    self.mode['uni_frac']="(?:[\u00BC-\u00BE]|[\u2150-\u215E])"


    def __call__(self,regex):   
        
    def compile(self.regex):
        #https://stackoverflow.com/questions/6487501/python-3-2-how-to-pass-a-dictionary-into-str-format
        return re.compile(
                    regex.format(**self.models)
                    )
