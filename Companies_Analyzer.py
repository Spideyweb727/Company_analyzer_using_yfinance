'''
A Market Intelligence Analyzer Project
1. View the companies in the database
2. Find the largest company by market cap
3. Find the smallest company by market cap
4. Calculate the total market cap
5. Calculate the average market cap
6. Find companies by country
7. Find companies by sector
8. Find companies with market cap > $1,000B
9. Find the company with the highest market cap in each sector
'''
import time
import yfinance as yf

print("\n**********Company Analyzer**********")
time.sleep(1)
print("\nA simple Python based tool that analyzes companies based on key information such as"+
       "market capitalization, country, and industry."+"\nUsers can perform various operations on the company database."+
       "Please check the main menu for the available options."+
       "\n\nNote: All text inputs, including company names, sectors, and countries, are case sensitive."+
       "Please enter the information exactly as required by the program to ensure accurate results.")


tickers = [
    # United States
    "AAPL",       # Apple
    "MSFT",       # Microsoft
    "NVDA",       # NVIDIA
    "AMZN",       # Amazon
    "GOOGL",      # Alphabet
    "META",       # Meta Platforms
    "TSLA",       # Tesla
    "AVGO",       # Broadcom
    "JPM",        # JPMorgan Chase
    "V",          # Visa
    "MA",         # Mastercard
    "WMT",        # Walmart
    "COST",       # Costco
    "JNJ",        # Johnson & Johnson
    "LLY",        # Eli Lilly
    "UNH",        # UnitedHealth Group
    "XOM",        # Exxon Mobil
    "CVX",        # Chevron
    "HD",         # Home Depot
    "CAT",        # Caterpillar
    "NFLX",       # Netflix
    "CRM",        # Salesforce
    "ORCL",       # Oracle
    "AMD",        # AMD
    "ADBE",       # Adobe

    # Germany
    "SAP.DE",     # SAP
    "SIE.DE",     # Siemens
    "ALV.DE",     # Allianz
    "DTE.DE",     # Deutsche Telekom
    "BMW.DE",     # BMW
    "VOW3.DE",    # Volkswagen
    "MBG.DE",     # Mercedes-Benz Group
    "BAS.DE",     # BASF
    "MRK.DE",     # Merck KGaA
    "MUV2.DE",    # Munich Re

    # United Kingdom
    "SHEL.L",     # Shell
    "AZN.L",      # AstraZeneca
    "HSBA.L",     # HSBC
    "ULVR.L",     # Unilever
    "BP.L",       # BP
    "RIO.L",      # Rio Tinto
    "GSK.L",      # GSK
    "REL.L",      # RELX
    "LSEG.L",     # London Stock Exchange Group
    "BARC.L",     # Barclays

    # France
    "MC.PA",      # LVMH
    "OR.PA",      # L'Oréal
    "TTE.PA",     # TotalEnergies
    "SAN.PA",     # Sanofi
    "AIR.PA",     # Airbus
    "SU.PA",      # Schneider Electric
    "BNP.PA",     # BNP Paribas
    "AI.PA",      # Air Liquide

    # Switzerland
    "NESN.SW",    # Nestlé
    "NOVN.SW",    # Novartis
    "UBSG.SW",    # UBS
    "ABBN.SW",    # ABB

    # Netherlands
    "ASML.AS",     # ASML
    "INGA.AS",     # ING Group
    "ADYEN.AS",    # Adyen N.V. 
    "PHIA.AS",     # Philips

    # Japan
    "6758.T",     # Sony
    "6861.T",     # Keyence
    "8306.T",     # Mitsubishi UFJ Financial Group
    "6501.T",     # Hitachi
    "8035.T",     # Tokyo Electron
    "9432.T",     # NTT
    "9984.T",     # SoftBank Group

    # South Korea
    "005930.KS",  # Samsung Electronics
    "000660.KS",  # SK Hynix
    "005380.KS",  # Hyundai Motor
    "035420.KS",  # NAVER

    # Taiwan
    "2330.TW",    # TSMC
    "2317.TW",    # Hon Hai Precision
    "2454.TW",    # MediaTek
    "2308.TW",    # Delta Electronics

    # India
    "RELIANCE.NS", # Reliance Industries
    "TCS.NS",      # Tata Consultancy Services
    "HDFCBANK.NS", # HDFC Bank
    "INFY.NS",     # Infosys
    "ICICIBANK.NS",# ICICI Bank
    "BHARTIARTL.NS", # Bharti Airtel

    # China / Hong Kong
    "9988.HK",    # Alibaba
    "0700.HK",    # Tencent
    "1810.HK",    # Xiaomi
    "0941.HK",    # China Mobile
    "9618.HK",    # JD.com

    # Australia
    "BHP.AX",     # BHP Group
    "CBA.AX",     # Commonwealth Bank
    "CSL.AX",     # CSL
    "WBC.AX",     # Westpac
    "FMG.AX",     # Fortescue

    # Saudi Arabia
    "2222.SR",    # Saudi Aramco
    "1150.SR",    # Al Rajhi Bank
    "2010.SR",    # Saudi Basic Industries Corporation

    # Brazil
    "VALE3.SA",   # Vale
    "PETR4.SA",   # Petrobras
    "ITUB4.SA",   # Itaú Unibanco
    "ABEV3.SA",   # Ambev

    # Canada
    "RY.TO",      # Royal Bank of Canada
    "TD.TO",      # Toronto-Dominion Bank
    "SHOP.TO",    # Shopify
    "ENB.TO",     # Enbridge
    "CNQ.TO"      # Canadian Natural Resources
]
#Need to change the currency of the market cap and convert everything into USD. Currently they are into domestic currency
company=[]

for ticker in tickers:

    cmp_tckr = yf.Ticker(ticker)
    infos = cmp_tckr.info

    mrkt_cap = infos.get("marketCap")
    crncy = infos.get("currency")

    if mrkt_cap is None:
        print(f"Market cap unavailable for {ticker}")
        continue

    # USD company
    if crncy == "USD":
        market_cap_usd = mrkt_cap

    # EUR company
    elif crncy == "EUR":
        exchange_rate = yf.Ticker("EURUSD=X").fast_info["last_price"]
        market_cap_usd = mrkt_cap * exchange_rate

    # GBP company
    elif crncy == "GBP":
        exchange_rate = yf.Ticker("GBPUSD=X").fast_info["last_price"]
        market_cap_usd = mrkt_cap * exchange_rate

    # British Pence company
    elif crncy == "GBp":
        exchange_rate = yf.Ticker("GBPUSD=X").fast_info["last_price"]
        market_cap_usd = (mrkt_cap / 100) * exchange_rate

    # JPY company
    elif crncy == "JPY":
        exchange_rate = yf.Ticker("USDJPY=X").fast_info["last_price"]
        market_cap_usd = mrkt_cap / exchange_rate

    # CHF company
    elif crncy == "CHF":
        exchange_rate = yf.Ticker("USDCHF=X").fast_info["last_price"]
        market_cap_usd = mrkt_cap / exchange_rate

    # CAD company
    elif crncy == "CAD":
        exchange_rate = yf.Ticker("USDCAD=X").fast_info["last_price"]
        market_cap_usd = mrkt_cap / exchange_rate

    # AUD company
    elif crncy == "AUD":
        exchange_rate = yf.Ticker("AUDUSD=X").fast_info["last_price"]
        market_cap_usd = mrkt_cap * exchange_rate

    # INR company
    elif crncy == "INR":
        exchange_rate = yf.Ticker("USDINR=X").fast_info["last_price"]
        market_cap_usd = mrkt_cap / exchange_rate

    # CNY company
    elif crncy == "CNY":
        exchange_rate = yf.Ticker("USDCNY=X").fast_info["last_price"]
        market_cap_usd = mrkt_cap / exchange_rate

    # HKD company
    elif crncy == "HKD":
        exchange_rate = yf.Ticker("USDHKD=X").fast_info["last_price"]
        market_cap_usd = mrkt_cap / exchange_rate

    # KRW company
    elif crncy == "KRW":
        exchange_rate = yf.Ticker("USDKRW=X").fast_info["last_price"]
        market_cap_usd = mrkt_cap / exchange_rate

    # TWD company
    elif crncy == "TWD":
        exchange_rate = yf.Ticker("USDTWD=X").fast_info["last_price"]
        market_cap_usd = mrkt_cap / exchange_rate

    # BRL company
    elif crncy == "BRL":
        exchange_rate = yf.Ticker("USDBRL=X").fast_info["last_price"]
        market_cap_usd = mrkt_cap / exchange_rate

    # SAR company
    elif crncy == "SAR":
        exchange_rate = yf.Ticker("USDSAR=X").fast_info["last_price"]
        market_cap_usd = mrkt_cap / exchange_rate

    else:
        print(f"Currency not supported for {ticker}: {crncy}")
        continue

    # Convert to USD billions
    market_cap_usd = round((market_cap_usd / 1_000_000_000),3)

    company_list = (
        infos.get("longName"),
        infos.get("country"),
        infos.get("sector"),
        market_cap_usd
    )

    company.append(company_list)

time.sleep(1)
print("\nMain Menu\n1.View the companies in the database\n2.Find the largest company by market cap\n3.Find the smallest company by market cap"
      "\n4.Calculate the total market cap\n5.Calculate the average market cap\n6.Find the companies by country\n7.Find the companies by Sector" \
      "\n8.Find the companies with a market cap over a certain threshold\n9.Find the company with the highest market cap in each sector\n10.Exit: Close the program")

time.sleep(2)

while True:
    x=input("\nSelect your choice from the main menu: ")
    if x =="1":
        print("\n------------Companies in the dataset------------")
        print(f"\n{("Company"):<50}{"Country":<30}{"Sector":<35}{("Market Cap in $Bn"):<25}")
        print("---------------------------------------------------------------------------------------------------------------------")
        for i in range(len(company)):
            print(f"{(company[i][0]):<50}{(company[i][1]):<30}{(company[i][2]):<35}{(company[i][3]):<25}")
    elif x=="2":
        max_market_cap=(company[0][3])
        for j in range(len(company)):
            if (company[j][3])>max_market_cap:
                max_market_cap=company[j][3]
            else:
                continue
        for k,item in enumerate(company):
            if max_market_cap in item:
                Tuple_max_index=k
                max_market_cap_idx=item.index(max_market_cap)
        time.sleep(1)
        print(f"\n{company[Tuple_max_index][0]} is the largest company, with a market cap of ${max_market_cap}Bn")
    elif x=="3":
        min_market_cap=(company[0][3])
        for l in range(len(company)):
            if (company[l][3])<min_market_cap:
                min_market_cap=company[l][3]
            else:
                continue
        for m,item in enumerate(company):
            if min_market_cap in item:
                Tuple_min_index=m
                min_market_cap_idx=item.index(min_market_cap)
        time.sleep(1)
        print(f"\n{company[Tuple_min_index][0]} is the smallest company, with a market cap of ${round(min_market_cap,3)}Bn")        
    elif x=="5":
        avg_mcp=company[0][3]
        for n in range(len(company)):
            if n==0:
                avg_mcp+=0
            else:
                avg_mcp+=company[n][3]
        avg_market_cap=avg_mcp/len(company)
        time.sleep(1)
        print(f"\nThe average market cap for {len(company)} companies in our database is ${round(avg_market_cap,3)}Bn")       
    elif x=="4":
        ttl_mcp=company[0][3]
        for o in range(len(company)):
            if o==0:
                ttl_mcp+=0
            else:
                ttl_mcp+=company[o][3]
        time.sleep(1)
        print(f"\nThe total market cap for {len(company)} companies in our database is ${round(ttl_mcp,3)}Bn")   
    elif x=="6":
        list_cty=[]
        for r in range(len(company)):
            list_cty.append(company[r][1])
        countrylist=set(list_cty)
        countrylst=list(countrylist)
        print(f"\nThe companies included in the database are headquartered in the following countries:\n{countrylst}")            
        country=input("\nSelect a country to locate the companies: ")
        company_country_list=[]
        for p,item in enumerate(company):
            if country in item:
                Tuple_country_idx=p
                company_country_list.append(company[Tuple_country_idx])
        print(f"\nList of companies in {country}"+f"\nTotal number:{(len(company_country_list))}")
        time.sleep(1)
        print(f"\n{("Company"):<50}{"Country":<30}{"Sector":<35}{("Market Cap in $Bn"):<25}")
        print("--------------------------------------------------------------------------------------------------")
        for q in range(len(company_country_list)):
            print(f"{(company_country_list[q][0]):<50}{(company_country_list[q][1]):<30}{(company_country_list[q][2]):<35}{(company_country_list[q][3]):<25}")
    elif x=="7":
        list_sect=[]
        for s in range(len(company)):
            list_sect.append(company[s][2])
        sectorlist=set(list_sect)
        sectorlst=list(sectorlist)
        print(f"\nThe companies included in the database are operating in the following sectors:\n{sectorlst}")            
        sector=input("\nSelect a sector to locate the companies: ")
        company_sector_list=[]
        for sec,term in enumerate(company):
            if sector in term:
                Tuple_sector_idx=sec
                company_sector_list.append(company[Tuple_sector_idx])
        print(f"\nList of companies in {sector}"+f"\nTotal number:{(len(company_sector_list))}")
        time.sleep(1)
        print(f"\n{("Company"):<50}{"Country":<30}{"Sector":<35}{("Market Cap in $Bn"):<25}")
        print("--------------------------------------------------------------------------------------------------")
        for st in range(len(company_sector_list)):
            print(f"{company_sector_list[st][0]:<50}{company_sector_list[st][1]:<30}{company_sector_list[st][2]:<35}{company_sector_list[st][3]:<25}")
    elif x=="8":
        rng=int(input("\nEnter the minimum market capitalization to display companies above this threshold: "))
        comp_market_cap=[]
        for mc,marketcap in enumerate(company):
            if int(company[mc][3])>=rng:
                comp_market_cap.append(company[mc])
        print(f"\nList of companies above ${rng}Bn"+f"\nTotal number:{(len(comp_market_cap))}")
        time.sleep(1)
        print(f"\n{("Company"):<50}{"Country":<30}{"Sector":<35}{("Market Cap in $Bn"):<25}")
        print("--------------------------------------------------------------------------------------------------")
        for mut in range(len(comp_market_cap)):
            print(f"{comp_market_cap[mut][0]:<50}{comp_market_cap[mut][1]:<30}{comp_market_cap[mut][2]:<35}{comp_market_cap[mut][3]:<25}")
    elif x=="9":
        list_sect2=[]
        for sm in range(len(company)):
            list_sect2.append(company[sm][2])
            sectorlist2=set(list_sect2)
            sectorlst2=list(sectorlist2)
        print(f"\nThe companies included in the database are operating in the following sectors:\n{sectorlst2}")
        for jtt in range(len(sectorlst2)):
            if jtt<len(sectorlst2):
                print(f"\nLets take a look at the sector **{sectorlst2[jtt]}**")
                sector_new9=sectorlst2[jtt]
                company_sector_list_new9=[]
                for secn9,term in enumerate(company):
                    if sector_new9 in term:
                        Tuple_sector_new9_idx=secn9
                        company_sector_list_new9.append(company[Tuple_sector_new9_idx])
                print(f"\nTotal number of companies in {sector_new9} are {(len(company_sector_list_new9))}")
                max_market_cap_new9=(company_sector_list_new9[0][3])
                for jn9 in range(len(company_sector_list_new9)):
                    if (company_sector_list_new9[jn9][3])>max_market_cap_new9:
                        max_market_cap_new9=company_sector_list_new9[jn9][3]
                    else:
                        continue
                for kn9,itemn9 in enumerate(company_sector_list_new9):
                    if max_market_cap_new9 in itemn9:
                        Tuple_max_n9_index=kn9
                        max_market_cap_n9_idx=itemn9.index(max_market_cap_new9)
                print(f"{(company_sector_list_new9[Tuple_max_n9_index][0])} is the largest company"+f" in the sector {(sector_new9)} "+f"and a market cap of ${(max_market_cap_new9)}Bn")
                print("--------------------------------------------------------------------------------------------------------")
                time.sleep(1)
            elif jtt==len(sectorlst2):
                break

    elif x=="10":
        print("Thank you: Closing the program")
        time.sleep(1)
        break 
    else:
        print("Wrong Choice! Please select the correct option.")
        
        


