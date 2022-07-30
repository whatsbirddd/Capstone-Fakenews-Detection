from flask import Flask, request, render_template
from util import get_title_body_from_link
from ml import process

app = Flask(__name__)


@app.route("/")
def get_index_page():
    return render_template('main/Enter_URL_Before.html')


@app.route("/result")
def get_result_page():
    link = request.args.get('url')
    title, body = get_title_body_from_link(link)
    probability, result, preprocessed_title, preprocessed_body_20 = process(title, body)
    print(probability, result)
    return f'{"가짜뉴스" if result == 1 else "진짜뉴스"} 확률: {probability}% \n {preprocessed_title}\n{preprocessed_body_20}'
    # return render_template('result.html')

app.run(debug=True)
