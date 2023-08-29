from transformers import pipeline
import requests

class QuestionAnswering:
    # def __init__(self, model_name="distilbert-base-uncased-distilled-squad"):
    #     self.nlp = pipeline('question-answering', model=model_name)

    # def get_answer(self, question, context):
    #     result = self.nlp(question=question, context=context)
    #     return result['answer']

    def __init__(self):
        pass


    def get_wikipedia_search(self, query):
        response = requests.get(
            'https://en.wikipedia.org/w/api.php',
            params={
                'action': 'query',
                'format': 'json',
                'list': 'search',
                'srsearch': query,
            }
        ).json()
        print(response['query']['search'])
        print('\n\n\n\n\n')
        return response['query']['search']


    def get_wikipedia_summary(self, query):
        thisQuery = query
        response = requests.get(
            'https://en.wikipedia.org/w/api.php',
            params={
                'action': 'query',
                'format': 'json',
                'titles': thisQuery,
                'prop': 'extracts',
                'exintro': True,
                'explaintext': True,
            }
        ).json()
        
        page = next(iter(response['query']['pages'].values()))
        # print(page.get('extract', ''))
        # print('\n\n\n\n\n')
        return page.get('extract', '')


    def get_wikipedia_page_text(self, title):
        response = requests.get(
            'https://en.wikipedia.org/w/api.php',
            params={
                'action': 'query',
                'format': 'json',
                'titles': title,
                'prop': 'extracts',
                'explaintext': True,  # Get plain text, not HTML
            }
        ).json()

        page = next(iter(response['query']['pages'].values()))
        print(page.get('extract', ''))
        return page.get('extract', '')


        # take this, use as list builder and then on click rerun above methods
        # to get proper data.
    def get_wikipedia_links(self, title):
        response = requests.get(
            'https://en.wikipedia.org/w/api.php',
            params={
                'action': 'query',
                'format': 'json',
                'titles': title,
                'prop': 'links',
                'pllimit': 'max',  # Get as many links as possible
            }
        ).json()

        page = next(iter(response['query']['pages'].values()))
        print([link['title'] for link in page.get('links', [])])
        return [link['title'] for link in page.get('links', [])]


    def get_wikipedia_links_urls(self, title):
        response = requests.get(
            'https://en.wikipedia.org/w/api.php',
            params={
                'action': 'query',
                'format': 'json',
                'titles': title,
                'prop': 'links',
                'pllimit': 'max',
            }
        ).json()

        page = next(iter(response['query']['pages'].values()))
        link_titles = [link['title'] for link in page.get('links', [])]
        link_urls = ['https://en.wikipedia.org/wiki/' + title.replace(' ', '_') for title in link_titles]
        for link in link_urls:
            print(link)
        return link_urls

    def get_context_data(self, context):
        nlp = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")
        # nlp = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
        # nlp = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")



        
        question = "What is Neil weight?"

        answer = nlp(question=question, context=context)
        print(answer)
        return answer