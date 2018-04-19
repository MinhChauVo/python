class SinhVien:
	"""docstring for ClassName"""

	def __init__(self, MSSV, HoTen,MaKhoa):
		super(SinhVien, self).__init__()
		self.MSSV= MSSV
		self.HoTen = HoTen
		self.MaKhoa = MaKhoa

	def toString(self):
		print(self.MSSV, self.HoTen, self.MaKhoa)
	def getMSSV(self):
		return self.MSSV
	def getHoTen(self):
		return self.HoTen
	def getMaKhoa(self):
		return self.MaKhoa
class Khoa:
	"""docstring for ClassName"""
	def __init__(self, MaKhoa, TenKhoa):
		super(Khoa, self).__init__()
		self.MaKhoa = MaKhoa
		self.TenKhoa = TenKhoa
	def toString(self):
		print(self.MaKhoa, self.TenKhoa)
	def getMaKhoa(self):
		return self.MaKhoa
	def getTenKhoa(self):
		return self.TenKhoa
a= []
a.append(SinhVien(001, 'Mai A', 01))
a.append(SinhVien(002, 'Mai B', 03))
a.append(SinhVien(003, 'Mai C', 01))
a.append(SinhVien(004, 'Mai D', 02))
a.append(SinhVien(005, 'Mai E', 01))
a.append(SinhVien(006, 'Mai F', 03))

for i in xrange(0,a):
	i.toString()
k = []
k. append(Khoa(56, 'Khoa 56 CNTT'))
k.append(Khoa(57, 'Khoa 57 CNTT'))
k.append(Khoa(58, 'Khoa 58 CNTT'))
k. append(Khoa(59, 'Khoa 59 CNTT'))

for i in xrange(0,a):
	print(str(get.Khoa) == 57)
	i.toString()
		