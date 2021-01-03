import sys, os
from PyQt5 import QtWidgets

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path += [BASE_DIR+r'\pieces']

from filter import FilterBlock


class Test(QtWidgets.QWidget):
	def __init__(self):
		super().__init__()
		# self.resize(500, 500)

		lay = QtWidgets.QVBoxLayout(self)

		vio = [
			'<div>&#xe973;</div>',
			'<div>&#xe971;</div>',
			'<div>&#xe96f;</div>',
			'<div>&#xe96d;</div>',
			'<div>&#xe96b;</div>',
			'<div>&#xe969;</div>'
		]
		vion = [
			'<div>&#xe972;</div>',
			'<div>&#xe970;</div>',
			'<div>&#xe96e;</div>',
			'<div>&#xe96c;</div>',
			'<div>&#xe96a;</div>',
			'<div>&#xe968;</div>'
		]
		ret = [
			'<div>&#xe93f;</div>',
			'<div>&#xe941;</div>',
			'<div>&#xe985;</div>'
		]
		retn = [
			'<div>&#xe93e;</div>',
			'<div>&#xe940;</div>',
			'<div>&#xe984;</div>'
		]

		pol = [
			'<div>&#xe97b;</div>',
			'<div>&#xe979;</div>',
			'<div>&#xe977;</div>',
			'<div>&#xe975;</div>'
		]
		poln = [
			'<div>&#xe97a;</div>',
			'<div>&#xe978;</div>',
			'<div>&#xe976;</div>',
			'<div>&#xe974;</div>'
		]
		obs = [
			'<div>&#xe94b;</div>',
			'<div>&#xe998;</div>',
			'<div>&#xe9a4;</div>',
			'<div>&#xe9a2;</div>',
			'<div>&#xe949;</div>',
			'<div>&#xe9a0;</div>'
			]
		obsn = [
			'<div>&#xe94a;</div>',
			'<div>&#xe997;</div>',
			'<div>&#xe9a3;</div>',
			'<div>&#xe9a1;</div>',
			'<div>&#xe948;</div>',
			'<div>&#xe99f;</div>'
		]

		nud = [
			'<div>&#xe939;</div>',
			'<div>&#xe937;</div>',
			'<div>&#xe92d;</div>',
			'<div>&#xe92b;</div>',
			'<div>&#xe929;</div>',
			'<div>&#xe935;</div>',
			'<div>&#xe933;</div>',
			'<div>&#xe931;</div>',
			'<div>&#xe92f;</div>',
			'<div>&#xe927;</div>',
			'<div>&#xe926;</div>',
			'<div>&#xe925;</div>',
		]
		nudn = [
			'<div>&#xe938;</div>',
			'<div>&#xe936;</div>',
			'<div>&#xe92c;</div>',
			'<div>&#xe92a;</div>',
			'<div>&#xe928;</div>',
			'<div>&#xe934;</div>',
			'<div>&#xe932;</div>',
			'<div>&#xe930;</div>',
			'<div>&#xe92e;</div>',
			'<div>&#xe924;</div>',
			'<div>&#xe924;</div>',
			'<div>&#xe924;</div>'
		]
		mai = [
			'<div>&#xe955;</div>',
			'<div>&#xe953;</div>',
			'<div>&#xe951;</div>',
			'<div>&#xe94f;</div>',
			'<div>&#xe94d;</div>'
		]
		main = [
			'<div>&#xe954;</div>',
			'<div>&#xe952;</div>',
			'<div>&#xe950;</div>',
			'<div>&#xe94e;</div>',
			'<div>&#xe94c;</div>'
		]
		lus = [
			'<div>&#xe967;</div>',
			'<div>&#xe93d;</div>',
			'<div>&#xe965;</div>',
			'<div>&#xe963;</div>',
			'<div>&#xe961;</div>',
			'<div>&#xe93b;</div>',
			'<div>&#xe95f;</div>',
			'<div>&#xe95d;</div>',
			'<div>&#xe95b;</div>'
		]
		lusn = [
			'<div>&#xe966;</div>',
			'<div>&#xe93c;</div>',
			'<div>&#xe964;</div>',
			'<div>&#xe962;</div>',
			'<div>&#xe960;</div>',
			'<div>&#xe93a;</div>',
			'<div>&#xe95e;</div>',
			'<div>&#xe95c;</div>',
			'<div>&#xe95a;</div>'
		]
		lex = [
			'<div>&#xe99e;</div>',
			'<div>&#xe99c;</div>',
			'<div>&#xe99a;</div>'
		]
		lexn = [
			'<div>&#xe99d;</div>',
			'<div>&#xe99b;</div>',
			'<div>&#xe999;</div>'
		]
		hor = [
			'<div>&#xe97d;</div>',
			'<div>&#xe916;</div>',
			'<div>&#xe918;</div>',
			'<div>&#xe91a;</div>',
			'<div>&#xe91c;</div>'
		]
		horn = [
			'<div>&#xe97c;</div>',
			'<div>&#xe915;</div>',
			'<div>&#xe917;</div>',
			'<div>&#xe919;</div>',
			'<div>&#xe91b;</div>'
		]

		exc_1 = [
			'<div>&#xe9a6;</div>',
		]
		excn_1 = [
			'<div>&#xe9a5;</div>',
		]
		exc_2 = [
			'<div>&#xe9a6;</div>',
			'<div>&#xe959;</div>'
		]
		excn_2 = [
			'<div>&#xe9a5;</div>',
			'<div>&#xe958;</div>'
		]
		exc_3 = [
			'<div>&#xe9a6;</div>',
			'<div>&#xe91e;</div>',
			'<div>&#xe957;</div>'
		]
		excn_3 = [
			'<div>&#xe9a5;</div>',
			'<div>&#xe91d;</div>',
			'<div>&#xe956;</div>'
		]
		epi = [
			'<div>&#xe981;</div>',
			'<div>&#xe97f;</div>'
		]
		epin = [
			'<div>&#xe980;</div>',
			'<div>&#xe97e;</div>'
		]
		dis = [
			'<div>&#xe996;</div>',
			'<div>&#xe994;</div>',
			'<div>&#xe992;</div>',
			'<div>&#xe991;</div>',
			'<div>&#xe98f;</div>'
		]
		disn = [
			'<div>&#xe995;</div>',
			'<div>&#xe993;</div>',
			'<div>&#xe980;</div>',
			'<div>&#xe990;</div>',
			'<div>&#xe98e;</div>'
		]
		dep = [
			'<div>&#xe923;</div>',
			'<div>&#xe921;</div>',
			'<div>&#xe922;</div>',
			'<div>&#xe920;</div>'
		]
		depn = [
			'<div>&#xe91f;</div>',
			'<div>&#xe91f;</div>',
			'<div>&#xe91f;</div>',
			'<div>&#xe91f;</div>'
		]

		dan = [
			'<div>&#xe947;</div>',
			'<div>&#xe945;</div>',
			'<div>&#xe943;</div>'
		]
		dann = [
			'<div>&#xe946;</div>',
			'<div>&#xe944;</div>',
			'<div>&#xe942;</div>'
		]
		com = [
			'<div>&#xe983;</div>',
			'<div>&#xe987;</div>',
			'<div>&#xe989;</div>',
			'<div>&#xe98b;</div>',
			'<div>&#xe98d;</div>',
			'<div>&#xe983;</div>',
			'<div>&#xe987;</div>',
			'<div>&#xe989;</div>',
			'<div>&#xe98b;</div>',
			'<div>&#xe98d;</div>',
			'<div>&#xe983;</div>',
			'<div>&#xe987;</div>',
			'<div>&#xe989;</div>',
			'<div>&#xe98b;</div>',
			'<div>&#xe98d;</div>',
			'<div>&#xe983;</div>',
			'<div>&#xe987;</div>',
			'<div>&#xe989;</div>',
			'<div>&#xe98b;</div>',
			'<div>&#xe98d;</div>',
		]
		comn = [
			'<div>&#xe982;</div>',
			'<div>&#xe986;</div>',
			'<div>&#xe988;</div>',
			'<div>&#xe98a;</div>',
			'<div>&#xe98c;</div>',
			'<div>&#xe982;</div>',
			'<div>&#xe986;</div>',
			'<div>&#xe988;</div>',
			'<div>&#xe98a;</div>',
			'<div>&#xe98c;</div>',
			'<div>&#xe982;</div>',
			'<div>&#xe986;</div>',
			'<div>&#xe988;</div>',
			'<div>&#xe98a;</div>',
			'<div>&#xe98c;</div>',
			'<div>&#xe982;</div>',
			'<div>&#xe986;</div>',
			'<div>&#xe988;</div>',
			'<div>&#xe98a;</div>',
			'<div>&#xe98c;</div>',
		]

		array_icon = {
			'com':[
				'<div>&#xe900;</div>',
				'<div>&#xe901;</div>',
				'<div>&#xe902;</div>',
				'<div>&#xe903;</div>',
				'<div>&#xe904;</div>',
			],
			'comn':[
				'<div>&#xe900;</div>',
				'<div>&#xe901;</div>',
				'<div>&#xe902;</div>',
				'<div>&#xe903;</div>',
				'<div>&#xe904;</div>',
			],

			'exc_1': [
				'<div>&#xe913;</div>',
			],
			'excn_1': [
				'<div>&#xe90f;</div>',
			],

			'exc_2': [
				'<div>&#xe913;</div>',
				'<div>&#xe916;</div>',
			],
			'excn_2': [
				'<div>&#xe90f;</div>',
				'<div>&#xe912;</div>',
			],


			'exc_3': [
				'<div>&#xe913;</div>',
				'<div>&#xe914;</div>',
				'<div>&#xe915;</div>',
			],
			'excn_3': [
				'<div>&#xe90f;</div>',
				'<div>&#xe910;</div>',
				'<div>&#xe911;</div>',
			],

			'dan': [
				'<div>&#xe905;</div>',
				'<div>&#xe906;</div>',
				'<div>&#xe907;</div>',
			],
			'dep': [
				'<div>&#xe908;</div>',
				'<div>&#xe909;</div>',
				'<div>&#xe90a;</div>',
				'<div>&#xe90b;</div>',
			],
			'dis': [
				'<div>&#xe90c;</div>',
				'<div>&#xe90d;</div>',
				'<div>&#xe90e;</div>',
				'<div>&#xe90f;</div>',
				'<div>&#xe910;</div>',
			],
			'epi': [
				'<div>&#xe911;</div>',
				'<div>&#xe912;</div>',
			],
			'hor': [
				'<div>&#xe917;</div>',
				'<div>&#xe918;</div>',
				'<div>&#xe919;</div>',
				'<div>&#xe91a;</div>',
				'<div>&#xe91b;</div>',
			],
			'lex': [
				'<div>&#xe91c;</div>',
				'<div>&#xe91d;</div>',
				'<div>&#xe91e;</div>',
			],
			'lus': [
				'<div>&#xe91f;</div>',
				'<div>&#xe920;</div>',
				'<div>&#xe921;</div>',
				'<div>&#xe922;</div>',
				'<div>&#xe923;</div>',
				'<div>&#xe924;</div>',
				'<div>&#xe925;</div>',
				'<div>&#xe926;</div>',
				'<div>&#xe927;</div>',
			],
			'mai': [
				'<div>&#xe928;</div>',
				'<div>&#xe929;</div>',
				'<div>&#xe92a;</div>',
				'<div>&#xe92b;</div>',
				'<div>&#xe92c;</div>',
			],
			'nud': [
				'<div>&#xe92d;</div>',
				'<div>&#xe92e;</div>',
				'<div>&#xe92f;</div>',
				'<div>&#xe930;</div>',
				'<div>&#xe931;</div>',
				'<div>&#xe932;</div>',
				'<div>&#xe933;</div>',
				'<div>&#xe934;</div>',
				'<div>&#xe935;</div>',
				'<div>&#xe936;</div>',
				'<div>&#xe937;</div>',
				'<div>&#xe938;</div>',
			],
			'obs': [
				'<div>&#xe939;</div>',
				'<div>&#xe93a;</div>',
				'<div>&#xe93b;</div>',
				'<div>&#xe93c;</div>',
				'<div>&#xe93d;</div>',
				'<div>&#xe93e;</div>',
			],
			'pol': [
				'<div>&#xe93f;</div>',
				'<div>&#xe940;</div>',
				'<div>&#xe941;</div>',
				'<div>&#xe942;</div>',
			],
			'ret': [
				'<div>&#xe943;</div>',
				'<div>&#xe944;</div>',
				'<div>&#xe945;</div>',
			],
			'vio': [
				'<div>&#xe946;</div>',
				'<div>&#xe947;</div>',
				'<div>&#xe948;</div>',
				'<div>&#xe949;</div>',
				'<div>&#xe94a;</div>',
				'<div>&#xe94b;</div>',
			],

			'dann': [
				'<div>&#xe905;</div>',
				'<div>&#xe906;</div>',
				'<div>&#xe907;</div>',
			],
			'depn': [
				'<div>&#xe908;</div>',
				'<div>&#xe908;</div>',
				'<div>&#xe908;</div>',
				'<div>&#xe908;</div>',
			],
			'disn': [
				'<div>&#xe909;</div>',
				'<div>&#xe90a;</div>',
				'<div>&#xe90b;</div>',
				'<div>&#xe90c;</div>',
				'<div>&#xe90d;</div>',
			],
			'epin': [
				'<div>&#xe90b;</div>',
				'<div>&#xe90e;</div>',
			],
			'horn': [
				'<div>&#xe913;</div>',
				'<div>&#xe914;</div>',
				'<div>&#xe915;</div>',
				'<div>&#xe916;</div>',
				'<div>&#xe917;</div>',
			],
			'lexn': [
				'<div>&#xe918;</div>',
				'<div>&#xe919;</div>',
				'<div>&#xe91a;</div>',
			],
			'lusn': [
				'<div>&#xe91b;</div>',
				'<div>&#xe91c;</div>',
				'<div>&#xe91d;</div>',
				'<div>&#xe91e;</div>',
				'<div>&#xe91f;</div>',
				'<div>&#xe920;</div>',
				'<div>&#xe921;</div>',
				'<div>&#xe922;</div>',
				'<div>&#xe923;</div>',
			],
			'main': [
				'<div>&#xe924;</div>',
				'<div>&#xe925;</div>',
				'<div>&#xe926;</div>',
				'<div>&#xe927;</div>',
				'<div>&#xe928;</div>',
			],
			'nudn': [
				'<div>&#xe929;</div>',
				'<div>&#xe92a;</div>',
				'<div>&#xe92b;</div>',
				'<div>&#xe92c;</div>',
				'<div>&#xe92d;</div>',
				'<div>&#xe92e;</div>',
				'<div>&#xe92f;</div>',
				'<div>&#xe930;</div>',
				'<div>&#xe931;</div>',
				'<div>&#xe932;</div>',
				'<div>&#xe932;</div>',
				'<div>&#xe932;</div>',
			],
			'obsn': [
				'<div>&#xe933;</div>',
				'<div>&#xe934;</div>',
				'<div>&#xe935;</div>',
				'<div>&#xe936;</div>',
				'<div>&#xe937;</div>',
				'<div>&#xe938;</div>',
			],
			'poln': [
				'<div>&#xe939;</div>',
				'<div>&#xe93a;</div>',
				'<div>&#xe93b;</div>',
				'<div>&#xe93c;</div>',
			],
			'retn': [
				'<div>&#xe93d;</div>',
				'<div>&#xe93e;</div>',
				'<div>&#xe93f;</div>',
			],
			'vion': [
				'<div>&#xe940;</div>',
				'<div>&#xe941;</div>',
				'<div>&#xe942;</div>',
				'<div>&#xe943;</div>',
				'<div>&#xe944;</div>',
				'<div>&#xe945;</div>',
			],



		}

		name_icon = 'vio'
		name_exc_icon = '2'




		wid = FilterBlock(
			step_back_arr=array_icon[name_icon],
			step_neon_arr=array_icon[name_icon+'n'],
			excep_back_arr=array_icon['exc_'+name_exc_icon],
			excep_neon_arr=array_icon['excn_'+name_exc_icon],

			main_color='brown',

			title_back_color='red',
			title_text_color='orange',
			left_block_color='yellow',
			right_block_color='green',

			step_block_color='black',
			step_min_color='#cacad2',
			step_max_color='purple',
			step_back_color='#8181a0',
			step_neon_color='#c8c8c8',
			step_hover_color='white',

			exce_max_color='red',


			slider_back_color='pink',
			slider_square_back_color='brown',
			slider_square_border_color='yellow',

			icon_block_margin=[3],
			icon_size=0.9,
			icon_block_height=1,
			icon_block_width=100,

			v_margin=[5],  # margin between vertical set block
			h_margin=[0],  # margin between horizontal set block

			title_size=30,
			title_padding=[10],

			font_weight_neon=100,
			font_weight_qss=488,


			neon_effect=True,

		)

		lay.addWidget(wid)


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	w = Test()
	w.show()
	sys.exit(app.exec_())