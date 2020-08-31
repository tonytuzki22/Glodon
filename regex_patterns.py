patterns = {}

#general
patterns['following words, in parentheses, at end of line'] = '(?<=[\u4e00-\u9fff]\()\S+(?=\)\s?$)'
patterns['with # in front, not in parentheses, at the end of line'] = '(?<=\s)\d\S+?(?=\s?$)'
patterns['not following anything, in parentheses, at end of line'] = '(?<=\s\()\S+(?=\)\s?$)'

#units
#patterns['m'] = '\d+(\.\d+)?m(以内|以外|以上|以下)?'
patterns['mm'] = '\d+(\.\d+)?mm(以内|以外|以上|以下)?'
patterns['MPa'] = '\d+(\.\d+)?MPa(以内|以外|以上|以下)?'
patterns['m3'] = '\d+(\.\d+)?m3(以内|以外|以上|以下)?'
patterns['W'] = '\d+(\.\d+)?W(以内|以外|以上|以下)?'
patterns['L'] = '\d+(\.\d+)?L(以内|以外|以上|以下)?'

#0309
#patterns['公称直径'] = '(?<=公称直径\()(单栓|双栓)?\d+mm(以内|以外|内|外)?'
#patterns['MPa'] = '\d+(\.\d+)MPa'
patterns['浅深x型'] = '(浅|深)(.+)?型'
#patterns['# following 式'] = '(?<=式\s)\d+(?!点|\d)'
patterns['箱半周长'] = '(?<=箱半周长)\d+m(以下|以上)'
#patterns['管外径'] = '(?<=管外径\()\d+mm(以内|以外)'
#patterns['贮存容器规格'] = '(?<=贮存容器规格\()\d+L'
patterns['#+letters following 机式'] = '(?<=机式\s)\S+'
patterns['一台设备的灌浆体积'] = '(?<=一台设备的灌浆体积\()(\>|\<)?\d+(\.+\d+)(\s)?m\d(以内|以外)'
patterns['PH following 型号'] = '(?<=型号\s)\S+' #(?<=型号\s)PH(P|F|Y)?(\d+)?(\／\d+)?
#patterns['#+点 following 式'] = '((?<=式\)\s)|(?<=式\s))\d+点(以下|以上)?'
#patterns['路 following 远程控制器安装'] = '(?<=远程控制器安装\s)\d+路(以下|以上)?'
#patterns['点 following 装置调试'] = '(?<=装置调试\s)\d+点(以下|以上)'
#patterns['#+门 following 安装'] = '(?<=安装\s)\d+门'
#patterns['Ｗ功放 following 安装'] = '(?<=安装\s)\d+Ｗ功放'
#patterns['试验容器规格'] = '(?<=试验容器规格\()\d+L'

#0310
patterns['每组重量'] = '(?<=每组重量\()\S+(?=\))'
patterns['#+letters following 自闭式冲洗'] = '(?<=自闭式冲洗\s)DN\d+'
#patterns['总容量'] = '(?<=总容量\()\d+(\.\d)?m3(?=\))'
#patterns['容量 in L or kVA'] = '(?<=容量\()\d+(\.\d+)?(L|kVA)(以内|以外|以下|以上)(?=\))'
#patterns['水箱、水池消毒、冲洗 水箱或水池容量'] = '(?<=水箱、水池消毒、冲洗\s水箱或水池容量\()\S+(?=\))'
patterns['设备重量'] = '(?<=设备重量\()\S+(?=\))'
#patterns['设备容量'] = '(?<=设备容量\()\d+m3\/h(以内|以外)(?=\))'
#patterns['台座重量'] = '(?<=台座重量\()\S+(?=\))'
#patterns['罐体直径'] = '(?<=罐体直径\()\S+(?=\))'
#patterns['设备处理水量'] = '(?<=设备处理水量\()\S+(?=\))'
#patterns['设备供水量'] = '(?<=设备供水量\()\S+(?=\))'
#patterns['#+letters following 规格'] = '(?<=规格\s)\d+m\d+'
#patterns['调压器安装 规格'] = '(?<=调压器安装\s规格\()\S+(?=\))'
#patterns['#~ following 片数'] = '(?<=片数\s)\d+～\d+片'
#patterns['#~ following 便槽'] = '(?<=便槽\s)\d+#～\d+#'
patterns['#~ following 无缝黄铜、紫铜管热煨弯头'] = '(?<=无缝黄铜、紫铜管热煨弯头\()\d+°~\d+°(?=\))'
patterns['#~ following 型'] = '(?<=型\()\d+(\.\d+)?~\d+(\.\d+)?m(?=\))'
#patterns['#m3/h following 规格'] = '(?<=规格\s)\d+(.\d)?m3\/h(单表头|双表头)?'
#patterns['每个箱重'] = '(?<=每个箱重\()\d+~\d+kg'
patterns['H#×/'] = 'H\d+(×|/)\d+(×|/)?\d+(以内|以外)?'

#0304
#patterns['10kV\/容量'] = '10kV\/容量'
#patterns['断路器'] = '((?<=断路器\())电流\d+A(以下|以上)(?=\))'
#patterns['负荷开关'] = '((?<=负荷开关\())电流\d+A(以下|以上)(?=\))'
#patterns['真空接触器'] = '(?<=真空接触器\()\d+V\/\d+A(以下|以上)(?=\))'
patterns['电流互感器'] = '((?<=电流互感器\())电流\d+A(以下|以上)(?=\))'
#patterns['#A by itself'] = '(?<=\s)\d+A(以下|以上)'
#patterns['器'] = '(?<=器\()\s?\S+(?=\))'
#patterns['带高压开关柜'] = '(?<=带高压开关柜\()\S+(?=\))'
#patterns['截面'] = '(?<=截面\()\S+(?=\))'
#patterns['每相'] = '(?<=每相\()\S+(?=\))'

patterns['孔深 not at end of line'] = '(?<=\、孔深\()\S+(?=\))(?!\s?$)'
patterns['连接 not at the end of line'] = '(?<=连接\()\S+(?=\))(?!\s?$)'
patterns['半周长 not in parentheses'] = '(?<=\s)半周长\S+$'
patterns['#路'] = '(?<=\s)\d+路以(下|上)(?=\s)'
patterns['words#kW following 摇摆传动器'] = '(?<=摇摆传动器\s)\S+?(?=\s?$)'
patterns['#kW following 电动机台数'] = '(?<=电动机台数\()\d+kW以(下|上)(?=\))'
patterns['公称直径#mm following 管'] = '(?<=管\()公称直径\d+mm以(下|上)(?=\))'
patterns['平均运距m'] = '(?<=\s)平均运距\d+m以(内|上)(?=\s)'
patterns['Φ#'] = '(?<=\s)Φ\d+(?=\s?$)'
patterns['#横架式'] = '(?<=\s)\d+横架式(?=\s)'
patterns['灯体直径'] = '(?<=灯体直径\()\d+mm以(外|内)(?=\))'
patterns['灯体垂吊长度'] = '(?<=灯体垂吊长度\()\d+mm以(外|内)(?=\))'
patterns['灯体半周长'] = '(?<=灯体半周长\()\d+mm以(外|内)(?=\))'
patterns['臂长#dmm not in parentheses'] = '(?<=\s)臂长\d+mm以(上|下)(?=\s?$)'
patterns['臂长#dmm in parentheses'] = '(?<=\()臂长\d+(\.+\d+)?m(以上|以下)?(?=\))'
patterns['灯高#M'] = '(?<=\s)灯高\d+m(以上|以下)?(?=\s)'
patterns['每个洞口填堵体积'] = '(?<=每个洞口填堵体积\()\d+(\.\d+)?m3'
patterns['宇宙灯'] = '(?<=宇宙灯\()\S+(?=\))'
patterns['直径'] = '(?<=\s)直径\d+～\d+(?=\s?$)'
patterns['灯具直径'] = '(?<=灯具直径\()\d+(?=\))'
patterns['宽\+高'] = '宽\+高'
patterns['每根管长'] = '(?<=每根管长\()\d+mm(?=\))'
patterns['金属软管敷设公称管径'] = '(?<=金属软管敷设公称管径\()\d+mm(以外|以内)(?=\))'