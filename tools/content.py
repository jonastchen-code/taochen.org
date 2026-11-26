# Page content for taochen.org. Source: CV Tao Chen_Oct2026.docx (Dropbox, modified 14 Oct 2026)
# and CV-Tao_CHEN_NTU_Nov2026.docx (keynote topics).
import html
E = lambda s: html.escape(str(s), quote=True)

SCHOLAR = "https://scholar.google.com/citations?user=NzpHEjkAAAAJ&amp;hl=en"
SSRN = "https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=952261"
ORCID_URL = "https://orcid.org/0000-0003-4110-0529"
NTU_PAGE = "https://personal.ntu.edu.sg/jtchen/"

HOME_DESC = ("Tao (Jonas) Chen is Provost's Chair Professor in Finance and Associate Professor in Finance at Nanyang Business School, NTU Singapore. "
             "His research covers sustainable finance; FinTech, AI, and finance; and how investors and monitors shape corporate policy.")

HOME_INTRO = """<p>Welcome. I am an associate professor in finance at Nanyang Business School. My research is in sustainable finance; FinTech, AI, and finance; and how investors and monitors shape corporate policy.</p>"""

STATS = [("5,687", "Citations"), ("20", "h-index"), ("10", "FT50 publications"), ("6", "UTD 24 publications"),
         ("1", "Nature Index publication"), ("Top 2%", "Stanford/Elsevier scientists")]
STATS_NOTE = ("Citations and h-index from Google Scholar, 26 November 2026. Journal lists: Financial Times 50, UT Dallas 24, Nature Index. "
              "Stanford/Elsevier list of the top 2% of scientists, 2024–2026.")

POSITIONS = [("2025–", "Provost’s Chair Professor in Finance, Nanyang Business School, NTU"),
             ("2020–", "Associate Professor (with tenure) in Finance, NTU"),
             ("2014–2020", "Assistant Professor in Finance, NTU")]
FELLOWSHIPS = [("2026–", "Fellow, Asian Bureau of Finance and Economic Research (ABFER)"),
             ("2024–", "Executive Committee and Fellow, NTU Teaching Excellence Academy (TEA)"),
             ("2020–", "Fellow, NTU Institute of Science and Technology for Humanity (NISTH)")]
EDUCATION = [("2014", "PhD in Finance, The Chinese University of Hong Kong"),
             ("2011", "MPhil in Finance, The Hong Kong University of Science and Technology"),
             ("2004", "BA in English and Finance, Beijing Foreign Studies University")]

PERSON = {"@type": "Person", "@id": "https://taochen.org/#person", "name": "Tao Chen", "alternateName": ["Tao (Jonas) Chen", "Jonas Chen", "Chen Tao"],
          "url": "https://taochen.org/", "image": "https://taochen.org/assets/img/tao-chen-720.jpg", "email": "mailto:jtchen@ntu.edu.sg",
          "jobTitle": ["Provost's Chair Professor in Finance", "Associate Professor in Finance"],
          "worksFor": {"@type": "CollegeOrUniversity", "name": "Nanyang Technological University", "department": {"@type": "Organization", "name": "Nanyang Business School"}},
          "alumniOf": [{"@type": "CollegeOrUniversity", "name": "The Chinese University of Hong Kong"},
                       {"@type": "CollegeOrUniversity", "name": "The Hong Kong University of Science and Technology"},
                       {"@type": "CollegeOrUniversity", "name": "Beijing Foreign Studies University"}],
          "knowsAbout": ["Sustainable finance", "ESG", "FinTech", "Artificial intelligence in finance", "Corporate finance", "Corporate governance"],
          "identifier": {"@type": "PropertyValue", "propertyID": "ORCID", "value": "0000-0003-4110-0529"},
          "sameAs": ["https://scholar.google.com/citations?user=NzpHEjkAAAAJ", SSRN, ORCID_URL, NTU_PAGE]}

def TEACHING_HTML(dated):
    courses = [("2026–", "EM6011 Financial Decision Making I — Global EMBA"),
               ("2020–", "FF6121 Investments — MSc Finance"),
               ("2017–2023", "BF2201 Investments — undergraduate core course"),
               ("2019–2023", "BF2100 Ethics in the Investment Profession — undergraduate"),
               ("2014–2016", "BF2207 International Finance — undergraduate core course")]
    phd = [("2026", "Yaqi Wang (supervisor) — Associate Professor, Dongbei University of Finance and Economics"),
           ("2023", "Chengyuan Qu (supervisor) — China Securities Regulatory Commission"),
           ("2019", "Li Zhang (co-supervisor) — Associate Professor, University of Science and Technology of China")]
    return f"""<section aria-labelledby="h-c"><h2 id="h-c">Courses at Nanyang Business School</h2>{dated([(y, E(t)) for y, t in courses])}</section>
<section aria-labelledby="h-r"><h2 id="h-r">Programme roles</h2>
{dated([("2023–", "Academic Director, MSc Finance programme"), ("2020–2022, 2025–", "PhD Programme Coordinator, Finance")])}</section>
<section aria-labelledby="h-p"><h2 id="h-p">Doctoral advising</h2>
<p>Graduated PhD students I supervised, with first placements:</p>
{dated([(y, E(t)) for y, t in phd])}
<p>I also serve on thesis committees in finance, economics and computer science at NTU, and as an external examiner. Prospective PhD students should apply through the <a href="https://www.ntu.edu.sg/business">Nanyang Business School</a> PhD programme in finance.</p></section>
<p>Teaching awards are listed on the <a href="/awards/">Awards</a> page.</p>"""

EDITORIAL = [("2022–", "Associate Editor, <cite>Financial Management</cite>"),  # FM first (Jonas, 15 Nov 2026)
             ("2025–", "Associate Editor, <cite>The British Accounting Review</cite>"),
             ("2023–", "Associate Editor, <cite>Journal of Business Research</cite>"),
             ("2023–", "Guest Editor, <cite>Pacific-Basin Finance Journal</cite>")]

def SERVICE_HTML(dated):
    ed = EDITORIAL
    prof = [("2026–", "Fellow, Asian Bureau of Finance and Economic Research (ABFER)"),
            ("2026", "Co-Chair, Financial Management Association (FMA) Asia/Pacific Conference"),
            ("2023–", "Vice President (Programs), Asian Finance Association"),
            ("2023–", "Co-Chair, Asian Finance Association Annual Conference"),
            ("2021–", "Board Member, Asian Finance Association"),
            ("2020–2023", "Co-Chair, Singapore Scholars Symposium")]
    univ = [("2026–", "Faculty Affiliate, Global Institute of Finance, Technology, and Society (GIFTS), NTU"),
            ("2024–", "Executive Committee and Fellow, NTU Teaching Excellence Academy"),
            ("2023–", "Academic Director, MSc Finance programme, Nanyang Business School"),
            ("2023–", "Academic Committee, Centre for Sustainable Finance Innovation"),
            ("2022–2025", "NTU Senator"),
            ("2021–", "NTU Teaching Council"),
            ("2020–2022, 2025–", "PhD Programme Coordinator, Finance, Nanyang Business School"),
            ("2020–", "Fellow, NTU Institute of Science and Technology for Humanity")]
    return f"""<section aria-labelledby="h-e"><h2 id="h-e">Editorial</h2>{dated(ed)}</section>
<section aria-labelledby="h-pr"><h2 id="h-pr">Professional associations and conferences</h2>{dated(prof)}
<p>Program committees: European Finance Association Annual Meeting; SFS Cavalcade Asia-Pacific; FMA Asia/Pacific Conference; American Marketing Association Winter Academic Conference, etc.</p></section>
<section aria-labelledby="h-u"><h2 id="h-u">University</h2>{dated(univ)}</section>
<section aria-labelledby="h-g"><h2 id="h-g">Grant review and refereeing</h2>
<p>Recent grant reviews for the Swiss National Science Foundation, the Research Grants Council of Hong Kong, the Hong Kong Monetary Authority / Hong Kong Institute for Monetary Research, etc.</p>
<p>Recent refereeing for journals including <cite>Review of Financial Studies</cite>, <cite>Management Science</cite>, <cite>The Accounting Review</cite>, <cite>Journal of Financial and Quantitative Analysis</cite>, <cite>Review of Finance</cite>, <cite>Contemporary Accounting Research</cite>, <cite>Research Policy</cite>, <cite>Journal of Public Economics</cite>, <cite>Journal of Development Economics</cite>, <cite>Journal of Corporate Finance</cite>, etc.</p></section>"""

def AWARDS_HTML(dated):
    research = [("2026", "Best Paper Award for Capital Markets, Craigs Investment Partners"),
                ("2026", "Best Paper Award for Investments, Institute of Finance Professionals New Zealand (INFINZ)"),
                ("2025", "Best Paper Award, 15th Financial Markets and Corporate Governance Conference"),
                ("2024", "Robert C. Witt Award, American Risk and Insurance Association"),
                ("2024", "Top Finalist, Nanyang Research Award, NTU"),
                ("2023", "Best Paper Award, Marketing Strategy track, AMA Winter Academic Conference"),
                ("2022", "NBS Research Excellence Award, Nanyang Business School"),
                ("2022", "Best Paper Award, 6th Academy of Finance and Accounting Annual Conference"),
                ("2022", "Best Paper Award, Maritime Silk Road Accounting and Finance Meeting"),
                ("2022", "Best Paper Award, International Accounting Section of the American Accounting Association Midyear Meeting"),
                ("2022", "Best Paper Award, Industrial Securities Co., Ltd."),
                ("2020", "Pioneer Award, Peak Initiative, 2019–2020 Digital Finance Open Research Plan (Alibaba)"),
                ("2019", "Best Paper Award, Asian Finance Association Conference"),
                ("2019", "Finalist, Best Paper Award in Corporate Finance, FMA Asia/Pacific Conference"),
                ("2014", "Outstanding Paper Award, Annual Conference on Asia-Pacific Financial Markets, Korean Securities Association"),
                ("2014", "Semi-finalist, Best Paper Award in Corporate Finance, Financial Management Association"),
                ("2013", "Semi-finalist, Best Paper Award in Corporate Finance, Financial Management Association")]
    teaching = [("2024", "Nanyang Education Award (College), NTU"),
                ("2023", "Teacher of the Year Award, MSc Finance programme, NTU"),
                ("2022", "Nanyang Education Award (School), NTU"),
                ("2019", "NBS Teaching Excellence Award, Nanyang Business School")]
    honours = [("2024–2026", "Stanford/Elsevier list of the top 2% of scientists"),
               ("2026–", "Fellow, Asian Bureau of Finance and Economic Research (ABFER)"),
               ("2024–", "Executive Committee and Fellow, NTU Teaching Excellence Academy (TEA)"),
               ("2020–", "Fellow, NTU Institute of Science and Technology for Humanity (NISTH)"),
               ("2016, 2018, 2024", "Visiting Research Fellowship, Hong Kong Monetary Authority"),
               ("2014", "CUHK Young Scholars Thesis Award, The Chinese University of Hong Kong")]
    service = [("2021", "Excellence in Reviewing Award, International Accounting Section, American Accounting Association")]
    f = lambda rows: dated([(y, E(t)) for y, t in rows])
    return f"""<section aria-labelledby="h-ra"><h2 id="h-ra">Research</h2>{f(research)}</section>
<section aria-labelledby="h-ta"><h2 id="h-ta">Teaching</h2>{f(teaching)}</section>
<section aria-labelledby="h-ho"><h2 id="h-ho">Honours and fellowships</h2>{f(honours)}</section>
<section aria-labelledby="h-sa"><h2 id="h-sa">Service</h2>{f(service)}</section>"""

def TALKS_HTML(dated):
    keynotes = [("Dec 2026", "2026 Massey Sustainable Finance Conference, Queenstown", "Sustainable Finance and Beyond: From Investors and Institutions to Real Impact"),
                ("Jan 2026", "10th China Accounting and Finance Conference, Hangzhou", "Sustainable Finance: ESG and ESG Investing"),
                ("Dec 2025", "2025 International Conference on Business and Finance, Ho Chi Minh City", "Sustainable Finance: ESG and ESG Investing"),
                ("Jan 2025", "9th China Accounting and Finance Conference, Wuhan", "Generative AI and Mutual Fund Investment"),
                ("Oct 2024", "10th Indonesian Finance Association International Conference, Jakarta", "Investment Research in Emerging Capital Markets"),
                ("Aug 2024", "2024 Accounting and Finance Summer School, Wuhan", "Sustainable Finance and FinTech"),
                ("Jul 2024", "2024 Accounting and Finance Workshop, Guangzhou", "FinTech Lending, Generative AI, and Mutual Funds: Evidence from FinTech Data in China"),
                ("Jul 2019", "2019 International Conference on Financial Markets, Jinan", "Finance and Firm Volatility"),
                ("Jun 2015", "2015 China Finance Annual Conference, Chengdu", "Financial Flexibility and Corporate Cash Policy")]
    seminars = [("2026", "Cornell University; Harvard University; MIT; Purdue University; University of New Mexico; The Chinese University of Hong Kong, Shenzhen"),
                ("2025", "Hong Kong Monetary Authority; Qilu University of Technology; Shandong Academy of Sciences; Jinan University"),
                ("2024", "Hong Kong Monetary Authority; University of Science and Technology of China; Zhongnan University of Economics and Law; Jinan University; Zhejiang University"),
                ("2023", "University of Macau; Jinan University"),
                ("2022", "Southern University of Science and Technology; Tianjin University; Nanjing Agricultural University; Jinan University; Jiangxi University of Finance and Economics; North China Electric Power University"),
                ("2021", "KAIST; Dongbei University of Finance and Economics; Nanjing Agricultural University; Xiamen University"),
                ("2020", "Sun Yat-sen University; Tianjin University; Nanjing Agricultural University; Jinan University"),
                ("2019", "University of New South Wales; Australian National University; University of Sydney; Wuhan University; Wuhan University of Technology; Jinan University; Shandong University"),
                ("2018", "Hong Kong Baptist University; Sun Yat-sen University; Xiamen University; University of Otago; Massey University; University of Sydney; Lanzhou University; Jinan University"),
                ("2017", "University of Sydney; University of International Business and Economics; Zhejiang University"),
                ("2016", "Xiamen University; Massey University"),
                ("2015", "Southwestern University of Finance and Economics; Zhejiang University"),
                ("2014", "University of New South Wales; Nanyang Technological University; Hong Kong Polytechnic University; The Chinese University of Hong Kong; Xiamen University"),
                ("2012", "The Chinese University of Hong Kong; The Hong Kong University of Science and Technology")]
    k = dated([(d, f"{E(v)}<br><span class=\"meta\">{E(t)}</span>") for d, v, t in keynotes])
    return f"""<section aria-labelledby="h-k"><h2 id="h-k">Keynote speeches</h2>{k}</section>
<section aria-labelledby="h-s"><h2 id="h-s">Invited seminars</h2>{dated([(y, E(t)) for y, t in seminars])}</section>"""

def MEDIA_HTML(dated):
    # (date, title, outlet, link, video); links as on personal.ntu.edu.sg/jtchen (checked 2026-11-15)
    NTU = "https://personal.ntu.edu.sg/jtchen/"
    op = [("Sep 2026", "“Getting Tech Finance Right: Lessons from Singapore’s Stock Market Support for Hard Tech” (with Xiaoyu Chen)", "Tsinghua Financial Review", "", ""),
          ("12 Dec 2023", "“The Social Cost of Investor Distraction: Evidence from Institutional Cross-Blockholding”", "Harvard Law School Forum on Corporate Governance", "https://corpgov.law.harvard.edu/2023/12/12/the-social-cost-of-investor-distraction-evidence-from-institutional-cross-blockholding/", ""),
          ("26 Dec 2021", "“Commentary: Binance’s exchange closure in Singapore could usher in more regulations on cryptocurrencies”", "CNA", "https://www.channelnewsasia.com/commentary/binance-withdraws-application-singapore-cryptocurrency-cryptocurrencies-mas-monetary-authority-singapore-2399571", "")]
    # TV: (date, title, outlet, article, YouTube id). Dates as on Jonas's NTU page.
    tv = [("27 Mar 2026", "“Fuel costs rise $3,000 a month for businesses”", "8world, Frontline", "https://www.8world.com/in-depth/frontline/fuel-costs-rise-3000-a-month-hit-businesses-3098591", "vVB1ZWZte3Y"),
          ("27 Mar 2026", "“How one driver saves a thousand dollars a year on fuel”", "8world, Frontline", "https://www.8world.com/in-depth/frontline/how-man-saves-thousand-a-year-on-fuel-3098581", "zqSTdNNub9M"),
          ("27 Mar 2026", "“Diesel overtakes petrol in price”", "8world, Frontline", "https://www.8world.com/in-depth/frontline/diesel-overtakes-petrol-price-3098571", "kevciVcR4sQ"),
          ("4 May 2023", "“US Fed interest rate hike”", "Channel 8, Hello Singapore", "", "eTQQfWdM-GU"),
          ("26 May 2022", "“Inflation”", "Channel 8, Hello Singapore", "", "wFQHH671PqQ"),
          ("28 Apr 2022", "“Economic outlook”", "Channel 8, Hello Singapore", "", "cnA43TXGVIo@122"),
          ("28 Apr 2022", "“Q1 labour market advance release”", "Channel 8 News", "", "Ljwg4ugyMZQ")]
    quoted = [("30 Jul 2023", "On investment advice from financial influencers", "Lianhe Zaobao", "https://www.zaobao.com.sg/finance/singapore/story20230730-1418143", ""),
              ("15 Jun 2023", "“Can the Asean Taxonomy help achieve the region's sustainability ambitions?”", "Eco-Business", "https://www.eco-business.com/news/can-the-asean-taxonomy-help-achieve-the-regions-sustainability-ambitions/", ""),
              ("25 Jan 2023", "On the Global Financial Centres Index, Singapore and Hong Kong", "Lianhe Zaobao", NTU + "Lianhe_Zaobao_Prof%20Chen%20on%20HK-SG.pdf", ""),
              ("21 Jul 2022", "“Why borrowing money to fund insurance policies can prove detrimental”", "The Straits Times", NTU + "Funding%20insurance%20policies%20with%20loans%20could%20prove%20detrimental_ST%2022%20Jul.pdf", ""),
              ("18 Apr 2022", "“Asean logistics sector could get tech boost as Alibaba unit looks to region for growth”", "The Business Times", "https://www.businesstimes.com.sg/international/asean/asean-logistics-sector-could-get-tech-boost-alibaba-unit-looks-region-growth", ""),
              ("13 Mar 2022", "“As inflation rises, how much more are you paying for your groceries?”", "CNA", "https://www.channelnewsasia.com/singapore/groceries-cost-prices-supermarkets-inflation-eggs-2551636", ""),
              ("3 Mar 2022", "“Higher prices for petrol, electricity and food: How Russia's invasion of Ukraine might affect people in Singapore”", "CNA", "https://www.channelnewsasia.com/singapore/ukraine-invasion-russia-higher-prices-petrol-food-electricity-singapore-2532281", ""),
              ("20 Jan 2022", "“Crypto curbs: Industry players say ad ban not the only way to protect retail investors in Singapore”", "CNA", "https://www.channelnewsasia.com/singapore/mas-no-cryptocurrency-advertisement-marketing-protect-retail-investors-2447321", ""),
              ("25 May 2016", "On the BSI closure and Singapore as a financial centre", "Lianhe Zaobao", NTU + "LHZB_162505_2_Singapores%20position%20as%20a%20financial%20hub%20can%20be%20strengthened%20by%20shutting%20down%20BSI%20Bank.pdf", "")]
    research = [("Sep 2019", "“Institutional investors drive (and seek) firm CSR”", "Network for Business Sustainability", "https://www.nbs.net/articles/report-from-the-research-frontier-september-2019", ""),
                ("17 Mar 2013", "“Innovation gone bad requires regulation”", "Financial Times", "https://www.ft.com/content/5ad61394-8ca2-11e2-8ee0-00144feabdc0", ""),
                ("22 Jan 2013", "“Financial innovation: The bright and the dark sides”", "All About Finance, World Bank", "https://blogs.worldbank.org/en/allaboutfinance/financial-innovation-the-bright-and-the-dark-sides", ""),
                ("2 Oct 2012", "“Financial innovation: The bright and the dark sides”", "VoxEU", "https://cepr.org/voxeu/columns/financial-innovation-bright-and-dark-sides", "")]
    def row(t, o, link, video):
        h = f'<a href="{E(link)}">{E(t)}</a>' if link else (f'<a href="{E(video)}">{E(t)}</a>' if video else E(t))
        h += f", <cite>{E(o)}</cite>"
        if link.endswith(".pdf"): h += " (PDF)"
        if video: h += f' · <a href="{E(video)}" class="video">Watch video</a>' if link else " (video)"
        return h
    def tvrow(t, o, link, vid):
        vid, _, start = vid.partition("@")
        url = f"https://www.youtube.com/watch?v={vid}" + (f"&t={start}s" if start else "")
        icon = ('<svg class="yt-ico" viewBox="0 0 28 20" width="21" height="15" aria-hidden="true" focusable="false">'
                '<rect width="28" height="20" rx="5" fill="#d42020"/><path d="M11 5.5v9l8-4.5z" fill="#fff"/></svg>')
        h = f'<a href="{E(url)}">{E(t)}</a>, <cite>{E(o)}</cite> <a class="yt" href="{E(url)}" aria-label="Watch on YouTube">{icon}</a>'
        if link: h += f' · <a href="{E(link)}">Article</a>'
        return h
    f = lambda rows: dated([(d, row(t, o, l, v)) for d, t, o, l, v in rows])
    ftv = lambda rows: dated([(d, tvrow(t, o, l, v)) for d, t, o, l, v in rows])
    return f"""<section aria-labelledby="h-o"><h2 id="h-o">Commentary</h2>{f(op)}</section>
<section aria-labelledby="h-tv"><h2 id="h-tv">Television interviews</h2>{ftv(tv)}</section>
<section aria-labelledby="h-q"><h2 id="h-q">Quoted in the news</h2>{f(quoted)}</section>
<section aria-labelledby="h-rc"><h2 id="h-rc">Coverage of research</h2>{f(research)}</section>"""


# News box on Home (idea from blogs.ntu.edu.sg/shirleysho, Jonas 15 Nov 2026). Newest first, 3–5 items.
# (date, html text). Facts taken from the site's own lists (papers, awards, fellowships, keynotes, media).
NEWS = [("Dec 2026", 'Keynote, 2026 Massey Sustainable Finance Conference, Queenstown: “Sustainable Finance and Beyond: From Investors and Institutions to Real Impact” <a href="/talks/">(talks)</a>'),
        ("2026", 'New paper in <cite>Nature Climate Change</cite>: <a href="/research/ecological-integrity-avoided-deforestation-ncc-2026/">“Ecological integrity of avoided deforestation projects”</a>'),
        ("2026", 'Became a Fellow of the Asian Bureau of Finance and Economic Research (ABFER)'),
        ("2026", 'Best Paper Award for Capital Markets, Craigs Investment Partners <a href="/awards/">(awards)</a>'),
        ("2026", 'Best Paper Award for Investments, Institute of Finance Professionals New Zealand (INFINZ) <a href="/awards/">(awards)</a>'),
        ("Mar 2026", 'On 8world <cite>Frontline</cite>, on fuel costs for businesses and drivers <a href="/media/">(media)</a>'),
        ("Jan 2026", 'Keynote, 10th China Accounting and Finance Conference, Hangzhou: “Sustainable Finance: ESG and ESG Investing” <a href="/talks/">(talks)</a>')]
