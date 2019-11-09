def get_clean_words(file_name):
        """Get a list of single-word strings from source text.
            Param: file_name(str)
            Return: words(list) """
        words = []
        with open(file_name, "r") as file:
            # make a list ofd words, contains non alphabetic chars
            words = file.read().split()
            # remove all occurrences of non-alpha chars from data
            clean_words = []
            for word in words:
                clean_word = ([char for char in word if not (
                    char == "." or
                    char == "?" or
                    char == "!" or
                    char == "," or
                    char == ":" or
                    char == ";" or
                    char == "(" or
                    char == ")" or
                    char == "\""  # or
                    # char == "'" or
                    # char == "-"
                )])
                clean_words.append(clean_word)
            # make a list of whole words only containing letters
            clean_words_as_str = []
            for list_of_chars in clean_words:
                whole_word = ""
                clean_words_as_str.append(whole_word.join(list_of_chars))

        return clean_words_as_str

