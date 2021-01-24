# convert test

# [TEXT]

import time, re, os, random, sys, json;  # This is required to include time module.

from get_text import get_text_image


BASE_DIR =  os.path.dirname(os.path.abspath(__file__))
 



def file_pack(url_1,format=False):
	array = []
	os.chdir(url_1)
	for root, dirs, files in os.walk('.', topdown = False):
		for name in files:
			path_to_file_open = os.path.join(root, name)[1:]
			
			
			
			
			
			# get format
			pattern = re.compile(r'\w+')
			file_format = pattern.findall(path_to_file_open)[-1]
			
			if not format or format.lower() == file_format.lower():
				# create tags
				ari = root.split("\\")
				ari.remove('.')
				
				# create info
				list = {'path':url_1+path_to_file_open, 'tags':ari, 'format':file_format}
				array.append(list)
			
			
			
			


	return array

#print(post_pack_image(dir_1, dir_2))




 



def get_obj(get='type_arr'):
	doc = ['biblatex', 'bibtex', 'commonmark', 'commonmark_x', 'creole', 'csljson', 'csv', 'docbook',   'dokuwiki',   'gfm', 'haddock','ipynb', 'jats', 'jira', 'latex', 'man', 'markdown', 'markdown_github', 'markdown_mmd', 'markdown_phpextra', 'markdown_strict', 'mediawiki', 'muse', 'native', 'odt', 'opml', 'org', 'rst', 't2t', 'textile', 'tikiwiki', 'twiki', 'vimwiki', 'md', 'asciidoc', 'asciidoctor', 'beamer', 'context', 'docbook4', 'docbook5', 'dzslides', 'icml', 'jats_archiving', 'jats_articleauthoring', 'jats_publishing', 'ms', 'opendocument', 'plain', 'pptx', 'revealjs', 'rtf', 's5', 'slideous', 'slidy', 'tei', 'texinfo', 'xwiki', 'zimwiki', 'txt']

	sub = ['srt']

	doctoimg = ['fb2', 'docx','doc','pdf','html','json', 'epub','epub2', 'epub3', 'html4', 'html5', ]

	img = ['png', 'bmp','tga']
	
	img_jpg = ['jpg', 'jpeg',]
	
	img_layers = ['psd','psb','sai','sai2']

	imgtovid = ['gif','webp']

	svgtovid = ['swf']

	aud = ['wav','aiff' ,'mp3','aac','ogg','wma' ,'flac','alac']

	vid = ['webm', 'mp4', 'fvl', 'avi', 'ts', 'mkv','m4v'] 

	svg = ['svg']

	font = ['eot','ttf','woff']

	obj = ['3ds', '3mf', 'amf', 'assimp', 'awd', 'babylon', 'ctm', 'dae', 'drc', 'fbx', 'gcode', 'js', 'json', 'kmz', 'md2', 'mmd','pmx', 'pmd', 'nrrd', 'obj', 'pcd', 'pdb', 'ply', 'prwm', 'sea', 'stl',  'vrm', 'vtk', 'webm' ,'wrl', 'x', 'blend', 'max', 'gltf']

	arr = ['zip', 'rar', 'bz2', '7z','gzip','bzip2', 'xz', 'tar']

	swf = ['swf']

	code = ['py','ui']


	type_arr = {
		'text':{
			'give' : doc+doctoimg,
			'get' : doc+doctoimg
		},

		'image':{
			'give' : img+img_jpg+imgtovid+doctoimg+img_layers+vid,
			'get' : img+img_jpg+imgtovid
		},
		'audio':{
			'give' : aud+vid,
			'get' : aud
		},

		'video':{
			'give' : vid+imgtovid,
			'get' : vid
		},


		'object':{
			'give' : img+imgtovid+doctoimg+svg+obj+vid+font+img_layers,
			'get' : obj
		},


		'font':{
			'give' : font + svg,
			'get' : font
		},

		'archive':{
			'give' : arr,
			'get' : arr
		},

		'subtitles':{
			'give' : doc+doctoimg+img_layers+sub,
			'get' : sub
		},
		
		'code':{
			'give' : doc+doctoimg+img_layers+code,
			'get' : code
		}
		
	}
	
	main_obj = {
		'type_arr':type_arr,
		'doc':doc,
		'sub':sub,
		'doctoimg':doctoimg,
		'img':img,
		'img_jpg':img_jpg,
		'img_layers':img_layers,
		'imgtovid':imgtovid,
		'svgtovid':svgtovid,
		'aud':aud,
		'vid':vid,
		'svg':svg,
		'font':font,
		'obj':obj,
		'arr':arr,
		'swf':swf,
		'code':code,
	}
	
	return main_obj[get]


def check_format(format=False):
	# get object
	obj = get_obj()
	# available types
	type_format = ['text','image','audio','video','object','subtitles','code','font','archive']
	check_arr = []
	for type in type_format:
		if format in obj[type]['give'] :
			check_arr.append(type) 
	if not format:
		check_arr = type_format
	
	return check_arr


 

def ultimate_converter(give_path,get_folder,get_format,type=False,cut_text=False,crop_gif=['00:00:00.00','00:00:01.00',1],tags=False):
	ask_continue = True
	
	# check paths
	if not os.path.exists(get_folder) and ask_continue:
		get_folder = BASE_DIR+'/'+get_folder
		print(get_folder)
		if not os.path.exists(get_folder) :
			print('path end are not exist')
			ask_continue = False


	if not os.path.exists(give_path) and ask_continue :
		give_path = BASE_DIR+'/'+give_path
		print(give_path)
		if not os.path.exists(give_path) :
			print('path start are not exist')
			ask_continue = False






	if ask_continue :
		# give format
		pattern = re.compile(r'\w+')
		give_format = pattern.findall(give_path)[-1]
		print(give_format)
		if get_format != give_format:
			print('corect format')
			# get name
			ticks = time.time()
			get_name = str(round(ticks * 1000000))+str(random.randint(0, 9))
			# generate path
			get_path = get_folder+get_name+'.'+get_format
			print(get_path)

			# get object
			type_arr = get_obj()
			
			

				
				
			if not type:
				# available type
				check_arr = []

				if give_format in type_arr['text']['get'] :
					check_arr.append('text') 
				if give_format in type_arr['image']['get'] :
					check_arr.append('image') 
				if give_format in type_arr['audio']['get'] :
					check_arr.append('audio') 
				if give_format in type_arr['video']['get'] :
					check_arr.append('video') 
				if give_format in type_arr['object']['get'] :
					check_arr.append('object') 
				if give_format in type_arr['subtitles']['get'] :
					check_arr.append('subtitles') 
				if give_format in type_arr['code']['get'] :
					check_arr.append('code') 
				if give_format in type_arr['font']['get'] :
					check_arr.append('font') 
				if give_format in type_arr['archive']['get'] :
					check_arr.append('archive') 
					
					
					
					
				print(check_arr)
				
				# select type
				if len(check_arr) == 0:
					sys.exit()
				elif len(check_arr) > 1:
					i = False
					while i == False:
						try :
							select_type = input('select type format like index:')
							select_type = int(select_type)
							check_arr[select_type]
							i = True
						except:
							print('wrong type')
				else:
					select_type = 0
					print('only one type')
			
				type = check_arr[select_type]
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			# check is format in array
			#print([get_format,type_arr[type]['get']])
			#print([give_format,type_arr[type]['give']])
			
			
			if get_format in type_arr[type]['get'] and give_format in type_arr[type]['give']:
				print('corect format')
				json_settings = []
				
				
				# Type TEXT
				if type == 'text':
					import pypandoc
					print('type text')
					if give_format == 'pdf':
						print('give_file is pdf file')
						# convert pdf to docx
						from pdf2docx import parse 
						# get new path
						get_doc_path = get_folder+get_name+'.docx'
						parse(give_path, get_doc_path, start=0, end=None)
						# convert docx to format
						if get_format != 'docx':
							output = pypandoc.convert_file(get_doc_path, get_format, outputfile=get_path)
							# delete old file
							os.remove(get_doc_path)
					else :
						output = pypandoc.convert_file(give_path, get_format, outputfile=get_path)
						
						
						
						
				# Type IMAGE
				elif type == 'image':
					print('type image')
					from PIL import Image
					arr = get_obj('doctoimg')+get_obj('img_layers')
					arr2 = get_obj('vid')
					if give_format in arr:
						print('give_file is pdf file')
						from wand.image import Image as wi
						# create new path
						path = get_folder+get_name
						os.mkdir(path)
						pdf = wi(filename=give_path, resolution=300)
						pdfimage= pdf.convert("png")
						i=1
						# create images
						for img in pdfimage.sequence:
							page = wi(image=img)
							img_path = path+'/'+str(i)+".png"
							page.save(filename=img_path)
						
							# create info
							file_info = {'filename':str(i), 'format':get_format,'path':get_folder+get_name+'/'}
							# cut text
							if cut_text :
								text = get_text_image(get_path,600,120)
								print(text)
								file_info['text'] = []
								file_info['text'].append({'x':0,'y':0,'width':0,'height':0,'text':text})
							# add tags
							if tags:
								file_info['tags'] = tags
							# add to json
							json_settings.append(file_info)
						
							# change format
							if get_format != 'png':
								image = Image.open(img_path)
								arr=get_obj('img_jpg')
								if get_format in arr :
									image = image.convert('RGB')
								cur_path = path+'/'+str(i)+'.'+get_format
								image.save(cur_path)
								# delete old file
								os.remove(img_path)
								
							i+=1
							
							
					elif give_format in arr2 and get_format == 'gif':
						print('crop gif')
						# 1,22.65 = 1 min 22 sec 65 milisec
						movie_start = crop_gif[0]
						movie_end =  crop_gif[1]
						try:
							size = crop_gif[2]
						except:
							size = 1
							
						from moviepy.editor import VideoFileClip
						clip = (VideoFileClip(give_path)
							.subclip((movie_start),(movie_end))
							.resize(size))
						clip.write_gif(get_path)
					
					
					
					else:
						image = Image.open(give_path)
						arr=get_obj('img_jpg')
						if get_format in arr :
							image = image.convert('RGB')
						image.save(get_path)
						# create info
						file_info = {'filename':get_name, 'format':get_format,'path':get_folder}
						# cut text
						if cut_text :
							text = get_text_image(get_path,600,120)
							print(text)
							# add text
							file_info['text'] = []
							file_info['text'].append({'x':0,'y':0,'width':0,'height':0,'text':text})
						# add to json
						if tags:
							file_info['tags'] = tags
						json_settings.append(file_info)
				# Type AUDIO
				elif type == 'audio':
					import ffmpy
					print('type audio')
					if get_format == 'mp3':
						from moviepy.editor import VideoFileClip
						# create new path
						get_mp3_path = get_folder+get_name+'.mp3'
						# Create file
						videoclip = VideoFileClip(give_path)
						audioclip = videoclip.audio
						audioclip.write_audiofile(get_mp3_path)
						audioclip.close()
						videoclip.close()
						# change format
						if get_format != 'mp3':
							ff = ffmpy.FFmpeg(
								inputs={get_mp3_path: None},
								outputs={get_path: None}
							)
							ff.run()
							# delete old file
							os.remove(get_mp3_path)
					else :
						ff = ffmpy.FFmpeg(
							inputs={give_path: None},
							outputs={get_path: None}
						)
						ff.run()
				
				
				
				# Type VIDEO
				elif type == 'video':
					print('type video')
					if get_format == 'gif':
						# 1,22.65 = 1 min 22 sec 65 milisec
						movie_start = crop_gif[0]
						movie_end =  crop_gif[1]
						from moviepy.editor import VideoFileClip
						clip = (VideoFileClip(give_path)
							.subclip((movie_start),(movie_end))
							.resize(1))
						clip.write_gif(get_path)
					else:
						import ffmpy
						ff = ffmpy.FFmpeg(
							inputs={give_path: None},
							outputs={get_path: None}
						)
						ff.run()
				
				
				
				
				
				
				
				
				
				
				
				# create standart info
				if len(json_settings) == 0:
					# create info
					file_info = {'filename':get_name, 'format':get_format,'path':get_folder, 'page':0}
					if tags:
						file_info['tags'] = tags
					json_settings.append(file_info)
				
				
				# Write JSON
				json_file = open(get_folder + get_name+'.json', 'w+')
				json_file.write(json.dumps(json_settings))
				json_file.close()
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
			
			else:
				print('wrong format')


			return get_path
		else:
			print('format should not be the same')
	else:
		print('ask_continue False')




'''
get_obj2 = get_obj()


check_type = 'image'
check_give_format = 'mp4'
check_get_format = 'gif'


for type in get_obj2:
	if type == check_type or not check_type :
		give = get_obj2[type]['give']
		get = get_obj2[type]['get']
		for give_format in give:
			for get_format in get:
				if give_format == check_give_format or not check_give_format :
					if get_format == check_get_format or not check_get_format :
						try:
							ultimate_converter(r"media/test."+give_format,r"return/",get_format,type)
							print('success:'+give_format+'->'+get_format)
						except:
							print('error:'+give_format+'->'+get_format)
'''







