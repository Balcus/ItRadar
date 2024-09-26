from flask import Flask, render_template, request  # type: ignore
from SearchEngine import SearchEngine
import os

app = Flask(__name__)
article_number = None
search_engine = SearchEngine()

def main() :
    global article_number, search_engine
    json_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'json_folder')  
    search_engine.index_json_files(json_folder)
    article_number = search_engine.number_of_documents


@app.route('/', methods=['GET', 'POST'])
def index():
    global search_engine
    results = None
    query = None
    top_results = None
    if request.method == 'POST':
        query = request.form.get('query') 
        results = search_engine.search(query)
        top_results = sorted(results, key=lambda item: item['score'], reverse=True)[:50]
    return render_template('index.html', article_number=article_number, top_results=top_results)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    main()
    app.run(debug=True)
