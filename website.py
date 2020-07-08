from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/Maps/PosCases/US')
def usposmap():
    return render_template("map.html")

@app.route('/US')
def us():
    return render_template("us_covid-19_positivityrate.html")

@app.route('/States')
def dd():
    return render_template("AA_main.html")

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

if __name__=="__main__":
    app.run(debug=True)

