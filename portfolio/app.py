from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="template",
    static_folder="statics"
            )

@app.route("/")
def index_view():
    about_me = "I am a dedicated Web Developer based in Tabriz, Iran, bringing 17 years of experience to the field. My expertise lies in creating robust and functional web solutions. I am fluent in both English and German, allowing me to collaborate effectively on international projects."
    context={"username":"Mohammad","introducing":about_me}
    return render_template("index.html", context=context)

@app.route("/skills")
def skills_view():
    context={"skills":["Python3", "django", "Frontend"]}
    return render_template("skills.html", context=context)

@app.route("/projects")
def projects_view():
    context={"github":"https://github.com/MohammadAghazadeh2009"}
    return render_template("projects.html", context=context)

if __name__ == "__main__":
    app.run(debug=True)