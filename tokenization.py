import nltk
#nltk.download('punkt')
#nltk.download('wordnet')
#nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.stem import PorterStemmer
from konlpy.tag import Okt
from konlpy.tag import Kkma
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.preprocessing.text import text_to_word_sequence
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# print(WordPunctTokenizer().tokenize("Don't be fooled by the dark sounding name, "
#                     "Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))

#
# print(text_to_word_sequence
#       ("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))


#OKT

# okt=Okt()
# print(okt.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
#
# ;
# print(okt.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
# ;
#꼬마

# kkma=Kkma()
# print(kkma.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
# print(kkma.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))


# n=WordNetLemmatizer()
# words=['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']
# n.lemmatize('watched', 'v')
# n.lemmatize('dies', 'v')
# n.lemmatize('has', 'v')
# print([n.lemmatize(w) for w in words])

# 마틴 포터 추출 -  어간 추출(Stemming)


# s = PorterStemmer()
# text="This was not the map we found in Billy Bones's chest, but an accurate copy, complete in all things--names and heights and soundings--with the single exception of the red crosses and the written notes."
# words=word_tokenize(text)
# print(words)
#
# a = [s.stem(w) for w in words]
# print(a)

#불용어 처리

# a=stopwords.words('english')[:10]
#
# print(a)



#특정 문구를 토큰화 하고 불용어 처리 해보기 실습.

# example = "Family is not an important thing. It's everything."
# stop_words = set(stopwords.words('english'))
# word_tokens = word_tokenize(example)
#
# result=[]
# for w in word_tokens :
#       if w not in stop_words:
#             result.append(w)
#
# print(word_tokens)
# print(result)

#한국어의 불용어 처리
#
# example = "고기를 아무렇게나 구우려고 하면 안 돼. 고기라고 다 같은 게 아니거든. 예컨대 삼겹살을 구울 때는 중요한 게 있지."
# stop_words = "아무거나 아무렇게나 어찌하든지 같다 비슷하다 예컨대 이럴정도로 하면 아니거든"
#
# stop_words=stop_words.split(' ')
# words_tokens=word_tokenize(example)
#
# result=[]
# for w in words_tokens:
#       if w not in stop_words:
#             result.append(w)
# result = [word for word in word_tokens if not word in stop_words]
# print(words_tokens)
# print(result)




