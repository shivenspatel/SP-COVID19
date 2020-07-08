statelist = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

stateabbreviations = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

stateabbreviationslower = []
for i in stateabbreviations:
    stateabbreviationslower.append(i.lower())

stateabbreviationsmap = []
for i in stateabbreviationslower:
    stateabbreviationsmap.append(i + 'm')

stateabbreviationsgraph = []
for i in stateabbreviationslower:
    stateabbreviationsgraph.append(i + 'g')
    
stateabbreviationscases = []
for i in stateabbreviationslower:
    stateabbreviationscases.append(i + 'p')

stateabbreviationsdeaths = []
for i in stateabbreviationslower:
    stateabbreviationsdeaths.append(i + 'c')
# for sal, sl in zip(stateabbreviationslower, statelist):
#     code3="""<div><a href="{{ url_for('%s') }}"><button><h5>%s</h5></button></a></div>""" % (sal, sl)
#     print(code3)

for sa, sal, sam, sag, sac, sad in zip(stateabbreviations, stateabbreviationslower, stateabbreviationsmap, stateabbreviationsgraph, stateabbreviationscases, stateabbreviationsdeaths):
    code="""
        @app.route('/States/{0}')
        def {1}():
            return render_template("statepages/{2}-page.html")

        @app.route('/Maps/PosCases/{3}')
        def {4}():
            return render_template("countymaps/{5}_covid-19_countymap.html")

        @app.route('/Graphs/PosRate/{6}')
        def {7}():
            return render_template("positivityrate/{8}_covid-19_positivityrate.html") 

        @app.route('/Graphs/NewCases/{9}')
        def {10}():
            return render_template("newcases/{11}_covid-19_newpositive.html") 

        @app.route('/Graphs/NewDeaths/{12}')
        def {13}():
            return render_template("newdeaths/{14}_covid-19_newdeaths.html") 
    """.format(sa, sal, sa, sa, sam, sa, sa, sag, sa, sa, sac, sa, sa, sad, sa)
    print(code)

for sl, sam, sa, sag, sac, sad in zip(statelist, stateabbreviationsmap, stateabbreviations, stateabbreviationsgraph, stateabbreviationscases, stateabbreviationsdeaths):
    code1="""
    <!DOCTYPE html>
    <html>
        <head>
            <link rel="stylesheet" href="static/css/main.css">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
            <script>
                $(document).ready(function() {
                    $("#GraphSelect").change(function() {
                        var value = $(this).val();

                        console.log(value);
                        $("#Frame").attr('src', value);
                    })
                });
            </script>
        </head>
    """
    code2=f"""
        <body>
            <div class='custom-select'>
                <select id="GraphSelect">
                    <option value="{{{{ url_for('{sag}') }}}}">Positivity Rate</option>
                    <option value="{{{{ url_for('{sad}') }}}}">Daily New Deaths</option>
                    <option value="{{{{ url_for('{sac}') }}}}">Daily New Positives</option>
                </select>
            </div>
            <div class="map">
                <iframe src="{{{{ url_for('{sam}') }}}}" frameborder="0" scrolling="no" width="50%" height="625" align="right"> </iframe>
            </div>
            
            <div class="box">
                <iframe id="Frame"  src="{{{{ url_for('{sag}') }}}}" frameborder="0" scrolling="no" width="50%" height="625" align="left"></iframe>
            </div>
        </body>
    </html> 
    """
    
    with open("templates/statepages/{0}-page.html".format(sa), "w") as site:
        site.write(code1+code2)     