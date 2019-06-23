from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/standard/", methods=['POST'])
def standard():
    height = int(request.form.get('height'))
    weight = int(request.form.get('weight'))
    std_h_w = height - 105
    if weight >= 40:
        comment = "重度肥胖"
    elif weight >= 35 and weight < 40:
        comment = "中度肥胖"
    elif weight >= 30 and weight < 35:
        comment = "輕度肥胖"
    elif weight >= 25 and weight < 30:
        comment = "超重"
    elif weight >= 18 and weight < 25:
        comment = "正常"
    elif weight < 18:
        comment = "過輕"
    return render_template(
        'index.html', comment=comment, weight=weight, height=height
        )
