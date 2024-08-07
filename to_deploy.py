import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import flet as ft
except ImportError:
    install("flet")
    import flet as ft

try:
    import nest_asyncio
except ImportError:
    install("nest_asyncio")
    import nest_asyncio

import pandas as pd
import numpy as np

nest_asyncio.apply()

stip = pd.read_csv('/Users/henriquerodrigues/Desktop/OECD/Database/STIP_Survey.csv', sep='|', encoding='utf-8', na_values=['', ' ', 'NaN'])
stip = stip.iloc[1:]

dict_themes = {
    "TH102": "Government capabilities for net zero transitions",
    "TH103": "Net zero transitions in transport and mobility",
    "TH104": "Net zero transitions in food and agriculture",
    "TH105": "Cross-sectoral policies for net zero",
    "TH106": "Digital transformation of research-performing organisations",
    "TH107": "Open and enhanced access to publications",
    "TH108": "Open and enhanced access to research data",
    "TH109": "Research security",
    "TH13": "STI plan or strategy",
    "TH14": "Strategic policy intelligence",
    "TH15": "Evaluation and impact assessment",
    "TH18": "Public research strategies",
    "TH19": "Competitive research funding",
    "TH20": "Non-competitive research funding",
    "TH21": "Research integrity and reproducibility",
    "TH22": "Structural change in the public research system",
    "TH23": "High-risk high-reward research",
    "TH24": "Research and technology infrastructures",
    "TH25": "Internationalisation in public research",
    "TH26": "Cross-disciplinary research",
    "TH27": "Third-party funding",
    "TH30": "Business innovation policy strategies",
    "TH31": "Financial support to business R&D and innovation",
    "TH32": "Non-financial support to business R&D and innovation",
    "TH33": "Stimulating demand for innovation and market creation",
    "TH34": "Entrepreneurship capabilities and culture",
    "TH35": "Targeted support to SMEs and young innovative enterprises",
    "TH36": "Foreign direct investment",
    "TH38": "Access to finance for innovation",
    "TH41": "Knowledge exchange and co-creation strategies",
    "TH42": "Collaborative research and innovation",
    "TH43": "Commercialisation of public research results",
    "TH44": "Inter-sectoral mobility",
    "TH46": "Intellectual property rights in public research",
    "TH47": "Cluster policies",
    "TH50": "STI human resources strategies",
    "TH51": "STEM skills",
    "TH52": "Doctoral and postdoctoral researchers",
    "TH53": "Research careers",
    "TH54": "Equity, diversity and inclusion (EDI)",
    "TH55": "International mobility of human resources",
    "TH58": "Research and innovation for society strategy",
    "TH61": "Research and innovation for developing countries",
    "TH63": "International STI governance policy",
    "TH65": "Multi-stakeholder engagement",
    "TH66": "Science, technology and innovation culture",
    "TH82": "Digital transformation of firms",
    "TH89": "Ethics of emerging technologies",
    "TH9": "Horizontal policy coordination",
    "TH91": "Mission-oriented innovation policies",
    "TH92": "Net zero transitions in energy"}

dict_groups = {
    'TG20': 'Higher education institutes',
    'TG21': 'Public research institutes',
    'TG22': 'Private research and development lab',
    'TG9': 'Established researchers',
    'TG11': 'Postdocs and other early-career researchers',
    'TG41': 'Programme managers and other research support staff',
    'TG10': 'Undergraduate and master students',
    'TG38': 'Secondary education students',
    'TG12': 'PhD students',
    'TG13': 'Teachers',
    'TG29': 'Firms of any size',
    'TG30': 'Micro-enterprises',
    'TG31': 'SMEs',
    'TG32': 'Large firms',
    'TG33': 'Multinational enterprises',
    'TG25': 'Firms of any age',
    'TG26': 'Nascent firms (0 to less than 1 year old)',
    'TG27': 'Young firms (1 to 5 years old)',
    'TG28': 'Established firms (more than 5 years old)',
    'TG34': 'Incubators, accelerators, science parks or technoparks',
    'TG35': 'Technology transfer offices',
    'TG36': 'Industry associations',
    'TG37': 'Academic societies / academies',
    'TG42': 'Non-governmental organisations (NGOs)',
    'TG40': 'International entity',
    'TG23': 'National government',
    'TG24': 'Subnational government',
    'TG18': 'Entrepreneurs',
    'TG17': 'Private investors',
    'TG19': 'Labour force in general',
    'TG14': 'Women',
    'TG15': 'Disadvantaged and excluded groups',
    'TG16': 'Civil society'}

dict_inst = {
    "PI024": "Strategies, agendas and plans",
    "PI030": "Creation or reform of governance structure or public body",
    "PI031": "Policy intelligence (e.g. evaluations, benchmarking and forecasts)",
    "PI025": "Formal consultation of stakeholders or experts",
    "PI026": "Horizontal STI coordination bodies",
    "PI033": "Regulatory oversight and ethical advice bodies",
    "PI027": "Standards and certification for technology development and adoption",
    "PI028": "Public awareness campaigns and other outreach activities",
    "PI006": "Institutional funding for public research",
    "PI007": "Project grants for public research",
    "PI008": "Grants for business R&D and innovation",
    "PI009": "Centres of excellence grants",
    "PI010": "Procurement programmes for R&D and innovation",
    "PI011": "Fellowships and postgraduate loans and scholarships",
    "PI012": "Loans and credits for innovation in firms",
    "PI013": "Equity financing",
    "PI014": "Innovation vouchers",
    "PI015": "Tax or social contributions relief for firms investing in R&D and innovation",
    "PI016": "Tax relief for individuals supporting R&D and innovation",
    "PI029": "Debt guarantees and risk sharing schemes",
    "PI021": "Networking and collaborative platforms",
    "PI022": "Dedicated support to research and technical infrastructures",
    "PI023": "Information services and access to datasets",
    "PI017": "Technology extension and business advisory services",
    "PI032": "Science and technology regulation and soft law",
    "PI018": "Labour mobility regulation and incentives",
    "PI019": "Intellectual property regulation and incentives",
    "PI020": "Science and innovation challenges, prizes and awards"}

th_columns = [col for col in stip.columns if col.startswith('TH')]
tg_columns = [col for col in stip.columns if col.startswith('TG')]

stip[tg_columns] = stip[tg_columns].apply(pd.to_numeric, errors='coerce')
stip['TGroup_List'] = stip[tg_columns].apply(lambda row: [col for col in tg_columns if row[col] == 1], axis=1)
stip[th_columns] = stip[th_columns].apply(pd.to_numeric, errors='coerce')
stip['Theme_List'] = stip[th_columns].apply(lambda row: [col for col in th_columns if row[col] == 1], axis=1)

initiative_instruments = stip.groupby('InitiativeID')['InstrumentTypeCode'].apply(list).reset_index()

stip_merged = pd.merge(stip, initiative_instruments, on='InitiativeID', suffixes=('', '_List'))

stip_merged.rename(columns={'InstrumentTypeCode_List': 'Inst_List'}, inplace=True)

stip_init = stip_merged.drop_duplicates(subset='InitiativeID')

def conditional_probability(df, type_x, event_x, type_y, event_y):
    # Define column names based on the types
    type_x_col = 'TGroup_List' if type_x == 'target_groups' else 'Theme_List' if type_x == 'themes' else 'Inst_List'
    type_y_col = 'TGroup_List' if type_y == 'target_groups' else 'Theme_List' if type_y == 'themes' else 'Inst_List'
    
    # Find rows where event_x is in the list for type_x
    event_x_in_rows = df[df[type_x_col].apply(lambda x: event_x in x)]
    
    # Find rows within event_x_in_rows where event_y is in the list for type_y
    event_x_and_y_in_rows = event_x_in_rows[event_x_in_rows[type_y_col].apply(lambda x: event_y in x)]
    
    # Calculate counts
    x = len(event_x_in_rows)
    x_and_y = len(event_x_and_y_in_rows)
    
    # Calculate and return conditional probability
    if x == 0:
        return 0
    return x_and_y / x

def main(page: ft.Page):
    page.title = "Conditional Probability Calculator"

    # define list of category choices
    tg_items = sorted(dict_groups.items(), key=lambda item: item[1])
    tg_options = [ft.dropdown.Option(key, value) for key, value in tg_items]

    th_items = sorted(dict_themes.items(), key=lambda item: item[1])
    th_options = [ft.dropdown.Option(key, value) for key, value in th_items]

    inst_items = sorted(dict_inst.items(), key=lambda item: item[1])
    inst_options = [ft.dropdown.Option(key, value) for key, value in inst_items]

    # dropdown for selecting category type 1
    category1_dropdown = ft.Dropdown(label="Select Category Type 1", options=[
        ft.dropdown.Option("themes", "Themes"),
        ft.dropdown.Option("target_groups", "Target Groups"),
        ft.dropdown.Option("instruments", "Instruments")])

    # dropdown for selecting category 1 value
    category1_value_dropdown = ft.Dropdown(label="Select Category Value 1", options=[], visible=False)

    # dropdown for selecting category type 2
    category2_dropdown = ft.Dropdown(label="Select Category Type 2", options=[
        ft.dropdown.Option("themes", "Themes"),
        ft.dropdown.Option("target_groups", "Target Groups"),
        ft.dropdown.Option("instruments", "Instruments")], visible=True)

    # dropdown for selecting category 2 value 
    category2_value_dropdown = ft.Dropdown(label="Select Category Value 2", options=[], visible=False)

    result_text = ft.Text("Conditional Probability: ", size=16)

    def update_value_dropdown(choice, dropdown):
        # read category choice
        selected_category = choice
        # clear previous selection
        dropdown.options = []

        # update category value choice with correct name
        if selected_category == "themes":
            dropdown.options = th_options
            dropdown.label = "Select Theme"

        elif selected_category == "target_groups":
            dropdown.options = tg_options
            dropdown.label = "Select Target Group"

        elif selected_category == "instruments":
            dropdown.options = inst_options
            dropdown.label = "Select Instrument"

        dropdown.visible = True
        page.update()

    def on_category1_change(e):
        # make cat1 value choice appear after cat1 is selected
        update_value_dropdown(category1_dropdown.value, category1_value_dropdown)
        page.update()

    def on_category2_change(e):
        # make cat2 value choice appear ONLY after cat2 is selected
        page.update()
        update_value_dropdown(category2_dropdown.value, category2_value_dropdown)
        page.update()

    def calculate_prob(e):
        cat1_type = category1_dropdown.value
        cat1_value = category1_value_dropdown.value
        cat2_type = category2_dropdown.value
        cat2_value = category2_value_dropdown.value

        if cat1_type and cat1_value and cat2_type and cat2_value and cat1_value!=cat2_value:
            result = conditional_probability(stip_init, cat1_type, cat1_value, cat2_type, cat2_value) * 100
            result_text.value = f"Conditional Probability: {result:.2f}%"
        else:
            result_text.value = "Please select valid categories and values."
        page.update()

    # attach event handlers
    category1_dropdown.on_change = on_category1_change
    category2_dropdown.on_change = on_category2_change

    calculate_button = ft.ElevatedButton(text="Calculate", on_click=calculate_prob)

    # add components to the page
    page.add(category1_dropdown, category1_value_dropdown, category2_dropdown, category2_value_dropdown, calculate_button, result_text)

# run the app
ft.app(target=main, view=ft.AppView.WEB_BROWSER)