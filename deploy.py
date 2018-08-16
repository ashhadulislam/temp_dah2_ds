from flask import Flask, render_template, request, Markup
import constants as c



def main():
    print("At main, just once")


app = Flask(__name__)

app.config["DEBUG"]=True







@app.route('/submit_form1', methods=[ 'POST'])
def give_graph():

    wordkey=str(request.form['wordkey']).lower()

    print("key you put is ",wordkey," key from constants is ",c.match_key)
    if wordkey == c.match_key:
        whole_div="<div>Congratulations!! You nailed it.</br>Here are the co ordinates.<br><a href='"+c.map_url+"'>DS Club Secret Location</a>"
        whole_div=whole_div+"</br>Be there at 3</div>"
    else:
        whole_div="<div>Just not there yet.</br>Try again</div>"
    return render_template('home.html',div_graph_placeholder=Markup(whole_div))


@app.route('/')
def start():
    # generate_data_for_district("Andhra Pradesh","Hyderabad")
    # full_div=generateGraphsAndData()
    # return "hello"
    # return render_template('home.html',div_graph_placeholder=Markup(full_div))
    # full_div="<div><h2>State, District</h2></div>"
    full_div=""
    return render_template('home.html',div_graph_placeholder=Markup(full_div))

if __name__=="__main__":
    main()
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port)