#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):

        return self.render_template("hello.html")
class ResultHandler(BaseHandler):
    def post(self):
        dna=str(self.request.get("dnk"))
        dnk_analiza=analiziraj(dna)
        last="Program po vrsti vrne naslenje lastnosti: Barva las, Oblika obraza, Barva oci, Spol, Rasa:"
        params={"vrni":dnk_analiza, "lastn":last}
        return self.render_template("result.html", params=params)
def analiziraj(dna):
    F=dna
    seznam=[]
    print("Hair color: ")
    dnalas=["CCAGCAATCGC", "GCCAGTGCCG", "TTAGCTATCGC"]
    barvalas =["Crna", "Rjava", "Svetlolasa"]
    x=0
    for i in dnalas:
        if i in F:
            print(barvalas[x])
            seznam.append(barvalas[x])
        x += 1


    print("Oblika obraza: ")
    oblika=["GCCACGG", "ACCACAA", "AGGCCTCA"]
    obraz =["Kvadratna", "Okrogla" , "Ovalna"]
    x=0
    for i in oblika:
        if i in F:
            print(obraz[x])
            seznam.append(obraz[x])
        x += 1


    print("Barva oci: ")
    barva=["TTGTGGTGGC", "GGGAGGTGGC", "AAGTAGTGAC"]
    oci =["Modra", "Zelena" , "Rjava"]
    x=0
    for i in barva:
        if i in F:
            print(oci[x])
            seznam.append(oci[x])
        x += 1



    print("Spol: ")
    spol=["TGAAGGACCTTC", "TGCAGGAACTTC"]
    spol1 =["Zenska", "Moski"]
    x=0
    for i in spol:
        if i in F:
            print(spol1[x])
            seznam.append(spol1[x])
        x += 1


    print("Rasa: ")
    rasa=["AAAACCTCA", "CGACTACAG", "CGCGGGCCG"]
    rasa1 =["Bela", "Crna", "Azijska"]
    x=0
    for i in rasa:
        if i in F:
            print(rasa1[x])
            seznam.append(rasa1[x])
        x += 1

    return seznam



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/result', ResultHandler),
], debug=True)
