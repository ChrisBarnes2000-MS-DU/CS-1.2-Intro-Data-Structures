import re

def tokenize(text):
    print("--Text--\n", text, "\n")
    no_punc_text = remove_punctuation(text)
    lines = split_on_end(no_punc_text)
    # tokens = split_on_whitespace(lines)
    # return tokens
    return lines

def remove_punctuation(text):
    no_punc_text = re.sub('[,()]', '', text)
    no_punc_text = re.sub('--', ' ', no_punc_text)
    print("--No Punctuation--\n", no_punc_text, "\n")
    return no_punc_text

def split_on_end(text):
    print("--Split by line--")
    text = re.sub(r'\.', " [STOP].", text)
    lines = re.split(r'\.', text)
    [print(line) for line in lines]
    return lines

def split_on_whitespace(text):
    return re.split(r'\s+', text)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        source = open(filename).read()
        tokens = tokenize(source)
        # print(tokens)
    else:
        print('No source text filename given as argument')
