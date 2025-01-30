import json

# List of usernames
usernames  =["syndicategold001",
"ukoil_free_signals",
"thesyndicate001",
"dubaigoldsellers",
"fxsignals_gold",
"gold_silver_crude_zinc_mcx_calls",
"gldsclpr",
"gold_trading_xauusd_signals",
"frank_gold_free_admin",
"goldsniperofficialbot",
"gold_news_channel",
"gold_forex_signal11",
"gold_fx_signals3",
"gold_forex_signals0",
"gold_forex_trading_signal",
"gold_fx_trading_oi",
"gold_forex_signal18",
"gold_master_killer",
"xauusd_gold_forex_freesignal",
"gold_forex_signals11",
"goldsignalsforexbee",
"gold_trading_signals43",
"gold_forex_trading1",
"gold_trading_signalls",
"goldsignalsprofessorfree",
"clinqcoingold",
"xauusd_gold_signal_invest",
"forexgoldportal_academy",
"goldfx_signall1",
"gary_the_trade",
"capitalraisegold",
"garythe_traderx",
"proscalpergolds",
"freegoldtradingsignal",
"xcoingoldsignalsfx",
"alex_gold_hunter1",
"wfxgold",
"goldtradingsignals_by_marcus",
"forexmastermike"
"eurusd_gold_gbpusd_usdjpy_audusd",
"analysis_gfr1",
"fxgoldsclub",
"fxgoldforexsignalsfxfx",
"bestscalperfx",
"goldmastamik",
"frankgoldsignals",
"vaultorovip",
"usoiltexgoldsignal",
"goldsignalsi",
"goldamnfish",
"bengooldtrade",
"goldtraderbal",
"trading_mentor7",
"goldgreenpip",
"zedasignals0",
"goldfxsign1",
"bengoldtraderz",
"ultragoldfx9",
"goldpipskillers",
"goldsignalsdaily01",
"gldpip",
"goldpipskiiler",
"goldmegasignals",
"usdjp",
"whitewavecapitalfxsignalslimited",
"digitalmoneymakers",
"goldsignals1001",
"nas100_fx_trading_signals",
"goldforexsignalsq",
"pranksbackup",
"yoforexgold3",
"etg_official",
"drsimonegold",
"goldclubhouse11",
"cyber_gold1",
"fxtm_signal",
"allaboutgold999",
"goldforexsignalspro",
"alexxgoldhunter",
"goldishold1593",
"zaynn_goldtrader1",
"marygoldtips",
"vipgoldtraders",
"forexpipseaofficial",
"goldpesaofficial",
"free_signal_forex2021",
"apocalypsesignals",
"noiambillio_laurent",
"clickforexpipzsignals",
"fxpremier_original01",
"solaralertsgroup",
"xauusdsas_join_bot",
"only_gold_master1",
"gold_accuracy",
"goldus30trade",
"fx_gold_killler",
"free_signals",
"jay_gold_wallpapers",
"trading_pit_signal",
"gbpusd_gbpaud_xauusd_trader",
"smartoptionsio",
"joinchatglobalcommoditytraders",
"forexgateway",
"mcxtradelearn",
"bpfx_bot",
"britainfirst",
"genevatradingbusinessch",
"bot_forex_signals_bot",
"fxprosignal68",
"tradesafeinvestments",
"tyroforex2020",
"trademasterfx",
"forexgiants21",
"p1phunters",
"miningst0cks",
"bestforexscalpingsignal",
"tradefoxofficial",
"fxoverseas",
"elliottwavemonitor",
"sgms18",
"forexcitybot",
"miscoforex",
"forexsignalsgrowmore",
"stonksscan",
"hiddensecretsfx",
"forexwikiii",
"drsultanng",
"free_binary_option_signal_quotex",
"zahidfxx420",
"lighthousefxfree",
"gx12bot",
"americanfxmaster",
"forexsignalsclub01",
"goldenforexhits",
"michfx24",
"forexgoldexpert",
"ttradingzone",
"growpips",
"gotraderpros",
"technicalanalysis90",
"i_mforexboss",
"justforex_official",
"bitstamp_signalexchange",
"goldofficialcontent",
"alchemyassets",
"dubaitradercircle_0",
"gbpusdusdcadnzdjpysignal",
"eurusdusdjpygbpusdsignalsfx",
"fxgoatsignals03",
"gain_paxg",
"goldsignalsofficial1",
"rlindarkes1",
"bluegeek_forex_pricetator",
"arrrashfx",
"tansrimillionaires20230",
"xauusdusdjpyeurusdfx",
"fxlifestyle89",
"gbpusdeurusdgbpcad",
"cityindextradingsignals",
"helpy_fx0",
"magic_tradersignalss",
"expertoptionnewsfx",
"forexsignals64",
"cityindextradingsignalsfx",
"forex_copytrading_xauusd",
"goldsignalofficials01",
"vasilytrading",
"anderstrading2",
"forexclini",
"oanda_forex_signal",
"jorgonpipsofficials",
"xm_brokersignalsfx",
"ashcartelofficial",
"superb_scalperfx",
"goldforexsignal63",
"xauusdeurusdcadjpysignalsfx",
"ictanalysis1",
"metatrader45forexsignal",
"gfr_smc_analysis",
"smc_analysis1",
"joash_naidoo_s",
"ranajit_788",
"a1tradingfxanalysis",
"fxxhunterwealth",
"clifhighwoo1",
"xauusdmasteer",
"goldglobalclub1",
"lepcoin_official",
"benzitrader109",
"tonkombatofficial",
"realhachidog",
"market_monk_original",
"metatrader5signalfx010",
"gold_snipersfx",
"goldtradersfamily",
"gold_plaza_satta_king_com",
"gold_hunters_clubfx",
"gold_fx_official",
"ladygoldtrader",
"goldforexsignalsever",
"xauusd_gold_master6666",
"goldforexhunter",
"gbpusdxauusdusdcad",
"goldlionea",
"kupikod_gold",
"us30_nasdaq_xau_signals",
"gold_tips1",
"arrashfx_0",
"goldfxtradeaccuracy0001",
"forexgoldpk",
"gold_forextradingg",
"xauusd_gold_forex_signals_free01",
"gold_forex_signal",
"goldfreesignalss12",
"forextradinganalysis_080",
"gold_fx_tradingss",
"gruppe_kolloidales_silber",
"reeglod2pipssignals",
"jamesgoldmasterx",
"kingofgoldkrarshi108",
"goldfx_signal001",
"fxextra",
"goldtrader_mo1",
"autotradegoldcanalfrance",
"goldempirefx_01",
"zaynn_goldtrader",
"analisaforexindonesia",
"nextleveltradingfx1",
"fxgoldsignal9",
"goldgraphicsys",
"forexgoldexpert318",
"sonsndndnddddd",
"goldfxtrading101",
"xauusdgoldfreesignals0",
"king_goldpips0",
"mikegoldfxx",
"goldbetteam_bot",
"forextredin",
"jayfxgold",
"fxgoldexpraet",
"goldviphub",
"xauusdforexsignals",
"bitsofgoldnews",
"goldscalper",
"mauricegoldbet365",
"imrankhan804khan",
"kettneredelmetalle0ffizieller",
"goldmasterwadra07",
"johngoidscalper",
"ict_analysis1",
"gold_forexsignalsfree",
"eurusd_gold_usdjpy_audusd_nzdusd",
"goldzillaofficiall",
"forextamil_channel",
"goldforexhubofficial",
"forexhunters0",
"forexsignalfxx_factory",
"gold_vip_signal100",
"xauusd_fx_treding",
"fxzeus",
"tommyprofitabletrader_0",
"mbngoldcsi",
"gold_group_vip_forex",
"switzerlandtrading",
"gold_fx_signalz",
"swing_basic",
"londonforexorders1",
"forexfiresignals",
"goldfxpro88",
"goldzillaofficial0",
"djendralkenkenfx",
"justalphacc",
"olivierbornet",
"xauusdshoother",
"finanziellgesund",
"aof_sohbet",
"goldxauusdio",
"ben_vipcircles",
"forexvipsignals00",
"gyan_yes24",
"tonskuf",
"dicascripto_01",
"forexsignalsstreet",
"xmforexbrokerfx17",
"thevarietyhutsignals",
"iwinforexsigna",
"smc_world_service",
"etoroforex_brokersignals",
"pbfxtradinggroup",
"forexgoldedu",
"fxpremieresignalsexperts",
"lofipopelectro",
"johneyjan",
"theprofitcenter",
"atakanvip",
"rauf_sahab_12",
"trikaalcapital_free",
"waboeldahab",
"topforexscalper",
"superprofitsystem",
"ft_ekonomist",
"paramountcommodityanalysis",
"familytrading01",
"piyasatrendi",
"forexhollywood",
"elitetraders_fxsignals",
"ftmo_forex1",
"sniprtrade",
"mt4_mt5_forexsignal",
"kingforextradingfx",
"hknforex",
"cloudtsociety_01",
"xauusdcharlie",
"xsignalsgold",
"jamesgoldmaster",
"natefxctrade",
"bestforexsignal",
"Gary_TheTrader",
"forextrade",
"goldsnipers11",
"GOLDUS30FREESIGNALS",
"GOLDUSDMASTER",
"whh521gold",
"goldtradingpk",
"AliZafarSheikh50",
"Goldmine_Investment",
"golddailysignals001",
"HuracanFx_Gold",
"AltSignalsFX_TradingSignals1",
"FxLondonSignalsA",
"Apexbullfirexsignalfx",
"Signal1000Pipsbuilder",
"learn2trade",
"kingofchartgold",
"FoxGoldSignals",
"goldhunteracademyfx_fx",
"Signals_OlympTrade_Quotex",
"RealGoldSnipers",
"goldingtrade1",
"usoil_crudeoiIsignal",
"Gold_SignalsOfficials",
"xauusd_gold_signalfx",
"Gold_Signals_daily_Original",
"fx_goldxauusdsignal1",
"signale",
"XAUUSD_ninjatraders_proforex",
"GOLDXAUUSDPIPSHUNTERCLUB",
"FOREX_XAUUSD_GOLD_SIGNAL",
"XAUUSDA",
"NASDAQ_XAUUSD_US30",
"MrKingTeamGoldSignals",
"signal_golds1",
"usoilwtisignals",
"wolf_forex_fxx",
"vipgoldtradermo",
"safe_pip",
"glaad_elgold_1",
"Forex_Signals_4x",
"Forex_Signals_Ocean",
"Forex_Signal_Freeeeee",
"Forex_Signals_Bulls1",
"Forex_Signals_Level_Up",
"gbpjpy_gold_gbpusd_usdjpy_audusd",
"gbpnzd_gbpusdexpert",
"garythe_trader1",
"sir_mangoldhunter",
"gold_eurusd_usdjpy_gbpusd_gbpjpy",
"gbpjpy_usdjpymaster",
"gary_the_trader",
"forexgoldsignals_official",
"goldforexsignalsforex",
"goldxauusdeurusdusdjpy",
"wallstreetforex_signals",
"us30dowjones_usa_usoil_nas100",
"eurusdusdjpygbpusdsignalsfxfx",
"gbpjpyforexfree",
"gbpjpyfxforex",
"fx20minutetrader",
"goldsnipersprovider",
"bengoidtrade",
"gold_fx_signald",
"gold_fx_signalls",
"gold_signalfx_daily",
"gold_forex_signals21",
"gary_the_gold_trader",
"gold_forex_signals7",
"goldscalperninja",
"xauusdalerts",
"nas100_us30_gold_tradingcompany",
"goldtradingsignal_by_marcus",
"goldtradermo",
"goldsexpertsignals",
"gfr_signal",
"catgoldminerann",
"intradaytradingsignals",
"fabioforex001",
"goldsignalsprofessor1",
"goldfx_signalls",
"canadagoldscalpers",
"goldsignalsprofessor",
"xauusdgoldtradingfx",
"holy_grail_fxking",
"goldfx_free",
"timezonegoldfreesignals",
"goldfx_officials",
"goldforexsignals002",
"goldforexsgnals",
"goldmaster_p",
"goldforexsignals18",
"goldforexsignalsoriginal",
"goldsignals_fx1",
"jamesgoldmasters",
"httpstmegoldsignalsdailyuk2",
"fxsharktanks",
"fxmarketforexsignals",
"adamfxnj2",
"karyongfx_gold_indices_us30_nas1",
"wolvestradesforex",
"hanzsuper",
"arrashfx_1",
"babypipsfxs1",
"wall_streetforexsignals",
"CaptainScalpingSignalsfx",
"city_index_tradings",
"aaafxofficial",
"investopediaacadem",
"dailyforex_signals",
"forexxbluepips",
"eurusgbpusdusdjpy",
"fxwolfxsignals",
"gbpjpyforexfxfx",
"anderstradingx",
"craig_percoc0",
"jackskipp_fx",
"eurjpy_xauusd_usdchf",
"gbpjpy_xauusd_usdjpy_forexsignal",
"us30_gold_nasdaq_forex_trading",
"goldfxsignalsls",
"goldplatinum_trader",
"sureshotgold",
"garythegoldtraders",
"dengoldtrader0",
"forexweb_forexclub",
"goldtradermo_01",
"goldfx_signallss",
"paulgoldhunterfxsignals",
"goldbossfx",
"gold_leofx1",
"analysis_gfr",
"austinsilverfx_gold_us30_nas100",
"primetradingoptions",
"xauusdnzdusdgpbjay",
"goldsignals_ioz001",
"goldsignalsfx015",
"Xauusd_Gold_Signals_Pips1",
"haridrashin",
"XAUUSD_GOLD_forex_signalsfx11",
"Goldforexsignalfx11",
"xauusd_gold_forexs2",
"XAUUSD_GOLD_PIPS_SIGNAL",
"FX_GOLD_XAUUSD_SIGNALS1",
"XAUUSD_GOLD_FOREX_SIGNALS_PIPS1",
"GOLD_FOREX_SIGN",
"XAUUSD_GOLD_FOREX_SIGNALS_FREEE2",
"XAUUSD_GOLD_FOREXs1",
"forexgoldsignalOfficiaI",
"BestGoldForexSignalInvests",
"gold_forexinvest002",
"Trading_forex_signal_kanal",
"ForexGoldensignall",
"GoldForexSignals001",
"Xauusd_Goldsignals0",
"TheFxGoldInvestments",
"garry1_signals",
"+CoUMrFhFDC4zMTRl",
]



# Format the usernames into URLs
formatted_urls = [f"https://t.me/{username}" for username in usernames]

# Export to a JSON file
output_data = {"urls": formatted_urls}

with open("formatted_urls.json", "w") as json_file:
    json.dump(output_data, json_file, indent=4)

print("Exported successfully to formatted_urls.json")
