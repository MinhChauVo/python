class SinhVien:
	"""docstring for ClassName"""

	def __init__(self, MSSV, HoTen,MaKhoa):
		super(SinhVien, self).__init__()
		self.MSSV= MSSV
		self.HoTen = HoTen
		self.MaKhoa = MaKhoa

	def getMSSV(self):
		return self.MSSV
	def setMSSV(self,MSSV):
		self.MSSV = MSSV
	def getHoTen(self):
		return self.HoTen
	def setHoTen(self,HoTen):
		self.HoTen = HoTen
	def getMaKhoa(self):
		return self.MaKhoa
	def setMaKhoa(self,MaKhoa):
		self.MaKhoa = MaKhoa
	def Xuat(self)
		print (self.MSSV, self.HoTen, self.MaKhoa)
class Khoa(object):
	"""docstring for ClassName"""
	def __init__(self, MaKhoa, TenKhoa):
		super(Khoa, self).__init__()
		self.MaKhoa = MaKhoa
		self.TenKhoa = TenKhoa
	def getMaKhoa(self)
		return self.MaKhoa
	def setMaKhoa(self,MaKhoa)
		self.MaKhoa = MaKhoa
	def getTenKhoa(self)
		return self.TenKhoa
	def setTenKhoa(self, TenKhoa)
		self.TenKhoa = TenKhoa
	def xuat(self)
		print self.MaKhoa, self.TenKhoa


		