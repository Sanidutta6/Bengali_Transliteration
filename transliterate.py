BengaliAlpha = {'Swarbarna': {'অ': 'a', 'আ': 'a', 'ই': 'i', 'ঈ': 'e', 'উ': 'u', 'ঊ': 'uu', 'ঋ': 'ri', 'ঌ': 'li', 'এ': 'e', 'ঐ': 'oi', 'ও': 'o', 'ঔ': 'ou'},
		'Byanjanbarna': {'ক': 'k', 'খ': 'kh', 'গ': 'g', 'ঘ': 'gh', 'ঙ': 'ng', 'চ': 'ch', 'ছ': 'chh', 'জ': 'j', 'ঝ': 'jh', 'ঞ': 'n', 'ট': 't', 'ঠ': 'th', 'ড': 'd', 'ঢ': 'dh', 'ণ': 'n', 'ত':'t', 'থ': 'th', 'দ': 'd', 'ধ': 'dh', 'ন': 'n', 'প': 'p', 'ফ': 'ph', 'ব': 'b', 'ভ': 'bh', 'ম': 'm', 'য': 'j', 'র': 'r', 'ল': 'l', 'শ': 'sh', 'ষ': 'sh', 'স': 's', 'হ': 'h', 'য়': 'y', 'ড়': 'rh', 'ঢ়': 'rhh', 'ক্ষ': 'ksh', 'ঞ': 'y'},
		'special': {'া': 'a', 'ি': 'i', 'ী': 'e', 'ু': 'u', 'ূ': 'u', 'ৃ': 'ri', 'ৄ':'', 'ে': 'e', 'ৈ': 'oi', 'ো': 'o', 'ৌ': 'ou', '্': '', 'ৎ': 't', 'ং': 'ng', 'ঃ': 'h', '‍ঁ': '', '‍্': '', '‍্য': 'yo', '‍‍্র': 'r', '‍্ব': ''}}

# BExamples = ['খুব সুন্দর ধন্যবাদ', 'অসাধারণ ভিডিও শেয়ার করলাম ধন্যবাদ', 'দাদা তোমার গানটা খুব ভালো লাগলো', 'প্রাণ খুলে হাসলাম ️', 'দারুন', 'বিজ্ঞাপন ', 'মৃন্ময় দা তুমি একটা জিনিস ভাই', 'মানসম্মান রাখার খাতিরে যারা গালিগালাজ দিতে পারেননি তারা লাইক করুন', 'দাদা আধখানা রুটির সেই স্বাদ বাঙ্গালীর মন জয় করে নিয়েছে', 'না হেসে পারলাম না আমাকে সবাই সাপোর্ট করেন।আমি যাতে আপনাদের মতো হতে পারি।', 'তোমার ভিডিও দেখে সারাদিনের ক্লান্তি দূর হয়ে যায় দাদা', 'অসাধারণ সব কনসেপ্ট গুলো নিয়ে ভিডিও তৈরি করে শেষ পর্যন্ত হাসির ফোয়ারা চলে', 'দাদার ভাষার মাঝে আমাদের বাংলাদেশের একটা টান আছে ', 'ভিডিও এর শেষে যে এতো সুন্দর গান শুনাবেন ভাবতে পারিনি দাদা', 'অ্যাড গুলো সত্যি অস্কার পাওয়ার মতো তবে শেষে যে গানটার অপমান করলে সেটা ঠিক না মেয়েটি তার নিজের ভাষায় গানটি করেছে তাই নিজের মাতৃভাষাকে যেমন সন্মান করো ঠিক তেমন অন্য দের মাতৃভাষাকেও সন্মান করো দেখবে ভালোই লাগবে মন্দ লাগবে না']

w = ['সে ঘুরে ল্যাংডনের চোখের দিকে তাকায়।', 'সব মানুষের মধ্যে সমতা আনতে হলে কারও না কারও স্বাধীনতায় হস্তক্ষেপ করতেই হবে।',
			'যাই জিজ্ঞেস কর না কেন, সব প্রশ্নের জবাব দিব ডিনারের পর। ঠিক যখন আমি সভাকে শুভরাত জানিয়ে বিদায় নিতে উদ্যত, একজন লোক সত্বর আমার কাছে এসে নিজের পরিচয় দেয়। যেতে দিন!',
			'এবার ক্যামারলেনগো ঘুরে দাঁড়াল আবার, তাকাল অন্য সৈনিকদের দিকে, জোয়ানগণ, আমি আর কোন প্রাণঘাতি ঘটনা দেখতে চাই না এই সন্ধ্যায়। তাদের ট্যাক্সি এখন কোথায়?', 
			'বেশিরভাগ গবেষকই মনে করেন যে, এতসব গুরুত্বপূর্ণ আবিষ্কারের পেছনে নিশ্চয়ই সেপিয়েন্সদের বুদ্ধিবৃত্তিক দক্ষতার কোনো পরিবর্তন দায়ী।', 
			'দশকের পর দশক ধরে এসব প্রাণীর জীবাশ্ম আর দেহাবশেষের খোঁজে দুই আমেরিকার পাহাড় ও সমতলে চষে বেড়াচ্ছেন বিশেষজ্ঞরা।', 
			'যখনই তাঁরা কোনো কিছু খুঁজে পাচ্ছেন পরম যত্নে সেগুলো পাঠিয়ে দিচ্ছেন গবেষণাগারে।', 
			'এটা প্রাপ্ত বয়স্কদের জন্য এক রকমের স্কুলও বলা চলে।']

def Expand(bWords):
	bWords = bWords.split(' ')
	expandedBW = []

	for word in bWords:
		size = len(word)
		prevW = ''
		for i in range(size):
			#print(word[i])
			if word[i] == 'য' and prevW != '' and prevW not in BengaliAlpha['Swarbarna']:
				expandedBW.append('')
			else:
				expandedBW.append(word[i])

			try:
				if i+1 == size:
					break
				#elif word[i] == 'য' and prevW != '' and prevW not in BengaliAlpha['Swarbarna']:
				#	expandedBW.append('')
				elif (word[i] in BengaliAlpha['Byanjanbarna'].keys()) and (word[i] not in BengaliAlpha['special'].keys()) and (word[i+1] not in BengaliAlpha['special'].keys()) and (word[i] != 'ও'):
					expandedBW.append('অ')
				#else:
				#	expandedBW.append(word[i])
			except IndexError as e:
				pass

			if word[i] not in BengaliAlpha['special'].keys():
				prevW = word[i]

		if len(bWords) > 1:
			expandedBW.append(' ')

	return expandedBW

def Replace(expandedBW):
	engWord = ''
	for i in expandedBW:
		if i in BengaliAlpha['Swarbarna']:
			engWord += BengaliAlpha['Swarbarna'][i]
		elif i in BengaliAlpha['Byanjanbarna']:
			engWord += BengaliAlpha['Byanjanbarna'][i]
		elif i in BengaliAlpha['special']:
			engWord += BengaliAlpha['special'][i]
		elif i == ' ':
			engWord += ' '
		else:
			engWord += i

	return engWord

for i in w:
	expandedBW = Expand(i)
	#print(expandedBW)
	engWord = Replace(expandedBW)
	print(engWord)
