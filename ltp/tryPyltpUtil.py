from LtpUtil import LtpUtil


ltpUtil = LtpUtil()
sentence = '周杰伦关于妈妈的歌'
words = list(ltpUtil.Segmentor(sentence))
postags = list(ltpUtil.Postagger_with_words(words))
netags = list(ltpUtil.NamedEntityRecognizer_with_wordsAndPostags(words,postags))
arcs = ltpUtil.Parser_with_wordsAndPostags(words,postags)
print(words)
print(postags)
print(netags)
print('\t'.join('%s:%s' % (arc.head,arc.relation) for arc in arcs))






