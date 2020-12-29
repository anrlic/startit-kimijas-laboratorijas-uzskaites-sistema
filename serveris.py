from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Labrīt!"

@app.route('/sveiki')
def sveiki():
    return "Nav vairs nekāds rīts!"

# dinamiskie celi8
@app.route('/sveiki/<vards>')
def sveikiPersona(vards):
    # 1 varioants
    #return "Sveiki {}".format(vards)
    # 2 variants
    return f"Sveiki {vards}"

@app.route('/cik/<sk1>/<sk2>')
def rezinajums(sk1, sk2):
  sk1=int(sk1)
  sk2=int(sk2)
  r=sk1*sk2;
  return str(r)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)

    # debug=True automatiski parstartee 
    # serveri pec izmainaam .py failaa
