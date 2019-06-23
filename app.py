from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    """
    Index Page
    """
    return render_template('index.html')

@app.route("/standard/", methods=['POST'])
def standard():
    """
    Standard Weight
    """
    height = int(request.form.get('height'))
    weight = int(request.form.get('weight'))
    std_h_w = height - 105
    if std_h_w >= 40:
        comment = "重度肥胖"
    elif std_h_w >= 35 and std_h_w < 40:
        comment = "中度肥胖"
    elif std_h_w >= 30 and std_h_w < 35:
        comment = "輕度肥胖"
    elif std_h_w >= 25 and std_h_w < 30:
        comment = "超重"
    elif std_h_w >= 18 and std_h_w < 25:
        comment = "正常"
    elif std_h_w < 18:
        comment = "過輕"
    return render_template(
        'index.html', comment=comment, weight=weight, height=height
        )
