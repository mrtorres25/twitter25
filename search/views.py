from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.shortcuts import render
from tweepy import API
from tweepy import OAuthHandler
import json
import  requests as r
languages=[
        {"code":"0","name":"Cualquiera","nativeName":""},
      {"code":"ab","name":"Abkhaz","nativeName":"аҧсуа"},
      {"code":"aa","name":"Afar","nativeName":"Afaraf"},
      {"code":"af","name":"Afrikaans","nativeName":"Afrikaans"},
      {"code":"ak","name":"Akan","nativeName":"Akan"},
      {"code":"sq","name":"Albanian","nativeName":"Shqip"},
      {"code":"am","name":"Amharic","nativeName":"አማርኛ"},
      {"code":"ar","name":"Arabic","nativeName":"العربية"},
      {"code":"an","name":"Aragonese","nativeName":"Aragonés"},
      {"code":"hy","name":"Armenian","nativeName":"Հայերեն"},
      {"code":"as","name":"Assamese","nativeName":"অসমীয়া"},
      {"code":"av","name":"Avaric","nativeName":"авар мацӀ, магӀарул мацӀ"},
      {"code":"ae","name":"Avestan","nativeName":"avesta"},
      {"code":"ay","name":"Aymara","nativeName":"aymar aru"},
      {"code":"az","name":"Azerbaijani","nativeName":"azərbaycan dili"},
      {"code":"bm","name":"Bambara","nativeName":"bamanankan"},
      {"code":"ba","name":"Bashkir","nativeName":"башҡорт теле"},
      {"code":"eu","name":"Basque","nativeName":"euskara, euskera"},
      {"code":"be","name":"Belarusian","nativeName":"Беларуская"},
      {"code":"bn","name":"Bengali","nativeName":"বাংলা"},
      {"code":"bh","name":"Bihari","nativeName":"भोजपुरी"},
      {"code":"bi","name":"Bislama","nativeName":"Bislama"},
      {"code":"bs","name":"Bosnian","nativeName":"bosanski jezik"},
      {"code":"br","name":"Breton","nativeName":"brezhoneg"},
      {"code":"bg","name":"Bulgarian","nativeName":"български език"},
      {"code":"my","name":"Burmese","nativeName":"ဗမာစာ"},
      {"code":"ca","name":"Catalan; Valencian","nativeName":"Català"},
      {"code":"ch","name":"Chamorro","nativeName":"Chamoru"},
      {"code":"ce","name":"Chechen","nativeName":"нохчийн мотт"},
      {"code":"ny","name":"Chichewa; Chewa; Nyanja","nativeName":"chiCheŵa, chinyanja"},
      {"code":"zh","name":"Chinese","nativeName":"中文 (Zhōngwén), 汉语, 漢語"},
      {"code":"cv","name":"Chuvash","nativeName":"чӑваш чӗлхи"},
      {"code":"kw","name":"Cornish","nativeName":"Kernewek"},
      {"code":"co","name":"Corsican","nativeName":"corsu, lingua corsa"},
      {"code":"cr","name":"Cree","nativeName":"ᓀᐦᐃᔭᐍᐏᐣ"},
      {"code":"hr","name":"Croatian","nativeName":"hrvatski"},
      {"code":"cs","name":"Czech","nativeName":"česky, čeština"},
      {"code":"da","name":"Danish","nativeName":"dansk"},
      {"code":"dv","name":"Divehi; Dhivehi; Maldivian;","nativeName":"ދިވެހި"},
      {"code":"nl","name":"Dutch","nativeName":"Nederlands, Vlaams"},
      {"code":"en","name":"English","nativeName":"English"},
      {"code":"eo","name":"Esperanto","nativeName":"Esperanto"},
      {"code":"et","name":"Estonian","nativeName":"eesti, eesti keel"},
      {"code":"ee","name":"Ewe","nativeName":"Eʋegbe"},
      {"code":"fo","name":"Faroese","nativeName":"føroyskt"},
      {"code":"fj","name":"Fijian","nativeName":"vosa Vakaviti"},
      {"code":"fi","name":"Finnish","nativeName":"suomi, suomen kieli"},
      {"code":"fr","name":"French","nativeName":"français, langue française"},
      {"code":"ff","name":"Fula; Fulah; Pulaar; Pular","nativeName":"Fulfulde, Pulaar, Pular"},
      {"code":"gl","name":"Galician","nativeName":"Galego"},
      {"code":"ka","name":"Georgian","nativeName":"ქართული"},
      {"code":"de","name":"German","nativeName":"Deutsch"},
      {"code":"el","name":"Greek, Modern","nativeName":"Ελληνικά"},
      {"code":"gn","name":"Guaraní","nativeName":"Avañeẽ"},
      {"code":"gu","name":"Gujarati","nativeName":"ગુજરાતી"},
      {"code":"ht","name":"Haitian; Haitian Creole","nativeName":"Kreyòl ayisyen"},
      {"code":"ha","name":"Hausa","nativeName":"Hausa, هَوُسَ"},
      {"code":"he","name":"Hebrew (modern)","nativeName":"עברית"},
      {"code":"hz","name":"Herero","nativeName":"Otjiherero"},
      {"code":"hi","name":"Hindi","nativeName":"हिन्दी, हिंदी"},
      {"code":"ho","name":"Hiri Motu","nativeName":"Hiri Motu"},
      {"code":"hu","name":"Hungarian","nativeName":"Magyar"},
      {"code":"ia","name":"Interlingua","nativeName":"Interlingua"},
      {"code":"id","name":"Indonesian","nativeName":"Bahasa Indonesia"},
      # {"code":"ie","name":"Interlingue","nativeName":"Originally called Occidental; then Interlingue after WWII"},
      {"code":"ga","name":"Irish","nativeName":"Gaeilge"},
      {"code":"ig","name":"Igbo","nativeName":"Asụsụ Igbo"},
      {"code":"ik","name":"Inupiaq","nativeName":"Iñupiaq, Iñupiatun"},
      {"code":"io","name":"Ido","nativeName":"Ido"},
      {"code":"is","name":"Icelandic","nativeName":"Íslenska"},
      {"code":"it","name":"Italian","nativeName":"Italiano"},
      {"code":"iu","name":"Inuktitut","nativeName":"ᐃᓄᒃᑎᑐᑦ"},
      {"code":"ja","name":"Japanese","nativeName":"日本語 (にほんご／にっぽんご)"},
      {"code":"jv","name":"Javanese","nativeName":"basa Jawa"},
      {"code":"kl","name":"Kalaallisut, Greenlandic","nativeName":"kalaallisut, kalaallit oqaasii"},
      {"code":"kn","name":"Kannada","nativeName":"ಕನ್ನಡ"},
      {"code":"kr","name":"Kanuri","nativeName":"Kanuri"},
      {"code":"ks","name":"Kashmiri","nativeName":"कश्मीरी, كشميري‎"},
      {"code":"kk","name":"Kazakh","nativeName":"Қазақ тілі"},
      {"code":"km","name":"Khmer","nativeName":"ភាសាខ្មែរ"},
      {"code":"ki","name":"Kikuyu, Gikuyu","nativeName":"Gĩkũyũ"},
      {"code":"rw","name":"Kinyarwanda","nativeName":"Ikinyarwanda"},
      {"code":"ky","name":"Kirghiz, Kyrgyz","nativeName":"кыргыз тили"},
      {"code":"kv","name":"Komi","nativeName":"коми кыв"},
      {"code":"kg","name":"Kongo","nativeName":"KiKongo"},
      {"code":"ko","name":"Korean","nativeName":"한국어 (韓國語), 조선말 (朝鮮語)"},
      {"code":"ku","name":"Kurdish","nativeName":"Kurdî, كوردی‎"},
      {"code":"kj","name":"Kwanyama, Kuanyama","nativeName":"Kuanyama"},
      {"code":"la","name":"Latin","nativeName":"latine, lingua latina"},
      {"code":"lb","name":"Luxembourgish, Letzeburgesch","nativeName":"Lëtzebuergesch"},
      {"code":"lg","name":"Luganda","nativeName":"Luganda"},
      {"code":"li","name":"Limburgish, Limburgan, Limburger","nativeName":"Limburgs"},
      {"code":"ln","name":"Lingala","nativeName":"Lingála"},
      {"code":"lo","name":"Lao","nativeName":"ພາສາລາວ"},
      {"code":"lt","name":"Lithuanian","nativeName":"lietuvių kalba"},
      {"code":"lu","name":"Luba-Katanga","nativeName":""},
      {"code":"lv","name":"Latvian","nativeName":"latviešu valoda"},
      {"code":"gv","name":"Manx","nativeName":"Gaelg, Gailck"},
      {"code":"mk","name":"Macedonian","nativeName":"македонски јазик"},
      {"code":"mg","name":"Malagasy","nativeName":"Malagasy fiteny"},
      {"code":"ms","name":"Malay","nativeName":"bahasa Melayu, بهاس ملايو‎"},
      {"code":"ml","name":"Malayalam","nativeName":"മലയാളം"},
      {"code":"mt","name":"Maltese","nativeName":"Malti"},
      {"code":"mi","name":"Māori","nativeName":"te reo Māori"},
      {"code":"mr","name":"Marathi (Marāṭhī)","nativeName":"मराठी"},
      {"code":"mh","name":"Marshallese","nativeName":"Kajin M̧ajeļ"},
      {"code":"mn","name":"Mongolian","nativeName":"монгол"},
      {"code":"na","name":"Nauru","nativeName":"Ekakairũ Naoero"},
      {"code":"nv","name":"Navajo, Navaho","nativeName":"Diné bizaad, Dinékʼehǰí"},
      {"code":"nb","name":"Norwegian Bokmål","nativeName":"Norsk bokmål"},
      {"code":"nd","name":"North Ndebele","nativeName":"isiNdebele"},
      {"code":"ne","name":"Nepali","nativeName":"नेपाली"},
      {"code":"ng","name":"Ndonga","nativeName":"Owambo"},
      {"code":"nn","name":"Norwegian Nynorsk","nativeName":"Norsk nynorsk"},
      {"code":"no","name":"Norwegian","nativeName":"Norsk"},
      {"code":"ii","name":"Nuosu","nativeName":"ꆈꌠ꒿ Nuosuhxop"},
      {"code":"nr","name":"South Ndebele","nativeName":"isiNdebele"},
      {"code":"oc","name":"Occitan","nativeName":"Occitan"},
      {"code":"oj","name":"Ojibwe, Ojibwa","nativeName":"ᐊᓂᔑᓈᐯᒧᐎᓐ"},
      # {"code":"cu","name":"Old Church Slavonic, Church Slavic, Church Slavonic, Old Bulgarian, Old Slavonic","nativeName":"ѩзыкъ словѣньскъ"},
      {"code":"om","name":"Oromo","nativeName":"Afaan Oromoo"},
      {"code":"or","name":"Oriya","nativeName":"ଓଡ଼ିଆ"},
      {"code":"os","name":"Ossetian, Ossetic","nativeName":"ирон æвзаг"},
      {"code":"pa","name":"Panjabi, Punjabi","nativeName":"ਪੰਜਾਬੀ, پنجابی‎"},
      {"code":"pi","name":"Pāli","nativeName":"पाऴि"},
      {"code":"fa","name":"Persian","nativeName":"فارسی"},
      {"code":"pl","name":"Polish","nativeName":"polski"},
      {"code":"ps","name":"Pashto, Pushto","nativeName":"پښتو"},
      {"code":"pt","name":"Portuguese","nativeName":"Português"},
      {"code":"qu","name":"Quechua","nativeName":"Runa Simi, Kichwa"},
      {"code":"rm","name":"Romansh","nativeName":"rumantsch grischun"},
      {"code":"rn","name":"Kirundi","nativeName":"kiRundi"},
      {"code":"ro","name":"Romanian, Moldavian, Moldovan","nativeName":"română"},
      {"code":"ru","name":"Russian","nativeName":"русский язык"},
      {"code":"sa","name":"Sanskrit (Saṁskṛta)","nativeName":"संस्कृतम्"},
      {"code":"sc","name":"Sardinian","nativeName":"sardu"},
      {"code":"sd","name":"Sindhi","nativeName":"सिन्धी, سنڌي، سندھی‎"},
      {"code":"se","name":"Northern Sami","nativeName":"Davvisámegiella"},
      {"code":"sm","name":"Samoan","nativeName":"gagana faa Samoa"},
      {"code":"sg","name":"Sango","nativeName":"yângâ tî sängö"},
      {"code":"sr","name":"Serbian","nativeName":"српски језик"},
      {"code":"gd","name":"Scottish Gaelic; Gaelic","nativeName":"Gàidhlig"},
      {"code":"sn","name":"Shona","nativeName":"chiShona"},
      {"code":"si","name":"Sinhala, Sinhalese","nativeName":"සිංහල"},
      {"code":"sk","name":"Slovak","nativeName":"slovenčina"},
      {"code":"sl","name":"Slovene","nativeName":"slovenščina"},
      {"code":"so","name":"Somali","nativeName":"Soomaaliga, af Soomaali"},
      {"code":"st","name":"Southern Sotho","nativeName":"Sesotho"},
      {"code":"es","name":"Spanish; Castilian","nativeName":"español, castellano"},
      {"code":"su","name":"Sundanese","nativeName":"Basa Sunda"},
      {"code":"sw","name":"Swahili","nativeName":"Kiswahili"},
      {"code":"ss","name":"Swati","nativeName":"SiSwati"},
      {"code":"sv","name":"Swedish","nativeName":"svenska"},
      {"code":"ta","name":"Tamil","nativeName":"தமிழ்"},
      {"code":"te","name":"Telugu","nativeName":"తెలుగు"},
      {"code":"tg","name":"Tajik","nativeName":"тоҷикӣ, toğikī, تاجیکی‎"},
      {"code":"th","name":"Thai","nativeName":"ไทย"},
      {"code":"ti","name":"Tigrinya","nativeName":"ትግርኛ"},
      {"code":"bo","name":"Tibetan Standard, Tibetan, Central","nativeName":"བོད་ཡིག"},
      {"code":"tk","name":"Turkmen","nativeName":"Türkmen, Түркмен"},
      {"code":"tl","name":"Tagalog","nativeName":"Wikang Tagalog, ᜏᜒᜃᜅ᜔ ᜆᜄᜎᜓᜄ᜔"},
      {"code":"tn","name":"Tswana","nativeName":"Setswana"},
      {"code":"to","name":"Tonga (Tonga Islands)","nativeName":"faka Tonga"},
      {"code":"tr","name":"Turkish","nativeName":"Türkçe"},
      {"code":"ts","name":"Tsonga","nativeName":"Xitsonga"},
      {"code":"tt","name":"Tatar","nativeName":"татарча, tatarça, تاتارچا‎"},
      {"code":"tw","name":"Twi","nativeName":"Twi"},
      {"code":"ty","name":"Tahitian","nativeName":"Reo Tahiti"},
      {"code":"ug","name":"Uighur, Uyghur","nativeName":"Uyƣurqə, ئۇيغۇرچە‎"},
      {"code":"uk","name":"Ukrainian","nativeName":"українська"},
      {"code":"ur","name":"Urdu","nativeName":"اردو"},
      {"code":"uz","name":"Uzbek","nativeName":"zbek, Ўзбек, أۇزبېك‎"},
      {"code":"ve","name":"Venda","nativeName":"Tshivenḓa"},
      {"code":"vi","name":"Vietnamese","nativeName":"Tiếng Việt"},
      {"code":"vo","name":"Volapük","nativeName":"Volapük"},
      {"code":"wa","name":"Walloon","nativeName":"Walon"},
      {"code":"cy","name":"Welsh","nativeName":"Cymraeg"},
      {"code":"wo","name":"Wolof","nativeName":"Wollof"},
      {"code":"fy","name":"Western Frisian","nativeName":"Frysk"},
      {"code":"xh","name":"Xhosa","nativeName":"isiXhosa"},
      {"code":"yi","name":"Yiddish","nativeName":"ייִדיש"},
      {"code":"yo","name":"Yoruba","nativeName":"Yorùbá"},
      # {"code":"za","name":"Zhuang, Chuang","nativeName":"Saɯ cueŋƅ, Saw cuengh"}
    ]

# country=[
#         {"name":"Cualquiera"},
#         {"name":"España"},
#         {"name":"Francia"},
#         {"name":"Estados Unidos"},
#         {"name":"Reino Unido"},
#         {"name":"Spain"},
# ]
# countries=[{"AF":"Afganist\u00e1n","AL":"Albania","DE":"Alemania","AD":"Andorra","AO":"Angola","AI":"Anguila","AQ":"Ant\u00e1rtida","AG":"Antigua y Barbuda","SA":"Arabia Saud\u00ed","DZ":"Argelia","AR":"Argentina","AM":"Armenia","AW":"Aruba","AU":"Australia","AT":"Austria","AZ":"Azerbaiy\u00e1n","BS":"Bahamas","BD":"Banglad\u00e9s","BB":"Barbados","BH":"Bar\u00e9in","BE":"B\u00e9lgica","BZ":"Belice","BJ":"Ben\u00edn","BM":"Bermudas","BY":"Bielorrusia","BO":"Bolivia","BA":"Bosnia-Herzegovina","BW":"Botsuana","BR":"Brasil","BN":"Brun\u00e9i","BG":"Bulgaria","BF":"Burkina Faso","BI":"Burundi","BT":"But\u00e1n","CV":"Cabo Verde","KH":"Camboya","CM":"Camer\u00fan","CA":"Canad\u00e1","BQ":"Caribe neerland\u00e9s","QA":"Catar","EA":"Ceuta y Melilla","TD":"Chad","CL":"Chile","CN":"China","CY":"Chipre","VA":"Ciudad del Vaticano","CO":"Colombia","KM":"Comoras","KP":"Corea del Norte","KR":"Corea del Sur","CI":"Costa de Marfil","CR":"Costa Rica","HR":"Croacia","CU":"Cuba","CW":"Curazao","DG":"Diego Garc\u00eda","DK":"Dinamarca","DM":"Dominica","EC":"Ecuador","EG":"Egipto","SV":"El Salvador","AE":"Emiratos \u00c1rabes Unidos","ER":"Eritrea","SK":"Eslovaquia","SI":"Eslovenia","ES":"Espa\u00f1a","US":"Estados Unidos","EE":"Estonia","ET":"Etiop\u00eda","PH":"Filipinas","FI":"Finlandia","FJ":"Fiyi","FR":"Francia","GA":"Gab\u00f3n","GM":"Gambia","GE":"Georgia","GH":"Ghana","GI":"Gibraltar","GD":"Granada","GR":"Grecia","GL":"Groenlandia","GP":"Guadalupe","GU":"Guam","GT":"Guatemala","GF":"Guayana Francesa","GG":"Guernesey","GN":"Guinea","GQ":"Guinea Ecuatorial","GW":"Guinea-Bis\u00e1u","GY":"Guyana","HT":"Hait\u00ed","HN":"Honduras","HU":"Hungr\u00eda","IN":"India","ID":"Indonesia","IR":"Ir\u00e1n","IQ":"Iraq","IE":"Irlanda","CX":"Isla Christmas","AC":"Isla de la Ascensi\u00f3n","IM":"Isla de Man","NU":"Isla Niue","NF":"Isla Norfolk","IS":"Islandia","AX":"Islas \u00c5land","KY":"Islas Caim\u00e1n","IC":"islas Canarias","CC":"Islas Cocos","CK":"Islas Cook","FO":"Islas Feroe","GS":"Islas Georgia del Sur y Sandwich del Sur","FK":"Islas Malvinas","MP":"Islas Marianas del Norte","MH":"Islas Marshall","UM":"Islas menores alejadas de EE. UU.","PN":"Islas Pitcairn","SB":"Islas Salom\u00f3n","TC":"Islas Turcas y Caicos","VG":"Islas V\u00edrgenes Brit\u00e1nicas","VI":"Islas V\u00edrgenes de EE. UU.","IL":"Israel","IT":"Italia","JM":"Jamaica","JP":"Jap\u00f3n","JE":"Jersey","JO":"Jordania","KZ":"Kazajist\u00e1n","KE":"Kenia","KG":"Kirguist\u00e1n","KI":"Kiribati","XK":"Kosovo","KW":"Kuwait","LA":"Laos","LS":"Lesoto","LV":"Letonia","LB":"L\u00edbano","LR":"Liberia","LY":"Libia","LI":"Liechtenstein","LT":"Lituania","LU":"Luxemburgo","MK":"Macedonia","MG":"Madagascar","MY":"Malasia","MW":"Malaui","MV":"Maldivas","ML":"Mali","MT":"Malta","MA":"Marruecos","MQ":"Martinica","MU":"Mauricio","MR":"Mauritania","YT":"Mayotte","MX":"M\u00e9xico","FM":"Micronesia","MD":"Moldavia","MC":"M\u00f3naco","MN":"Mongolia","ME":"Montenegro","MS":"Montserrat","MZ":"Mozambique","MM":"Myanmar (Birmania)","NA":"Namibia","NR":"Nauru","NP":"Nepal","NI":"Nicaragua","NE":"N\u00edger","NG":"Nigeria","NO":"Noruega","NC":"Nueva Caledonia","NZ":"Nueva Zelanda","OM":"Om\u00e1n","NL":"Pa\u00edses Bajos","PK":"Pakist\u00e1n","PW":"Palau","PA":"Panam\u00e1","PG":"Pap\u00faa Nueva Guinea","PY":"Paraguay","PE":"Per\u00fa","PF":"Polinesia Francesa","PL":"Polonia","PT":"Portugal","PR":"Puerto Rico","HK":"RAE de Hong Kong (China)","MO":"RAE de Macao (China)","GB":"Reino Unido","CF":"Rep\u00fablica Centroafricana","CZ":"Rep\u00fablica Checa","CG":"Rep\u00fablica del Congo","CD":"Rep\u00fablica Democr\u00e1tica del Congo","DO":"Rep\u00fablica Dominicana","RE":"Reuni\u00f3n","RW":"Ruanda","RO":"Ruman\u00eda","RU":"Rusia","EH":"S\u00e1hara Occidental","WS":"Samoa","AS":"Samoa Americana","BL":"San Bartolom\u00e9","KN":"San Crist\u00f3bal y Nieves","SM":"San Marino","MF":"San Mart\u00edn","PM":"San Pedro y Miquel\u00f3n","VC":"San Vicente y las Granadinas","SH":"Santa Elena","LC":"Santa Luc\u00eda","ST":"Santo Tom\u00e9 y Pr\u00edncipe","SN":"Senegal","RS":"Serbia","SC":"Seychelles","SL":"Sierra Leona","SG":"Singapur","SX":"Sint Maarten","SY":"Siria","SO":"Somalia","LK":"Sri Lanka","SZ":"Suazilandia","ZA":"Sud\u00e1frica","SD":"Sud\u00e1n","SS":"Sud\u00e1n del Sur","SE":"Suecia","CH":"Suiza","SR":"Surinam","SJ":"Svalbard y Jan Mayen","TH":"Tailandia","TW":"Taiw\u00e1n","TZ":"Tanzania","TJ":"Tayikist\u00e1n","IO":"Territorio Brit\u00e1nico del Oc\u00e9ano \u00cdndico","TF":"Territorios Australes Franceses","PS":"Territorios Palestinos","TL":"Timor Oriental","TG":"Togo","TK":"Tokelau","TO":"Tonga","TT":"Trinidad y Tobago","TA":"Trist\u00e1n da Cunha","TN":"T\u00fanez","TM":"Turkmenist\u00e1n","TR":"Turqu\u00eda","TV":"Tuvalu","UA":"Ucrania","UG":"Uganda","UY":"Uruguay","UZ":"Uzbekist\u00e1n","VU":"Vanuatu","VE":"Venezuela","VN":"Vietnam","WF":"Wallis y Futuna","YE":"Yemen","DJ":"Yibuti","ZM":"Zambia","ZW":"Zimbabue"}]
countries=[
{"name": "Cualquiera", "code": "Cualquiera"},
{"name": "Afghanistan", "code": "AF"},
{"name": "Åland Islands", "code": "AX"},
{"name": "Albania", "code": "AL"},
{"name": "Algeria", "code": "DZ"},
{"name": "American Samoa", "code": "AS"},
{"name": "Andorra", "code": "AD"},
{"name": "Angola", "code": "AO"},
{"name": "Anguilla", "code": "AI"},
{"name": "Antarctica", "code": "AQ"},
{"name": "Antigua and Barbuda", "code": "AG"},
{"name": "Argentina", "code": "AR"},
{"name": "Armenia", "code": "AM"},
{"name": "Aruba", "code": "AW"},
{"name": "Australia", "code": "AU"},
{"name": "Austria", "code": "AT"},
{"name": "Azerbaijan", "code": "AZ"},
{"name": "Bahamas", "code": "BS"},
{"name": "Bahrain", "code": "BH"},
{"name": "Bangladesh", "code": "BD"},
{"name": "Barbados", "code": "BB"},
{"name": "Belarus", "code": "BY"},
{"name": "Belgium", "code": "BE"},
{"name": "Belize", "code": "BZ"},
{"name": "Benin", "code": "BJ"},
{"name": "Bermuda", "code": "BM"},
{"name": "Bhutan", "code": "BT"},
{"name": "Bolivia", "code": "BO"},
{"name": "Bosnia and Herzegovina", "code": "BA"},
{"name": "Botswana", "code": "BW"},
{"name": "Bouvet Island", "code": "BV"},
{"name": "Brazil", "code": "BR"},
{"name": "British Indian Ocean Territory", "code": "IO"},
{"name": "Brunei Darussalam", "code": "BN"},
{"name": "Bulgaria", "code": "BG"},
{"name": "Burkina Faso", "code": "BF"},
{"name": "Burundi", "code": "BI"},
{"name": "Cambodia", "code": "KH"},
{"name": "Cameroon", "code": "CM"},
{"name": "Canada", "code": "CA"},
{"name": "Cape Verde", "code": "CV"},
{"name": "Cayman Islands", "code": "KY"},
{"name": "Central African Republic", "code": "CF"},
{"name": "Chad", "code": "TD"},
{"name": "Chile", "code": "CL"},
{"name": "China", "code": "CN"},
{"name": "Christmas Island", "code": "CX"},
{"name": "Cocos (Keeling) Islands", "code": "CC"},
{"name": "Colombia", "code": "CO"},
{"name": "Comoros", "code": "KM"},
{"name": "Congo", "code": "CG"},
{"name": "Congo, The Democratic Republic of the", "code": "CD"},
{"name": "Cook Islands", "code": "CK"},
{"name": "Costa Rica", "code": "CR"},
{"name": "Cote D'Ivoire", "code": "CI"},
{"name": "Croatia", "code": "HR"},
{"name": "Cuba", "code": "CU"},
{"name": "Cyprus", "code": "CY"},
{"name": "Czech Republic", "code": "CZ"},
{"name": "Denmark", "code": "DK"},
{"name": "Djibouti", "code": "DJ"},
{"name": "Dominica", "code": "DM"},
{"name": "Dominican Republic", "code": "DO"},
{"name": "Ecuador", "code": "EC"},
{"name": "Egypt", "code": "EG"},
{"name": "El Salvador", "code": "SV"},
{"name": "Equatorial Guinea", "code": "GQ"},
{"name": "Eritrea", "code": "ER"},
{"name": "Estonia", "code": "EE"},
{"name": "Ethiopia", "code": "ET"},
{"name": "Falkland Islands (Malvinas)", "code": "FK"},
{"name": "Faroe Islands", "code": "FO"},
{"name": "Fiji", "code": "FJ"},
{"name": "Finland", "code": "FI"},
{"name": "France", "code": "FR"},
{"name": "French Guiana", "code": "GF"},
{"name": "French Polynesia", "code": "PF"},
{"name": "French Southern Territories", "code": "TF"},
{"name": "Gabon", "code": "GA"},
{"name": "Gambia", "code": "GM"},
{"name": "Georgia", "code": "GE"},
{"name": "Germany", "code": "DE"},
{"name": "Ghana", "code": "GH"},
{"name": "Gibraltar", "code": "GI"},
{"name": "Greece", "code": "GR"},
{"name": "Greenland", "code": "GL"},
{"name": "Grenada", "code": "GD"},
{"name": "Guadeloupe", "code": "GP"},
{"name": "Guam", "code": "GU"},
{"name": "Guatemala", "code": "GT"},
{"name": "Guernsey", "code": "GG"},
{"name": "Guinea", "code": "GN"},
{"name": "Guinea-Bissau", "code": "GW"},
{"name": "Guyana", "code": "GY"},
{"name": "Haiti", "code": "HT"},
{"name": "Heard Island and Mcdonald Islands", "code": "HM"},
{"name": "Holy See (Vatican City State)", "code": "VA"},
{"name": "Honduras", "code": "HN"},
{"name": "Hong Kong", "code": "HK"},
{"name": "Hungary", "code": "HU"},
{"name": "Iceland", "code": "IS"},
{"name": "India", "code": "IN"},
{"name": "Indonesia", "code": "ID"},
{"name": "Iran, Islamic Republic Of", "code": "IR"},
{"name": "Iraq", "code": "IQ"},
{"name": "Ireland", "code": "IE"},
{"name": "Isle of Man", "code": "IM"},
{"name": "Israel", "code": "IL"},
{"name": "Italy", "code": "IT"},
{"name": "Jamaica", "code": "JM"},
{"name": "Japan", "code": "JP"},
{"name": "Jersey", "code": "JE"},
{"name": "Jordan", "code": "JO"},
{"name": "Kazakhstan", "code": "KZ"},
{"name": "Kenya", "code": "KE"},
{"name": "Kiribati", "code": "KI"},
{"name": "Korea, Democratic People\'S Republic of", "code": "KP"},
{"name": "Korea, Republic of", "code": "KR"},
{"name": "Kuwait", "code": "KW"},
{"name": "Kyrgyzstan", "code": "KG"},
{"name": "Lao People\'S Democratic Republic", "code": "LA"},
{"name": "Latvia", "code": "LV"},
{"name": "Lebanon", "code": "LB"},
{"name": "Lesotho", "code": "LS"},
{"name": "Liberia", "code": "LR"},
{"name": "Libyan Arab Jamahiriya", "code": "LY"},
{"name": "Liechtenstein", "code": "LI"},
{"name": "Lithuania", "code": "LT"},
{"name": "Luxembourg", "code": "LU"},
{"name": "Macao", "code": "MO"},
{"name": "Macedonia, The Former Yugoslav Republic of", "code": "MK"},
{"name": "Madagascar", "code": "MG"},
{"name": "Malawi", "code": "MW"},
{"name": "Malaysia", "code": "MY"},
{"name": "Maldives", "code": "MV"},
{"name": "Mali", "code": "ML"},
{"name": "Malta", "code": "MT"},
{"name": "Marshall Islands", "code": "MH"},
{"name": "Martinique", "code": "MQ"},
{"name": "Mauritania", "code": "MR"},
{"name": "Mauritius", "code": "MU"},
{"name": "Mayotte", "code": "YT"},
{"name": "Mexico", "code": "MX"},
{"name": "Micronesia, Federated States of", "code": "FM"},
{"name": "Moldova, Republic of", "code": "MD"},
{"name": "Monaco", "code": "MC"},
{"name": "Mongolia", "code": "MN"},
{"name": "Montserrat", "code": "MS"},
{"name": "Morocco", "code": "MA"},
{"name": "Mozambique", "code": "MZ"},
{"name": "Myanmar", "code": "MM"},
{"name": "Namibia", "code": "NA"},
{"name": "Nauru", "code": "NR"},
{"name": "Nepal", "code": "NP"},
{"name": "Netherlands", "code": "NL"},
{"name": "Netherlands Antilles", "code": "AN"},
{"name": "New Caledonia", "code": "NC"},
{"name": "New Zealand", "code": "NZ"},
{"name": "Nicaragua", "code": "NI"},
{"name": "Niger", "code": "NE"},
{"name": "Nigeria", "code": "NG"},
{"name": "Niue", "code": "NU"},
{"name": "Norfolk Island", "code": "NF"},
{"name": "Northern Mariana Islands", "code": "MP"},
{"name": "Norway", "code": "NO"},
{"name": "Oman", "code": "OM"},
{"name": "Pakistan", "code": "PK"},
{"name": "Palau", "code": "PW"},
{"name": "Palestinian Territory, Occupied", "code": "PS"},
{"name": "Panama", "code": "PA"},
{"name": "Papua New Guinea", "code": "PG"},
{"name": "Paraguay", "code": "PY"},
{"name": "Peru", "code": "PE"},
{"name": "Philippines", "code": "PH"},
{"name": "Pitcairn", "code": "PN"},
{"name": "Poland", "code": "PL"},
{"name": "Portugal", "code": "PT"},
{"name": "Puerto Rico", "code": "PR"},
{"name": "Qatar", "code": "QA"},
{"name": "Reunion", "code": "RE"},
{"name": "Romania", "code": "RO"},
{"name": "Russian Federation", "code": "RU"},
{"name": "RWANDA", "code": "RW"},
{"name": "Saint Helena", "code": "SH"},
{"name": "Saint Kitts and Nevis", "code": "KN"},
{"name": "Saint Lucia", "code": "LC"},
{"name": "Saint Pierre and Miquelon", "code": "PM"},
{"name": "Saint Vincent and the Grenadines", "code": "VC"},
{"name": "Samoa", "code": "WS"},
{"name": "San Marino", "code": "SM"},
{"name": "Sao Tome and Principe", "code": "ST"},
{"name": "Saudi Arabia", "code": "SA"},
{"name": "Senegal", "code": "SN"},
{"name": "Serbia and Montenegro", "code": "CS"},
{"name": "Seychelles", "code": "SC"},
{"name": "Sierra Leone", "code": "SL"},
{"name": "Singapore", "code": "SG"},
{"name": "Slovakia", "code": "SK"},
{"name": "Slovenia", "code": "SI"},
{"name": "Solomon Islands", "code": "SB"},
{"name": "Somalia", "code": "SO"},
{"name": "South Africa", "code": "ZA"},
{"name": "South Georgia and the South Sandwich Islands", "code": "GS"},
{"name": "Spain", "code": "ES"},
{"name": "Sri Lanka", "code": "LK"},
{"name": "Sudan", "code": "SD"},
{"name": "Suriname", "code": "SR"},
{"name": "Svalbard and Jan Mayen", "code": "SJ"},
{"name": "Swaziland", "code": "SZ"},
{"name": "Sweden", "code": "SE"},
{"name": "Switzerland", "code": "CH"},
{"name": "Syrian Arab Republic", "code": "SY"},
{"name": "Taiwan, Province of China", "code": "TW"},
{"name": "Tajikistan", "code": "TJ"},
{"name": "Tanzania, United Republic of", "code": "TZ"},
{"name": "Thailand", "code": "TH"},
{"name": "Timor-Leste", "code": "TL"},
{"name": "Togo", "code": "TG"},
{"name": "Tokelau", "code": "TK"},
{"name": "Tonga", "code": "TO"},
{"name": "Trinidad and Tobago", "code": "TT"},
{"name": "Tunisia", "code": "TN"},
{"name": "Turkey", "code": "TR"},
{"name": "Turkmenistan", "code": "TM"},
{"name": "Turks and Caicos Islands", "code": "TC"},
{"name": "Tuvalu", "code": "TV"},
{"name": "Uganda", "code": "UG"},
{"name": "Ukraine", "code": "UA"},
{"name": "United Arab Emirates", "code": "AE"},
{"name": "United Kingdom", "code": "GB"},
{"name": "United States", "code": "US"},
{"name": "United States Minor Outlying Islands", "code": "UM"},
{"name": "Uruguay", "code": "UY"},
{"name": "Uzbekistan", "code": "UZ"},
{"name": "Vanuatu", "code": "VU"},
{"name": "Venezuela", "code": "VE"},
{"name": "Viet Nam", "code": "VN"},
{"name": "Virgin Islands, British", "code": "VG"},
{"name": "Virgin Islands, U.S.", "code": "VI"},
{"name": "Wallis and Futuna", "code": "WF"},
{"name": "Western Sahara", "code": "EH"},
{"name": "Yemen", "code": "YE"},
{"name": "Zambia", "code": "ZM"},
{"name": "Zimbabwe", "code": "ZW"}
]

@login_required(login_url='/login/')
def tweet_list(request):
    return render(request, 'search/tweet_list.html', {'errorcode':-1,'message':"Introduzca el texto a buscar",'languages':languages,'countries':countries})

@login_required(login_url='/login/')
def get_queryset(request):
    auth = OAuthHandler('wbSKrzlEya3UJgBzkIkSEkz3F',
                        '5GXAfWSO99HZ2QFhEihb4NF4y9lTvIaCt80mvpUCTr2kMha9Fi')
    auth.set_access_token('800728740082765824-MEGhu5oDdSajvFKtcS3jcMrb8rmEkGq',
                          'RxJYOFORpm3CMX8BwCW6o5ckJ0q1TwaVfa0n3eUeAoLnR')
    api = API(auth)
    tosearch=request.GET['q']
    languageCode=request.GET['languageCode']
    country = request.GET['countryCode']
    error=0
    message=""
    results=""
    if (tosearch and tosearch.strip()):
        # country=api.reverse_geocode(lat=40.447269,long=-3.691702,granularity='country')
        # print(api.reverse_geocode(lat=40.447269,long=-3.691702,granularity='country'))
        # for c in country:
        # print(api.get_status('805709551337086980'))
        # countryid=country[0].id
        # print(countryid)

        # for country in countries:
        #     print(country)
        # print(languageCode)

        messagelang="Idioma seleccionado: "
        if(languageCode!="0"):
            messagelang=messagelang+languageCode.capitalize()
            if (country != "Cualquiera"):
                messagelang = messagelang + " ---- País seleccionado: "+country.capitalize()
                results = api.search(tosearch, count=100, lang=languageCode, geocode=countrycoord(country))
            else:
                messagelang = messagelang + " ---- País seleccionado: " + country.capitalize()
                results = api.search(tosearch, count=100, lang=languageCode)

        else:
            messagelang = messagelang + "Cualquiera"
            if (country != "Cualquiera"):
                messagelang = messagelang + " ---- País seleccionado: "+country.capitalize()
                results = api.search(tosearch, count=100, geocode=countrycoord(country))
            else:
                results = api.search(tosearch, count=100)
                messagelang = messagelang + " ---- País seleccionado: " + country.capitalize()
            message = "Se ha realizado correctamente su búsqueda de: \""+tosearch+"\" ---- "+messagelang

            coordinates = locateTweets(results)

            if(len(coordinates)!=0):

                msg = "http://maps.google.com/maps/api/staticmap?center="+coordinates[0]+"&zoom=2&size=1024x1024&maptype=roadmap"
                for coord in coordinates:
                    msg += "&markers="+coord
                    msg = msg + "&sensor=false"
            else:
                msg = "http://maps.google.com/maps/api/staticmap?zoom=2&size=1024x1024&maptype=roadmap"
    else:
        error=1
        message="No se puede realizar la búsqueda de: \""+tosearch+"\""

    context = {
        'result_with_text': results,
        'errorcode':error,
        'message':message,
        'languages': languages,
        'countries':countries,
        'mapurl' : msg
               }
    return render(request, 'search/tweet_list.html', context)

def countrycoord(country):
    response = r.get("https://restcountries.eu/rest/v1/alpha/" + country)
    j = response.json()
    print(j['latlng'][0])
    print(j['latlng'][1])

    return (str(j['latlng'][0])+","+str(j['latlng'][1])+",100km")

def getTweetPlace(tweet):
    if (tweet.place) is not None:
        # geocode_result = gmaps.geocode(loc)
        # print(geocode_result)
        # lat = geocode_result[0]["geometry"]["location"]["lat"]
        # lon = geocode_result[0]["geometry"]["location"]["lng"]
        lon = tweet.place.bounding_box.coordinates[0][0][0]
        lat = tweet.place.bounding_box.coordinates[0][0][1]
        returnstr = str(lat) + "," + str(lon)
    else:
        returnstr = ""

    return returnstr

def locateTweets(results):
    locations = []
    for result in results:
        location = getTweetPlace(result)
        if(location!=""):
            locations.append(location)

    print(locations)
    return locations
