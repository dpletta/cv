# -*- coding: utf-8 -*-
"""Structured content model for David R. Pletta's academic CV.

Inline markup used in string fields:
    **bold**   *italic*
Right-aligned date on an entry heading is carried in the `date` key.
"""

LAST_UPDATED = "October 14, 2026"
ORCID_URL = "https://orcid.org/0000-0003-0363-153X"

NAME = "DAVID R. PLETTA, PhD, MPH"
CONTACT = [
    "Department of Epidemiology, University of Michigan School of Public Health, Ann Arbor, MI",
    "dpletta@umich.edu",
    "ORCID: https://orcid.org/0000-0003-0363-153X",
]

# ---------------------------------------------------------------- EDUCATION
EDUCATION = [
    dict(org="Harvard University", loc="Cambridge, MA",
         role="PhD, Population Health Sciences", date="2020-2023",
         sub=["Harvard Kenneth C. Griffin Graduate School of Arts and Sciences",
              "Department of Social and Behavioral Sciences"]),
    dict(org="Boston University", loc="Boston, MA",
         role="MPH, Epidemiology and Biostatistics", date="2017-2019",
         sub=["Boston University School of Public Health",
              "Departments of Epidemiology & Biostatistics"]),
    dict(org="University of California, Santa Cruz", loc="Santa Cruz, CA",
         role="BS, Cognitive Science, cum laude", date="2011-2014",
         sub=[]),
    dict(org=None, loc=None,
         role="BA, Psychology, cum laude", date="2011-2014",
         sub=["Department of Psychology"]),
]

# -------------------------------------------------------- ACADEMIC POSITIONS
POSITIONS = [
    ("University of Michigan", "Ann Arbor, MI", "Research Area Specialist Lead", "2024-Present", "Department of Epidemiology"),
    ("University of Michigan", "Ann Arbor, MI", "Research Associate", "2024", "Department of Epidemiology"),
    ("Brown University School of Public Health", "Providence, RI", "Data Scientist", "2023-2024", "Department of Behavioral and Social Sciences"),
    ("Brigham and Women’s Hospital", "Boston, MA", "Epidemiology Analyst", "2021-2023", "Division of Endocrinology, Diabetes, and Hypertension"),
    ("The Fenway Institute at Fenway Health", "Boston, MA", "Epidemiology Analyst", "2019-2021", "Department of Epidemiology"),
    ("Boston Children’s Hospital", "Boston, MA", "Clinical Research Specialist", "2018-2019", "Division of General Pediatrics & Division of Adolescent/Young Adult Medicine"),
    ("The Fenway Institute at Fenway Health", "Boston, MA", "Epidemiology Graduate Intern", "2018", "Department of Epidemiology"),
    ("Boston Children’s Hospital", "Boston, MA", "Qualitative Research Assistant", "2017-2019", "Division of Adolescent/Young Adult Medicine"),
    ("University of California, Santa Cruz", "Santa Cruz, CA", "Research Coordinator", "2014-2016", "Department of Psychology"),
    ("University of Southern California", "Los Angeles, CA", "Visiting Research Assistant in Neuroscience", "2014", "Leonard Davis School of Gerontology"),
    ("University of California, Santa Cruz", "Santa Cruz, CA", "Senior Research Assistant", "2014", "Department of Psychology"),
    ("University of California, Santa Cruz", "Santa Cruz, CA", "Research Assistant", "2013-2014", "Department of Psychology"),
]

# ------------------------------------------------ EXTRAMURAL RESEARCH SUPPORT
GRANTS_AWARDED = [
    dict(
        title="National Longitudinal Study of Violence and Substance Use in the United States",
        date="2027-2031",
        fields=[
            ("Role", "Co-Investigator (Multiple Principal Investigators: Sari Reisner, Kristi Gamarel)"),
            ("Funder", "National Institute on Drug Abuse (NIDA), National Institutes of Health (NIH)"),
            ("Mechanism", "Research Project Grant (R01)"),
            ("Award No.", "R01 DA066104"),
            ("Total Costs", "$3,899,971"),
        ],
        aims="Estimate the prevalence of, and explore the prospective associations between, gender-based violence, social safety threats, protective factors, and behavioral health outcomes in a national cohort of adults, using a community-centered digital cohort model to inform public health interventions.",
    ),
    dict(
        title="Diagnosis-Agnostic Sequence Mining to Detect Bipolar-Pattern Suicide Risk and Structural Inequities in Adolescents and Young Adults",
        date="2026-2028",
        fields=[
            ("Role", "Principal Investigator"),
            ("Funder", "National Institute on Minority Health and Health Disparities (NIMHD), National Institutes of Health (NIH)"),
            ("Mechanism", "Loan Repayment Program (L70), Facilitating Opportunities in Cutting-edge Science (FOCUS)"),
            ("Award No.", "1L70MD021651-01"),
            ("Total Costs", "$31,013"),
        ],
        aims="Develop a machine learning algorithm using a national electronic health records database to identify sequences of healthcare utilization, prescription medications, and diagnostic codes that are probabilistically indicative of prodromal bipolar disorder in adolescents and young adults. These sequences will be taxonomized in collaboration with community members and psychiatrists, and a case-control study will estimate each sequence’s relative risk for future suicide attempt and death by suicide.",
    ),
]

GRANTS_UNDER_REVIEW = [
    dict(
        title="Quantifying Multi-Agent Re-identification Risk in Open and Public Datasets",
        date="2027-2029",
        fields=[
            ("Role", "Multiple Principal Investigator (with Stephen Hutt and Sari Reisner)"),
            ("Funder", "Schmidt Sciences, in collaboration with Google DeepMind, the Cooperative AI Foundation, the Advanced Research and Invention Agency (ARIA), and Google.org"),
            ("Program", "Scaling AI Safety for a Multi-Agent World"),
            ("Total Costs", "$300,000"),
        ],
        aims="Assess whether cooperative teams of artificial intelligence (AI) agents can re-identify research participants in open and public datasets. Using rarity metadata from existing public health and education datasets, we will generate a synthetic population, then select a target individual and random samples of varying size. Iterative simulation trials across multi-agent structures will quantify the accuracy, precision, and recall of agents’ performance in correctly re-identifying the target or excluding it from the sample. Findings will inform privacy-protective tools for research with human subjects (e.g., a sandbox that strips high-risk identifiers from repository-bound datasets), supporting open science as AI capabilities continue to advance.",
    ),
]

GRANTS_IN_PREP = [
    dict(
        title="Pre-Diagnostic Electronic Health Record Trajectories and Suicide Risk in Adolescents and Young Adults with Emerging Bipolar Disorder",
        date="",
        fields=[
            ("Role", "Multiple Principal Investigator (with Sari Reisner)"),
            ("Funder", "National Institute of Mental Health (NIMH), National Institutes of Health (NIH)"),
            ("Mechanism", "Research Project Grant (R01)"),
        ],
        aims="Identify pre-diagnostic electronic health record (EHR) event sequences preceding bipolar disorder, organize these sequences into a clinically interpretable taxonomy informed by patients and clinicians, and quantify sequence-specific risks of suicide attempt and death by suicide among adolescents and young adults, using national EHR data with external validation in a health system cohort.",
    ),
]

# ------------------------------------------------ SCHOLARSHIPS & FELLOWSHIPS
FELLOWSHIPS = [
    ("University of Michigan", "Ann Arbor, MI", "Fellow", "2026-Present",
     ["Data and AI Intensive Research with Rigor and Reproducibility (DAIR3) Program",
      "Michigan Institute for Data & AI in Society; program supported by the National Institutes of Health (NIH)"]),
    ("Harvard University", "Cambridge, MA", "Graduate Prize Fellow", "2020-2023",
     ["Five-year full tuition scholarship and stipend for doctoral training",
      "Harvard Kenneth C. Griffin Graduate School of Arts and Sciences"]),
    ("Boston University", "Boston, MA", "Advancing Public Health Excellence Award", "2017-2019",
     ["Partial tuition scholarship for MPH training",
      "Boston University School of Public Health"]),
    ("San Francisco State University", "San Francisco, CA", "Summer Institute Tuition Scholarship", "2015",
     ["Center for Research and Education on Gender and Sexuality (CREGS)"]),
]

# ---------------------------------------------------- HONORS & RECOGNITION
# (title, date, detail lines, conferring body, location)
HONORS = [
    ("Richard Green Founding Editor Essay Award", "2021",
     ["Best peer-reviewed publication on gender or sexual behavior, for “Gay men’s health and identity: Social change and the life course”"],
     "The International Academy of Sex Research", "Bloomington, IN"),
    ("Outstanding Researcher Award", "2015", [],
     "Department of Psychology, University of California, Santa Cruz", "Santa Cruz, CA"),
    ("University Honors (cum laude), BS in Cognitive Science & BA in Psychology", "2014", [],
     "Department of Psychology, University of California, Santa Cruz", "Santa Cruz, CA"),
    ("Departmental Honors, BS in Cognitive Science & BA in Psychology", "2014", [],
     "Department of Psychology, University of California, Santa Cruz", "Santa Cruz, CA"),
    ("College Leadership Distinction", "2014", [],
     "College Ten, University of California, Santa Cruz", "Santa Cruz, CA"),
]

# ------------------------------------------------------------ PUBLICATIONS
# Each: (authors, title, journal, cite, ids)
PUBLISHED = [
    ("Dusic E, Madden D, Rios IE, Restar A, Milan T, Patterson J, **Pletta DR**, Rabinowitz S, Ramos MA, Aguayo-Romero R, Baker K, Horowitz CR, Reisner SL.",
     "“Will it be enough to be respected?”: Understanding personal, institutional, and societal harms and benefits of transgender identity genomics research.",
     "Journal of Community Genetics.", "In press.", ""),

    ("Dusic E, Madden D, Rios IE, Hwang B, Rabinowitz S, Ramos M, **Pletta DR**, Aguayo-Romero R, Lunn M, Baker K, Horowitz C, Reisner SL.",
     "Perceptions of and willingness to participate in genomics research among a US sample.",
     "Frontiers in Genetics.", "", "doi:10.3389/fgene.2026.1808576."),

    ("**Pletta DR**, Quint M, Keuroghlian AS, Radix AE, Deutsch MB, Mayer KH, Potter J, Pardee DJ, Campbell J, Hughto JMW, Reisner SL.",
     "Situated vulnerabilities and resiliencies associated with lifetime and past 6-month suicide attempt among transgender and gender diverse primary care patients.",
     "Psychiatry Research.", "2026;364:117350.",
     "doi:10.1016/j.psychres.2026.117350. PMID: 42541935."),

    ("**Pletta DR**, Reisner SL, Feng C, Morrow C, Clark MC, Omar B, Keuroghlian AS, Xu R.",
     "Diagnostic delays and suicidal thoughts and behaviors among young adults with a history of mood disorders.",
     "Frontiers in Psychiatry.", "2026;17:1894148.",
     "doi:10.3389/fpsyt.2026.1894148. PMID: 42558474. PMCID: PMC13437458."),

    ("Silcox J, **Pletta DR**, Hughto JMW, Rapisarda S, Zaragoza S, Kelly PJA, Vento S, Rich J, Green T.",
     "Contrasting perspectives and applications of the Good Samaritan Overdose Prevention Law: Insights from people who use and distribute drugs in Rhode Island.",
     "Health & Justice.", "2026;14(1):35.",
     "doi:10.1186/s40352-026-00433-0. PMID: 42343044. PMCID: PMC13445650."),

    ("Xu R, **Pletta DR**, Feng C, Morrow C, Clark MC, Omar B, Keuroghlian AS, Reisner SL.",
     "Delays in diagnosis and treatment of depressive disorder among young adults: A national online survey-based cross-sectional study.",
     "PLoS ONE.", "2026;21(6):e0351402.",
     "doi:10.1371/journal.pone.0351402. PMID: 42284287. PMCID: PMC13262879."),

    ("**Pletta DR**, Chen JT, Reisner SL, Hughto JMW, Austin SB.",
     "Gender minority stress is associated with past-year suicidal ideation in a national probability sample of transgender and gender diverse adults.",
     "Psychology of Sexual Orientation and Gender Diversity.", "2026;13(3):613-622.",
     "doi:10.1037/sgd0000760. PMID: 40895806. PMCID: PMC12396565."),

    ("Hughto JMW, Vento S, **Pletta DR**, Noh M, Shireman TI, Santostefano CM, Hughes L, Peterson L, Seymour E, Stettenbauer EG, Dow PM.",
     "Medicaid prescription cap policies and exemptions for medications for opioid use disorder: A process and content analysis.",
     "Health Affairs Scholar.", "2025;3(11):qxaf203.",
     "doi:10.1093/haschl/qxaf203. PMID: 41245506. PMCID: PMC12612678."),

    ("Reisner SL, Scheim A, Cole SW, Wirtz AL, Poteat T, Mimiaga MJ, Marzinke M, Meyer AI, Smith K, **Pletta DR**, Mayer KH.",
     "Transgender men and transmasculine one-on-one and group-delivered empowerment for targeted HIV reduction (TOGETHR) study: Protocol for a digital factorial randomized controlled trial.",
     "JMIR Research Protocols.", "2025;14:e76831.",
     "doi:10.2196/76831. PMID: 41115262. PMCID: PMC12583947."),

    ("**Pletta DR**, Quint M, Radix A, Mayer KH, Potter J, Coon D, Keuroghlian AS, Hughto JMW, Reisner SL.",
     "Gender-affirming surgical history, satisfaction, and unmet needs among transgender adults.",
     "JAMA Network Open.", "2025;8(9):e2532494.",
     "doi:10.1001/jamanetworkopen.2025.32494. PMID: 40965883. PMCID: PMC12447237."),

    ("Balkan E, Babbs G, Meyers DJ, Kelly PJA, Yee K, **Pletta DR**, Shireman TI, Alpert AB, Baker KE, Hughto JMW.",
     "Gender-affirming surgery for transgender and gender diverse Medicare beneficiaries.",
     "JAMA Network Open.", "2025;8(5):e258072.",
     "doi:10.1001/jamanetworkopen.2025.8072. PMID: 40310645. PMCID: PMC12046427."),

    ("Reisner SL, **Pletta DR**, Mayer KH, Deutsch MB, Poteat T, Potter J, Wirtz AL, Harris A, Campbell J, Keuroghlian AS, Hughto JMW, Gonzalez A, Radix AE.",
     "HIV seropositivity and viral non-suppression in transgender, non-binary, and gender-diverse people in primary care receiving gender-affirming hormone therapy in the USA between 2013 and 2019 (LEGACY): An observational, longitudinal, cohort study.",
     "Lancet HIV.", "2025;12(4):e283-e292.",
     "doi:10.1016/S2352-3018(25)00004-9. PMID: 40158515. PMCID: PMC12355900."),

    ("Babbs G, Mulcahy A, Ellison J, Varma H, **Pletta DR**, Yee K, Hughes LD, Shireman TI, Hughto JMW.",
     "Chronic conditions among transgender Medicare beneficiaries: Variation by race, ethnicity, and Medicaid dual-enrollment.",
     "Disability and Health Journal.", "2025;18(2):101764.",
     "doi:10.1016/j.dhjo.2024.101764. PMID: 39701841. PMCID: PMC11885010."),

    ("Reisner SL, **Pletta DR**, Keuroghlian AS, Mayer KH, Deutsch MB, Potter J, Hughto JMW, Harris A, Radix A.",
     "Gender-affirming hormone therapy and depressive symptoms among transgender adults.",
     "JAMA Network Open.", "2025;8(3):e250955.",
     "doi:10.1001/jamanetworkopen.2025.0955. PMID: 40094660. PMCID: PMC11915065."),

    ("Hughto JMW, Varma H, Yee K, Babbs G, Hughes LD, **Pletta DR**, Meyers DJ, Shireman TI.",
     "Characterizing disparities in the HIV care continuum among U.S. transgender and cisgender Medicare beneficiaries, 2008-2017.",
     "AIDS Care.", "2025;37(3):423-434.",
     "doi:10.1080/09540121.2025.2453831. PMID: 39886758. PMCID: PMC11922666."),

    ("Hughto JMW, Kelly PJA, Vento SA, **Pletta DR**, Noh M, Silcox J, Rich JD, Green TC.",
     "Characterizing and responding to stimulant overdoses: Findings from a mixed methods study of people who use cocaine and other stimulants in New England.",
     "Drug and Alcohol Dependence.", "2024;266:112501.",
     "doi:10.1016/j.drugalcdep.2024.112501. PMID: 39608288. PMCID: PMC11685032."),

    ("**Pletta DR**, Mayer KH, Chen JT, Hughto JMW, Keuroghlian AS, Radix AE, Reisner SL.",
     "Gender-affirming hormone therapy is associated with increased odds of screening for sexually transmitted infections in a clinical cohort of transgender and nonbinary adults.",
     "Transgender Health.", "2024;9(6):508-515.",
     "doi:10.1089/trgh.2023.0159. PMID: 39735371. PMCID: PMC11669630."),

    ("Hughto JMW, Rich J, Kelly PJA, Vento S, Silcox J, Noh M, **Pletta DR**, Erowid E, Erowid F, Green T.",
     "Preventing overdoses involving stimulants: The POINTS study protocol.",
     "BMC Public Health.", "2024;24(1):2325.",
     "doi:10.1186/s12889-024-19779-x. PMID: 39192313. PMCID: PMC11348517."),

    ("**Pletta DR**, Austin SB, Chen JT, Radix AE, Keuroghlian AS, Hughto JMW, Reisner SL.",
     "Lower levels of social support are associated with risk for future suicide attempts in a clinical sample of transgender and gender diverse adults.",
     "Social Psychiatry and Psychiatric Epidemiology.", "2024;59(8):1401-1412.",
     "doi:10.1007/s00127-023-02606-w. PMID: 38182830. PMCID: PMC11869392."),

    ("Reisner SL, Deutsch MB, Mayer KH, **Pletta DR**, Campbell J, Potter J, Keuroghlian AS, Hughto JMW, Asquith A, Pardee DJ, Harris A, Quint M, Grasso C, Gonzalez A, Radix A.",
     "Decreased anogenital gonorrhea and chlamydia in transgender and gender diverse primary care patients receiving gender-affirming care.",
     "Journal of General Internal Medicine.", "2024;39(7):1164-1172.",
     "doi:10.1007/s11606-023-08531-7. PMID: 37989820. PMCID: PMC11116345."),

    ("Hammack PL, **Pletta DR**, Hughes SD, Atwood JM, Cohen EM, Clark RC.",
     "Community support for sexual and gender diversity, minority stress, and mental health: A mixed-methods study of adolescents with minoritized sexual and gender identities.",
     "Psychology of Sexual Orientation and Gender Diversity.", "2024;11(2):250-268.",
     "doi:10.1037/sgd0000591."),

    ("Reisner SL, **Pletta DR**, Harris A, Campbell J, Asquith A, Pardee DJ, Deutsch MB, Aguayo-Romero R, Quint M, Keuroghlian A, Radix A.",
     "Exploring gender euphoria in a sample of transgender and gender diverse patients at two U.S. urban community health centers.",
     "Psychiatry Research.", "2023;329:115541.",
     "doi:10.1016/j.psychres.2023.115541. PMID: 37857133."),

    ("Reisner SL, **Pletta DR**, Pardee DJ, Deutsch MB, Peitzmeier SM, Hughto JMW, Quint M, Potter J.",
     "Digital-assisted self-interview of HIV or sexually transmitted infection risk behaviors in transmasculine adults: Development and field testing of the transmasculine sexual health assessment.",
     "JMIR Public Health and Surveillance.", "2023;9:e40503.",
     "doi:10.2196/40503. PMID: 36930204. PMCID: PMC10131935."),

    ("**Pletta DR**, Hughto JMW, Peitzmeier S, Deutsch MB, Pardee D, Potter J, Reisner SL.",
     "Factors associated with transmasculine adults recently engaging in sexual behavior with partners of unknown STI and HIV status.",
     "AIDS and Behavior.", "2022;26(9):3139-3145.",
     "doi:10.1007/s10461-022-03651-3. PMID: 35362909. PMCID: PMC10266479."),

    ("**Pletta DR**, Kant JD, Ehrensaft D, MacNish M, Cahill S, Katz-Wise SL.",
     "The 2016 United States presidential election’s impact on families with transgender adolescents in New England.",
     "Journal of Family Psychology.", "2022;36(1):23-34.",
     "doi:10.1037/fam0000873. PMID: 34043404. PMCID: PMC8626525."),

    ("Garcia Saiz E, Sarda V, **Pletta DR**, Reisner SL, Katz-Wise SL.",
     "Family functioning as a protective factor for sexual risk behaviors among gender minority adolescents.",
     "Archives of Sexual Behavior.", "2021;50(7):3023-3033.",
     "doi:10.1007/s10508-021-02079-5. PMID: 34586546. PMCID: PMC9116415."),

    ("Reisner SL, Deutsch MB, Mayer KH, Grasso C, Potter J, Gonzales A, Keuroghlian A, Hughto JM, Campbell J, Asquith A, Pardee DJ, **Pletta DR**, Radix A.",
     "Longitudinal cohort study of gender affirmation and HIV-related health in transgender and gender diverse adults: The LEGACY Project protocol.",
     "JMIR Research Protocols.", "2021;10(3):e24198.",
     "doi:10.2196/24198. PMID: 33646126. PMCID: PMC7961399."),

    ("Hughto JMW, **Pletta DR**, Gordon L, Cahill S, Mimiaga M, Reisner SL.",
     "Negative transgender-related media messages are associated with adverse mental health outcomes in a multistate study of transgender adults.",
     "LGBT Health.", "2021;8(1):32-41.",
     "doi:10.1089/lgbt.2020.0279. PMID: 33170060. PMCID: PMC7826438."),

    ("Reisner SL, **Pletta DR**, Potter J, Deutsch MB.",
     "Initial psychometric evaluation of a brief sexual functioning screening tool for transmasculine adults: Transmasculine Sexual Functioning Index.",
     "Sexual Medicine.", "2020;8(3):350-360.",
     "doi:10.1016/j.esxm.2020.05.006. PMID: 32703760. PMCID: PMC7471062."),

    ("**Pletta DR**, Hughto JMW, Peitzmeier S, Deutsch MB, Pardee D, Potter J, Reisner SL.",
     "Individual- and partnership-level correlates of protective barrier use in a sample of transmasculine adults with diverse sexual partnerships.",
     "AIDS Patient Care and STDs.", "2020;34(5):237-246.",
     "doi:10.1089/apc.2019.0296. PMID: 32396475. PMCID: PMC7232705."),

    ("Hammack PL, Frost DM, Meyer IH, **Pletta DR**.",
     "Gay men’s health and identity: Social change and the life course.",
     "Archives of Sexual Behavior.", "2018;47(1):59-74.",
     "doi:10.1007/s10508-017-0990-9. PMID: 28585157. PMCID: PMC5903851."),

    ("Dodge B, Herbenick D, Friedman MR, Schick V, Fu TC, Bostwick W, Bartelt E, Munoz-Laboy M, **Pletta DR**, Reece M, Sandfort TG.",
     "Attitudes toward bisexual men and women among a nationally representative probability sample of adults in the United States.",
     "PLoS One.", "2016;11(10):e0164430.",
     "doi:10.1371/journal.pone.0164430. PMID: 27783644. PMCID: PMC5082634."),
]

UNDER_REVIEW = [
    ("**Pletta DR**, Reisner SL, Feng C, Morrow C, Clark MC, Omar B, Keuroghlian AS, Xu R.",
     "Symptom onset patterns, diagnostic delay, and lifetime adverse psychiatric events among young adults with bipolar disorder in the United States: a cross-sectional study.",
     "BMJ Connections Mental Health,", "R&R.", ""),
    ("Reisner SL, **Pletta DR**, Radix A, Keuroghlian AS, Mayer KH, Xu R.",
     "Psychiatric epidemiology of transgender young adult primary care patients at two U.S. urban community health centers: A cross-sectional study.",
     "BMC Psychiatry.", "", ""),
]

IN_PREPARATION = [
    ("**Pletta DR**, Quint M, Mayer KH, Potter J, Radix A, Hughto JMW, Bhasin S, Keuroghlian AS, Reisner SL.",
     "Transgender and gender diverse adult primary care patients screening positive for suicide risk in a New England community health center.",
     "", "(Target journal: *American Journal of Preventive Medicine*)", ""),
    ("Rios IE, **Pletta DR**, Perez-Brumer A, Silva-Santisteban A, Apedaile D, Heurta L, Aguayo-Romero R, Reisner SL.",
     "Suicidality and severe psychological distress among young transgender women in Peru.",
     "", "(Target journal: *Lancet Child & Adolescent Health*)", ""),
    ("Reisner SL, **Pletta DR**, McFarlane M, et al.",
     "Everyday discrimination and posttraumatic stress disorder among transgender, nonbinary, and gender diverse young adults in primary care.",
     "", "(Target journal: *Social Psychiatry and Psychiatric Epidemiology*)", ""),
    ("Reisner SL, **Pletta DR**, et al.",
     "Syndemic latent classes and sexual-health outcomes among transfeminine adults in the USA: A cross-sectional analysis of the ENCORE cohort.",
     "", "(Target journal: *Lancet HIV*)", ""),
    ("Reisner SL, **Pletta DR**, et al.",
     "Cumulative adversity and recent non-suicidal self-injury in young adults with a history of depression.",
     "", "(Target journal: *Psychiatry Research*)", ""),
]

# ------------------------------------------------- SCIENTIFIC PRESENTATIONS
ORAL = [
    "Reisner SL, **Pletta DR**, Wirtz AL, Radix AE, Poteat T, Borquez A, Linton S, Beyrer C, Althoff KN, Miller M, Brown C, Lint A, Pontes C, Stevenson M, Humes E, Schneider J, Rodriguez A, Cooney EE, ENCORE Study Group. Syndemic risk-resilience profiles and HIV vulnerability among transgender women and transfeminine adults in the US: Findings from ENCORE. *World Professional Association for Transgender Health.* Mexico City, Mexico. 2026.",
    "Dusic E, Madden D, Rios IE, Hwang BJ, Rabinowitz S, Ramos M, **Pletta DR**, Aguayo-Romero R, Lunn MR, Baker K, Horowitz CR, Reisner SL. Transgender, nonbinary, and gender diverse adults’ perceptions of and willingness to participate in transgender identity genomics research. *7th Ethical, Legal, and Social Implications (ELSI) Congress, National Human Genome Research Institute (NHGRI).* Chapel Hill, NC, USA. 2026.",
    "Dusic E, Starks H, Madden D, Rios IE, Restar A, **Pletta DR**, Ramos M, Baker K, Horowitz C, Reisner SL. Vilifying or validating? The political impact of biological determinism. *UCSF National Transgender Health Summit.* San Francisco, CA, USA. 2025.",
    "Dow PM, George M, Hughes L, **Pletta DR**, Shireman TI, Donohue JM, Hughto JMW. Association of state Medicaid prescription cap policies with adherence trajectories of buprenorphine treatment for opioid use disorder. *Addiction Health Services Research Conference.* San Francisco, CA, USA. 2024.",
    "Kelly P, Green T, Rich J, Vento S, Noh M, **Pletta DR**, Silcox J, Davis M, Toffey A, Silva V, Tobin S, Hughto JMW. Self-reported pathways through which illicitly manufactured fentanyl enters the stimulant supply: Insights from people who use and distribute drugs. *American Public Health Association Annual Meeting.* Minneapolis, MN, USA. 2024.",
    "Reisner SL, **Pletta DR**, Quint M, Deutsch MB, Mayer KH, Potter J, O’Brien-Coon D, Bhasin S, Keuroghlian A, Hughto JMW, Radix A. Gender-affirming surgical history, satisfaction, and unmet needs in transgender and gender diverse community health center patients: Findings from the LEGACY Project. *UCSF National Transgender Health Summit.* San Francisco, CA, USA. 2023.",
    "Reisner SL, Deutsch MB, Mayer KH, Grasso C, Campbell J, **Pletta DR**, Potter J, Gonzales A, Keuroghlian AS, Hughto JMW, Asquith A, Pardee DJ, Harris A, Quint M, Radix A. Improved clinical outcomes in transgender and gender diverse primary care patients receiving gender-affirming care: Findings from the LEGACY Project. *World Professional Association for Transgender Health.* Montreal, Quebec, Canada. 2022.",
    "Kant JD, **Pletta DR**, MacNish M, Katz-Wise SL. Finding safety: Implications for clinical work with transgender and non-binary youth and their families from a qualitative study of the 2016-2018 U.S. political climate. *Transgender Professional Association for Transgender Health.* Virtual Meeting. 2021.",
    "Reisner SL, **Pletta DR**, Campbell J, Mayer KH, Potter J, Gonzalez A, Hughto JMW, Asquith A, Pardee D, Bhasin S, Keuroghlian A. Methods to ascertain suicide attempts in adult transgender and nonbinary patients: Implications for suicide prevention interventions in community health centers. *American Public Health Association.* Virtual Meeting. 2020.",
    "Reisner SL, **Pletta DR**, Campbell J, Mayer KH, Potter J, Gonzalez A, Hughto JMW, Asquith A, Pardee D, Radix A, Deutsch M, Keuroghlian A. Suicide attempts among transgender and nonbinary adult primary care patients in a community health center cohort. *American Public Health Association.* Virtual Meeting. 2020.",
    "Hughto JMW, Cahill S, McMahon J, Santostefano C, **Pletta DR**, Mimiaga MJ, Reisner SL. Negative transgender-related media messages are associated with adverse mental health outcomes in an online sample of transgender adults. *American Public Health Association.* Philadelphia, PA, USA. 2019.",
    "**Pletta DR**, Reisner SL. Individual- and partnership-level correlates of protective barrier use in a sample of transgender masculine individuals. *National LGBTQ Health Conference.* Atlanta, GA, USA. 2019.",
]

ROUNDTABLES = [
    "Asquith A, **Pletta DR**, Mayer KH, Campbell J, Potter J, Gonzalez A, Hughto JMW, Pardee DJ, Keuroghlian A, Radix A, Deutsch M, Reisner SL. Factors associated with pre-exposure prophylaxis (PrEP) prescriptions among transgender and non-binary patients in primary care at an urban community health center. *American Public Health Association.* Virtual Meeting. 2020.",
    "Hughto JMW, Reisner SL, Cahill S, Santostefano C, McMahon J, **Pletta DR**, Mimiaga MJ. Understanding facilitators and barriers to pre-exposure prophylaxis (PrEP) use among PrEP-naïve and PrEP-experienced transgender adults. *American Public Health Association.* Philadelphia, PA, USA. 2019.",
    "Hammack PL, **Pletta DR**, Schindler A. LGBTQ youth and community climate toward sexual and gender identity development in California. *American Psychological Association.* Denver, CO, USA. 2016.",
]

POSTERS = [
    "Balkan E, Babbs G, Meyers DJ, Kelly P, Yee K, **Pletta DR**, Shireman TI, Alpert A, Hughto JMW. Prevalence of gender-affirming surgery for transgender and gender diverse Medicare beneficiaries from 2016-2020. *AcademyHealth.* Baltimore, MD, USA. 2024.",
    "Quint M, **Pletta DR**, Radix A, Deutsch MB, Campbell J, Harris A, Mayer KH, Potter J, Asquith A, Pardee DJ, Esquivel B, Guerra A, Reisner SL. Binding and tucking practices in a cohort of transgender and gender diverse adult community health center patients: Findings from the LEGACY Project. *World Professional Association for Transgender Health.* Montreal, Quebec, Canada. 2022.",
    "**Pletta DR**, Kant JD, Ehrensaft D, MacNish M, Cahill S, Katz-Wise SL. How the 2016 United States presidential election affected families with transgender and nonbinary adolescents in New England: A qualitative study. *American Public Health Association.* Virtual Meeting. 2020.",
    "Kant JD, **Pletta DR**, Katz-Wise SL. Integrating family systems theory into thematic analysis of interviews with families of transgender youth. *LGBT Health Week, Boston Children’s Hospital / Harvard Medical School.* Boston, MA, USA. 2020.",
    "**Pletta DR**. Sexual orientation disparities in human papillomavirus (HPV) vaccination. *Sexual Orientation and Gender Identity and Expression (SOGIE) Working Group, Boston Children’s Hospital & Harvard T.H. Chan School of Public Health.* Boston, MA, USA. 2019.",
    "**Pletta DR**, Katz-Wise SL, Post J, Thomson K. Creating a safe space: Evaluating the effectiveness of Safe Zone trainings in improving gender and sexuality awareness at Boston Children’s Hospital. *Health Professionals Education Poster Session, Boston Children’s Hospital.* Boston, MA, USA. 2019.",
    "**Pletta DR**, Katz-Wise SL, Post J, Thomson K. Creating a safe space: Evaluating the effectiveness of Safe Zone trainings in improving gender and sexuality awareness at Boston Children’s Hospital. *LGBTQ Health Awareness Week, Boston Children’s Hospital.* Boston, MA, USA. 2019.",
]

# ------------------------------------------------------ TEACHING EXPERIENCE
TEACHING = [
    ("Harvard T.H. Chan School of Public Health", "Boston, MA",
     "Graduate Teaching Fellow, HIV Interventions: Rationale, Design, and Evaluation", "2023",
     ["Graduate lecture (12 students)"]),
    ("Harvard T.H. Chan School of Public Health", "Boston, MA",
     "Graduate Teaching Fellow, Principles of Social and Behavioral Research", "2022",
     ["Graduate lecture (50 students) and lab (~15 students)"]),
    ("Harvard T.H. Chan School of Public Health", "Boston, MA",
     "Graduate Teaching Assistant, Reproductive Health, Rights, and Justice", "2021",
     ["Graduate lecture (17 students)"]),
    ("Indiana University School of Public Health", "Bloomington, IN",
     "Graduate Teaching Fellow, Introduction to Public Health", "2016",
     ["Undergraduate lecture (~60 students)"]),
    ("University of California, Santa Cruz", "Santa Cruz, CA",
     "Undergraduate Co-Instructor, Social Justice and Community Workshop", "2013",
     ["Undergraduate workshop (~25 students)"]),
    ("University of California, Santa Cruz", "Santa Cruz, CA",
     "Undergraduate Instructional Assistant, Introduction to Psychology", "2013",
     ["Undergraduate lecture (~300 students); co-taught section (~25 students)"]),
    ("University of California, Santa Cruz", "Santa Cruz, CA",
     "Undergraduate Instructional Assistant, College Ten Core: Social Justice and Community", "2012",
     ["Undergraduate lecture (~25 students)"]),
    ("University of California, Santa Cruz", "Santa Cruz, CA",
     "Writing Tutor, Writing Program", "2012-2013",
     ["Individual and group tutoring (~25 students); training in pedagogical grammar, English composition, and English as a Second Language (ESL) instruction"]),
]

INVITED_TEACHING = [
    "**Pletta DR**. Assessing community climate for sexual and gender minority youth: A mixed-methods approach. Guest lecture, graduate course “Principles of Social and Behavioral Research.” *Harvard T.H. Chan School of Public Health*, Boston, MA. 2022.",
    "**Pletta DR**. LGBTQ+ adoption panel. Guest lecture, graduate course “Reproductive Health, Rights, and Justice.” *Harvard T.H. Chan School of Public Health*, Boston, MA. 2021.",
    "**Pletta DR**, Kant JD, Godwin EG, Katz-Wise SL. Politics at the dinner table: Impact of the 2016 presidential election on families with transgender and nonbinary teens in New England. *Sexual Orientation and Gender Identity and Expression (SOGIE) Working Group, Boston Children’s Hospital / Harvard Medical School / Harvard T.H. Chan School of Public Health*, Boston, MA. 2020.",
    "**Pletta DR**. LGBTQ+ health across the life course. Recorded guest lecture, graduate epidemiology course. *College of Natural and Health Sciences, University of Northern Colorado*, Greeley, CO. 2020.",
    "**Pletta DR**. Emerging topics in epidemiology: LGBTQ+ health across the life course. Invited guest lecture, graduate epidemiology course. *College of Natural and Health Sciences, University of Northern Colorado*, Greeley, CO. 2019.",
    "**Pletta DR**. Conceptualizations of transitioning among gender nonbinary and gender fluid young adults. *Sexual Orientation and Gender Identity and Expression (SOGIE) Working Group, Boston Children’s Hospital / Harvard Medical School / Harvard T.H. Chan School of Public Health*, Boston, MA. 2018.",
]

# ---------------------------------- LOCAL, NATIONAL & INTERNATIONAL SERVICE
# (heading, location or scope, committee/role line, dates, host institution)
SERVICE = [
    ("Member", "Ann Arbor, MI",
     "Organizational Culture and Belonging Committee", "2026",
     "Department of Epidemiology, University of Michigan School of Public Health"),
    ("Judge", "International",
     "Consortium for Mathematics and Its Applications (COMAP)", "2026",
     None),
    ("California Institute of Integral Studies", "San Francisco, CA",
     "Lead Curriculum Consultant, Public Health Analysis Track", "2024-2025",
     "Master of Science in Critical Sexuality Studies"),
    ("Invited Member", "Ann Arbor, MI",
     "Peer Review Committee for the Harburg Award", "2025",
     "Center for Social Epidemiology and Population Health, University of Michigan School of Public Health"),
    ("Invited Member", "Boston, MA",
     "Sexual Orientation and Gender Identity and Expression (SOGIE) Working Group", "2017-2024",
     "Boston Children’s Hospital / Harvard Medical School / Harvard T.H. Chan School of Public Health"),
    ("Abstract Reviewer", "National",
     "LGBT Caucus of Public Health Professionals", "2019",
     "American Public Health Association (APHA)"),
    ("Administrator, Terminology Chapter", "International",
     "Standards of Care, Version 8", "2019",
     "World Professional Association for Transgender Health (WPATH)"),
    ("Member", "Boston, MA",
     "LGBT Rainbow Consortium for Sexual and Gender Diversity", "2018",
     "Boston Children’s Hospital / Harvard Medical School"),
]

# ------------------------------------------------------ EDITORIAL ACTIVITIES
AD_HOC_JOURNALS = [
    "Addiction Science and Clinical Practice",
    "Advances in Patient-Reported Outcomes",
    "AIDS and Behavior",
    "AIDS Care",
    "American Journal of Epidemiology",
    "Digital Health",
    "Journal of Homosexuality",
    "LGBT Health",
    "PLoS One",
    "Psychology of Sexual Orientation and Gender Diversity",
    "Public Health Reports",
    "Sexuality Research and Social Policy",
    "Social Science & Medicine",
    "Stigma and Health",
    "Transgender Health",
]

# ------------------------------------- PROFESSIONAL SOCIETIES & ORGANIZATIONS
SOCIETIES = [
    ("Member, American Statistical Association (ASA)", "2025-Present"),
    ("Member, Society for Epidemiologic Research (SER)", "2025-Present"),
    ("Member, World Professional Association for Transgender Health (WPATH)", "2018-Present"),
    ("Member, American Public Health Association (APHA)", "2018-Present"),
    ("Member, International Epidemiological Association (IEA)", "2018"),
    ("Member, Association for Gender Affirming Professionals (AGAP)", "2017-2019"),
    ("Member, International Society for Political Psychology (ISPP)", "2016-2017"),
    ("Invited Member, Golden Key International Honour Society", "2014"),
    ("Invited Member, Psi Chi International Honor Society in Psychology", "2013"),
    ("Invited Member, National Society of Collegiate Scholars", "2012"),
]

# ----------------------------------------------------- SCIENTIFIC TRAININGS
# (title, location, host, date)
TRAININGS = [
    ("Data and AI Intensive Research with Rigor and Reproducibility (DAIR3) Bootcamp", "Ann Arbor, MI",
     "Michigan Institute for Data & AI in Society, University of Michigan", "2026"),
    ("Transition to First R01 Workshop", "Ann Arbor, MI",
     "Institute for Healthcare Policy & Innovation (IHPI), University of Michigan", "2026"),
    ("K Writing Workshop", "Ann Arbor, MI",
     "Institute for Healthcare Policy & Innovation (IHPI), University of Michigan", "2026"),
    ("NIH Pre-Conference Workshop", "Atlanta, GA",
     "National LGBTQ Health Conference, Emory University", "2019"),
]
