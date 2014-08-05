# -*- coding: utf-8 -*-
"""
Data source from http://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_(data_file)
"""
import re
from numbers import Integral
from collections import namedtuple


__all__ = ["countries"]

Country = namedtuple('Country', 'name, alpha2, alpha3, numeric, continent')

_records = [
    Country(u"Afghanistan","AF","AFG","004","AS"),
    Country(u"Albania","AL","ALB","008","EU"),
    Country(u"Algeria","DZ","DZA","012","AF"),
    Country(u"American Samoa","AS","ASM","016","OC"),
    Country(u"Andorra","AD","AND","020","EU"),
    Country(u"Angola","AO","AGO","024","AF"),
    Country(u"Antigua and Barbuda","AG","ATG","028","NA"),
    Country(u"Azerbaijan","AZ","AZE","031","EU"),
    Country(u"Azerbaijan","AZ","AZE","031","AS"),
    Country(u"Argentina","AR","ARG","032","SA"),
    Country(u"Australia","AU","AUS","036","OC"),
    Country(u"Austria","AT","AUT","040","EU"),
    Country(u"Bahamas","BS","BHS","044","NA"),
    Country(u"Bahrain","BH","BHR","048","AS"),
    Country(u"Bangladesh","BD","BGD","050","AS"),
    Country(u"Armenia","AM","ARM","051","EU"),
    Country(u"Armenia","AM","ARM","051","AS"),
    Country(u"Barbados","BB","BRB","052","NA"),
    Country(u"Belgium","BE","BEL","056","EU"),
    Country(u"Bermuda","BM","BMU","060","NA"),
    Country(u"Bhutan","BT","BTN","064","AS"),
    Country(u"Bolivia","BO","BOL","068","SA"),
    Country(u"Bosnia and Herzegovina","BA","BIH","070","EU"),
    Country(u"Botswana","BW","BWA","072","AF"),
    Country(u"Bouvet Island (Bouvetoya)","BV","BVT","074","AN"),
    Country(u"Brazil","BR","BRA","076","SA"),
    Country(u"Belize","BZ","BLZ","084","NA"),
    Country(u"British Indian Ocean Territory (Chagos Archipelago)","IO","IOT","086","AS"),
    Country(u"Solomon Islands","SB","SLB","090","OC"),
    Country(u"British Virgin Islands","VG","VGB","092","NA"),
    Country(u"Brunei Darussalam","BN","BRN","096","AS"),
    Country(u"Bulgaria","BG","BGR","100","EU"),
    Country(u"Myanmar","MM","MMR","104","AS"),
    Country(u"Burundi","BI","BDI","108","AF"),
    Country(u"Belarus","BY","BLR","112","EU"),
    Country(u"Cambodia","KH","KHM","116","AS"),
    Country(u"Cameroon","CM","CMR","120","AF"),
    Country(u"Canada","CA","CAN","124","NA"),
    Country(u"Cape Verde","CV","CPV","132","AF"),
    Country(u"Cayman Islands","KY","CYM","136","NA"),
    Country(u"Central African Republic","CF","CAF","140","AF"),
    Country(u"Sri Lanka","LK","LKA","144","AS"),
    Country(u"Chad","TD","TCD","148","AF"),
    Country(u"Chile","CL","CHL","152","SA"),
    Country(u"China","CN","CHN","156","AS"),
    Country(u"Taiwan","TW","TWN","158","AS"),
    Country(u"Christmas Island","CX","CXR","162","AS"),
    Country(u"Cocos (Keeling) Islands","CC","CCK","166","AS"),
    Country(u"Colombia","CO","COL","170","SA"),
    Country(u"Comoros","KM","COM","174","AF"),
    Country(u"Mayotte","YT","MYT","175","AF"),
    Country(u"Congo","CG","COG","178","AF"),
    Country(u"Congo","CD","COD","180","AF"),
    Country(u"Cook Islands","CK","COK","184","OC"),
    Country(u"Costa Rica","CR","CRI","188","NA"),
    Country(u"Croatia","HR","HRV","191","EU"),
    Country(u"Cuba","CU","CUB","192","NA"),
    Country(u"Cyprus","CY","CYP","196","EU"),
    Country(u"Cyprus","CY","CYP","196","AS"),
    Country(u"Czech Republic","CZ","CZE","203","EU"),
    Country(u"Benin","BJ","BEN","204","AF"),
    Country(u"Denmark","DK","DNK","208","EU"),
    Country(u"Dominica","DM","DMA","212","NA"),
    Country(u"Dominican Republic","DO","DOM","214","NA"),
    Country(u"Ecuador","EC","ECU","218","SA"),
    Country(u"El Salvador","SV","SLV","222","NA"),
    Country(u"Equatorial Guinea","GQ","GNQ","226","AF"),
    Country(u"Ethiopia","ET","ETH","231","AF"),
    Country(u"Eritrea","ER","ERI","232","AF"),
    Country(u"Estonia","EE","EST","233","EU"),
    Country(u"Faroe Islands","FO","FRO","234","EU"),
    Country(u"Falkland Islands (Malvinas)","FK","FLK","238","SA"),
    Country(u"South Georgia and the South Sandwich Islands","GS","SGS","239","AN"),
    Country(u"Fiji","FJ","FJI","242","OC"),
    Country(u"Finland","FI","FIN","246","EU"),
    Country(u"Åland Islands","AX","ALA","248","EU"),
    Country(u"France","FR","FRA","250","EU"),
    Country(u"French Guiana","GF","GUF","254","SA"),
    Country(u"French Polynesia","PF","PYF","258","OC"),
    Country(u"French Southern Territories","TF","ATF","260","AN"),
    Country(u"Djibouti","DJ","DJI","262","AF"),
    Country(u"Gabon","GA","GAB","266","AF"),
    Country(u"Georgia","GE","GEO","268","EU"),
    Country(u"Georgia","GE","GEO","268","AS"),
    Country(u"Gambia","GM","GMB","270","AF"),
    Country(u"Palestinian Territory","PS","PSE","275","AS"),
    Country(u"Germany","DE","DEU","276","EU"),
    Country(u"Ghana","GH","GHA","288","AF"),
    Country(u"Gibraltar","GI","GIB","292","EU"),
    Country(u"Kiribati","KI","KIR","296","OC"),
    Country(u"Greece","GR","GRC","300","EU"),
    Country(u"Greenland","GL","GRL","304","NA"),
    Country(u"Grenada","GD","GRD","308","NA"),
    Country(u"Guadeloupe","GP","GLP","312","NA"),
    Country(u"Guam","GU","GUM","316","OC"),
    Country(u"Guatemala","GT","GTM","320","NA"),
    Country(u"Guinea","GN","GIN","324","AF"),
    Country(u"Guyana","GY","GUY","328","SA"),
    Country(u"Haiti","HT","HTI","332","NA"),
    Country(u"Heard Island and McDonald Islands","HM","HMD","334","AN"),
    Country(u"Holy See (Vatican City State)","VA","VAT","336","EU"),
    Country(u"Honduras","HN","HND","340","NA"),
    Country(u"Hong Kong","HK","HKG","344","AS"),
    Country(u"Hungary","HU","HUN","348","EU"),
    Country(u"Iceland","IS","ISL","352","EU"),
    Country(u"India","IN","IND","356","AS"),
    Country(u"Indonesia","ID","IDN","360","AS"),
    Country(u"Iran","IR","IRN","364","AS"),
    Country(u"Iraq","IQ","IRQ","368","AS"),
    Country(u"Ireland","IE","IRL","372","EU"),
    Country(u"Israel","IL","ISR","376","AS"),
    Country(u"Italy","IT","ITA","380","EU"),
    Country(u"Cote d'Ivoire","CI","CIV","384","AF"),
    Country(u"Jamaica","JM","JAM","388","NA"),
    Country(u"Japan","JP","JPN","392","AS"),
    Country(u"Kazakhstan","KZ","KAZ","398","EU"),
    Country(u"Kazakhstan","KZ","KAZ","398","AS"),
    Country(u"Jordan","JO","JOR","400","AS"),
    Country(u"Kenya","KE","KEN","404","AF"),
    Country(u"North Korea","KP","PRK","408","AS"),
    Country(u"South Korea","KR","KOR","410","AS"),
    Country(u"Kuwait","KW","KWT","414","AS"),
    Country(u"Kyrgyz Republic","KG","KGZ","417","AS"),
    Country(u"Lao People's Democratic Republic","LA","LAO","418","AS"),
    Country(u"Lebanon","LB","LBN","422","AS"),
    Country(u"Lesotho","LS","LSO","426","AF"),
    Country(u"Latvia","LV","LVA","428","EU"),
    Country(u"Liberia","LR","LBR","430","AF"),
    Country(u"Libyan Arab Jamahiriya","LY","LBY","434","AF"),
    Country(u"Liechtenstein","LI","LIE","438","EU"),
    Country(u"Lithuania","LT","LTU","440","EU"),
    Country(u"Luxembourg","LU","LUX","442","EU"),
    Country(u"Macao","MO","MAC","446","AS"),
    Country(u"Madagascar","MG","MDG","450","AF"),
    Country(u"Malawi","MW","MWI","454","AF"),
    Country(u"Malaysia","MY","MYS","458","AS"),
    Country(u"Maldives","MV","MDV","462","AS"),
    Country(u"Mali","ML","MLI","466","AF"),
    Country(u"Malta","MT","MLT","470","EU"),
    Country(u"Martinique","MQ","MTQ","474","NA"),
    Country(u"Mauritania","MR","MRT","478","AF"),
    Country(u"Mauritius","MU","MUS","480","AF"),
    Country(u"Mexico","MX","MEX","484","NA"),
    Country(u"Monaco","MC","MCO","492","EU"),
    Country(u"Mongolia","MN","MNG","496","AS"),
    Country(u"Moldova","MD","MDA","498","EU"),
    Country(u"Montenegro","ME","MNE","499","EU"),
    Country(u"Montserrat","MS","MSR","500","NA"),
    Country(u"Morocco","MA","MAR","504","AF"),
    Country(u"Mozambique","MZ","MOZ","508","AF"),
    Country(u"Oman","OM","OMN","512","AS"),
    Country(u"Namibia","NA","NAM","516","AF"),
    Country(u"Nauru","NR","NRU","520","OC"),
    Country(u"Nepal","NP","NPL","524","AS"),
    Country(u"Netherlands","NL","NLD","528","EU"),
    Country(u"Netherlands Antilles","AN","ANT","530","NA"),
    Country(u"Curaçao","CW","CUW","531","NA"),
    Country(u"Aruba","AW","ABW","533","NA"),
    Country(u"Sint Maarten (Netherlands)","SX","SXM","534","NA"),
    Country(u"Bonaire","BQ","BES","535","NA"),
    Country(u"New Caledonia","NC","NCL","540","OC"),
    Country(u"Vanuatu","VU","VUT","548","OC"),
    Country(u"New Zealand","NZ","NZL","554","OC"),
    Country(u"Nicaragua","NI","NIC","558","NA"),
    Country(u"Niger","NE","NER","562","AF"),
    Country(u"Nigeria","NG","NGA","566","AF"),
    Country(u"Niue","NU","NIU","570","OC"),
    Country(u"Norfolk Island","NF","NFK","574","OC"),
    Country(u"Norway","NO","NOR","578","EU"),
    Country(u"Northern Mariana Islands","MP","MNP","580","OC"),
    Country(u"United States Minor Outlying Islands","UM","UMI","581","OC"),
    Country(u"United States Minor Outlying Islands","UM","UMI","581","NA"),
    Country(u"Micronesia","FM","FSM","583","OC"),
    Country(u"Marshall Islands","MH","MHL","584","OC"),
    Country(u"Palau","PW","PLW","585","OC"),
    Country(u"Pakistan","PK","PAK","586","AS"),
    Country(u"Panama","PA","PAN","591","NA"),
    Country(u"Papua New Guinea","PG","PNG","598","OC"),
    Country(u"Paraguay","PY","PRY","600","SA"),
    Country(u"Peru","PE","PER","604","SA"),
    Country(u"Philippines","PH","PHL","608","AS"),
    Country(u"Pitcairn Islands","PN","PCN","612","OC"),
    Country(u"Poland","PL","POL","616","EU"),
    Country(u"Portugal","PT","PRT","620","EU"),
    Country(u"Guinea-Bissau","GW","GNB","624","AF"),
    Country(u"Timor-Leste","TL","TLS","626","AS"),
    Country(u"Puerto Rico","PR","PRI","630","NA"),
    Country(u"Qatar","QA","QAT","634","AS"),
    Country(u"Reunion","RE","REU","638","AF"),
    Country(u"Romania","RO","ROU","642","EU"),
    Country(u"Russian Federation","RU","RUS","643","EU"),
    Country(u"Russian Federation","RU","RUS","643","AS"),
    Country(u"Rwanda","RW","RWA","646","AF"),
    Country(u"Saint Barthelemy","BL","BLM","652","NA"),
    Country(u"Saint Helena","SH","SHN","654","AF"),
    Country(u"Saint Kitts and Nevis","KN","KNA","659","NA"),
    Country(u"Anguilla","AI","AIA","660","NA"),
    Country(u"Saint Lucia","LC","LCA","662","NA"),
    Country(u"Saint Martin","MF","MAF","663","NA"),
    Country(u"Saint Pierre and Miquelon","PM","SPM","666","NA"),
    Country(u"Saint Vincent and the Grenadines","VC","VCT","670","NA"),
    Country(u"San Marino","SM","SMR","674","EU"),
    Country(u"Sao Tome and Principe","ST","STP","678","AF"),
    Country(u"Saudi Arabia","SA","SAU","682","AS"),
    Country(u"Senegal","SN","SEN","686","AF"),
    Country(u"Serbia","RS","SRB","688","EU"),
    Country(u"Seychelles","SC","SYC","690","AF"),
    Country(u"Sierra Leone","SL","SLE","694","AF"),
    Country(u"Singapore","SG","SGP","702","AS"),
    Country(u"Slovakia (Slovak Republic)","SK","SVK","703","EU"),
    Country(u"Vietnam","VN","VNM","704","AS"),
    Country(u"Slovenia","SI","SVN","705","EU"),
    Country(u"Somalia","SO","SOM","706","AF"),
    Country(u"South Africa","ZA","ZAF","710","AF"),
    Country(u"Zimbabwe","ZW","ZWE","716","AF"),
    Country(u"Spain","ES","ESP","724","EU"),
    Country(u"South Sudan","SS","SSD","728","AF"),
    Country(u"Western Sahara","EH","ESH","732","AF"),
    Country(u"Sudan","SD","SDN","736","AF"),
    Country(u"Suriname","SR","SUR","740","SA"),
    Country(u"Svalbard & Jan Mayen Islands","SJ","SJM","744","EU"),
    Country(u"Swaziland","SZ","SWZ","748","AF"),
    Country(u"Sweden","SE","SWE","752","EU"),
    Country(u"Switzerland","CH","CHE","756","EU"),
    Country(u"Syrian Arab Republic","SY","SYR","760","AS"),
    Country(u"Tajikistan","TJ","TJK","762","AS"),
    Country(u"Thailand","TH","THA","764","AS"),
    Country(u"Togo","TG","TGO","768","AF"),
    Country(u"Tokelau","TK","TKL","772","OC"),
    Country(u"Tonga","TO","TON","776","OC"),
    Country(u"Trinidad and Tobago","TT","TTO","780","NA"),
    Country(u"United Arab Emirates","AE","ARE","784","AS"),
    Country(u"Tunisia","TN","TUN","788","AF"),
    Country(u"Turkey","TR","TUR","792","EU"),
    Country(u"Turkey","TR","TUR","792","AS"),
    Country(u"Turkmenistan","TM","TKM","795","AS"),
    Country(u"Turks and Caicos Islands","TC","TCA","796","NA"),
    Country(u"Tuvalu","TV","TUV","798","OC"),
    Country(u"Uganda","UG","UGA","800","AF"),
    Country(u"Ukraine","UA","UKR","804","EU"),
    Country(u"Macedonia","MK","MKD","807","EU"),
    Country(u"Egypt","EG","EGY","818","AF"),
    Country(u"United Kingdom of Great Britain & Northern Ireland","GB","GBR","826","EU"),
    Country(u"Guernsey","GG","GGY","831","EU"),
    Country(u"Jersey","JE","JEY","832","EU"),
    Country(u"Isle of Man","IM","IMN","833","EU"),
    Country(u"Tanzania","TZ","TZA","834","AF"),
    Country(u"United States of America","US","USA","840","NA"),
    Country(u"United States Virgin Islands","VI","VIR","850","NA"),
    Country(u"Burkina Faso","BF","BFA","854","AF"),
    Country(u"Uruguay","UY","URY","858","SA"),
    Country(u"Uzbekistan","UZ","UZB","860","AS"),
    Country(u"Venezuela","VE","VEN","862","SA"),
    Country(u"Wallis and Futuna","WF","WLF","876","OC"),
    Country(u"Samoa","WS","WSM","882","OC"),
    Country(u"Yemen","YE","YEM","887","AS"),
    Country(u"Zambia","ZM","ZMB","894","AF")]


def _build_index(idx):
    return dict((r[idx].upper(), r) for r in _records)

_by_alpha2 = _build_index(1)
_by_alpha3 = _build_index(2)
_by_numeric = _build_index(3)
_by_name = _build_index(0)


NOT_FOUND = object()


class _CountryLookup(object):

    def get(self, key, default=NOT_FOUND):
        if isinstance(key, Integral):
            r = _by_numeric.get("%03d" % key, default)
        else:
            k = key.upper()
            if len(k) == 2:
                r = _by_alpha2.get(k, default)
            elif len(k) == 3 and re.match(r"[0-9]{3}", k):
                r = _by_numeric.get(k, default)
            elif len(k) == 3:
                r = _by_alpha3.get(k, default)
            else:
                r = _by_name.get(k, default)

        if r == NOT_FOUND:
            raise KeyError(key)

        return r

    __getitem__ = get

    def __iter__(self):
        return iter(_records)

    def __contains__(self, item):
        try:
            self.get(item)
            return True
        except KeyError:
            return False

    def _filter_continent(self,con):
        return [c for c in _records if c.continent==con]

    @property
    def africa(self):
        return self._filter_continent('AF')
    
    @property
    def asia(self):
        return self._filter_continent('AS')

    @property
    def europe(self):
        return self._filter_continent('EU')

    @property
    def oceania(self):
        return self._filter_continent('OC')

    @property
    def north_america(self):
        return self._filter_continent('NA')

    @property
    def south_america(self):
        return self._filter_continent('SA')


    @property
    def apac(self):
        return self.asia+self.oceania

    @property
    def america(self):
        return self.north_america+self.south_america

    @property
    def worldwid(self):
        return _records


countries = _CountryLookup()
