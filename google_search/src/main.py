from googlesearch import search

def google_search(query, num_results=5, lang='en'):
    try:
        search_results = search(query, num_results=num_results, lang=lang)
        return search_results
    except Exception as e:
        print("An error occurred:", str(e))
        return []

if __name__ == '__main__':
    query = input('enter your query:  ')
    result = google_search(query)
    
    if result:
        print('search result:')
        
        for index, results in enumerate(result,start=1):
            print(f"{index}>{results}")
    else:
        print('No result found!!')
        