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

stateabbreviationsgooglemobility = []
for i in stateabbreviationslower:
    stateabbreviationsgooglemobility.append(i + 'gm')

stateabbreviationshospital = []
for i in stateabbreviationslower:
    stateabbreviationshospital.append(i + 'am')

for sa, sal, sam, sag, sac, sad, sadr, sagm, saam in zip(stateabbreviations, stateabbreviationslower, stateabbreviationsmap, stateabbreviationsgraph, stateabbreviationscases, stateabbreviationsdeaths, stateabbreviationsdeathrate, stateabbreviationsgooglemobility, stateabbreviationshospital):
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
        
        @app.route('/Graphs/Mobility/Google/{sa}')
        def {sagm}():
            return render_template("googlemobility/{sa}_covid-19_gmobilityreport.html") 

        @app.route('/Graphs/Hospital/{sa}')
        def {saam}():
            return render_template("hospital/{sa}_covid-19_hospital.html") 
    """
    print(code)

for sl, sam, sa, sag, sac, sad, sd, sagm, saam in zip(statelist, stateabbreviationsmap, stateabbreviations, stateabbreviationsgraph, stateabbreviationscases, stateabbreviationsdeaths, stateabbreviationsdeathrate, stateabbreviationsgooglemobility, stateabbreviationshospital):
    code1="""
        <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body{
                    margin: 0;
                }
                .map{
                    width: 50%;
                    height: 800px;
                    overflow: hidden;
                    float: right;
                }
                .box{
                    width: 50%;
                    height: 800px;
                    overflow: hidden;
                    float: left;
                }
                #GraphSelect{
                    width: 50%;
                    height: 50px;
                    font-size: 25px;
                    font-weight: bold;
                    background-color: rgba(0, 0, 0, 0.849);
                    color: antiquewhite;
                    border: none;
                    text-indent: 20px;
                }
                .custom-select{
                    border: none;
                }
                @media only screen and (max-width: 800px) {
                    .map{
                        width: 90%;
                        height: 600px;
                        overflow: hidden;
                        float: none;
                    }
                    .box{
                        width: 620px;
                        overflow: hidden;
                        float: none;
                        -ms-zoom: 0.6;
                        -moz-transform: scale(0.6);
                        -moz-transform-origin: 0 0;
                        -o-transform: scale(0.6);
                        -o-transform-origin: 0 0;
                        -webkit-transform: scale(0.6);
                        -webkit-transform-origin: 0 0;
                    }
                    .custom-select{
                        padding-bottom: 5px;
                        padding-top: 5px;
                        padding-left: 0;
                        padding-right: 0;
                        width: 100%;
                        text-align: center;
                    }
                    #GraphSelect{
                        text-align-last: center;
                        width: 100%;
                    } 
                }
            </style>
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
            <div class="map">
                <iframe src="{{{{url_for('{sam}')}}}}" frameborder="0" scrolling="no" width="100%" height="625"> </iframe>
            </div>
            <div class='custom-select'>
                <select id="GraphSelect">
                    <option value="{{{{url_for('{sag}')}}}}">Positivity Rate</option>
                    <option value="{{{{url_for('{sad}')}}}}">Daily New Deaths</option>
                    <option value="{{{{url_for('{sac}')}}}}">Daily New Positives</option>
                    <option value="{{{{url_for('{saam}')}}}}">Hospitalization Data</option>
                    <option value="{{{{url_for('{sd}')}}}}">Death Rate</option>
                    <option value="{{{{url_for('{sagm}')}}}}">Google Mobility Report</option>
                </select>
            </div>
            <div class="box">
                <iframe id="Frame"  src="{{{{url_for('{sag}')}}}}" frameborder="0" scrolling="no" width="100%" height="625"></iframe>
            </div>
        </body>
    </html> 
    """
    
    with open("templates/statepages/{0}-page.html".format(sa), "w") as site:
        site.write(code1+code2)     