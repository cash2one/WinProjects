# -*- coding: iso-8859-1 -*-
XSD_TYPES= \
{
	"char"		:"xs:byte",
	"BYTE"		:"xs:unsignedByte",
	"short"		:"xs:short",
	"WORD"		:"xs:unsignedShort",
	"int"		:"xs:int",
	"long"		:"xs:int",
	"DWORD"		:"xs:unsignedInt",
	"QWORD"		:"xs:unsignedLong",
	"TIME_SEC"	:"xs:int",
	"TIME_MSEL"	:"xs:long",
	"POS2D_W"		:"POS2D_W",
	"POS2D_S"		:"POS2D_S",
	"GRADS_C"		:"GRADS_C",
}

LENGTH_USERNAME			=12			#玩家账号长度
LENGTH_PASSWORD			=32			#密码长度
LENGTH_NICKNAME			=16			#昵称/名字长度(设定上统一)
LENGTH_ITEMNAME			=24			#道具名称长度
LENGTH_ITEMCODE			=24			#道具编码长度
LENGTH_FILEPATH			=255			#文件路径长度
LENGTH_RANASCRIPT		=3000			#Rana脚本长度

EXT_TYPES = \
{
	"UserName"			:["Zoic::String<%d>" % LENGTH_USERNAME,	"玩家账号"],
	"PassWord"			:["Zoic::String<%d>" % LENGTH_PASSWORD,	"密码"],
	"NickName"			:["Zoic::String<%d>" % LENGTH_NICKNAME,	"角色(包括玩家)昵称"],
	"ItemName"			:["Zoic::String<%d>" % LENGTH_ITEMNAME,	"道具名称"],
	"ItemCode"			:["Zoic::String<%d>" % LENGTH_ITEMCODE,	"道具编码"],
	"FilePath"			:["Zoic::String<%d>" % LENGTH_FILEPATH,	"文件路径"],
	"RanaScript"			:["Zoic::String<%d>" % LENGTH_RANASCRIPT,	"文件路径"],
}
