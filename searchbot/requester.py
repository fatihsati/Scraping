import requests
import time

search_word = ['Turkish', 'English', 'Japan', 'python', 'java', 'c']

for i in range(1000):
    word = search_word[i%len(search_word)]
    print(word)
    url = f'https://www.google.com/search?q=how to count 1 to 10 in{word}'
    
    r = requests.get(url)
    
    print(r.status_code)
    print(r.content)
    if r.status_code != 200:
        print('!!!!!!!!!!!!!!')
        break

    time.sleep(1)
    
    
    