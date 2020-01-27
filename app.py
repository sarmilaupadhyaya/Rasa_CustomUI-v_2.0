from flask import Flask, render_template, request
import os
import aiml
from autocorrect import spell

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    query = request.args.get('msg')
#    query = [spell(w) for w in (query.split())]
 #   question = " ".join(query)
 #   response = k.respond(question)
  #  if response:
   #     return (str(response))
  #  else:
   #     return (str(":)"))

    result = get_rasa(query)
    
    return result

if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0', port='5000')



