from flask import Flask, render_template, request, Markup
import constants as c



def main():
    print("At main, just once")


app = Flask(__name__)

app.config["DEBUG"]=True







@app.route('/submit_form1', methods=[ 'POST'])
def give_graph():

    wordkey=str(request.form['wordkey']).lower()

    print("key you put is ",wordkey," the key from constants is ",c.match_key)
    if wordkey == c.match_key:
        whole_div="<div>Congratulations!! You nailed it.</br>This is where you need to go<br><img class='img-responsive' src='"+c.loc_img+"'>"
        whole_div=whole_div+"</br>See you there at 3:30pm</div>"
    else:
        if int(wordkey)<=3:
            whole_div="<div>Thats all you do at office?</br>Try again</div>"
        elif int(wordkey)<=5:
            whole_div="<div>Seriously!!! How do you fill your timesheet?</br>Try again</div>"
        elif int(wordkey)<=10:
            whole_div="<div>Are you running for the busiest employee of the year award? </br>Newsflash!! There's no such prize here...</br>Try again</div>"
        elif int(wordkey)<=13:
            whole_div="<div>Are you sure you are not superman? </br>Go back to metropolis you work monster...</br>Try again</div>"
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