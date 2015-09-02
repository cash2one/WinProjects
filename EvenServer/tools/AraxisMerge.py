import _winreg 

VAL="""0
2
0
AgoServer
10
0
0
2
*
0
1
1
release;debug;bin;.svn;.deps
0
1
1
mysql;lua;zlib;html
0
1
0
.#*
0
1
0
*.o;*.ncb;*.suo;*.pyc;*.a;*.x
0
1
0
Makefile;Makefile.in
0
1
1
autom4te.cache
0
1
0
config.*;configure;configure.lineno;depcomp;install-sh;missing;stamp-h1;aclocal.m4
0
1
2
NetLog;*.log
0
1
0
AI.conf;Zone.conf;Manager.conf;Assistant.conf;Gate.conf;Chat.conf;Map.conf;Stat.conf
0
Default
1
0
0
2
*
"""

KEY = _winreg.OpenKey(
	_winreg.HKEY_CURRENT_USER,
	"Software\\Araxis\\Merge\\6.5",
	0,
	_winreg.KEY_SET_VALUE)
_winreg.SetValueEx(
	KEY,
	"PatternFilterSchemes",
	0,
	_winreg.REG_SZ,
	VAL)
_winreg.CloseKey(KEY)
