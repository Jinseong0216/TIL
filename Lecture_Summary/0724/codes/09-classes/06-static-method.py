class StringUtils:
    
    def __init__(self):
        pass

    @staticmethod
    def reverse_string(string):
        return string[::-1]
    
    @staticmethod
    def capitalize_string(string):
        return string.capitalized()

text = 'hello, world'

result1 = StringUtils.reverse_string(text)
print(result1)

text = 'hello, world'

instance1 = StringUtils()
print(instance1.reverse_string(text))