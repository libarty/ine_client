from googletrans import Translator

# file for set  words for different languages

Lang_code = 'en'
# arrays for save words
lang_en = {
	'log_sign_in': 'Sign in',
	'log_nickname': 'Username',
	'log_password': 'Password',
	'log_password_c': 'Confirm password ',
	'log_registration': 'Registration',
	'log_email': 'Email',
	'log_phone': 'Phone',
	'log_check_code': 'Check code',
	'log_code-1': 'Uid',
	'log_code-2': 'Token',
	'log_entry_button': 'entry',
	'log_exit_button': 'exit',
	'log_registr_button': 'registration',
	'ServerError000': 'error_000',
	'login_error001': 'error_001',
	'login_error002': 'error_002',
	'login_error003': 'error_003',
	'login_error004.1': 'error_004.1',
	'login_error004.2': 'error_004.2',
	'login_error004.3': 'error_004.3',
	'login_error005.1': 'error_005.1',
	'login_error005.2': 'error_005.2',
	'login_error006.1': 'error_006.1',
	'login_error006.2': 'error_006.2',
	'login_error007.1': 'error_007.1',
	'login_error007.2': 'error_007.2',
	'login_error008': 'error_008',

}

lang_ar = {}
lang_ca = {}
lang_cz = {}
lang_de = {}
lang_es = {}
lang_fr = {}
lang_gr = {}
lang_he = {}
lang_hi = {}
lang_it = {}
lang_ja = {}
lang_pl = {}
#lang_ru = {}
lang_sh = {}
lang_sp = {}
lang_sv = {}
lang_zh = {}


lang_choose = {
	'en': lang_en,
	'ar': lang_ar,
	'ca': lang_ca,
	'cz': lang_cz,
	'de': lang_de,
	'es': lang_es,
	'fr': lang_fr,
	'gr': lang_gr,
	'he': lang_he,
	'hi': lang_hi,
	'it': lang_it,
	'ja': lang_ja,
	'pl': lang_pl,
	#'ru': lang_ru,
	'sh': lang_sh,
	'sp': lang_sp,
	'sv': lang_sv,
	'zh': lang_zh,
}


def get_lang(word, default_value='None'):
	# try translate in google translate
	google = {}
	if not Lang_code == 'en':
		try:
			translator = Translator()
			translations = translator.translate(lang_en.get(word, default_value), dest=Lang_code, src='en')
			google[word] = translations.text
		except:
			pass

	return lang_choose.get(Lang_code, {}).get(word, google.get(word, lang_en.get(word, default_value)))



















