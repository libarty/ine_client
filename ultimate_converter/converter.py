# convert test

# [TEXT]

import time, re, os, random, sys, json;  # This is required to include time module.

from get_text import get_text_image



 



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




 



def get_obj():
	doc = ['biblatex', 'bibtex', 'commonmark', 'commonmark_x', 'creole', 'csljson', 'csv', 'docbook',   'dokuwiki',   'gfm', 'haddock',   'ipynb', 'jats', 'jira', 'latex', 'man', 'markdown', 'markdown_github', 'markdown_mmd', 'markdown_phpextra', 'markdown_strict', 'mediawiki', 'muse', 'native', 'odt', 'opml', 'org', 'rst', 't2t', 'textile', 'tikiwiki', 'twiki', 'vimwiki', 'md', 'txt']

	sub = ['srt']

	doctoimg = ['fb2', 'docx','doc','pdf','html','json', 'epub','psd']

	img = ['png', 'jpg', 'jpeg']

	imgtovid = ['gif','webp']

	svgtovid = ['swf']

	aud = ['wav','aiff' ,'mp3','aac','ogg','wma' ,'flac','alac']

	vid = ['webm', 'mp4', 'fvl', 'avi', 'ts', 'mkv'] 

	svg = ['svg']

	font = ['eot','ttf','woff']

	obj = ['3ds', '3mf', 'amf', 'assimp', 'awd', 'babylon', 'ctm', 'dae', 'drc', 'fbx', 'gcode', 'js', 'json', 'kmz', 'md2', 'mmd', 'nrrd', 'obj', 'pcd', 'pdb', 'ply', 'prwm', 'sea', 'stl',  'vrm', 'vtk', 'webm' ,'wrl', 'x', 'blend', 'max', 'gltf']

	arr = ['zip', 'rar', 'bz2', '7z','gzip','bzip2', 'xz', 'tar']

	swf = ['swf']

	code = ['py','ui']


	type_arr = {
		'text':{
			'give' : doc+doctoimg,
			'get' : doc+doctoimg
		},

		'image':{
			'give' : img+imgtovid+doctoimg,
			'get' : img+imgtovid
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
			'give' : img+imgtovid+doctoimg+svg+obj+vid+font,
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
			'give' : doc+doctoimg+sub,
			'get' : sub
		},
		
		'code':{
			'give' : doc+doctoimg+code,
			'get' : code
		}
		
	}
	return type_arr


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


def ultimate_converter(give_path,get_folder,get_format,type=False,cut_text=False,tags=False):
	# check paths
	if not os.path.exists(get_folder) :
		print('patch end are not exist')
		sys.exit()


	if os.path.exists(give_path) :
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
			if get_format in type_arr[type]['get']:
				print('corect array')
				
				
				json_settings = []
				
				
				
				
				# Type TEXT
				if type == 'text':
					print('type text')
					import pypandoc
					if give_format == 'pdf':
						print('it is pdf file')
						# convert pdf to docx
						from pdf2docx import Converter
						cv = Converter(give_path)
						# get new patch
						get_doc_patch = get_folder+get_name+'.docx'
						cv.convert(get_doc_patch, start=0, end=None)
						cv.close()
						# convert docx to format
						if get_format != 'docx':
							output = pypandoc.convert_file(get_doc_patch, get_format, outputfile=get_path)
							# delete old file
							os.remove(get_doc_patch)
					else :
						output = pypandoc.convert_file(give_path, get_format, outputfile=get_path)
						
					# create info
					file_info = {'filename':get_name, 'format':get_format,'patch':get_folder, 'page':0}
					
					if tags:
						file_info['tags'] = tags
					json_settings.append(file_info)
			
			
			
			
			
				# Type IMAGE
				elif type == 'image':
					print('type image')
					from PIL import Image
					
					
					
					if give_format == 'pdf':
						print('format pdf')
						from wand.image import Image as wi
						pdf = wi(filename=give_path, resolution=300)
						pdfimage= pdf.convert("png")
						
						
						
						# create patch
						path = get_folder+get_name
						os.mkdir(path)
						# create images
						i=1
						for img in pdfimage.sequence:
							page = wi(image=img)
							img_patch = path+'/'+str(i)+".png"
							page.save(filename=img_patch)
							
							
							# create info
							file_info = {'filename':str(i), 'format':get_format,'patch':get_folder+get_name+'/'}
							# cut text
							if cut_text :
								text = get_text_image(get_path,600,120)
								print(text)
								file_info['text'] = []
								file_info['text'].append({'x':0,'y':0,'width':0,'height':0,'text':text})
								
							if tags:
								file_info['tags'] = tags
							# add to json
							json_settings.append(file_info)
							
							# change format
							if get_format != 'png':
								image = Image.open(img_patch)
								cur_patch = path+'/'+str(i)+'.'+get_format
								image.save(cur_patch)
								# delete old file
								os.remove(img_patch)
								
							i+=1
					else:
						image = Image.open(give_path)
						arr=['jpg','jpeg']
						if get_format in arr :
							image = image.convert('RGB')
						image.save(get_path)
						# create info
						file_info = {'filename':get_name, 'format':get_format,'patch':get_folder}
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
					print('type audio')
					if get_format == 'mp3':
						from moviepy.editor import VideoFileClip
						videoclip = VideoFileClip(give_path)
						audioclip = videoclip.audio
						audioclip.write_audiofile(get_path)
						audioclip.close()
						videoclip.close()
						# add json
						file_info = {'filename':get_name, 'format':get_format,'patch':get_folder}
						if tags:
							file_info['tags'] = tags
						json_settings.append(file_info)
						
				# Type VIDEO
				elif type == 'video':
					print('type audio')
					if get_format == 'gif':
						# 1,22.65 = 1 min 22 sec 65 milisec
						movie_start = 0,12.65
						movie_end =  0,12.90
						from moviepy.editor import VideoFileClip
						clip = (VideoFileClip(give_path)
							.subclip((movie_start),(movie_end))
							.resize(0.3))
						clip.write_gif(get_path)
					else:
						import ffmpy
						ff = ffmpy.FFmpeg(
							inputs={give_path: None},
							outputs={get_path: None}
						)
						ff.run()
						
					file_info = {'filename':get_name, 'format':get_format,'patch':get_folder}
					
					
					
					if tags:
						file_info['tags'] = tags
					json_settings.append(file_info)
			
			
			
				json_file = open(get_folder + get_name+'.json', 'w+')
				json_file.write(json.dumps(json_settings))
				json_file.close()
			
			else:
				print('wrong format')


			return get_path
		else:
			print('format should not be the same')
	else:
		print('patch start are not exist')






#ultimate_converter(r"media/test.png",r"return/","gif")


