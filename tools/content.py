# Page content for taochen.org. Source: CV Tao Chen_Oct2026.docx (Dropbox, modified 14 Oct 2026)
# and CV-Tao_CHEN_NTU_June2026.docx (keynote topics).
import html
E = lambda s: html.escape(str(s), quote=True)

SCHOLAR = "https://scholar.google.com/citations?user=NzpHEjkAAAAJ&amp;hl=en"
SSRN = "https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=952261"
ORCID_URL = "https://orcid.org/0000-0003-4110-0529"
NTU_PAGE = "https://personal.ntu.edu.sg/jtchen/"

HOME_DESC = ("Tao (Jonas) Chen is Provost's Chair Professor in Finance and Associate Professor of Finance at Nanyang Business School, NTU Singapore. "
             "His research covers sustainable finance; FinTech, AI, and finance; and how investors and monitors shape corporate policy.")

HOME_INTRO = """<p>Welcome. I am an associate professor of finance at Nanyang Business School. My research is in sustainable finance; FinTech, AI, and finance; and how investors and monitors shape corporate policy.</p>"""

STATS = [("5,500+", "Citations"), ("20", "h-index"), ("10", "FT50 publications"), ("6", "UTD 24 publications"),
         ("1", "Nature Index publication"), ("Top 2%", "Stanford/Elsevier scientists")]
STATS_NOTE = ("Citations and h-index from Google Scholar, October 2026. Journal lists: Financial Times 50, UT Dallas 24, Nature Index. "
              "Stanford/Elsevier list of the top 2% of scientists, 2025.")

POSITIONS = [("2025–", "Provost’s Chair Professor in Finance, Nanyang Business School, NTU"),
             ("2020–", "Associate Professor (with tenure) in Finance, NTU"),
             ("2014–2020", "Assistant Professor in Finance, NTU")]
EDUCATION = [("2014", "PhD in Finance, The Chinese University of Hong Kong"),
             ("2011", "MPhil in Finance, The Hong Kong University of Science and Technology"),
             ("2004", "BA in English and Finance, Beijing Foreign Studies University")]

PERSON = {"@type": "Person", "@id": "https://taochen.org/#person", "name": "Tao Chen", "alternateName": ["Tao (Jonas) Chen", "Jonas Chen", "Chen Tao"],
          "url": "https://taochen.org/", "email": "mailto:jtchen@ntu.edu.sg",
          "jobTitle": ["Provost's Chair Professor in Finance", "Associate Professor of Finance"],
          "worksFor": {"@type": "CollegeOrUniversity", "name": "Nanyang Technological University", "department": {"@type": "Organization", "name": "Nanyang Business School"}},
          "alumniOf": [{"@type": "CollegeOrUniversity", "name": "The Chinese University of Hong Kong"},
                       {"@type": "CollegeOrUniversity", "name": "The Hong Kong University of Science and Technology"},
                       {"@type": "CollegeOrUniversity", "name": "Beijing Foreign Studies University"}],
          "knowsAbout": ["Sustainable finance", "ESG", "FinTech", "Artificial intelligence in finance", "Corporate finance", "Corporate governance"],
          "identifier": {"@type": "PropertyValue", "propertyID": "ORCID", "value": "0000-0003-4110-0529"},
          "sameAs": ["https://scholar.google.com/citations?user=NzpHEjkAAAAJ", SSRN, ORCID_URL, NTU_PAGE]}

def TEACHING_HTML(dated):
    courses = [("2020–", "FF6121 Investments — MSc Finance"),
               ("2017–", "BF2201 Investments — undergraduate core course"),
               ("2019–", "BF2100 Ethics in the Investment Profession — undergraduate"),
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

def SERVICE_HTML(dated):
    ed = [("2025–", "Associate Editor, <cite>The British Accounting Review</cite>"),
          ("2023–", "Associate Editor, <cite>Journal of Business Research</cite>"),
          ("2022–", "Associate Editor, <cite>Financial Management</cite>"),
          ("2023–", "Guest Editor, <cite>Pacific-Basin Finance Journal</cite>")]
    prof = [("2026–", "Fellow, Asian Bureau of Finance and Economic Research (ABFER)"),
            ("2026–", "Co-Chair, Financial Management Association (FMA) Asia/Pacific Conference"),
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
<p>Program committees: European Finance Association Annual Meeting; SFS Cavalcade Asia-Pacific; FMA Asia/Pacific Conference; American Marketing Association Winter Academic Conference.</p></section>
<section aria-labelledby="h-u"><h2 id="h-u">University</h2>{dated(univ)}</section>
<section aria-labelledby="h-g"><h2 id="h-g">Grant review and refereeing</h2>
<p>Grant reviewer for the Swiss National Science Foundation, the Research Grants Council of Hong Kong, and the Hong Kong Monetary Authority / Hong Kong Institute for Monetary Research.</p>
<p>Referee for journals including <cite>Review of Financial Studies</cite>, <cite>Management Science</cite>, <cite>The Accounting Review</cite>, <cite>Journal of Financial and Quantitative Analysis</cite>, <cite>Review of Finance</cite>, <cite>Contemporary Accounting Research</cite>, <cite>Research Policy</cite>, <cite>Journal of Public Economics</cite>, <cite>Journal of Development Economics</cite> and <cite>Journal of Corporate Finance</cite>.</p></section>"""

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
    honours = [("2025", "Stanford/Elsevier list of the top 2% of scientists"),
               ("2016, 2018, 2024", "Visiting Research Fellowship, Hong Kong Monetary Authority"),
               ("2014", "CUHK Young Scholars Thesis Award, The Chinese University of Hong Kong")]
    service = [("2021", "Excellence in Reviewing Award, International Accounting Section, American Accounting Association")]
    f = lambda rows: dated([(y, E(t)) for y, t in rows])
    return f"""<section aria-labelledby="h-ra"><h2 id="h-ra">Research</h2>{f(research)}</section>
<section aria-labelledby="h-ta"><h2 id="h-ta">Teaching</h2>{f(teaching)}</section>
<section aria-labelledby="h-ho"><h2 id="h-ho">Honours and fellowships</h2>{f(honours)}</section>
<section aria-labelledby="h-sa"><h2 id="h-sa">Service</h2>{f(service)}</section>"""

def TALKS_HTML(dated):
    keynotes = [("Jan 2026", "10th China Accounting and Finance Conference, Hangzhou", "Sustainable Finance: ESG and ESG Investing"),
                ("Dec 2025", "2025 International Conference on Business and Finance, Ho Chi Minh City", "Sustainable Finance: ESG and ESG Investing"),
                ("Jan 2025", "9th China Accounting and Finance Conference, Wuhan", "Generative AI and Mutual Fund Investment"),
                ("Oct 2024", "10th Indonesian Finance Association International Conference, Jakarta (plenary)", "Investment Research in Emerging Capital Markets"),
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
    op = [("12 Dec 2023", "“The Social Cost of Investor Distraction: Evidence from Institutional Cross-Blockholding”", "Harvard Law School Forum on Corporate Governance"),
          ("26 Dec 2021", "“Commentary: Binance’s exchange closure in Singapore could usher in more regulations on cryptocurrencies”", "CNA")]
    tv = [("27 Mar 2026", "Fuel costs; diesel and petrol prices; saving on fuel (three segments)", "8world, Frontline"),
          ("4 May 2023", "US Federal Reserve interest rate rise", "Channel 8, Hello Singapore"),
          ("26 May 2022", "Inflation", "Channel 8, Hello Singapore"),
          ("28 Apr 2022", "Economic outlook; first-quarter labour market release", "Channel 8")]
    quoted = [("30 Jul 2023", "On investment advice from financial influencers", "Lianhe Zaobao"),
              ("15 Jun 2023", "“Can the Asean Taxonomy help achieve the region's sustainability ambitions?”", "Eco-Business"),
              ("25 Jan 2023", "On the Global Financial Centres Index, Singapore and Hong Kong", "Lianhe Zaobao"),
              ("21 Jul 2022", "“Why borrowing money to fund insurance policies can prove detrimental”", "The Straits Times"),
              ("18 Apr 2022", "“Asean logistics sector could get tech boost as Alibaba unit looks to region for growth”", "The Business Times"),
              ("13 Mar 2022", "“As inflation rises, how much more are you paying for your groceries?”", "CNA"),
              ("3 Mar 2022", "“Higher prices for petrol, electricity and food: How Russia's invasion of Ukraine might affect people in Singapore”", "CNA"),
              ("20 Jan 2022", "“Crypto curbs: Industry players say ad ban not the only way to protect retail investors in Singapore”", "CNA"),
              ("25 May 2016", "On the BSI closure and Singapore as a financial centre", "Lianhe Zaobao")]
    research = [("Sep 2019", "“Institutional investors drive (and seek) firm CSR”", "Network for Business Sustainability"),
                ("17 Mar 2013", "“Innovation gone bad requires regulation”", "Financial Times"),
                ("22 Jan 2013", "“Financial innovation: The bright and the dark sides”", "All About Finance, World Bank"),
                ("2 Oct 2012", "“Financial innovation: The bright and the dark sides”", "VoxEU")]
    f = lambda rows: dated([(d, f"{E(t)}, <cite>{E(o)}</cite>") for d, t, o in rows])
    return f"""<section aria-labelledby="h-o"><h2 id="h-o">Commentary</h2>{f(op)}</section>
<section aria-labelledby="h-tv"><h2 id="h-tv">Television interviews</h2>{f(tv)}</section>
<section aria-labelledby="h-q"><h2 id="h-q">Quoted in the news</h2>{f(quoted)}</section>
<section aria-labelledby="h-rc"><h2 id="h-rc">Coverage of research</h2>{f(research)}</section>"""
