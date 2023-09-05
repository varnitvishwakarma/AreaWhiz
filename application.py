from flask import Flask,render_template,jsonify,request

application = Flask(__name__)
app=application

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/square',methods=['GET','POST'])
def square():

    if request.method=='POST':
        side=float(request.form.get("side"))
        result=(side*side)
        return render_template("square.html",result=result)

    else:
        return render_template("square.html")


@app.route('/triangle',methods=['GET','POST'])
def triangle():
    if request.method=='POST':
        base=float(request.form.get("base"))
        height=float(request.form.get("height"))
        result=(base*height)/2
        return render_template("triangle.html",result=result)
    
    else:
        return render_template('triangle.html')

@app.route('/rectangle',methods=['GET','POST'])
def rectangle():
    if request.method=='POST':
        length=float(request.form.get("length"))
        weight=float(request.form.get("weight"))
        result=length*weight
        return render_template("rectangle.html",result=result)

    else:
        return render_template("rectangle.html")

@app.route('/circle',methods=['GET','POST'])
def circle():
    if request.method=='POST':
         radius=float(request.form.get("radius"))
         result=3.14159265359*(radius*radius)
         return render_template("circle.html",result=result)

    else:
        return render_template("circle.html")


@app.route('/cube',methods=['GET','POST'])
def cube():
    if request.method=='POST':
         side=float(request.form.get("side"))
         result=6*(side*side)
         return render_template("cube.html",result=result)

    else:
        return render_template("cube.html")

@app.route('/cone',methods=['GET','POST'])
def cone():
    
    if request.method=='POST':
        radius=float(request.form.get("radius"))
        height=float(request.form.get("height"))
        result=3.14159265359* radius * (radius + height)
        return render_template("cone.html",result=result)

    else:
        return render_template('cone.html')

@app.route('/cylinder',methods=['GET','POST'])
def cylinder():
    if request.method=='POST':
        radius=float(request.form.get("radius"))
        height=float(request.form.get("height"))
        result=2*3.14159265359* radius * (radius + height)
        return render_template("cylinder.html",result=result)
    
    else:
        return render_template("cylinder.html")

@app.route('/ellipse',methods=['GET','POST'])
def ellipse():
    if request.method=='POST':
        axis1=float(request.form.get("axis1"))
        axis2=float(request.form.get("axis2"))
        result=3.14159265359*(axis1*axis2)
        return render_template("Ellipse.html",result=result)
    
    else:
        return render_template("Ellipse.html")

@app.route('/parallelogram',methods=['GET','POST'])
def parallelogram():
    if request.method=='POST':
        base=float(request.form.get("base"))
        height=float(request.form.get("height"))
        result=base*height
        return render_template("parallelogram.html",result=result)
    
    else:
        return render_template("parallelogram.html")

@app.route('/rhombus',methods=['GET','POST'])
def rhombus():
    if request.method=='POST':
        diagonal1=float(request.form.get("diagonal1"))
        diagonal2=float(request.form.get("diagonal2"))
        result=(diagonal1*diagonal2)/2
        return render_template("Rhombus.html",result=result)
    
    else:
        return render_template("Rhombus.html")

@app.route('/sphere',methods=['GET','POST'])
def sphere():
    if request.method=='POST':
         radius=float(request.form.get("radius"))
         result=4*3.14159265359*(radius*radius)
         return render_template("Sphere.html",result=result)

    else:
        return render_template("Sphere.html")

@app.route('/decagon',methods=['GET','POST'])
def decagon():
    if request.method=='POST':
        side=float(request.form.get("side"))
        result=5/2*(side*side)*3.07768353718
        return render_template("decagon.html",result=result)

    else:
        return render_template("decagon.html")

@app.route('/nonagon',methods=['GET','POST'])
def nonagon():
    if request.method=='POST':
        side=float(request.form.get("side"))
        result=9/4*(side*side)*2.74747741945
        return render_template("nonagon.html",result=result)

    else:
        return render_template('nonagon.html')

@app.route('/octagon',methods=['GET','POST'])
def octagon():
    if request.method=='POST':
        side=float(request.form.get("side"))
        result=2*(1+1.41421356237)*(side*side)
        return render_template("octagon.html",result=result)
    
    else:
        return render_template("octagon.html")

@app.route('/heptagon',methods=['GET','POST'])
def heptagon():
    if request.method=='POST':
        side=float(request.form.get("side"))
        result=(7/4)*(side*side)*2.07652139657
        return render_template("heptagon.html",result=result)
    
    else:
        return render_template("heptagon.html")

@app.route('/hexagon',methods=['GET','POST'])
def hexagon():
    if request.method=='POST':
        side=float(request.form.get("side"))
        result=(3*1.73205080757)/2*(side*side)
        return render_template("hexagon.html",result=result)
    
    else:
        return render_template("hexagon.html")

@app.route('/pentagon',methods=['GET','POST'])
def pentagon():
    if request.method=='POST':
        side=float(request.form.get("side"))
        result=1/4*6.88190960236*(side*side)
        return render_template("pentagon.html",result=result)
    
    else:
        return render_template("pentagon.html")

@app.route('/trapezoid',methods=['GET','POST'])
def trapezoid():
    if request.method=='POST':
        base1=float(request.form.get("base1"))
        base2=float(request.form.get("base2"))
        height=float(request.form.get("height"))
        result=((base1+base2)/2)*height
        return render_template("trapezoid.html",result=result)
    
    else:
        return render_template("trapezoid.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__=="__main__":
    app.run(host="0.0.0.0")
