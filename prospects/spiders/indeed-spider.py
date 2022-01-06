# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request
from collections import OrderedDict
# import csv, json
import datetime

# TODO: Individual crawl delay for each spider. See if global setting overrides local spider setting.

class indeedSpider(scrapy.Spider):
    name = 'indeed'
    start_urls = ['https://www.indeed.com/worldwide']
    # custom_settings = {
    #     'DOWNLOAD_DELAY': '3',
    # }
    cities_data = {"United Kingdom": ["Aberdeen", "York", "Warrington", "West Bromwich", "Wolverhampton", "Telford", "Sheffield", "Slough", "Solihull", "Southampton", "Southend on Sea", "St. Helens, Merseyside", "Stockport", "Stoke-on-Trent", "Sunderland, Tyne and Wear", "Swansea", "Swindon", "Peterborough", "Plymouth", "Poole", "Portsmouth", "City of Preston, Lancashire", "Reading, Berkshire", "Rochdale", "Rotherham", "Oxford", "Newcastle upon Tyne", "Newport, Wales", "Northampton", "Norwich", "Nottingham", "Maidstone", "Manchester", "Middlesbrough", "Milton Keynes", "Leeds", "Leicester", "Liverpool", "London", "Luton", "Kingston upon Hull", "Ipswich", "Huddersfield", "Glasgow", "Gloucester", "Eastbourne", "Edinburgh", "Exeter", "Derby", "Derry", "Dudley", "Dundee", "Cambridge", "Cardiff", "Chester", "Colchester", "Coventry", "Crawley", "Belfast", "Birmingham", "Blackburn", "Blackpool", "Bolton", "Bournemouth", "Bradford", "Brighton", "Bristol"], "United States": ["Abilene, Texas", "Akron, Ohio", "Albuquerque, New Mexico", "Alexandria, Virginia", "Allentown, Pennsylvania", "Amarillo, Texas", "Anaheim, California", "Anchorage, Alaska", "Ann Arbor, Michigan", "Antioch, California", "Arlington, Texas", "Arlington, Virginia", "Arvada, Colorado", "Athens, Georgia", "Atlanta, Georgia", "Augusta, Georgia", "Aurora, Colorado", "Aurora, Illinois", "Austin, Texas", "Yonkers, New York", "Waco, Texas", "Warren, Michigan", "Washington, D.C.", "Waterbury, Connecticut", "West Covina, California", "West Jordan, Utah", "West Valley City, Utah", "Westminster, Colorado", "Wichita Falls, Texas", "Wichita, Kansas", "Wilmington, North Carolina", "Winston-Salem, North Carolina", "Worcester, Massachusetts", "Vallejo, California", "Vancouver, Washington", "Victorville, California", "Virginia Beach, Virginia", "Visalia, California", "Tacoma, Washington", "Tallahassee, Florida", "Tampa, Florida", "Temecula, California", "Tempe, Arizona", "Thornton, Colorado", "Thousand Oaks, California", "Toledo, Ohio", "Topeka, Kansas", "Torrance, California", "Tucson, Arizona", "Tulsa, Oklahoma", "Sacramento, California", "Salem, Oregon", "Salinas, California", "Salt Lake City, Utah", "San Antonio, Texas", "San Bernardino, California", "San Buenaventura, California", "San Diego, California", "San Francisco, California", "San Jose, California", "Santa Ana, California", "Santa Clara, California", "Santa Clarita, California", "Santa Rosa, California", "Savannah, Georgia", "Scottsdale, Arizona", "Seattle", "Shreveport, Louisiana", "Simi Valley, California", "Sioux Falls, South Dakota", "South Bend, Indiana", "Spokane, Washington", "Springfield, Illinois", "Springfield, Massachusetts", "Springfield, Missouri", "St. Louis, Missouri", "St. Paul, Minnesota", "St. Petersburg, Florida", "Stamford, Connecticut", "Sterling Heights, Michigan", "Stockton, California", "Sunnyvale, California", "Surprise, Arizona", "Syracuse, New York", "Palm Bay, Florida", "Palmdale, California", "Paradise, Nevada", "Pasadena, California", "Pasadena, Texas", "Paterson, New Jersey", "Pembroke Pines, Florida", "Peoria, Arizona", "Peoria, Illinois", "Philadelphia, Pennsylvania", "Phoenix, Arizona", "Pittsburgh, Pennsylvania", "Plano, Texas", "Pomona, California", "Ponce, Puerto Rico", "Port St. Lucie, Florida", "Portland, Oregon", "Raleigh, North Carolina", "Rancho Cucamonga, California", "Providence, Rhode Island", "Provo, Utah", "Pueblo, Colorado", "Reno, Nevada", "Oakland, California", "Richmond, California", "Richmond, Virginia", "Oceanside, California", "Riverside, California", "Oklahoma City", "Olathe, Kansas", "Rochester, Minnesota", "Rochester, New York", "Rockford, Illinois", "Omaha, Nebraska", "Ontario, California", "Roseville, California", "Round Rock, Texas", "Orange, California", "Orlando, Florida", "Overland Park, Kansas", "Oxnard, California", "Naperville, Illinois", "Nashville, Tennessee", "New Haven, Connecticut", "New Orleans, Louisiana", "New York City", "Newark, New Jersey", "Newport News, Virginia", "Norfolk, Virginia", "Norman, Oklahoma", "North Las Vegas, Nevada", "Norwalk, California", "Madison, Wisconsin", "Manchester, New Hampshire", "McAllen, Texas", "McKinney, Texas", "Memphis, Tennessee", "Mesa, Arizona", "Mesquite, Texas", "Miami Gardens, Florida", "Miami", "Midland, Texas", "Milwaukee", "Minneapolis", "Miramar, Florida", "Mobile, Alabama", "Modesto, California", "Montgomery, Alabama", "Moreno Valley, California", "Murfreesboro, Tennessee", "Murrieta, California", "Lafayette, Louisiana", "Lakewood, Colorado", "Lancaster, California", "Lansing", "Laredo, Texas", "Las Vegas", "Lexington, Kentucky", "Lincoln, Nebraska", "Little Rock", "Long Beach, California", "Los Angeles, California", "Louisville, Kentucky", "Lowell, Massachusetts", "Lubbock", "Kansas City, Kansas", "Kansas City, Missouri", "Killeen, Texas", "Knoxville", "Jackson, Mississippi", "Jacksonville", "Jersey City", "Joliet, Illinois", "Independence, Missouri", "Indianapolis", "Inglewood, California", "Irvine, California", "Irving, Texas", "Hampton, Virginia", "Hartford, Connecticut", "Hayward, California", "Henderson, Nevada", "Hialeah, Florida", "High Point, North Carolina", "Hollywood, Florida", "Honolulu", "Houston", "Huntington Beach, California", "Huntsville, Alabama", "Gainesville, Florida", "Garden Grove, California", "Garland, Texas", "Gilbert, Arizona", "Glendale, Arizona", "Glendale, California", "Grand Prairie", "Grand Rapids", "Green Bay, Wisconsin", "Greensboro", "Gresham, Oregon", "Fairfield, California", "Fargo, North Dakota", "Fayetteville, North Carolina", "Flint, Michigan", "Fontana, California", "Fort Collins", "Fort Lauderdale", "Fort Wayne", "Fort Worth", "Fremont, California", "Fresno", "Frisco, Texas", "Fullerton, California", "El Monte, California", "El Paso", "Elgin, Illinois", "Elizabeth, New Jersey", "Elk Grove, California", "Erie, Pennsylvania", "Escondido, California", "Eugene, Oregon", "Evansville, Indiana", "Everett, Washington", "Dallas", "Daly City", "Dayton, Ohio", "Denton, Texas", "Denver", "Des Moines", "Detroit", "Downey, California", "Durham, North Carolina", "Cambridge, Massachusetts", "Cape Coral, Florida", "Carlsbad, California", "Carrollton, Texas", "Cary, North Carolina", "Cedar Rapids", "Centennial, Colorado", "Chandler, Arizona", "Charleston, South Carolina", "Charlotte", "Chattanooga, Tennessee", "Chesapeake, Virginia", "Chicago", "Chula Vista, California", "Cincinnati", "Clarksville, Tennessee", "Clearwater, Florida", "Cleveland", "Colorado Springs, Colorado", "Columbia, Missouri", "Columbia, South Carolina", "Columbus, Georgia", "Columbus, Ohio", "Concord, California", "Coral Springs", "Corona, California", "Corpus Christi, Texas", "Costa Mesa", "Bakersfield, California", "Baltimore, Maryland", "Baton Rouge, Louisiana", "Beaumont, Texas", "Bellevue, Washington", "Berkeley, California", "Billings, Montana", "Birmingham, Alabama", "Boise, Idaho", "Boston", "Boulder, Colorado", "Bridgeport, Connecticut", "Brownsville, Texas", "Buffalo, New York", "Burbank, California"], "Australia": ["Adelaide", "Wollongong", "Toowoomba", "Townsville", "Sunshine Coast, Queensland", "Sydney", "Perth, Western Australia", "Newcastle, New South Wales", "Melbourne", "Hobart, Tasmania", "Geelong", "Gold Coast, Australia", "Darwin, Australia", "Cairns", "Canberra", "Central Coast (New South Wales)", "Ballarat", "Brisbane"], "India": ["Abohar", "Achalpur", "Adilabad", "Adityapur", "Adoni", "Agartala", "Agra", "Ahmedabad", "Ahmednagar", "Aizawl", "Ajmer", "Akbarpur, Ambedkar Nagar", "Akola city", "Alandur", "Alappuzha", "Aligarh, Uttar Pradesh", "Allahabad", "Allappuzha", "Alwar", "Amaravati (state capital)", "Ambala Sadar", "Ambala", "Ambarnath", "Ambattur", "Ambikapur, Chhattisgarh", "Ambur", "Amravati", "Amreli", "Amritsar", "Amroha", "Anand, Gujarat", "Anantapur", "Anantnag", "Arrah", "Asansol", "Ashoknagar, North 24 Parganas", "Aurangabad, Bihar", "Aurangabad, Maharashtra", "Avadi", "Azamgarh", "Yamuna Nagar", "Yavatmal", "Warangal", "Wardha", "Vadodara", "Valsad", "Vapi", "Varanasi", "Vasai-Virar", "Vellore", "Veraval", "Vidisha", "Vijayawada", "Visakhapatnam", "Vizianagaram", "Udaipur", "Udgir", "Udupi", "Ujjain", "Ulhasnagar", "Uluberia", "Unnao", "Uttarpara", "Tadepalligudem", "Tadipatri", "Tambaram", "Tenali", "Thane", "Thanesar", "Thanjavur", "Thiruvananthapuram", "Thoothukudi", "Thrissur", "Tiruchchirappalli", "Tiruchirappalli", "Tirunelveli", "Tirupati, Andhra Pradesh", "Tiruppur", "Tiruvannamalai", "Tiruvottiyur", "Titagarh", "Tonk, India", "Tumkur", "Tuticorin", "S.A.S. Nagar", "Sagar, Madhya Pradesh", "Saharanpur", "Saharsa", "Salem, Tamil Nadu", "Sambalpur", "Sambhal", "Sangli", "Santipur", "Sasaram", "Satara (city)", "Satna", "Sawai Madhopur", "Secunderabad", "Sehore", "Seoni, Madhya Pradesh", "Serampore", "Shahjahanpur", "Shamli", "Sheopur", "Shikohabad", "Shillong", "Shimla", "Shimoga", "Shivpuri", "Sikar", "Silchar", "Siliguri", "Singrauli", "Sirsa, Haryana", "Sitapur", "Siwan, Bihar", "Solapur", "Sonipat", "South Dum Dum", "Sri Muktsar Sahib", "Srikakulam", "Srinagar", "Sujangarh", "Sultan Pur Majra", "Sultanpur, Uttar Pradesh", "Surat", "Surendranagar Dudhrej", "Suryapet", "Palakkad", "Palanpur", "Pali, Rajasthan", "Pallavaram", "Palwal", "Panchkula", "Panihati", "Panipat", "Panvel", "Parbhani", "Patan, Gujarat", "Pathankot", "Patiala", "Patna", "Pilibhit", "Pimpri-Chinchwad", "Pithampur", "Pondicherry (city)", "Porbandar", "Port Blair", "Raebareli", "Raichur", "Raigad district", "Raiganj", "Raigarh", "Raipur", "Rajahmundry", "Rajapalayam", "Rajarhat", "Rajkot", "Rajnandgaon", "Rajpur Sonarpur", "Ramagundam", "Rampur, Uttar Pradesh", "Ranaghat", "Ranchi", "Ranebennuru", "Proddatur", "Puducherry", "Raniganj", "Ratlam", "Pudukkottai", "Pune", "Rewa, Madhya Pradesh", "Puri", "Purnia", "Purulia", "Rewari", "Rishra", "Robertsonpet", "Rohtak", "Ongole", "Orai", "Roorkee", "Rourkela", "Rudrapur, Uttarakhand", "Osmanabad", "Ozhukarai", "Nabadwip", "Nadiad", "Nagaon", "Nagapattinam", "Nagaur", "Nagda", "Nagercoil", "Nagpur", "Naihati", "Nalgonda", "Nanded", "Nanded-Waghala", "Nandurbar", "Nandyal", "Nangloi Jat", "Narasaraopet", "Nashik", "Navi Mumbai", "Navsari", "Neemuch", "Nellore", "New Delhi", "Neyveli", "Nizamabad, Telangana", "Noida", "North Barrackpur", "North Dumdum", "Machilipatnam", "Madanapalle", "Madhavaram", "Madhyamgram", "Madurai", "Mahbubnagar", "Maheshtala", "Mainpuri", "Malappuram", "Malegaon", "Malerkotla", "Mandoli, Delhi", "Mandsaur", "Mandya", "Mangalore", "Mango (Jamshedpur)", "Mathura, Uttar Pradesh", "Mau", "Medinipur", "Meerut", "Mehsana", "Mira-Bhayandar", "Miryalaguda", "Mirzapur-cum-Vindhyachal", "Modinagar", "Moga, Punjab", "Moradabad", "Morena", "Morvi", "Motihari", "Mughalsarai", "Mumbai", "Munger", "Murwara", "Mustafabad, Delhi", "Muzaffarnagar", "Muzaffarpur", "Mysore", "Lakhimpur, Uttar Pradesh", "Lalitpur, India", "Latur", "Loni, Ghaziabad", "Lucknow", "Ludhiana", "Kadapa", "Kaithal", "Kakinada", "Kalol, Gandhinagar", "Kalyan, India", "Kalyan-Dombivli", "Kalyani, West Bengal", "Kamarhati", "Kamptee", "Kanchipuram", "Kanchrapara", "Kanhangad", "Kannur", "Kanpur", "Karaikkudi", "Karawal Nagar", "Karimnagar", "Karnal", "Karur", "Kasganj", "Kashipur, Uttarakhand", "Katihar", "Khammam", "Khandwa", "Khanna, Ludhiana", "Kharagpur", "Khardaha", "Khargone", "Khora", "Khurja", "Kirari Suleman Nagar", "Kishanganj", "Kishangarh", "Kochi, India", "Kolar", "Kolhapur", "Kolkata", "Kollam", "Korba, Chhattisgarh", "Kota, Rajasthan", "Kottayam", "Kozhikode", "Krishnanagar, Nadia", "Kulti", "Kumbakonam", "Kurichi", "Kurnool", "Jabalpur", "Jagadhri", "Jagdalpur", "Jagtial", "Jaipur", "Jalandhar", "Jalgaon", "Jalna (city)", "Jalpaiguri", "Jamalpur, Bihar", "Jammu", "Jamnagar", "Jamshedpur", "Jamuria", "Jaunpur, Uttar Pradesh", "Jehanabad", "Jetpur, Navagadh", "Jhansi", "Jhunjhunu", "Jind", "Jodhpur", "Jorhat", "Junagadh", "Ichalakaranji", "Imphal", "Indore", "Habra", "Hajipur", "Haldia", "Haldwani-cum-Kathgodam", "Halisahar", "Hanumangarh", "Haora", "Hapur", "Hardoi", "Haridwar", "Hassan, India", "Hastsal", "Hathras", "Hazaribagh", "Hindaun", "Hindupur", "Hinganghat", "Hisar, India", "Hoshangabad", "Hoshiarpur", "Hospet", "Hosur", "Houghly-Chinsura", "Hubli\u2013Dharwad", "Hyderabad", "Gadag-Betgeri", "Gandhidham", "Gandhinagar", "Ganganagar", "Gangapur, Sawai Madhopur", "Gangavati, Karnataka", "Gangtok", "Gaya, India", "Ghaziabad, Uttar Pradesh", "Ghazipur", "Giridih", "Godhra", "Gojra", "Gokal Pur", "Gonda, Uttar Pradesh", "Gondal, India", "Gondiya", "Gorakhpur", "Greater Noida", "Gudivada", "Gujrat City", "Gulbarga", "Guna, India", "Guntakul", "Guntur", "Gurgaon", "Guwahati", "Gwalior", "Faizabad", "Faridabad", "Farrukhabad", "Fatehgarh", "Fatehpur, Uttar Pradesh", "Firozabad", "Firozpur", "Eluru", "English Bazar", "Erode", "Etah", "Etawah", "Dabgram", "Dahod", "Dallupura", "Damoh", "Danapur", "Darbhanga", "Darjeeling", "Datia", "Davangere", "Deesa", "Dehradun", "Dehri", "Delhi Cantonment", "Delhi", "Deoghar", "Deoli, Delhi", "Deoria, Uttar Pradesh", "Dewas", "Dhamtari district", "Dhanbad", "Dharmavaram, Anantapur district", "Dholpur", "Dhule", "Dibrugarh", "Dimapur", "Dindigul", "Dombivli", "Dum Dum", "Durg", "Durgapur", "Champdani", "Chandannagar", "Chandausi", "Chandigarh", "Chandrapur", "Chas", "Chennai", "Chhapra", "Chhatarpur", "Chhindwara", "Chikmagalur", "Chilakaluripet", "Chitradurga", "Chittoor", "Chittorgarh", "Churu", "Coimbatore", "Cuddalore", "Cuttack", "Badlapur", "Bagaha", "Bagalkot", "Bahadurgarh", "Baharampur", "Bahraich", "Baidyabati", "Baleshwar", "Ballia", "Bally, Bally-Jagachha", "Bally, Howrah", "Balurghat", "Banda, Uttar Pradesh", "Bangalore", "Bangaon", "Bankura", "Bansberia", "Banswara", "Baran, Rajasthan", "Baranagar", "Barasat", "Baraut", "Bardhaman", "Bareilly", "Baripada", "Barnala", "Barrackpur", "Barshi", "Basirhat", "Basti, Uttar Pradesh", "Batala", "Bathinda", "Beawar", "Beed", "Begusarai", "Belgaum", "Bellary", "Berhampur", "Bettiah", "Betul, Madhya Pradesh", "Bhadrak", "Bhadravathi, Karnataka", "Bhadreswar, Hooghly", "Bhagalpur", "Bhalswa Jahangir Pur", "Bharatpur, Rajasthan", "Bharuch", "Bhatpara", "Bhavnagar", "Bhilai", "Bhilwara", "Bhimavaram", "Bhind", "Bhiwadi", "Bhiwandi", "Bhiwani", "Bhopal", "Bhubaneswar", "Bhuj", "Bhusawal", "Bidar", "Bidhannagar", "Bihar Sharif", "Bijapur, Karnataka", "Bikaner", "Bilaspur, Chhattisgarh", "Bokaro Steel City", "Botad", "Budaun", "Bulandshahr", "Bundi", "Burari", "Burhanpur", "Buxar"]}

    # f2 = open('cities_data.csv')
    #
    # csv_items = csv.DictReader(f2)
    # cat_data = {}
    #
    # countries = ['Australia', 'India', 'United Kingdom', 'United States']
    #
    # for i, row in enumerate(csv_items):
    #     country = row.get('country')
    #     if country in countries:
    #         city = row.get('city')
    #         if not cities_data.get(country):
    #             cities_data[country] = []
    #         cities_data[country].append(city)
    # f2.close()



    # is_yield_item = False

    def parse(self, response):
        self.countries = []
        self.hrefs = {}
        a_tags = response.xpath('//table/tr[@class="countries"]/td/a')
        header = {

        }
        countries = ['Australia', 'India', 'United Kingdom', 'United States']
        for a_tag in a_tags:
            country = a_tag.xpath('./text()').extract_first()
            if not country or country not in countries:
                continue

            cities = self.cities_data.get(country)
            if not cities:
                continue
            main_domain = a_tag.xpath('./@href').extract_first().replace('http://', 'https://')
            main_domain = main_domain[:len(main_domain) - 1]
            header = {
                'referer': main_domain + '/?_ga=2.85629594.243178100.1561604893-1611201845.1561604893',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            }
            for city in cities:
                city_val = city.replace(' ', '+')
                url = main_domain + '/jobs?q=&l=' + city_val

                yield Request(url, callback=self.parse_list, headers=header, dont_filter=True, meta={'main_domain':main_domain, 'country': country, 'city': city, 'page_count': 1})
                break
            break

    def parse_list(self, response):
        main_domain = response.meta['main_domain']
        a_tags = response.xpath('//td[@id="resultsCol"]/div[contains(@class,"jobsearch-")]')
        for a_tag in a_tags:
            id_val = a_tag.xpath('./@data-jk').extract_first()

            response.meta['id_val'] = 'jl_' + id_val
            header = {
                'referer': 'https://ar.indeed.com/',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            }

            if a_tag.xpath('./div[@class="title"]/a/@href').extract_first():
                href = main_domain + a_tag.xpath('./div[@class="title"]/a/@href').extract_first()
                yield Request(href, self.parse_details, headers=header, dont_filter=True, meta=response.meta)
            # break

        header = {
                'referer': 'https://ar.indeed.com/',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            }

        # next_url = response.xpath('//div[@class="pagination"]/b/following-sibling::a/@href').extract_first()
        # if next_url and response.meta['page_count'] < 2:
        #     response.meta['page_count'] += 1
        #     yield Request(main_domain + next_url, callback=self.parse_list, headers=header, dont_filter=True, meta=response.meta)

    def parse_details(self, response):
        item = OrderedDict()
        title = response.xpath('//h3[contains(@class,"jobsearch-JobInfoHeader-title")]/text()').extract_first()
        if not title:
            return
        location = response.xpath('//div[contains(@class,"jobsearch-DesktopStickyContainer-companyrating")]/div[4]/text()').extract_first()
        if not location:
            location = ''
        company = response.xpath('//div[contains(@class,"jobsearch-DesktopStickyContainer-companyrating")]/div[1]/a/text()').extract_first()
        if not company:
            if '/cmp/' in response.url:
                company = response.url.split('/cmp/')[-1].split('/')[0]
            else:
                company = ''
        review_count = response.xpath('//div[contains(@class,"jobsearch-DesktopStickyContainer-companyrating")]//meta[@itemprop="ratingCount"]/@content').extract_first()
        if not review_count:
            review_count = ''
        review_val = response.xpath('//div[contains(@class,"jobsearch-DesktopStickyContainer-companyrating")]//meta[@itemprop="ratingValue"]/@content').extract_first()
        if review_val:
            review_val = str(round(float(review_val), 2))
        else:
            review_val = ''

        data = response.xpath('//div[contains(@class,"jobsearch-JobMetadataHeader-itemWithIcon")]')
        time_val = ''
        rate = ''
        per_rate = ''
        for d in data:
            if 'icl-IconFunctional icl-IconFunctional--jobs' in d.xpath('./div/@class').extract_first():
                time_val = d.xpath('./span/text()').extract_first()
            elif 'icl-IconFunctional icl-IconFunctional--location' in d.xpath('./div/@class').extract_first():
                location = d.xpath('./span/text()').extract_first()
            elif 'icl-IconFunctional icl-IconFunctional--salary' in d.xpath('./div/@class').extract_first():
                rate = d.xpath('./span/text()').extract_first()
                if rate:
                    rate = rate.split(' a ')
                    if len(rate) > 1:
                        per_rate = 'per ' + rate[1]
                    else:
                        rate = rate[0].split(' an ')
                        if len(rate) > 1:
                            per_rate = 'per ' + rate[1]
                    rate = rate[0]
        live_time = response.xpath('//div[@class="jobsearch-JobMetadataFooter"]/text()').extract_first()
        if live_time:
            live_time = live_time.replace('- ', '')
        else:
            live_time = ''

        descs_data = response.xpath('//div[@id="jobDescriptionText"]//text()').extract()
        descs = []
        for de in descs_data:
            de = de.strip()
            if de:
                descs.append(de)
        desc = ' '.join(descs)
        if not desc:
            desc = ''

        item['job id'] = response.meta.get('id_val')
        item['title'] = title.replace("'", "`")
        item['country'] = response.meta.get('country').replace("'", "`")
        item['location'] = location.replace("'", "`")
        item['company'] = company.replace("'", "`")
        item['review_count'] = review_count
        item['review_rating'] = review_val
        item['part time/full time/casual'] = time_val.replace("'", "`")
        item['salary/hourly rate'] = rate
        item['salary/hourly'] = per_rate
        item['how long job has been live'] = live_time.replace("'", "`")
        item['job description'] = desc.replace("'", "`")
        item['scrape timestamp'] = str(datetime.datetime.now())
        item['url'] = response.url

        print(item)

        yield item





