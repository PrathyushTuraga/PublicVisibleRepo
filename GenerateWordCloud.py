url = 'https://en.wikipedia.org/wiki/Data_science'
import requests
import nlp_rake
import matplotlib.pyplot as plt
from wordcloud import WordCloud
#Getting Data
text = requests.get(url).content.decode('utf-8')
print(text[:1000])
#Transforming Data
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    script = False
    res = ""
    def handle_starttag(self, tag, attrs):
        if tag.lower() in ["script","style"]:
            self.script = True
    def handle_endtag(self, tag):
        if tag.lower() in ["script","style"]:
            self.script = False
    def handle_data(self, data):
        if str.strip(data) == "" or self.script:
            return
        self.res += ' ' + data.replace('[edit]', '')

parser = MyHTMLParser()
parser.feed(text)
text = parser.res
print(text[:1000])
#Getting Insights
extractor = nlp_rake.Rake(max_words=2, min_freq=3, min_chars=5)
res = extractor.apply(text)
res
# Visualizing the Result
def plot(pair_list):
    k, v = zip(*pair_list)
    plt.bar(range(len(k)), v)
    plt.xticks(range(len(k)), k, rotation='vertical')
    plt.show()
plot(res)
wc = WordCloud(background_color='white', width=800, height=600)
plt.figure(figsize=(15, 7))
#plt.imshow(wc.generate_from_frequencies({k: v for k, v in res}))
plt.imshow(wc.generate(text))
plt.show()
wc.generate(text).to_file('ds_wordcloud.png')
