from flask import Flask
from flask import redirect

app = Flask(__name__)

htm1 = '''
<p> HALLO GUYS </p>
<p> Aku Sayang Kamu </p>
</br>
<p> Mau Nggak Jadi Pacar Aku ? </p>
</br>
<div>
<button onclick="document.location='/love-u'" class="glow-on-hover" type="button"> Iya </button>
</div>
</br>
<div>
<button onclick="document.location='/back'" type="button"> Tidak </button>
</div>
'''
html2 = '''
<p> Makasih Udah Mau Jadi Pacar Aku Mwwaaahhhhhh............. </p>

'''
html3 = '''
<meta http-equiv="Refresh" content="3; url='/'" />

<p> Kamu Yakin????? </p>
'''
@app.route("/")
def hello_world():
    return htm1

@app.route("/love-u")
def iya():
    return html2

@app.route('/back')
def tidak():
    return html3

if __name__ == '__main__':
    app.run(debug=True,port=5008,host="0.0.0.0")