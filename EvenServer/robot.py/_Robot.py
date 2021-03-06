# -*- coding: iso-8859-1 -*-

import socket,struct,time,select

#一次全部发完数据
class _RobotSocket:
	#构造函数
	def __init__(self, sock=None):
		if sock is None:
			self.sock = socket.socket(
				socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.sock = sock
		self.sock.setblocking(0)
		self.readlen=0
		self.msg=''
		self.packetlen=0
	
	#连接	
	def connect(self, host, port):
		try:
			print host
			print port
			self.sock.connect((host, port))
		except socket.error, e:
			if e[0]==36:
				tm_start=time.time()
				while time.time()-tm_start<5:
					if len(select.select([],[self.sock],[],0)[1])==1:
						return
				raise socket.error(61, "Connection refused")
			if e[0]==10035:
				self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				self.sock.connect((host, port))
				self.sock.settimeout(0.001)
				return
			raise e

	#包头打包
	def head_pack(self,length):
		return struct.pack("H",len(msg))

	#包头解包
	def head_unpack(self):
		if self.readlen<2:
			return None
		else:
			head=struct.unpack("H",self.msg[0:2])
			self.packetlen=head[0]
			self.readlen-=2
			self.msg=self.msg[2:]
			return self.packetlen

	#打包
	def packet(self,msg):
		return self.head_pack(len(msg))+ self.encode(msg)

	#解包
	def unpacket(self):
		if self.packetlen==0:
			if self.head_unpack() is None:
				return None
		if self.readlen<self.packetlen: return None
		pck=self.msg[0:self.packetlen]
		self.msg=self.msg[self.packetlen:]
		self.readlen-=self.packetlen
		self.packetlen=0
		return self.decode(pck)
		
	#加密
	def encode(self,msg):
		return msg

	#解密
	def decode(self,msg):
		return msg

	#接收数据
	def _recv(self):
		try:
			msg=self.sock.recv(4096)
			return msg
		except socket.timeout,e:
			return None
		except socket.error, e:
			if e[0]==35:return None		#没有数据
			if e[0]==54:return ''		#连接断开
			raise e

	#发送数据包
	def send(self,msg):
		data=self.packet(msg)
		length=len(data)
		sended=0
		while sended<length:
			try:
				snd=self.sock.send(data[sended:])
				sended+=snd
			except socket.error, e:
				raise e

	#接收数据包
	def recv(self):
		frm=self._recv()
		if frm == '':return ''
		if frm is not None:
			self.readlen+=len(frm)
			self.msg+=frm
		return self.unpacket()

#将数据先保存到发送队列中
class _RobotSocket_(_RobotSocket):
	def __init__(self):
		_RobotSocket.__init__(self)
		self.send_buf=""
		self.send_len=0
		
	def send(self,msg):
		data=self.packet(msg)
		self.send_buf+=data
		self.send_len+=len(data)
		
	def recv(self):
		pck=self.unpacket()
		if pck is not None: return pck
		
		if self.send_len>0:
			socks=select.select([self.sock],[self.sock],[],0.1)
			if len(socks[1])==1:
				snd=self.sock.send(self.send_buf)
				self.send_len-=snd
				self.send_buf=self.send_buf[snd:]
		else:
			socks=select.select([self.sock],[],[],0.1)
	
		if len(socks[0])==1:
			frm=self._recv()
			if frm == '':return ''
			if frm is not None:
				self.readlen+=len(frm)
				self.msg+=frm
		return None

class _RobotClient:
	def __init__(self):
		self.sock = _RobotSocket()
	def connect(self,host,port):
		self.sock.connect(host,port)
	def parseCmd(self,proto,data):
		return 0
	def parsePacket(self,msg):
		byte=struct.unpack("B",msg[0:1])
		return self.parseCmd(byte[0],msg[1:])
	def routine(self):
		msg=self.sock.recv()
		if msg is None: return 1
		if msg=='': return 0
		return self.parsePacket(msg)

