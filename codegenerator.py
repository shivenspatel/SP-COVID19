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

stateabbreviationsdeathrate = []
for i in stateabbreviationslower:
    stateabbreviationsdeathrate.append(i + 'dr')


for sa, sal, sam, sag, sac, sad, sadr in zip(stateabbreviations, stateabbreviationslower, stateabbreviationsmap, stateabbreviationsgraph, stateabbreviationscases, stateabbreviationsdeaths, stateabbreviationsdeathrate):
    code=f"""
        @app.route('/States/{sa}')
        def {sal}():
            return render_template("statepages/{sa}-page.html")

        @app.route('/Maps/PosCases/{sa}')
        def {sam}():
            return render_template("countymaps/{sa}_covid-19_countymap.html")

        @app.route('/Graphs/PosRate/{sa}')
        def {sag}():
            return render_template("positivityrate/{sa}_covid-19_positivityrate.html") 

        @app.route('/Graphs/NewCases/{sa}')
        def {sac}():
            return render_template("newcases/{sa}_covid-19_newpositive.html") 

        @app.route('/Graphs/NewDeaths/{sa}')
        def {sad}():
            return render_template("newdeaths/{sa}_covid-19_newdeaths.html") 

        @app.route('/Graphs/DeathRate/{sa}')
        def {sadr}():
            return render_template("deathrate/{sa}_covid-19_deathrate.html") 
    """
    print(code)

for sl, sam, sa, sag, sac, sad, sd in zip(statelist, stateabbreviationsmap, stateabbreviations, stateabbreviationsgraph, stateabbreviationscases, stateabbreviationsdeaths, stateabbreviationsdeathrate):
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
                    <option value="{{{{ url_for('{sac}') }}}}">Daily New Positives and Hospitalizations</option>
                    <option value="{{{{ url_for('{sd}') }}}}">Death Rate</option>
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