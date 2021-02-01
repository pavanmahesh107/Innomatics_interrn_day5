from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
 def handle_starttag(self, tag, attrs):
  print(tag)
  for attr in attrs:
      print("->", attr[0], ">", attr[1])
N = int(input())
raw = ""
for i in range(N):
 raw += input()
new = MyHTMLParser()
new.feed(raw)
