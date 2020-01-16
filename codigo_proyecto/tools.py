def make_paragraphs(texts, min_len = 10, max_len = 300):
    paragraphs_list = []
    
    for text in texts:
        paragraphs_list.extend([paragraph for paragraph in text.split('\n')])
    
    paragraphs_list = [par.strip() + 'EOS' for par in paragraphs_list if (len(par.split(' ')) < max_len and len(par.split(' ')) > min_len)]
    paragraphs_list.sort(key=len)
    return paragraphs_list 


def make_tokens(paragraphs):
    tokens = [par.split() for par in paragraphs]
    return tokens


