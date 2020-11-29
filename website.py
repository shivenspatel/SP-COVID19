from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/Maps/PosCases/US')
def usposmap():
    return render_template("positives.html")

@app.route('/Maps/Deaths/US')
def usdeamap():
    return render_template("deaths.html")

@app.route('/US')
def us():
    return render_template("ushome.html")

@app.route('/Compare')
def comp():
    return render_template("comparehome.html")

@app.route('/CompareH2H')
def comh2h():
    return render_template("comparepage.html")

@app.route('/Graphs/PosRate/US')
def usg():
    return render_template('positivityrate/US_covid-19_positivityrate.html')
    
@app.route('/Graphs/NewCases/US')
def usp():
    return render_template("newcases/US_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/US')
def usc():
    return render_template("newdeaths/US_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/US')
def usdr():
    return render_template("deathrate/US_covid-19_deathrate.html")

@app.route('/Graphs/Hospital/US')
def ush():
    return render_template("hospital/US_covid-19_hospital.html")

@app.route('/Graphs/Testing/US')
def ust():
    return render_template("testing/US_covid-19_testing.html")

@app.route('/Graphs/Mobility/US')
def usgm():
    return render_template("googlemobility/US_covid-19_gmobilityreport.html")

@app.route('/Graphs/Compare/Cases')
def cases():
    return render_template("compare/casescompare.html")

@app.route('/Graphs/Compare/Deaths')
def deaths():
    return render_template("compare/deathscompare.html")

@app.route('/Graphs/Compare/Cases100K')
def casespo():
    return render_template("compare/casespocompare.html")

@app.route('/Graphs/Compare/Deaths100K')
def deathspo():
    return render_template("compare/deathspocompare.html")

@app.route('/States')
def dd():
    return render_template("stateshome.html")

@app.route('/States/AL')
def al():
    return render_template("statepages/AL-page.html")

@app.route('/Maps/PosCases/AL')
def alm():
    return render_template("countymaps/AL_covid-19_countymap.html")

@app.route('/Graphs/PosRate/AL')
def alg():
    return render_template("positivityrate/AL_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/AL')
def alp():
    return render_template("newcases/AL_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/AL')
def alc():
    return render_template("newdeaths/AL_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/AL')
def aldr():
    return render_template("deathrate/AL_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/AL')
def algm():
    return render_template("googlemobility/AL_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/AL')
def alam():
    return render_template("hospital/AL_covid-19_hospital.html")

@app.route('/Graphs/Testing/AL')
def alt():
    return render_template("testing/AL_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/AL')
def alpop():
    return render_template("comparedeaths/AL_covid-19_deathspop.html")


@app.route('/States/AK')
def ak():
    return render_template("statepages/AK-page.html")

@app.route('/Maps/PosCases/AK')
def akm():
    return render_template("countymaps/AK_covid-19_countymap.html")

@app.route('/Graphs/PosRate/AK')
def akg():
    return render_template("positivityrate/AK_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/AK')
def akp():
    return render_template("newcases/AK_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/AK')
def akc():
    return render_template("newdeaths/AK_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/AK')
def akdr():
    return render_template("deathrate/AK_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/AK')
def akgm():
    return render_template("googlemobility/AK_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/AK')
def akam():
    return render_template("hospital/AK_covid-19_hospital.html")

@app.route('/Graphs/Testing/AK')
def akt():
    return render_template("testing/AK_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/AK')
def akpop():
    return render_template("comparedeaths/AK_covid-19_deathspop.html")


@app.route('/States/AZ')
def az():
    return render_template("statepages/AZ-page.html")

@app.route('/Maps/PosCases/AZ')
def azm():
    return render_template("countymaps/AZ_covid-19_countymap.html")

@app.route('/Graphs/PosRate/AZ')
def azg():
    return render_template("positivityrate/AZ_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/AZ')
def azp():
    return render_template("newcases/AZ_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/AZ')
def azc():
    return render_template("newdeaths/AZ_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/AZ')
def azdr():
    return render_template("deathrate/AZ_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/AZ')
def azgm():
    return render_template("googlemobility/AZ_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/AZ')
def azam():
    return render_template("hospital/AZ_covid-19_hospital.html")

@app.route('/Graphs/Testing/AZ')
def azt():
    return render_template("testing/AZ_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/AZ')
def azpop():
    return render_template("comparedeaths/AZ_covid-19_deathspop.html")


@app.route('/States/AR')
def ar():
    return render_template("statepages/AR-page.html")

@app.route('/Maps/PosCases/AR')
def arm():
    return render_template("countymaps/AR_covid-19_countymap.html")

@app.route('/Graphs/PosRate/AR')
def arg():
    return render_template("positivityrate/AR_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/AR')
def arp():
    return render_template("newcases/AR_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/AR')
def arc():
    return render_template("newdeaths/AR_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/AR')
def ardr():
    return render_template("deathrate/AR_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/AR')
def argm():
    return render_template("googlemobility/AR_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/AR')
def aram():
    return render_template("hospital/AR_covid-19_hospital.html")

@app.route('/Graphs/Testing/AR')
def art():
    return render_template("testing/AR_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/AR')
def arpop():
    return render_template("comparedeaths/AR_covid-19_deathspop.html")


@app.route('/States/CA')
def ca():
    return render_template("statepages/CA-page.html")

@app.route('/Maps/PosCases/CA')
def cam():
    return render_template("countymaps/CA_covid-19_countymap.html")

@app.route('/Graphs/PosRate/CA')
def cag():
    return render_template("positivityrate/CA_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/CA')
def cap():
    return render_template("newcases/CA_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/CA')
def cac():
    return render_template("newdeaths/CA_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/CA')
def cadr():
    return render_template("deathrate/CA_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/CA')
def cagm():
    return render_template("googlemobility/CA_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/CA')
def caam():
    return render_template("hospital/CA_covid-19_hospital.html")

@app.route('/Graphs/Testing/CA')
def cat():
    return render_template("testing/CA_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/CA')
def capop():
    return render_template("comparedeaths/CA_covid-19_deathspop.html")


@app.route('/States/CO')
def co():
    return render_template("statepages/CO-page.html")

@app.route('/Maps/PosCases/CO')
def com():
    return render_template("countymaps/CO_covid-19_countymap.html")

@app.route('/Graphs/PosRate/CO')
def cog():
    return render_template("positivityrate/CO_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/CO')
def cop():
    return render_template("newcases/CO_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/CO')
def coc():
    return render_template("newdeaths/CO_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/CO')
def codr():
    return render_template("deathrate/CO_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/CO')
def cogm():
    return render_template("googlemobility/CO_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/CO')
def coam():
    return render_template("hospital/CO_covid-19_hospital.html")

@app.route('/Graphs/Testing/CO')
def cot():
    return render_template("testing/CO_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/CO')
def copop():
    return render_template("comparedeaths/CO_covid-19_deathspop.html")


@app.route('/States/CT')
def ct():
    return render_template("statepages/CT-page.html")

@app.route('/Maps/PosCases/CT')
def ctm():
    return render_template("countymaps/CT_covid-19_countymap.html")

@app.route('/Graphs/PosRate/CT')
def ctg():
    return render_template("positivityrate/CT_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/CT')
def ctp():
    return render_template("newcases/CT_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/CT')
def ctc():
    return render_template("newdeaths/CT_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/CT')
def ctdr():
    return render_template("deathrate/CT_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/CT')
def ctgm():
    return render_template("googlemobility/CT_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/CT')
def ctam():
    return render_template("hospital/CT_covid-19_hospital.html")

@app.route('/Graphs/Testing/CT')
def ctt():
    return render_template("testing/CT_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/CT')
def ctpop():
    return render_template("comparedeaths/CT_covid-19_deathspop.html")


@app.route('/States/DE')
def de():
    return render_template("statepages/DE-page.html")

@app.route('/Maps/PosCases/DE')
def dem():
    return render_template("countymaps/DE_covid-19_countymap.html")

@app.route('/Graphs/PosRate/DE')
def deg():
    return render_template("positivityrate/DE_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/DE')
def dep():
    return render_template("newcases/DE_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/DE')
def dec():
    return render_template("newdeaths/DE_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/DE')
def dedr():
    return render_template("deathrate/DE_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/DE')
def degm():
    return render_template("googlemobility/DE_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/DE')
def deam():
    return render_template("hospital/DE_covid-19_hospital.html")

@app.route('/Graphs/Testing/DE')
def det():
    return render_template("testing/DE_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/DE')
def depop():
    return render_template("comparedeaths/DE_covid-19_deathspop.html")


@app.route('/States/FL')
def fl():
    return render_template("statepages/FL-page.html")

@app.route('/Maps/PosCases/FL')
def flm():
    return render_template("countymaps/FL_covid-19_countymap.html")

@app.route('/Graphs/PosRate/FL')
def flg():
    return render_template("positivityrate/FL_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/FL')
def flp():
    return render_template("newcases/FL_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/FL')
def flc():
    return render_template("newdeaths/FL_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/FL')
def fldr():
    return render_template("deathrate/FL_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/FL')
def flgm():
    return render_template("googlemobility/FL_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/FL')
def flam():
    return render_template("hospital/FL_covid-19_hospital.html")

@app.route('/Graphs/Testing/FL')
def flt():
    return render_template("testing/FL_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/FL')
def flpop():
    return render_template("comparedeaths/FL_covid-19_deathspop.html")


@app.route('/States/GA')
def ga():
    return render_template("statepages/GA-page.html")

@app.route('/Maps/PosCases/GA')
def gam():
    return render_template("countymaps/GA_covid-19_countymap.html")

@app.route('/Graphs/PosRate/GA')
def gag():
    return render_template("positivityrate/GA_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/GA')
def gap():
    return render_template("newcases/GA_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/GA')
def gac():
    return render_template("newdeaths/GA_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/GA')
def gadr():
    return render_template("deathrate/GA_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/GA')
def gagm():
    return render_template("googlemobility/GA_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/GA')
def gaam():
    return render_template("hospital/GA_covid-19_hospital.html")

@app.route('/Graphs/Testing/GA')
def gat():
    return render_template("testing/GA_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/GA')
def gapop():
    return render_template("comparedeaths/GA_covid-19_deathspop.html")


@app.route('/States/HI')
def hi():
    return render_template("statepages/HI-page.html")

@app.route('/Maps/PosCases/HI')
def him():
    return render_template("countymaps/HI_covid-19_countymap.html")

@app.route('/Graphs/PosRate/HI')
def hig():
    return render_template("positivityrate/HI_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/HI')
def hip():
    return render_template("newcases/HI_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/HI')
def hic():
    return render_template("newdeaths/HI_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/HI')
def hidr():
    return render_template("deathrate/HI_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/HI')
def higm():
    return render_template("googlemobility/HI_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/HI')
def hiam():
    return render_template("hospital/HI_covid-19_hospital.html")

@app.route('/Graphs/Testing/HI')
def hit():
    return render_template("testing/HI_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/HI')
def hipop():
    return render_template("comparedeaths/HI_covid-19_deathspop.html")


@app.route('/States/ID')
def id():
    return render_template("statepages/ID-page.html")

@app.route('/Maps/PosCases/ID')
def idm():
    return render_template("countymaps/ID_covid-19_countymap.html")

@app.route('/Graphs/PosRate/ID')
def idg():
    return render_template("positivityrate/ID_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/ID')
def idp():
    return render_template("newcases/ID_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/ID')
def idc():
    return render_template("newdeaths/ID_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/ID')
def iddr():
    return render_template("deathrate/ID_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/ID')
def idgm():
    return render_template("googlemobility/ID_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/ID')
def idam():
    return render_template("hospital/ID_covid-19_hospital.html")

@app.route('/Graphs/Testing/ID')
def idt():
    return render_template("testing/ID_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/ID')
def idpop():
    return render_template("comparedeaths/ID_covid-19_deathspop.html")


@app.route('/States/IL')
def il():
    return render_template("statepages/IL-page.html")

@app.route('/Maps/PosCases/IL')
def ilm():
    return render_template("countymaps/IL_covid-19_countymap.html")

@app.route('/Graphs/PosRate/IL')
def ilg():
    return render_template("positivityrate/IL_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/IL')
def ilp():
    return render_template("newcases/IL_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/IL')
def ilc():
    return render_template("newdeaths/IL_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/IL')
def ildr():
    return render_template("deathrate/IL_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/IL')
def ilgm():
    return render_template("googlemobility/IL_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/IL')
def ilam():
    return render_template("hospital/IL_covid-19_hospital.html")

@app.route('/Graphs/Testing/IL')
def ilt():
    return render_template("testing/IL_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/IL')
def ilpop():
    return render_template("comparedeaths/IL_covid-19_deathspop.html")


@app.route('/States/IN')
def ind():
    return render_template("statepages/IN-page.html")

@app.route('/Maps/PosCases/IN')
def inm():
    return render_template("countymaps/IN_covid-19_countymap.html")

@app.route('/Graphs/PosRate/IN')
def ing():
    return render_template("positivityrate/IN_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/IN')
def inp():
    return render_template("newcases/IN_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/IN')
def inc():
    return render_template("newdeaths/IN_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/IN')
def indr():
    return render_template("deathrate/IN_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/IN')
def ingm():
    return render_template("googlemobility/IN_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/IN')
def inam():
    return render_template("hospital/IN_covid-19_hospital.html")

@app.route('/Graphs/Testing/IN')
def inte():
    return render_template("testing/IN_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/IN')
def inpop():
    return render_template("comparedeaths/IN_covid-19_deathspop.html")


@app.route('/States/IA')
def ia():
    return render_template("statepages/IA-page.html")

@app.route('/Maps/PosCases/IA')
def iam():
    return render_template("countymaps/IA_covid-19_countymap.html")

@app.route('/Graphs/PosRate/IA')
def iag():
    return render_template("positivityrate/IA_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/IA')
def iap():
    return render_template("newcases/IA_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/IA')
def iac():
    return render_template("newdeaths/IA_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/IA')
def iadr():
    return render_template("deathrate/IA_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/IA')
def iagm():
    return render_template("googlemobility/IA_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/IA')
def iaam():
    return render_template("hospital/IA_covid-19_hospital.html")

@app.route('/Graphs/Testing/IA')
def iat():
    return render_template("testing/IA_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/IA')
def iapop():
    return render_template("comparedeaths/IA_covid-19_deathspop.html")


@app.route('/States/KS')
def ks():
    return render_template("statepages/KS-page.html")

@app.route('/Maps/PosCases/KS')
def ksm():
    return render_template("countymaps/KS_covid-19_countymap.html")

@app.route('/Graphs/PosRate/KS')
def ksg():
    return render_template("positivityrate/KS_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/KS')
def ksp():
    return render_template("newcases/KS_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/KS')
def ksc():
    return render_template("newdeaths/KS_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/KS')
def ksdr():
    return render_template("deathrate/KS_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/KS')
def ksgm():
    return render_template("googlemobility/KS_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/KS')
def ksam():
    return render_template("hospital/KS_covid-19_hospital.html")

@app.route('/Graphs/Testing/KS')
def kst():
    return render_template("testing/KS_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/KS')
def kspop():
    return render_template("comparedeaths/KS_covid-19_deathspop.html")


@app.route('/States/KY')
def ky():
    return render_template("statepages/KY-page.html")

@app.route('/Maps/PosCases/KY')
def kym():
    return render_template("countymaps/KY_covid-19_countymap.html")

@app.route('/Graphs/PosRate/KY')
def kyg():
    return render_template("positivityrate/KY_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/KY')
def kyp():
    return render_template("newcases/KY_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/KY')
def kyc():
    return render_template("newdeaths/KY_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/KY')
def kydr():
    return render_template("deathrate/KY_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/KY')
def kygm():
    return render_template("googlemobility/KY_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/KY')
def kyam():
    return render_template("hospital/KY_covid-19_hospital.html")

@app.route('/Graphs/Testing/KY')
def kyt():
    return render_template("testing/KY_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/KY')
def kypop():
    return render_template("comparedeaths/KY_covid-19_deathspop.html")


@app.route('/States/LA')
def la():
    return render_template("statepages/LA-page.html")

@app.route('/Maps/PosCases/LA')
def lam():
    return render_template("countymaps/LA_covid-19_countymap.html")

@app.route('/Graphs/PosRate/LA')
def lag():
    return render_template("positivityrate/LA_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/LA')
def lap():
    return render_template("newcases/LA_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/LA')
def lac():
    return render_template("newdeaths/LA_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/LA')
def ladr():
    return render_template("deathrate/LA_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/LA')
def lagm():
    return render_template("googlemobility/LA_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/LA')
def laam():
    return render_template("hospital/LA_covid-19_hospital.html")

@app.route('/Graphs/Testing/LA')
def lat():
    return render_template("testing/LA_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/LA')
def lapop():
    return render_template("comparedeaths/LA_covid-19_deathspop.html")


@app.route('/States/ME')
def me():
    return render_template("statepages/ME-page.html")

@app.route('/Maps/PosCases/ME')
def mem():
    return render_template("countymaps/ME_covid-19_countymap.html")

@app.route('/Graphs/PosRate/ME')
def meg():
    return render_template("positivityrate/ME_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/ME')
def mep():
    return render_template("newcases/ME_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/ME')
def mec():
    return render_template("newdeaths/ME_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/ME')
def medr():
    return render_template("deathrate/ME_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/ME')
def megm():
    return render_template("googlemobility/ME_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/ME')
def meam():
    return render_template("hospital/ME_covid-19_hospital.html")

@app.route('/Graphs/Testing/ME')
def met():
    return render_template("testing/ME_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/ME')
def mepop():
    return render_template("comparedeaths/ME_covid-19_deathspop.html")


@app.route('/States/MD')
def md():
    return render_template("statepages/MD-page.html")

@app.route('/Maps/PosCases/MD')
def mdm():
    return render_template("countymaps/MD_covid-19_countymap.html")

@app.route('/Graphs/PosRate/MD')
def mdg():
    return render_template("positivityrate/MD_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/MD')
def mdp():
    return render_template("newcases/MD_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/MD')
def mdc():
    return render_template("newdeaths/MD_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/MD')
def mddr():
    return render_template("deathrate/MD_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/MD')
def mdgm():
    return render_template("googlemobility/MD_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/MD')
def mdam():
    return render_template("hospital/MD_covid-19_hospital.html")

@app.route('/Graphs/Testing/MD')
def mdt():
    return render_template("testing/MD_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/MD')
def mdpop():
    return render_template("comparedeaths/MD_covid-19_deathspop.html")


@app.route('/States/MA')
def ma():
    return render_template("statepages/MA-page.html")

@app.route('/Maps/PosCases/MA')
def mam():
    return render_template("countymaps/MA_covid-19_countymap.html")

@app.route('/Graphs/PosRate/MA')
def mag():
    return render_template("positivityrate/MA_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/MA')
def map():
    return render_template("newcases/MA_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/MA')
def mac():
    return render_template("newdeaths/MA_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/MA')
def madr():
    return render_template("deathrate/MA_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/MA')
def magm():
    return render_template("googlemobility/MA_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/MA')
def maam():
    return render_template("hospital/MA_covid-19_hospital.html")

@app.route('/Graphs/Testing/MA')
def mat():
    return render_template("testing/MA_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/MA')
def mapop():
    return render_template("comparedeaths/MA_covid-19_deathspop.html")


@app.route('/States/MI')
def mi():
    return render_template("statepages/MI-page.html")

@app.route('/Maps/PosCases/MI')
def mim():
    return render_template("countymaps/MI_covid-19_countymap.html")

@app.route('/Graphs/PosRate/MI')
def mig():
    return render_template("positivityrate/MI_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/MI')
def mip():
    return render_template("newcases/MI_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/MI')
def mic():
    return render_template("newdeaths/MI_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/MI')
def midr():
    return render_template("deathrate/MI_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/MI')
def migm():
    return render_template("googlemobility/MI_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/MI')
def miam():
    return render_template("hospital/MI_covid-19_hospital.html")

@app.route('/Graphs/Testing/MI')
def mit():
    return render_template("testing/MI_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/MI')
def mipop():
    return render_template("comparedeaths/MI_covid-19_deathspop.html")


@app.route('/States/MN')
def mn():
    return render_template("statepages/MN-page.html")

@app.route('/Maps/PosCases/MN')
def mnm():
    return render_template("countymaps/MN_covid-19_countymap.html")

@app.route('/Graphs/PosRate/MN')
def mng():
    return render_template("positivityrate/MN_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/MN')
def mnp():
    return render_template("newcases/MN_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/MN')
def mnc():
    return render_template("newdeaths/MN_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/MN')
def mndr():
    return render_template("deathrate/MN_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/MN')
def mngm():
    return render_template("googlemobility/MN_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/MN')
def mnam():
    return render_template("hospital/MN_covid-19_hospital.html")

@app.route('/Graphs/Testing/MN')
def mnt():
    return render_template("testing/MN_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/MN')
def mnpop():
    return render_template("comparedeaths/MN_covid-19_deathspop.html")


@app.route('/States/MS')
def ms():
    return render_template("statepages/MS-page.html")

@app.route('/Maps/PosCases/MS')
def msm():
    return render_template("countymaps/MS_covid-19_countymap.html")

@app.route('/Graphs/PosRate/MS')
def msg():
    return render_template("positivityrate/MS_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/MS')
def msp():
    return render_template("newcases/MS_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/MS')
def msc():
    return render_template("newdeaths/MS_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/MS')
def msdr():
    return render_template("deathrate/MS_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/MS')
def msgm():
    return render_template("googlemobility/MS_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/MS')
def msam():
    return render_template("hospital/MS_covid-19_hospital.html")

@app.route('/Graphs/Testing/MS')
def mst():
    return render_template("testing/MS_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/MS')
def mspop():
    return render_template("comparedeaths/MS_covid-19_deathspop.html")


@app.route('/States/MO')
def mo():
    return render_template("statepages/MO-page.html")

@app.route('/Maps/PosCases/MO')
def mom():
    return render_template("countymaps/MO_covid-19_countymap.html")

@app.route('/Graphs/PosRate/MO')
def mog():
    return render_template("positivityrate/MO_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/MO')
def mop():
    return render_template("newcases/MO_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/MO')
def moc():
    return render_template("newdeaths/MO_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/MO')
def modr():
    return render_template("deathrate/MO_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/MO')
def mogm():
    return render_template("googlemobility/MO_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/MO')
def moam():
    return render_template("hospital/MO_covid-19_hospital.html")

@app.route('/Graphs/Testing/MO')
def mot():
    return render_template("testing/MO_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/MO')
def mopop():
    return render_template("comparedeaths/MO_covid-19_deathspop.html")


@app.route('/States/MT')
def mt():
    return render_template("statepages/MT-page.html")

@app.route('/Maps/PosCases/MT')
def mtm():
    return render_template("countymaps/MT_covid-19_countymap.html")

@app.route('/Graphs/PosRate/MT')
def mtg():
    return render_template("positivityrate/MT_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/MT')
def mtp():
    return render_template("newcases/MT_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/MT')
def mtc():
    return render_template("newdeaths/MT_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/MT')
def mtdr():
    return render_template("deathrate/MT_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/MT')
def mtgm():
    return render_template("googlemobility/MT_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/MT')
def mtam():
    return render_template("hospital/MT_covid-19_hospital.html")

@app.route('/Graphs/Testing/MT')
def mtt():
    return render_template("testing/MT_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/MT')
def mtpop():
    return render_template("comparedeaths/MT_covid-19_deathspop.html")


@app.route('/States/NE')
def ne():
    return render_template("statepages/NE-page.html")

@app.route('/Maps/PosCases/NE')
def nem():
    return render_template("countymaps/NE_covid-19_countymap.html")

@app.route('/Graphs/PosRate/NE')
def neg():
    return render_template("positivityrate/NE_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/NE')
def nep():
    return render_template("newcases/NE_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/NE')
def nec():
    return render_template("newdeaths/NE_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/NE')
def nedr():
    return render_template("deathrate/NE_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/NE')
def negm():
    return render_template("googlemobility/NE_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/NE')
def neam():
    return render_template("hospital/NE_covid-19_hospital.html")

@app.route('/Graphs/Testing/NE')
def net():
    return render_template("testing/NE_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/NE')
def nepop():
    return render_template("comparedeaths/NE_covid-19_deathspop.html")


@app.route('/States/NV')
def nv():
    return render_template("statepages/NV-page.html")

@app.route('/Maps/PosCases/NV')
def nvm():
    return render_template("countymaps/NV_covid-19_countymap.html")

@app.route('/Graphs/PosRate/NV')
def nvg():
    return render_template("positivityrate/NV_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/NV')
def nvp():
    return render_template("newcases/NV_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/NV')
def nvc():
    return render_template("newdeaths/NV_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/NV')
def nvdr():
    return render_template("deathrate/NV_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/NV')
def nvgm():
    return render_template("googlemobility/NV_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/NV')
def nvam():
    return render_template("hospital/NV_covid-19_hospital.html")

@app.route('/Graphs/Testing/NV')
def nvt():
    return render_template("testing/NV_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/NV')
def nvpop():
    return render_template("comparedeaths/NV_covid-19_deathspop.html")


@app.route('/States/NH')
def nh():
    return render_template("statepages/NH-page.html")

@app.route('/Maps/PosCases/NH')
def nhm():
    return render_template("countymaps/NH_covid-19_countymap.html")

@app.route('/Graphs/PosRate/NH')
def nhg():
    return render_template("positivityrate/NH_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/NH')
def nhp():
    return render_template("newcases/NH_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/NH')
def nhc():
    return render_template("newdeaths/NH_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/NH')
def nhdr():
    return render_template("deathrate/NH_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/NH')
def nhgm():
    return render_template("googlemobility/NH_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/NH')
def nham():
    return render_template("hospital/NH_covid-19_hospital.html")

@app.route('/Graphs/Testing/NH')
def nht():
    return render_template("testing/NH_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/NH')
def nhpop():
    return render_template("comparedeaths/NH_covid-19_deathspop.html")


@app.route('/States/NJ')
def nj():
    return render_template("statepages/NJ-page.html")

@app.route('/Maps/PosCases/NJ')
def njm():
    return render_template("countymaps/NJ_covid-19_countymap.html")

@app.route('/Graphs/PosRate/NJ')
def njg():
    return render_template("positivityrate/NJ_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/NJ')
def njp():
    return render_template("newcases/NJ_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/NJ')
def njc():
    return render_template("newdeaths/NJ_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/NJ')
def njdr():
    return render_template("deathrate/NJ_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/NJ')
def njgm():
    return render_template("googlemobility/NJ_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/NJ')
def njam():
    return render_template("hospital/NJ_covid-19_hospital.html")

@app.route('/Graphs/Testing/NJ')
def njt():
    return render_template("testing/NJ_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/NJ')
def njpop():
    return render_template("comparedeaths/NJ_covid-19_deathspop.html")


@app.route('/States/NM')
def nm():
    return render_template("statepages/NM-page.html")

@app.route('/Maps/PosCases/NM')
def nmm():
    return render_template("countymaps/NM_covid-19_countymap.html")

@app.route('/Graphs/PosRate/NM')
def nmg():
    return render_template("positivityrate/NM_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/NM')
def nmp():
    return render_template("newcases/NM_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/NM')
def nmc():
    return render_template("newdeaths/NM_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/NM')
def nmdr():
    return render_template("deathrate/NM_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/NM')
def nmgm():
    return render_template("googlemobility/NM_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/NM')
def nmam():
    return render_template("hospital/NM_covid-19_hospital.html")

@app.route('/Graphs/Testing/NM')
def nmt():
    return render_template("testing/NM_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/NM')
def nmpop():
    return render_template("comparedeaths/NM_covid-19_deathspop.html")


@app.route('/States/NY')
def ny():
    return render_template("statepages/NY-page.html")

@app.route('/Maps/PosCases/NY')
def nym():
    return render_template("countymaps/NY_covid-19_countymap.html")

@app.route('/Graphs/PosRate/NY')
def nyg():
    return render_template("positivityrate/NY_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/NY')
def nyp():
    return render_template("newcases/NY_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/NY')
def nyc():
    return render_template("newdeaths/NY_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/NY')
def nydr():
    return render_template("deathrate/NY_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/NY')
def nygm():
    return render_template("googlemobility/NY_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/NY')
def nyam():
    return render_template("hospital/NY_covid-19_hospital.html")

@app.route('/Graphs/Testing/NY')
def nyt():
    return render_template("testing/NY_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/NY')
def nypop():
    return render_template("comparedeaths/NY_covid-19_deathspop.html")


@app.route('/States/NC')
def nc():
    return render_template("statepages/NC-page.html")

@app.route('/Maps/PosCases/NC')
def ncm():
    return render_template("countymaps/NC_covid-19_countymap.html")

@app.route('/Graphs/PosRate/NC')
def ncg():
    return render_template("positivityrate/NC_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/NC')
def ncp():
    return render_template("newcases/NC_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/NC')
def ncc():
    return render_template("newdeaths/NC_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/NC')
def ncdr():
    return render_template("deathrate/NC_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/NC')
def ncgm():
    return render_template("googlemobility/NC_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/NC')
def ncam():
    return render_template("hospital/NC_covid-19_hospital.html")

@app.route('/Graphs/Testing/NC')
def nct():
    return render_template("testing/NC_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/NC')
def ncpop():
    return render_template("comparedeaths/NC_covid-19_deathspop.html")


@app.route('/States/ND')
def nd():
    return render_template("statepages/ND-page.html")

@app.route('/Maps/PosCases/ND')
def ndm():
    return render_template("countymaps/ND_covid-19_countymap.html")

@app.route('/Graphs/PosRate/ND')
def ndg():
    return render_template("positivityrate/ND_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/ND')
def ndp():
    return render_template("newcases/ND_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/ND')
def ndc():
    return render_template("newdeaths/ND_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/ND')
def nddr():
    return render_template("deathrate/ND_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/ND')
def ndgm():
    return render_template("googlemobility/ND_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/ND')
def ndam():
    return render_template("hospital/ND_covid-19_hospital.html")

@app.route('/Graphs/Testing/ND')
def ndt():
    return render_template("testing/ND_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/ND')
def ndpop():
    return render_template("comparedeaths/ND_covid-19_deathspop.html")


@app.route('/States/OH')
def oh():
    return render_template("statepages/OH-page.html")

@app.route('/Maps/PosCases/OH')
def ohm():
    return render_template("countymaps/OH_covid-19_countymap.html")

@app.route('/Graphs/PosRate/OH')
def ohg():
    return render_template("positivityrate/OH_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/OH')
def ohp():
    return render_template("newcases/OH_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/OH')
def ohc():
    return render_template("newdeaths/OH_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/OH')
def ohdr():
    return render_template("deathrate/OH_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/OH')
def ohgm():
    return render_template("googlemobility/OH_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/OH')
def oham():
    return render_template("hospital/OH_covid-19_hospital.html")

@app.route('/Graphs/Testing/OH')
def oht():
    return render_template("testing/OH_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/OH')
def ohpop():
    return render_template("comparedeaths/OH_covid-19_deathspop.html")


@app.route('/States/OK')
def ok():
    return render_template("statepages/OK-page.html")

@app.route('/Maps/PosCases/OK')
def okm():
    return render_template("countymaps/OK_covid-19_countymap.html")

@app.route('/Graphs/PosRate/OK')
def okg():
    return render_template("positivityrate/OK_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/OK')
def okp():
    return render_template("newcases/OK_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/OK')
def okc():
    return render_template("newdeaths/OK_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/OK')
def okdr():
    return render_template("deathrate/OK_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/OK')
def okgm():
    return render_template("googlemobility/OK_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/OK')
def okam():
    return render_template("hospital/OK_covid-19_hospital.html")

@app.route('/Graphs/Testing/OK')
def okt():
    return render_template("testing/OK_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/OK')
def okpop():
    return render_template("comparedeaths/OK_covid-19_deathspop.html")


@app.route('/States/OR')
def ore():
    return render_template("statepages/OR-page.html")

@app.route('/Maps/PosCases/OR')
def orm():
    return render_template("countymaps/OR_covid-19_countymap.html")

@app.route('/Graphs/PosRate/OR')
def org():
    return render_template("positivityrate/OR_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/OR')
def orp():
    return render_template("newcases/OR_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/OR')
def orc():
    return render_template("newdeaths/OR_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/OR')
def ordr():
    return render_template("deathrate/OR_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/OR')
def orgm():
    return render_template("googlemobility/OR_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/OR')
def oram():
    return render_template("hospital/OR_covid-19_hospital.html")

@app.route('/Graphs/Testing/OR')
def ort():
    return render_template("testing/OR_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/OR')
def orpop():
    return render_template("comparedeaths/OR_covid-19_deathspop.html")


@app.route('/States/PA')
def pa():
    return render_template("statepages/PA-page.html")

@app.route('/Maps/PosCases/PA')
def pam():
    return render_template("countymaps/PA_covid-19_countymap.html")

@app.route('/Graphs/PosRate/PA')
def pag():
    return render_template("positivityrate/PA_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/PA')
def pap():
    return render_template("newcases/PA_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/PA')
def pac():
    return render_template("newdeaths/PA_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/PA')
def padr():
    return render_template("deathrate/PA_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/PA')
def pagm():
    return render_template("googlemobility/PA_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/PA')
def paam():
    return render_template("hospital/PA_covid-19_hospital.html")

@app.route('/Graphs/Testing/PA')
def pat():
    return render_template("testing/PA_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/PA')
def papop():
    return render_template("comparedeaths/PA_covid-19_deathspop.html")


@app.route('/States/RI')
def ri():
    return render_template("statepages/RI-page.html")

@app.route('/Maps/PosCases/RI')
def rim():
    return render_template("countymaps/RI_covid-19_countymap.html")

@app.route('/Graphs/PosRate/RI')
def rig():
    return render_template("positivityrate/RI_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/RI')
def rip():
    return render_template("newcases/RI_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/RI')
def ric():
    return render_template("newdeaths/RI_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/RI')
def ridr():
    return render_template("deathrate/RI_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/RI')
def rigm():
    return render_template("googlemobility/RI_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/RI')
def riam():
    return render_template("hospital/RI_covid-19_hospital.html")

@app.route('/Graphs/Testing/RI')
def rit():
    return render_template("testing/RI_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/RI')
def ripop():
    return render_template("comparedeaths/RI_covid-19_deathspop.html")


@app.route('/States/SC')
def sc():
    return render_template("statepages/SC-page.html")

@app.route('/Maps/PosCases/SC')
def scm():
    return render_template("countymaps/SC_covid-19_countymap.html")

@app.route('/Graphs/PosRate/SC')
def scg():
    return render_template("positivityrate/SC_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/SC')
def scp():
    return render_template("newcases/SC_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/SC')
def scc():
    return render_template("newdeaths/SC_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/SC')
def scdr():
    return render_template("deathrate/SC_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/SC')
def scgm():
    return render_template("googlemobility/SC_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/SC')
def scam():
    return render_template("hospital/SC_covid-19_hospital.html")

@app.route('/Graphs/Testing/SC')
def sct():
    return render_template("testing/SC_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/SC')
def scpop():
    return render_template("comparedeaths/SC_covid-19_deathspop.html")


@app.route('/States/SD')
def sd():
    return render_template("statepages/SD-page.html")

@app.route('/Maps/PosCases/SD')
def sdm():
    return render_template("countymaps/SD_covid-19_countymap.html")

@app.route('/Graphs/PosRate/SD')
def sdg():
    return render_template("positivityrate/SD_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/SD')
def sdp():
    return render_template("newcases/SD_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/SD')
def sdc():
    return render_template("newdeaths/SD_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/SD')
def sddr():
    return render_template("deathrate/SD_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/SD')
def sdgm():
    return render_template("googlemobility/SD_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/SD')
def sdam():
    return render_template("hospital/SD_covid-19_hospital.html")

@app.route('/Graphs/Testing/SD')
def sdt():
    return render_template("testing/SD_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/SD')
def sdpop():
    return render_template("comparedeaths/SD_covid-19_deathspop.html")


@app.route('/States/TN')
def tn():
    return render_template("statepages/TN-page.html")

@app.route('/Maps/PosCases/TN')
def tnm():
    return render_template("countymaps/TN_covid-19_countymap.html")

@app.route('/Graphs/PosRate/TN')
def tng():
    return render_template("positivityrate/TN_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/TN')
def tnp():
    return render_template("newcases/TN_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/TN')
def tnc():
    return render_template("newdeaths/TN_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/TN')
def tndr():
    return render_template("deathrate/TN_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/TN')
def tngm():
    return render_template("googlemobility/TN_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/TN')
def tnam():
    return render_template("hospital/TN_covid-19_hospital.html")

@app.route('/Graphs/Testing/TN')
def tnt():
    return render_template("testing/TN_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/TN')
def tnpop():
    return render_template("comparedeaths/TN_covid-19_deathspop.html")


@app.route('/States/TX')
def tx():
    return render_template("statepages/TX-page.html")

@app.route('/Maps/PosCases/TX')
def txm():
    return render_template("countymaps/TX_covid-19_countymap.html")

@app.route('/Graphs/PosRate/TX')
def txg():
    return render_template("positivityrate/TX_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/TX')
def txp():
    return render_template("newcases/TX_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/TX')
def txc():
    return render_template("newdeaths/TX_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/TX')
def txdr():
    return render_template("deathrate/TX_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/TX')
def txgm():
    return render_template("googlemobility/TX_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/TX')
def txam():
    return render_template("hospital/TX_covid-19_hospital.html")

@app.route('/Graphs/Testing/TX')
def txt():
    return render_template("testing/TX_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/TX')
def txpop():
    return render_template("comparedeaths/TX_covid-19_deathspop.html")


@app.route('/States/UT')
def ut():
    return render_template("statepages/UT-page.html")

@app.route('/Maps/PosCases/UT')
def utm():
    return render_template("countymaps/UT_covid-19_countymap.html")

@app.route('/Graphs/PosRate/UT')
def utg():
    return render_template("positivityrate/UT_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/UT')
def utp():
    return render_template("newcases/UT_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/UT')
def utc():
    return render_template("newdeaths/UT_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/UT')
def utdr():
    return render_template("deathrate/UT_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/UT')
def utgm():
    return render_template("googlemobility/UT_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/UT')
def utam():
    return render_template("hospital/UT_covid-19_hospital.html")

@app.route('/Graphs/Testing/UT')
def utt():
    return render_template("testing/UT_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/UT')
def utpop():
    return render_template("comparedeaths/UT_covid-19_deathspop.html")


@app.route('/States/VT')
def vt():
    return render_template("statepages/VT-page.html")

@app.route('/Maps/PosCases/VT')
def vtm():
    return render_template("countymaps/VT_covid-19_countymap.html")

@app.route('/Graphs/PosRate/VT')
def vtg():
    return render_template("positivityrate/VT_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/VT')
def vtp():
    return render_template("newcases/VT_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/VT')
def vtc():
    return render_template("newdeaths/VT_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/VT')
def vtdr():
    return render_template("deathrate/VT_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/VT')
def vtgm():
    return render_template("googlemobility/VT_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/VT')
def vtam():
    return render_template("hospital/VT_covid-19_hospital.html")

@app.route('/Graphs/Testing/VT')
def vtt():
    return render_template("testing/VT_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/VT')
def vtpop():
    return render_template("comparedeaths/VT_covid-19_deathspop.html")


@app.route('/States/VA')
def va():
    return render_template("statepages/VA-page.html")

@app.route('/Maps/PosCases/VA')
def vam():
    return render_template("countymaps/VA_covid-19_countymap.html")

@app.route('/Graphs/PosRate/VA')
def vag():
    return render_template("positivityrate/VA_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/VA')
def vap():
    return render_template("newcases/VA_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/VA')
def vac():
    return render_template("newdeaths/VA_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/VA')
def vadr():
    return render_template("deathrate/VA_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/VA')
def vagm():
    return render_template("googlemobility/VA_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/VA')
def vaam():
    return render_template("hospital/VA_covid-19_hospital.html")

@app.route('/Graphs/Testing/VA')
def vat():
    return render_template("testing/VA_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/VA')
def vapop():
    return render_template("comparedeaths/VA_covid-19_deathspop.html")


@app.route('/States/WA')
def wa():
    return render_template("statepages/WA-page.html")

@app.route('/Maps/PosCases/WA')
def wam():
    return render_template("countymaps/WA_covid-19_countymap.html")

@app.route('/Graphs/PosRate/WA')
def wag():
    return render_template("positivityrate/WA_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/WA')
def wap():
    return render_template("newcases/WA_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/WA')
def wac():
    return render_template("newdeaths/WA_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/WA')
def wadr():
    return render_template("deathrate/WA_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/WA')
def wagm():
    return render_template("googlemobility/WA_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/WA')
def waam():
    return render_template("hospital/WA_covid-19_hospital.html")

@app.route('/Graphs/Testing/WA')
def wat():
    return render_template("testing/WA_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/WA')
def wapop():
    return render_template("comparedeaths/WA_covid-19_deathspop.html")


@app.route('/States/WV')
def wv():
    return render_template("statepages/WV-page.html")

@app.route('/Maps/PosCases/WV')
def wvm():
    return render_template("countymaps/WV_covid-19_countymap.html")

@app.route('/Graphs/PosRate/WV')
def wvg():
    return render_template("positivityrate/WV_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/WV')
def wvp():
    return render_template("newcases/WV_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/WV')
def wvc():
    return render_template("newdeaths/WV_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/WV')
def wvdr():
    return render_template("deathrate/WV_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/WV')
def wvgm():
    return render_template("googlemobility/WV_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/WV')
def wvam():
    return render_template("hospital/WV_covid-19_hospital.html")

@app.route('/Graphs/Testing/WV')
def wvt():
    return render_template("testing/WV_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/WV')
def wvpop():
    return render_template("comparedeaths/WV_covid-19_deathspop.html")


@app.route('/States/WI')
def wi():
    return render_template("statepages/WI-page.html")

@app.route('/Maps/PosCases/WI')
def wim():
    return render_template("countymaps/WI_covid-19_countymap.html")

@app.route('/Graphs/PosRate/WI')
def wig():
    return render_template("positivityrate/WI_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/WI')
def wip():
    return render_template("newcases/WI_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/WI')
def wic():
    return render_template("newdeaths/WI_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/WI')
def widr():
    return render_template("deathrate/WI_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/WI')
def wigm():
    return render_template("googlemobility/WI_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/WI')
def wiam():
    return render_template("hospital/WI_covid-19_hospital.html")

@app.route('/Graphs/Testing/WI')
def wit():
    return render_template("testing/WI_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/WI')
def wipop():
    return render_template("comparedeaths/WI_covid-19_deathspop.html")


@app.route('/States/WY')
def wy():
    return render_template("statepages/WY-page.html")

@app.route('/Maps/PosCases/WY')
def wym():
    return render_template("countymaps/WY_covid-19_countymap.html")

@app.route('/Graphs/PosRate/WY')
def wyg():
    return render_template("positivityrate/WY_covid-19_positivityrate.html")

@app.route('/Graphs/NewCases/WY')
def wyp():
    return render_template("newcases/WY_covid-19_newpositive.html")

@app.route('/Graphs/NewDeaths/WY')
def wyc():
    return render_template("newdeaths/WY_covid-19_newdeaths.html")

@app.route('/Graphs/DeathRate/WY')
def wydr():
    return render_template("deathrate/WY_covid-19_deathrate.html")

@app.route('/Graphs/Mobility/Google/WY')
def wygm():
    return render_template("googlemobility/WY_covid-19_gmobilityreport.html")

@app.route('/Graphs/Hospital/WY')
def wyam():
    return render_template("hospital/WY_covid-19_hospital.html")

@app.route('/Graphs/Testing/WY')
def wyt():
    return render_template("testing/WY_covid-19_testing.html")

@app.route('/Graphs/DeathsPop/WY')
def wypop():
    return render_template("comparedeaths/WY_covid-19_deathspop.html")
            
if __name__=="__main__":
    app.run(debug=True)

